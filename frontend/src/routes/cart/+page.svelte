<script>
    import { cart } from '$lib/stores/cart.js';
    import { onDestroy } from 'svelte';
    import Button from '../../components/button.svelte';

    let items = [];

    // Subscribe to the cart store
    const unsubscribe = cart.subscribe(value => {
        items = value;});

    onDestroy(() => {
        unsubscribe();});

    function increaseQty(productId) {
        cart.update(current =>
            current.map(item =>
                item._id === productId ? { ...item, quantity: item.quantity + 1 } : item));}

    function decreaseQty(productId) {
        cart.update(current =>
            current
                .map(item =>
                    item._id === productId
                        ? { ...item, quantity: item.quantity - 1 }
                        : item).filter(item => item.quantity > 0));}

    function removeItem(productId) {
        cart.update(current => current.filter(item => item._id !== productId));}

</script>

<style>

main{
    background-color: #8FD6E3;
	height: 100%;
    font-family: 'Ubuntu';
    margin: 0;
    min-height: 40vh;
    display: grid;
}

.shopping-cart-title, .empty-cart-msg{
    place-content: center;
    text-align: center;
}

.shopping-cart-title{
    font-size: 40px;
}

.cart-item {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
    border: 1px solid #afa6a6;
    padding: 10px;
    border-radius: 12px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    width: 50%;
    align-items: center;
}

img {
    width: 100px;
    height: 100px;
    object-fit: contain;
}

.total-price-buy{
    font-size: 40px;
    width: 40%;
    text-align: center;
    
}


</style>

<main>

<h2 class="shopping-cart-title">Shopping Cart</h2>

{#if items.length === 0}
    <p class="empty-cart-msg">Your cart is empty.</p>
{:else}
<ul>
    {#each $cart as item (item._id)}
      <li class="cart-item">
        <img src={`/products_images/${item.image}`} alt={item.name} />
        <div class="details">
            <h2>{item.name}</h2>
            <p>{item.description}</p>
            <p><strong>Price:</strong> {item.price}€</p>
            <p><strong>Quantity:</strong> {item.quantity}</p>
            <Button on:click={() => increaseQty(item._id)} class="add-sub">+</Button>
            <Button on:click={() => decreaseQty(item._id)} class="add-sub">-</Button>
            <Button on:click={() => removeItem(item._id)} class="rmv">Remove</Button>
        </div>
      </li>
    {/each}
  </ul>

  <div class="total-price-buy">
    <h3>Total price: 
        {items.reduce((total, item) => total + item.price * item.quantity, 0)}€</h3>
    <Button>Proceed to checkout</Button></div>

{/if}

</main>