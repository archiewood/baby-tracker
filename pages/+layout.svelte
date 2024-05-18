<script>
  import '@evidence-dev/tailwind/fonts.css';
  import '../app.css'; 
  import { EvidenceDefaultLayout } from '@evidence-dev/core-components';
  export let data;
</script>

<EvidenceDefaultLayout githubRepo="https://github.com/your-repo-url">
  <slot />
</EvidenceDefaultLayout>