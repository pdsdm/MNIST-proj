import { useState } from "react";
import axios from "axios";
import Canvas from "./Canvas"; // Importamos el canvas

function App() {
  const [variables, setVariables] = useState("");
  const [scriptExecute, setScriptExecute] = useState("predict");
  const [output, setOutput] = useState(null);
  const [imageUrl, setImageUrl] = useState(null);
  const [canvasImage, setCanvasImage] = useState(null);

  const handlePrediction = async (imageData) => {
    setCanvasImage(imageData); // Guardar la imagen en Base64 temporalmente
  };

  const handleRunScript = async () => {
    try {
      const fullVariables = scriptExecute + (variables ? `,${variables}` : "");
      const payload = {
        variables: fullVariables.split(",").map((v) => v.trim()),
      };

      if (scriptExecute === "paint" && canvasImage) {
        payload.image = canvasImage; // Enviar la imagen si se usa paint
      }

      const response = await axios.post("http://localhost:4002/run", payload);

      setOutput(response.data.output);
      setImageUrl(
        scriptExecute === "predict" || scriptExecute === "paint"
          ? `/predicted_image.png?timestamp=${new Date().getTime()}`
          : null
      );
    } catch (error) {
      alert("Error al ejecutar el script");
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Script to execute</h1>

      <select
        value={scriptExecute}
        onChange={(e) => setScriptExecute(e.target.value)}
      >
        <option value="predict">Predict</option>
        <option value="train">Train Model</option>
        <option value="paint">Paint</option>
      </select>

      {scriptExecute !== "paint" &&
        (scriptExecute === "train" ? (
          <input
            type="text"
            placeholder="Introduce variables separadas por comas"
            value={variables}
            onChange={(e) => setVariables(e.target.value)}
          />
        ) : (
          <input
            type="number"
            placeholder="Introduce un número"
            value={variables}
            onChange={(e) => setVariables(e.target.value)}
          />
        ))}

      {scriptExecute === "paint" && <Canvas onPredict={handlePrediction} />}

      <button onClick={handleRunScript}>Ejecutar</button>

      {output && <h2>Resultado: {output}</h2>}

      {imageUrl && scriptExecute === "predict" && (
        <div className="img-on-disp">
          <img src={imageUrl} alt="Predicción" width="200" />
        </div>
      )}
    </div>
  );
}

export default App;
