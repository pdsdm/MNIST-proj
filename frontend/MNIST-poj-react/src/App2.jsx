import { useState } from "react";
import axios from "axios";
import Canvas from "./Canvas"; // Importamos el componente Canvas

function App() {
  const [prediction, setPrediction] = useState(null);

  const handlePrediction = async (imageData) => {
    try {
      const response = await axios.post("http://localhost:4002/predict-image", {
        image: imageData,
      });

      setPrediction(response.data.prediction);
    } catch (error) {
      alert("Error al predecir el número");
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Reconocimiento de Números</h1>
      <Canvas onPredict={handlePrediction} />
      {prediction !== null && <h2>Predicción: {prediction}</h2>}
    </div>
  );
}

export default App;
