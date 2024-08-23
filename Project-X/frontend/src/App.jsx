import axios from 'axios';
import axiosInstance from './axiosInstance.jsx'; // Ensure this path is correct
import axiosInstanceNoCredentials from './axiosInstanceNoCredentials.jsx'; // Correct path and extension
import { useState, useEffect } from 'react';

function App() {
  const [product, setProduct] = useState([]);
  const [responseMessage, setResponseMessage] = useState('');

  useEffect(() => {
    axiosInstanceNoCredentials.get('/products')
      .then(response => {
        console.log('API response:', response);
        setProduct(response.data);
      })
      .catch(error => {
        console.error('Error fetching products:', error);
      });
  }, []);

  const addToCart = async (productObj) => {
    try {
      console.log(productObj);
      const response = await axios.post('http://127.0.0.1:4000/add-to-cart/', {
        product_id: productObj.product.id,
        quantity: 1,
        description: productObj.product.description,
        category: productObj.product.category,
        price: productObj.product.price,
        image: productObj.product.image,
        title: productObj.product.title,
        rating: productObj.product.rating,
      }, {
        withCredentials: true,
      });

      console.log(response.data);
      setResponseMessage(response.data.message);
    } catch (error) {
      console.error('Error adding to cart:', error);
      setResponseMessage('Error adding to cart');
    }
  };

  return (
    <div className='product-container'>
      {responseMessage && (
        <div className='response-message'>
          {responseMessage}
        </div>
      )}

      {product.map((product) => (
        <div className='product-individual-container' key={product.id}>
          <h3>{product.title}</h3>
          <img src={`${product.image}`} alt="" className='product-image' />
          <p>{product.description}</p>
          <button onClick={() => addToCart({product})}>Add to Cart</button>
        </div>
      ))}
    </div>
  );
}

export default App;