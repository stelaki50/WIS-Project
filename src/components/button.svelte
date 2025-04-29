<!-- Button.svelte -->
<script>
    
    export let type = 'primary';
    export const search = 'searchButton';
    
</script>

<button class="{type}" on:click>
    <slot />
</button>

<style>

button {
    font-size: 15px;
    padding: 15px 40px;
    background-color: #003835;
    color: white;
    border: none;
    border-radius: 10px;
    margin: 5px;
    cursor: pointer;
    transition: background-color 0.2s ease;
    font-family: 'Ubuntu', sans-serif;
}

button:hover {
    background-color: #005f5b;
}

.searchButton {
    font-size: 15px;
    padding: 8px 20px;
}

</style>
