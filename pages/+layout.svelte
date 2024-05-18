<script>
  import '@evidence-dev/tailwind/fonts.css';
  import '../app.css'; 
  import { EvidenceDefaultLayout } from '@evidence-dev/core-components';
  export let data;
</script>

<EvidenceDefaultLayout githubRepo="https://github.com/username/repo-name">
  <slot />  
</EvidenceDefaultLayout>