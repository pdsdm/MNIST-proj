import { useState } from "react";
import axios from "axios";
import train_csv from "../../../dataset/csv/train.csv";
import test_csv from "../../../dataset/csv/test.csv";

function App() {
  const [script, setScript] = useState("");
  const [variables, setVariables] = useState("");
  const [output, setOutput] = useState(null);

  const handleRunScript = async () => {
    if (!script) return alert("Selecciona un script");

    try {
      const response = await axios.post("http://localhost:4002/run", {
        script,
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
      <h1>Ejecutar Script</h1>
      <select onChange={(e) => setScript(e.target.value)}>
        <option value="">Selecciona un script</option>
        <option value="predict">Predict</option>
        <option value="train">Train</option>
      </select>

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
