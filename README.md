# Evidence Template Project

Welcome to Evidence. Use this project template to get started.

## Get Started from VS Code

The easiest way to get started is using the [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=evidence-dev.evidence), which copies this template.

1. Install the extension from the VS Code Marketplace
2. Open the Command Palette (Ctrl/Cmd + Shift + P) and enter `Evidence: New Evidence Project`
3. Click `Start Evidence` in the bottom status bar

## Get Started using the CLI

```bash
npx degit evidence-dev/template my-project
cd my-project 
npm install 
npm run sources
npm run dev 
```

Check out the docs for [alternative install methods](https://docs.evidence.dev/getting-started/install-evidence) including Docker, Github Codespaces, and alongside dbt.


## Codespaces

If you are using this template in Codespaces, click the `Start Evidence` button in the bottom status bar.

Alternatively, use the following commands to get started:

```bash
npm install
npm run sources
npm run dev -- --host 0.0.0.0
```

See [the CLI docs](https://docs.evidence.dev/cli/) for more command information.

**Note:** Codespaces is much faster on the Desktop app. After the Codespace has booted, select the hamburger menu → Open in VS Code Desktop.

## Connection Issues

If you see `✗ orders_by_month Missing database credentials`, you need to add the connection to the demo database:

1. Open the settings menu at [localhost:3000/settings](http://localhost:3000/settings)
2. select `DuckDB`
3. enter `needful_things`
4. select `.duckdb` and save

## Key Features

- Interactive dashboards built using Evidence and Vega
- Ability to filter and slice data by various dimensions like date range, product category, region, etc.
- Automated insights that surface interesting trends and anomalies 
- Shareable data stories that combine visualizations, text, and images

## Getting Started

1. Clone this repository
2. Install dependencies with `npm install` 
3. Run `npm run sources` to configure the database connection
4. Start the development server with `npm run dev`
5. Open `localhost:3000` in your browser

## Documentation

- [User Guide](docs/user-guide.md)
- [Database Schema](docs/schema.md)
- [Metrics Definitions](docs/metrics.md) 

## Support

If you have any questions or feedback, please open an issue on this repository or contact support@company.com
