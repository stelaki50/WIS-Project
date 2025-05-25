import { writable } from 'svelte/store';

let initialCart = [];

if (typeof window !== 'undefined') {
    const storedCart = localStorage.getItem('cart');
    if (storedCart) {
        initialCart = JSON.parse(storedCart);}}

export const cart = writable(initialCart);

if (typeof window !== 'undefined') {
    cart.subscribe(value => {
        localStorage.setItem('cart', JSON.stringify(value));});}
