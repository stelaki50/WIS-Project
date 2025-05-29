export async function load({ params, fetch }) {
    const { _id } = params;
  
    try {
      const res = await fetch(`http://localhost:5000/api/products/${_id}`);
  
      if (!res.ok) {
        throw new Error('Failed to fetch product');
      }
  
      const product = await res.json();
  
      return { product };
    } catch (error) {
      console.error('Error loading product:', error);
      return { product: null };
    }
  }
  