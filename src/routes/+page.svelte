<!-- MAIN/HOME PAGE -->
<script>
  	import Slide from '../components/Slide.svelte';
	import CardsHover from '../components/Cards_Hover.svelte';

</script>

<main>

	<h2>Explore the Future: Top Tech Picks for Your Next Build</h2>

  	<Slide/>

	<div class="cards_hover_container">

		<CardsHover title="A Gift from Us"
		body="For every purchase > 120$ you get a gift from us: ASUS 120mm ARGB PWM Chassis Fan"
		image="/images/cards_hover/pc_case_fan_gift_from_us.jpg"/>

		<CardsHover title="Item Combo Promotion"
		body="Add 4 or more items to your cart and enjoy 20% off each one!"
		image="/images/cards_hover/20_percent_off_promotion.png"/>

		<CardsHover title="1 Year Warranty"
		body="We've got your back! All purchases come with a 1-year warranty covering defects and malfunctions—no stress, no hassle."
		image="/images/cards_hover/1_year_warranty.png"/>
		
		<CardsHover title="Free Shipping"
		body="Enjoy fast, reliable delivery at no extra cost. We offer free shipping on all orders—no minimum required."
		image="/images/cards_hover/free_shipping.jpg"/>

	</div>
	

</main>

<style>

main{
	background-color: #8FD6E3;
	height: 100%;
}

h2{
	font-family: 'Ubuntu', sans-serif;
	font-size: 25px;
	position: relative;
	width: 650px;
	height: 10px;
	margin: 0 auto;
	padding-top: 70px;
}

.cards_hover_container{
	display: flex;
	align-items: flex-start;
	gap: 7rem;
	padding: 2rem;
	margin-left: 4%;
	flex-wrap: wrap;
}
 
</style>
