import { useState } from "react";
import axios from "axios";

function App() {
  const [variables, setVariables] = useState("");
  const [output, setOutput] = useState(null);

  const handleRunScript = async () => {
    try {
      const response = await axios.post("http://localhost:4002/run", {
        variables: variables.split(",").map((v) => v.trim()),
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
      <input
        type="text"
        placeholder="Introduce variables separadas por comas"
        onChange={(e) => setVariables(e.target.value)}
      />

      <button onClick={handleRunScript}>Ejecutar</button>

      {output && <h2>Resultado: {output}</h2>}
    </div>
  );
}

export default App;
