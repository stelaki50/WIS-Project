<!-- src/components/Card.svelte -->
<script>
    export let title = "";
    export let body = "";
    export let image = "";
    import Button from "./button.svelte";
  </script>
  
<style>
  :root {
    --clr-neutral-900: hsl(207, 19%, 9%);
    --clr-neutral-100: hsl(0, 0%, 100%);
    --clr-accent-400: #003835;
  }
  
  .card {
    color: var(--clr-neutral-100);
    font-family: 'Ubuntu';
    background-size: cover;
    padding: 10rem 0 0;
    max-width: 35ch;
    border-radius: 0.5rem;
    overflow: hidden;
    transition: transform 500ms ease;
    margin-top: 6%;
    height: 150px;
    width: 60%;
    border-radius: 1rem;
	box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
  }
  
  .card:hover,
  .card:focus-within {
    transform: scale(1.05);
  }
  
  .card-content {
    --padding: 1.5rem;
    padding: var(--padding);
    background: linear-gradient(
      hsl(0 0% 0% / 0),
      hsl(20 0% 0% / 0.3) 20%,
      hsl(0 0% 0% / 1)
    );
  }
  
  .card:hover .card-content,
  .card:focus-within .card-content {
    transform: translateY(0);
    transition-delay: 500ms;
  }
  
  .card:focus-within .card-content {
    transition-duration: 0ms;
  }
  
  .card-content > :not(.card-title) {
    opacity: 0;
    transition: opacity 500ms linear;
  }
  
  .card:hover .card-content > :not(.card-title),
  .card:focus-within .card-content > :not(.card-title) {
    opacity: 1;
    transition-delay: 850ms;
  }
  
  .card-title {
    position: relative;
    width: max-content;
  }
  
  .card-title::after {
    content: "";
    position: absolute;
    height: 3px;
    left: calc(var(--padding) * -1);
    bottom: -2px;
    width: calc(100% + var(--padding));
    background: var(--clr-accent-400);
    transform-origin: left;
    transition: transform 1000ms ease;
    transform: scaleX(0);
  }
  
  .card:hover .card-title::after,
  .card:focus-within .card-title::after {
    transform: scaleX(1);
  }
  
  .card-body {
    color: rgb(255 255 255 / 0.8);
    font-weight: bold;
  }
  
  .button {
    cursor: pointer;
    display: inline-block;
    text-decoration: none;
    color: var(--clr-neutral-900);
    background-color: var(--clr-accent-400);
    padding: 0.5rem 1.25rem;
    border-radius: 0.25rem;
  }
  
  .button:hover,
  .button:focus {
    background-color: var(--clr-neutral-100);
  }
  
  @media (hover) {
    .card-content {
      transform: translateY(70%);
      transition: transform 500ms ease;
    }
  
    .card:hover .card-content,
    .card:focus-within .card-content {
      transform: translateY(0);
      transition-delay: 500ms;
    }
  
    .card:focus-within .card-content {
      transition-duration: 0ms;
    }
  
    .card-content > * /*:not(.card-title)*/ {
      opacity: 0;
      transition: opacity 500ms linear;
    }
  
    .card:hover .card-content > *,
    .card:focus-within .card-content > * {
      opacity: 1;
      transition-delay: 850ms;
    }
  
    .card-title::after {
      transform: scaleX(0);
    }
  }
  </style>
  
  <div class="card" style={`background-image: url('${image}')`}>
    <div class="card-content">
      <h2 class="card-title">{title}</h2>
      <p class="card-body">{body}</p>
      <Button>Learn More</Button>
    </div>
  </div>
  