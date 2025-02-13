const express = require("express");
const cors = require("cors");
const { exec } = require("child_process");

const app = express();
app.use(express.json());
app.use(cors());

app.post("/run", (req, res) => {
  const { variables } = req.body;
  const command = `python3 backend/mainp.py ${variables.join(" ")}`;

  console.log("Ejecutando comando:", command);

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error("Error al ejecutar el script:", stderr);
      return res.status(500).json({ error: stderr });
    }
    console.log("Salida del script:", stdout);
    res.json({ output: stdout.trim() });
  });
});

app.listen(4002, () =>
  console.log("Servidor corriendo en http://localhost:4002")
);
