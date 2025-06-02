
<script>
    import { cart } from '$lib/stores/cart.js';
    export let data;
    let { product } = data;
    let showPopup = false;
  
    let quantity = 1; //The amount of products somone wants to add in their card
  
    function increase(){
      quantity = quantity+1;
    }
    function decrease() {
      if (quantity > 1)
          quantity = quantity - 1;
    }

    function addToCart() {
        cart.update(current => {
        const existing = current.find(item => item._id === product._id);
        if (existing) {
            return current.map(item =>
                item._id === product._id
                    ? { ...item, quantity: quantity + 1 }
                    : item
            );
        } else {
            return [...current, { ...product, quantity }];}});
        
        showPopup = true;
        setTimeout(() => {
        showPopup = false;}, 2000);}

   
  </script>
  
  <main>
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
  
      <button class="add-to-cart" on:click={addToCart}>Add to Cart</button>


      <h3 class="description-title">Details</h3>
      <p class="description">{product.description}</p>
  
    </div>
  </div>

        {#if showPopup}
        <div class="popup">Product successfully added to cart!</div>
        {/if}

  </main>

  <style>

    main{
      background-color: #8FD6E3;
    }
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

  .popup {
  position: fixed;
  top: 20px;
  right: 20px;
  background-color: #4caf50;
  color: white;
  padding: 12px 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.2);
  z-index: 1000;
  font-family: 'Ubuntu';
  font-size: 14px;
  }
  </style>
  