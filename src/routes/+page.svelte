<script>
  import Button from './button.svelte'
  import Header from './Header.svelte';
  import Footer from './Footer.svelte';
  import { images } from './imageData.js'
  import Slide from './images/Slide.svelte';



  let slides = [
		{ image: '/images/gpu.jpg', alt: 'Image 1', attr: 'Beautiful scenery' },
		{ image: '/images/box.jpg', alt: 'Image 2', attr: 'Sunset view' },
	];


 
	let current = 0;

	function next() {
		current = (current + 1) % slides.length;
	}

	function prev() {
		current = (current - 1 + slides.length) % slides.length;
	}

</script>


<main>
  
  <p class="eshop-title">PC-Parts e-Shop</p>  
  
</main>

<Header>


</Header>
<Button>Home</Button>



<Button>Product</Button>

<Footer>

</Footer>




<style>
 
 .eshop-title {
    font-size: 36px;
    font-weight: bold;
    margin: 10px 0 0 0; /* Reduce top space */
    color: #003835;
    text-align: center
  }
</style>


