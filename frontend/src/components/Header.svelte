<script>
    import Button from './button.svelte';
</script>

<style>

    :root{
    --gradient: linear-gradient(
        45deg,
        #845ec2,
        #d65db1,
        #ff6f91,
        #ff9671,
        #ffc75f,
        #f9f871);
    }

    header {
        display: flex;
        align-items: center;
        padding: 1rem 2rem;
        background-color: #f8f8f8;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        font-family: 'Ubuntu', sans-serif;
    }

    .logo-section {
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .logo-img {
        width: 60px;
        height: 60px;
        object-fit: cover;
    }

    .site-title {
    font-weight: 900;
    font-style: 'Ubuntu';
    font-size: 1.5rem;
    color: #ee6352;
    margin: 0;
    background-image: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-size: 300%;
    animation: bg-animation 10s infinite alternate;
    }

    @keyframes bg-animation{
        0% {background-position: left;}
        100% {background-position: right;}
    }

    .nav-container {
        display: flex;
        align-items: center;
        margin-left: 30rem; /* space from title */
    }

    .nav-buttons {
        display: flex;
        gap: 5rem; /* space between buttons */
    }

    a {
        text-decoration: none;
    }

    .cart-img{
        width: 60px;
        height: 45px;
    }

    .cart-tooltip {
        position: relative;
        display: inline-block;
        cursor: pointer;
    }

    .tooltip-text {
        visibility: hidden;
        width: 80px;
        background-color: black;
        color: #fff;
        text-align: center;
        border-radius: 5px;
        padding: 5px 0;

        /* Position the tooltip */
        position: absolute;
        bottom: -50%; /* show above the image */
        left: 50%;
        transform: translateX(-50%);

        /* Smooth fade-in */
        opacity: 0;
        transition: opacity 0.3s;
        font-size: 14px;
        z-index: 10;
    }

    .cart-tooltip:hover .tooltip-text {
        visibility: visible;
        opacity: 1;
    }

</style>


<header>
    <div class="logo-section">
        <img src="/images/main_logo_img.jpg" alt="Logo" class="logo-img" />
        <h1 class="site-title">PCPartakias e-shop</h1>
    </div>

    <div class="nav-container">
        <div class="nav-buttons">
            <a href="/"><Button>Home</Button></a>
            <a href="/products/"><Button>Products</Button></a>
            <a href="/services"><Button>Services</Button></a>
            <a href="/about"><Button>About Us</Button></a>
            <a href="/cart" class="cart-tooltip">
                <img class="cart-img" src="images/shopping_cart_img.png" alt="shopping_cart_img"/>
                <span class="tooltip-text">View Cart</span></a>
        </div>
    </div>
</header>
