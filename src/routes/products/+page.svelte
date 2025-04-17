<!--PRODUCTS PAGE-->

<script>
    import Products from "../../components/Products.svelte";
    import Button from "../../components/button.svelte";

    let Product = {
      img: '/products_images/gigabyte_rtx_5080_16gb.jpg',
      name: 'GIGABYTE GeForce RTX 5080 Gaming OC 16G Graphics Card, WINDFORCE Cooling System 16GB 256-bit GDDR7, GV-N5080GAMING OC-16GD Video Card',
      description: `Ahead of its time, ahead of the game is the GIGABYTE GeForce RTX 5080 GAMING OC 16G Graphics Cards. Powered by NVIDIA's
      new RTX architecture, the GIGABYTE GeForce RTX 5080 GAMING OC 16G brings stunning visuals, amazingly fast frame rates, and AI acceleration
      to games and creative applications with its enhanced RT Cores and Tensor Cores, along with a staggering 16 GB of GDDR7 memory.`,
      numOfLikes: 0
    }

    let Product1 = {
      img: '/products_images/ryzen9_9950x3d_cpu.jpg',
      name: 'AMD Ryzen™ 9 9950X 16-Core, 32-Thread Unlocked Desktop Processor',
      description: `Welcome to the new era of performance. AMD Ryzen 9000 Series ushers in the speed of “Zen 5” for gamers and creators with 
      pure power to tackle any game or workflow on the digital playground.`,
      numOfLikes: 0
    }

    let Product2 = {
      img: '/products_images/inteli9_14900K_cpu.jpg',
      name: 'Intel® Core™ i9-14900K Desktop Processor 24 cores (8 P-cores + 16 E-cores) up to 6.0 GHz',
      description: 'INTEL Core i9-14900K 3.2Ghz LGA1700 36MB Cache Box CPU',
      numOfLikes: 0
    }

    let Product3 = {
      img: '/products_images/inteli5_14600K_cpu.jpg',
      name: 'Intel® Core™ i5-14600K Desktop Processor 14 Cores (6 P-Cores + 8 E-Cores) up to 5.3 GHz',
      description: 'Intel® Core™ i5-14600K Desktop Processor 14 Cores (6 P-Cores + 8 E-Cores) up to 5.3 GHz',
      numOfLikes: 0
    }

    let Product4 = {
      img: '/products_images/nzxt_h9_elite_tower.jpg',
      name: 'NZXT H9 Elite Dual-Chamber ATX Mid-Tower PC Gaming Case – Includes 3 x 120mm F120 RGB Duo Fans with Controller– Glass Front, Top & Side Panels 360mm',
      description: `The H9 Elite is designed to cool o powerful GPUs with its expansive thermal capabilities, featuring a ten fan capacity and numerous 360mm radiator 
      mounting options. Show o every angle with a tempered glass top panel and a built-in RGB & Fan Controller. The unique wraparound glass design with a dual-chamber 
      layout is the perfect showcase for premium components.`,
      numOfLikes: 0
    }

    let Product5 = {
      img: '/products_images/crucial_ddr5_ram.jpg',
      name: 'Crucial Pro DDR5 RAM 32GB Kit (2x16GB) 6000MHz CL36, Overclocking Desktop Gaming Memory',
      description: `Push performance to the next level with the blazing speed and massive bandwidth of Crucial DDR5 Pro OC Gaming Memory. With support for next-gen 
      multi-core CPUs and the “sweet spot” speed of up to 6,400MHz, our gaming memory harnesses the power of low latency so you can beat the clock and focus on 
      outplaying your opponent instead of worrying about performance bottlenecks. `,
      numOfLikes: 0
    }

    let products = [Product, Product1, Product2, Product3, Product4, Product5]
    let variable = ""
    let filteredProducts = products

    function searchEngine(variable) {
      filteredProducts = products.filter((product) => product.name.includes(variable))
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
