<script>
     export let product;
    function manageLike(){
        product.numOfLikes++;
    }
</script>

<div class="card">
    <h2>
        {product.name}
    </h2>
    <div class="image"> {product.img}</div>
    <div class="description">
        {product.description}
    </div>
    <div class="likes">
        <button class=likeButton on:click={manageLike}>Like</button>
        {product.numOfLikes}
    </div>
</div>

<style>
    .card{
        padding-left: 10px;
    }
    .likes{
        text-align: left;
        padding:10px;
    }
    .likeButton{
        background-color: rgb(0, 174, 255);
        border: 1px solid #53535390;
        outline-color: black;
    }
</style>