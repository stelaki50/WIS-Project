<script>
	import Header from "./components/Header.svelte";
	import Footer from "./components/Footer.svelte";
	import Products from "./components/ProductsList.svelte";
	let Product={
        img:'TEMP-IMG',
        name:'NAME',
        description:'this grapchics card is really good blah blah blah latest technology yada yada yada djkfhg dkjfhg skdfhs sdkjfhs skjdfh skjdjhf sjd dfhsjskdhd f',
		numOfLikes:0
    }
	let Product1={
        img:'TEMP-IMG',
        name:'NAME2',
        description:'this grapchics card is really godkjfhs skjdfh skjdjhf sjd dfhsjskdhd f',
		numOfLikes:2
    }
    let products= [Product,Product,Product,Product1,Product,Product]
	let variable = ""
	let filteredProducts = products;
	function searchEngine(variable) {
		filteredProducts = products.filter((product)=> product.name.includes(variable))
}
</script>

<Header/>

<main>
	<div class="search">
		<input type="text" bind:value={variable} placeholder="Search..." />
		<button on:click = {searchEngine(variable)}>Search</button>

	</div>
	<div class="product-list">
		<Products {filteredProducts}/>
	</div>
</main>

<Footer/>

<style>
	:global(body) { margin: 0; padding: 0; }
	main {
		text-align: left;
		margin: 20 auto;
		padding-bottom: 20px;;
		background-color: #8FD6E3;
		min-height: 600px;
	}

	.product-list{
		padding-left: 20px;
		padding-right: 20px;
	}
	.search{
		padding: 20px;
		padding-bottom: 5px;
		text-align: center;
	}
	input{
		max-width: 300px;
		width: 80%;
	}
	button{
		min-width: 80px;
		text-align: center;
		width: 10%;
	}
</style>