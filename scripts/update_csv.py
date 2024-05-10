# Login to email and find it

import imaplib
import email
from email.header import decode_header
import pandas as pd
import re
import os
import requests

# Read secrets from environment variables
username = os.getenv('EMAIL_USERNAME')
password = os.getenv('EMAIL_PASSWORD')
imap_url = os.getenv('IMAP_URL')

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(imap_url)
mail.login(username, password)

# Select the inbox to search in
mail.select("inbox")

# Search for emails with a specific subject
subject = "Your data export has been delivered"
typ, msgs = mail.search(None, '(SUBJECT "{}")'.format(subject))

# Initialize a list to store email data
email_data = []

# Process the emails found
for num in msgs[0].split():
    typ, data = mail.fetch(num, '(RFC822)')
    for response_part in data:
        if isinstance(response_part, tuple):
            # Parse the email content
            msg = email.message_from_bytes(response_part[1])
            # Initialize a dictionary to store all headers
            email_details = {}
            # Iterate over all headers
            for header, value in msg.items():
                # Decode the header value if needed
                decoded_value = ''.join(
                    part[0].decode(part[1]) if part[1] else part[0]
                    for part in decode_header(value)
                )
                email_details[header] = decoded_value

            # Extract email body and find links
            body = ''
            if msg.is_multipart():
                # Iterate over each part of the email
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        part_body = part.get_payload(decode=True).decode()
                    except:
                        part_body = None
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        body += part_body
            else:
                # Extract body from non-multipart email
                content_type = msg.get_content_type()
                if content_type == "text/plain":
                    try:
                        body = msg.get_payload(decode=True).decode()
                    except:
                        body = None
            
            email_details["Body"] = body

            # Extract all URLs from the body
            links = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', body)
            email_details["Links"] = links

            # Append the email details to the list
            email_data.append(email_details)

# Close the connection
mail.close()
mail.logout()

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(email_data)

# Determine the maximum number of links in any email
max_links = max(len(email.get("Links", [])) for email in email_data)

# Unpack links into separate columns
for i in range(max_links):
    df[f'Link {i+1}'] = df['Links'].apply(lambda x: x[i] if i < len(x) else None)

# Drop the original 'Links' column
df.drop('Links', axis=1, inplace=True)

# get the latest download link
download_link=df["Link 2"].iloc[-1]

# Update the csv
save_path = 'sources/huckleberry/events.csv'

# Ensure the directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Send a HTTP request to the URL
response = requests.get(download_link)

# Check if the request was successful
if response.status_code == 200:
    # Write the content to the file
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print("CSV file has been downloaded and saved to:", save_path)
else:
    print("Failed to download the CSV file. Status code:", response.status_code)