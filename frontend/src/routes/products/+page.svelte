<!--PRODUCTS PAGE-->

<script>
  import { onMount } from 'svelte';
  import Button from '../../components/button.svelte';
  import Products from '../../components/Products.svelte';

  let products = [];
  let filteredProducts = [];
  let variable = '';
  let filter_category = 'All products';

  let filter_categories = [
    'All products', 'Graphics Card', 'Processor', 'Motherboard', 
    'RAM', 'M2-SSD-HDD', 'Case', 'CPU Cooler', 'Power Supply']

  onMount(async () => {
    try {
    const res = await fetch('http://localhost:5000/api/products');
    const data = await res.json();
    console.log('Fetched products:', data);

    products = data;
    filteredProducts = data;
  } catch (err) {
    console.error('Fetch failed:', err);}});



    async function searchEngine(searchTerm) {

      console.log('Searching for a product:', searchTerm);

      try {
          // Send a GET request to the backend API with the search term as a query parameter
          const response = await fetch(`http://localhost:5000/api/search?name=${encodeURIComponent(searchTerm)}`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
          });

          if (!response.ok) {
            const errorData = await response.json();
            console.error('Error fetching products:', errorData.error);
            return [];
          }

          const data = await response.json();
          console.log('Fetched products:', data);

          return data; // Return the products fetched from the backend
        
      }catch (error) {
        console.error('Fetch failed:', error);
        return [];
      }
}

async function handleSearch() {
    console.log("User searched for:", variable);
    filteredProducts = await searchEngine(variable);
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

.search-and-filter{
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
	<div class="search-and-filter">
		<input type="text" bind:value={variable} placeholder="Search for a product..." />


    <Button on:click={() => handleSearch()}>Search</Button>
     

    <select bind:value={filter_category} style="margin-left: 10px; height: 35px; border-radius: 10px;">
      {#each filter_categories as cat}
        <option value={cat}>{cat}</option>
      {/each}
    </select>

	</div>
	<div class="product-list">
		<Products {filteredProducts}/>
	</div>

</main>
