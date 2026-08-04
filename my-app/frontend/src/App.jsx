import React, { useState } from 'react'
import  Header  from "./components/Header/Header.jsx"
import ImageGrid from "./components/ImageGrid/ImageGrid.jsx"
import "./App.css"

export default function App() {
  const [images, setImages] = useState([]);

  return (
    <div  className="app">

       <Header setImages={setImages}/>
       <ImageGrid images={images} setImages={setImages} />

    </div>


  );
}


