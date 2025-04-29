<!--PRODUCTS PAGE-->

<script>
  import { onMount } from 'svelte';
  import Button from '../../components/button.svelte';
  import Products from '../../components/Products.svelte';

  let products = [];
  let filteredProducts = [];
  let variable = '';

  onMount(async () => {
  try {
    const res = await fetch('http://localhost:5000/api/products');
    const data = await res.json();
    console.log('Fetched products:', data);
    products = data;
    filteredProducts = data;
  } catch (err) {
    console.error('Fetch failed:', err);
  }});

async function searchEngine(variable){
    console.log('searching for a product:', variable)
  }

</script>
  
<style>
    
:global(body) { margin: 0; padding: 0; }
main {
  text-align: left;
	margin: 20 auto;
	padding-bottom: 20px;;
	background-color: #8FD6E3;
	height: 100%;
}

.product-list{
  padding-left: 20px;
	padding-right: 20px;
}

.search{
	padding: 20px;
	padding-bottom: 30px;
	text-align: center;
}

input{
  font: 'Ubuntu';
  font-size: 15px;
	max-width: 300px;
	width: 80%;
  height: 30px;
  margin-top: 30px;
  border-radius: 10px;
}

</style>

<main>
	<div class="search">
		<input type="text" bind:value={variable} placeholder="Search for a product..." />
		<Button type='searchButton' on:click={() => searchEngine(variable)}>
      Search
    </Button>

	</div>
	<div class="product-list">
		<Products {filteredProducts}/>
	</div>

</main>
