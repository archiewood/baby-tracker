<script context="module">
    export const evidenceInclude = true;
</script>
<script>
    import { QueryLoad } from '@evidence-dev/core-components';
    import InternalTimeline from './InternalTimeline.svelte';
    export let data;
    // Remove any undefined props (e.g. w/o defaults) to prevent them from being passed
    $: spreadProps = Object.fromEntries(Object.entries($$props).filter(([, v]) => v !== undefined));
    let queryID = data?.id;
</script>
<!-- Pass all the props through-->
<QueryLoad {data} let:loaded>
    <InternalTimeline {...spreadProps} data={loaded?.__isQueryStore ? Array.from(loaded) : loaded} {queryID}>
        <slot />
    </InternalTimeline>
</QueryLoad>