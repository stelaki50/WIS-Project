<script>
    import Card from "./Card.svelte";
    export let filteredProducts = [];
</script>

<div class="poll-list">
    {#each filteredProducts as product}
        <div>
            <Card {product}/>
        </div>
    {/each}
</div>

<style>
    .poll-list{
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-gap: 10px;
    }
</style>