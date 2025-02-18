import { useState } from "react";
import axios from "axios";

function App() {
  const [variables, setVariables] = useState("");
  const [scriptExecute, setScriptExecute] = useState("predict");
  const [output, setOutput] = useState(null);

  const handleRunScript = async () => {
    try {
      const fullVariables = scriptExecute + "," + variables;
      const response = await axios.post("http://localhost:4002/run", {
        variables: fullVariables.split(",").map((v) => v.trim()),
      });

      setOutput(response.data.output);
    } catch (error) {
      alert("Error al ejecutar el script");
      console.error(error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Script to execute</h1>

      <select
        value={scriptExecute}
        onChange={(e) => setScriptExecute(e.target.value)}
      >
        <option value="predict">Predict</option>
        <option value="train">Train Model</option>
      </select>

      {scriptExecute === "train" ? (
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
      )}

      <button onClick={handleRunScript}>Ejecutar</button>

      {output && <h2>Resultado: {output}</h2>}
    </div>
  );
}

export default App;
