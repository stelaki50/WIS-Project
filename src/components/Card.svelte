<script>
    export let product;

    async function manageLike(){
        console.log("Like pressed")
    }

    function handleClick(product) {
        console.log("Clicked product:", product);
    }
</script>

<div class="card">

   <h4>
    <a href="#" on:click={() => handleClick(product)}>
        {product.name}
      </a>
   </h4>

   <div class="content-row">
    <div class="image">
        <img src={`http://localhost:5000/static/products_images/${product.image}`} alt={product.name} />
    </div>

    <div class="description">
        {product.description}
    </div>
  </div>

   <div class="likes-price-cart">
       <button class=likeButton on:click={manageLike}>Like</button>
       {product.likes}

       <span class="priceTag">Price: {product.price}&euro;</span>

       <button class=cart>Add to Cart</button>
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
    flex: 1;
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

.cart{
    border: 1px solid black;
    border-radius: 10px;
    font-weight: bold;
    cursor: pointer;
}

</style>
