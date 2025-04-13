<script>
    export let type = 'primary';
    export let flat = false;
    export let inverse = false;

</script>

<button class = "{type} ">
<slot>

</slot>
</button>

<style>

    button{
        font-size: 15px;
      padding: 15px 40px;
      background-color: #003835;
      color: rgb(255, 255, 255);
      border: none;
      border-radius: 5px;
      margin: 5px;
      cursor: pointer;
      position: relative;
      top: 10px;
      left: 1300px;
    }
   
  
</style>
