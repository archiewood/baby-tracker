<script>
  import { EvidenceDefaultLayout } from '@evidence-dev/core-components';
  import site from '$lib/config/site';
  import '@evidence-dev/core-components/global.css';
</script>

<EvidenceDefaultLayout githubRepo="https://github.com/your-repo-url">
  <slot />
</EvidenceDefaultLayout>