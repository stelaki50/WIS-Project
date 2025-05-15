<script>
	import { fade } from 'svelte/transition';

	const slideshow_images = [
    {
      url: "/images/rtx_5000_series_gpu.jpg",
      description: "Nvidia RTX 50-series GPUs: Next-generation Nvidia Blackwell GPU architecture",
    },
    {
      url: "/images/ryzen_9_7000_series_cpu.jpg",
      description: "New AMD Ryzen 9950X3D and 9900X3D: Class-leading technology and performance",
    },
    {
      url: "/images/crucial_ddr5_ram.jpg",
      description: "Crucial's fastest DDR5 RAM modules for competitive tasks with great efficiency",
    },
	{
      url: "/images/nzxt_pc_case.jpg",
      description: "Get your PC to the next level with the best PC Cases out there from NZXT",
    },
	{
      url: "/images/corsair_icue_water_cooling.png",
      description: "Check out the unmatched thermal performance iCUE series water coolers from Corsair",
    },
	{
      url: "/images/intel_cpu_14th_generation.png",
      description: "The Intel® Core desktop processors (14th gen) deliver the ultimate immersive experience",
    },];

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
	  width: 100%;
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
	{#each [slideshow_images[current]] as item (item.url)}
	<div class="slide" transition:fade>
		<img src={item.url} alt={item.description} />
		<p class="description">{item.description}</p>
	  </div>
	{/each}

	<div class="buttons">
		<button on:click={prev}>❮</button>
		<button on:click={next}>❯</button>
	</div>
</div>
