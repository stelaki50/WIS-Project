<script>
    import Button from './button.svelte';
</script>

<style>
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
        font-size: 1.5rem;
        font-weight: bold;
        color: #222;
    }

    .nav-container {
        display: flex;
        align-items: center;
        margin-left: 30rem; /* space from title */
    }

    .nav-buttons {
        display: flex;
        gap: 8rem; /* space between buttons */
    }

    a {
        text-decoration: none;
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
        </div>
    </div>
</header>
