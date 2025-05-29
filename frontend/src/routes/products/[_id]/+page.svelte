<script>
  export let data;
  let { product } = data;

  let quantity = 1; //The amount of products somone wants to add in their card

  function increase(){
    quantity = quantity+1;
  }
  function decrease() {
    if (quantity > 1)
        quantity = quantity - 1;
  }

  function addToCard(){
    console.log("added to card");
  }
</script>

<div class="product-container">
  <div class="product-image">
    <img src={`/products_images/${product.image}`} alt={product.name} />
  </div>

  <div class="product-details">
    <h2>{product.name}</h2>
    <p class="price">&euro;{product.price}</p>
    
    <div class="quantity-selector">
      <button on:click={decrease}>-</button>
      <span>{quantity}</span>
      <button on:click={increase}>+</button>
    </div>

    <button class="add-to-cart" on:click={addToCart}>
      Add to Cart
    </button>

    <h3 class="description-title">Details</h3>
    <p class="description">{product.description}</p>

  </div>
</div>

<style>
.product-container {
  display: flex;
  grid-template-columns: 1fr 1.4fr;
  gap: 1rem;
  align-items: start;
  padding: 1rem;
  gap: 3rem; 
  margin-left: 3rem;
  
}
.product-image {
  flex: 0 0 600px;         
}

.product-image img {
  width: 100%;    
  height: auto;
  border-radius: 8px;
}
.product-details {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  max-width: 800px; 

}
.price {
  font-weight: bold;
  color: #2d6a4f;
  font-size: 1.2rem;
}

.description {
  color: #555;
  font-size: 1.2rem;
  line-height: 1.5;
  
  margin-bottom: 0.3rem
}

.quantity-selector {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 1rem;
}

.quantity-selector button {
  width: 32px;
  height: 32px;
  font-size: 1.2rem;
  font-weight: bold;
  background-color: #eee;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
}

.quantity-selector span {
  min-width: 24px;
  text-align: center;
  font-size: 1rem;
}

.add-to-cart{
  margin-top: 1rem;
  padding: 0.5rem 1em;  
  font-size: 0.9rem;  
  
  max-width: fit-content;   
  display: inline-block;    


  background-color: #407a91;
  color: white;
  border: none;
  border-radius: 10px;
  font-weight: bold;
  cursor: pointer;

}

.description-title {
  font-weight: bold;
  font-size: 1.4rem;
  margin-top: 2rem;
  color: #333;
}
</style>