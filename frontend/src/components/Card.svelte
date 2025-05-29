<script>
    import { cart } from '$lib/stores/cart.js';
  import Button from './button.svelte';
    export let product;
    
    async function manageLike(){
        try {
            const response = await fetch('http://localhost:5000/api/likes', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ id: product._id })});

            if (!response.ok) {
                const errorData = await response.json();
                console.error('Error liking product:', errorData.error);
                return;
            }

            const data = await response.json();
            console.log('Like successful:', data);

            // After successful like, update the product's likes count locally
            product.likes += 1;

        } catch (error) {
            console.error('Error:', error);
        }
    }

    function handleClick(product) {
        console.log("Clicked product:", product);}

    function addToCart() {
        cart.update(current => {
        const existing = current.find(item => item._id === product._id);
        if (existing) {
            return current.map(item =>
                item._id === product._id
                    ? { ...item, quantity: item.quantity + 1 }
                    : item
            );
        } else {
            return [...current, { ...product, quantity: 1 }];}});}
        
</script>

<div class="card">

    <h4>
        <a href={`/products/${product._id}`}>
            {product.name}
        </a>
       </h4>

   <div class="content-row">
    <div class="image">
        <img src={`/products_images/${product.image}`} alt={product.name} />
    </div>

    <div class="description">
        {product.description}
    </div>
  </div>

   <div class="likes-price-cart">
    <button class=likeButton on:click={manageLike}>Like</button>
       {product.likes}

       <span class="priceTag">Price: {product.price}&euro;</span>

       <Button class="cart" on:click={addToCart}>Add to Cart</Button>

   </div>
   

</div>

<style>

.card{
    padding-left: 10px;
    margin-left: 40px;
    border: 1px solid black;
    border-radius: 10px;
    height: 220px;
    width: 90%;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
}

.likes-price-cart{
    text-align: left;
    padding: 10px;
}

.likeButton{
    background-color: rgb(0, 174, 255);
    border: 1px solid #53535390;
    border-radius: 10px;
    outline-color: black;
    cursor: pointer;
}

.image{
    display: flex;
    width: 70px;
    height: 70px;
}

.content-row {
    display: flex;
    align-items: center;
    gap: 15px; /* space between image and description */
}

.description{
    font-family: 'Ubuntu';
    font-size: 15px;
    flex: 1;
}

h4{
    font-family: 'Ubuntu';
    font-size: 18px;
}

a {
    color: #0a3331;
    text-decoration: none;
    cursor: pointer;
}

a:hover {
    text-decoration: underline;
}

.priceTag{
    font-family: 'Ubuntu';
    font-weight: bold;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
    margin-right: 15px;
    margin-left: 20px;
}

</style>
