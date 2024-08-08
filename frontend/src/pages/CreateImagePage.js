import React, { useState } from 'react';
import axios from 'axios';

const CreateImagePage = () => {
  const [prompt, setPrompt] = useState('');
  const [image, setImage] = useState(null);

  const handlePromptChange = (event) => {
    setPrompt(event.target.value);
  };

  const handleCreateImage = async () => {
    try {
      const response = await axios.post('http://localhost:8000/create-image', {
        prompt: prompt  // Убедитесь, что ключ 'prompt' используется здесь
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      setImage(response.data.message);
    } catch (error) {
      console.error('Error creating image:', error);
    }
  };
  

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Create an Image</h1>
      <input
        type="text"
        value={prompt}
        onChange={handlePromptChange}
        placeholder="Enter your prompt"
        style={{ padding: '10px', width: '300px', fontSize: '16px' }}
      />
      <button onClick={handleCreateImage} style={{ padding: '10px 20px', fontSize: '16px', marginLeft: '10px' }}>
        Generate Image
      </button>

      {image && (
        <div style={{ marginTop: '20px' }}>
          <h2>Generated Image</h2>
          <img src={image} alt="Generated" style={{ width: '300px', height: '300px' }} />
        </div>
      )}
    </div>
  );
};

export default CreateImagePage;
