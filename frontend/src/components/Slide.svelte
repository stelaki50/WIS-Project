<script>
	import { fade } from 'svelte/transition';
	import { onMount } from 'svelte';

	let slideshow_images = [
    {
      image: "",
      description: "loading...",
    },];
    onMount(async () => {
        try {
        const res = await fetch('http://localhost:5000/api/popular_products');
        const data = await res.json();
        console.log('Fetched products:', data);

        slideshow_images = data;} catch (err) {
    	console.error('Fetch failed:', err);}});



	let current = 0;

	function next() {
		current = (current + 1) % slideshow_images.length;
	}

	function prev() {
		current = (current - 1 + slideshow_images.length) % slideshow_images.length;
	}
  
</script>


<style>
	.slideShow {
	  position: relative;
	  width: 900px;
	  height: 550px;
	  margin: auto;
	  margin-top: 3rem;
	  overflow: hidden;
	  border-radius: 1rem;
	  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
	}
	
	.slide {
	  position: absolute;
	  width: 100%;
	  height: 100%;
	}
	
	.slide img {
	  width: 100%;
	  height: 100%;
	  object-fit: cover;
	  border-radius: 1rem;
	}
	
	.slideShow .buttons {
	  display: flex;
	  justify-content: space-between;
	  position: absolute;
	  width: 95%;
	  top: 50%;
	  transform: translateY(-50%);
	  padding: 0 1rem;
	  z-index: 10;
	}
	
	button {
	  background: rgba(0, 0, 0, 0.5);
	  border: none;
	  color: white;
	  padding: 0.5rem 1rem;
	  font-size: 1.5rem;
	  cursor: pointer;
	  border-radius: 0.5rem;
	  transition: background 0.3s;
	}
	
	button:hover {
	  background: rgba(0, 0, 0, 0.8);
	}
	
	.description {
	  position: absolute;
	  bottom: 0;
	  width: 96.5%;
	  padding: 1rem;
	  background: rgba(0, 0, 0, 0.5);
	  color: white;
	  font-family: 'Ubuntu', sans-serif;
	  font-size: 1rem;
	  border-bottom-left-radius: 1rem;
	  border-bottom-right-radius: 1rem;
	  text-align: center;
	}
</style>
	

<div class="slideShow">
	{#each [slideshow_images[current]] as item (item.image)}
	<div class="slide" transition:fade>
		<img src={`/products_images/${item.image}`} alt={item.description} />
		<p class="description">{item.description}</p>
	  </div>
	{/each}

	<div class="buttons">
		<button on:click={prev}>❮</button>
		<button on:click={next}>❯</button>
	</div>
</div>
