const express = require("express");
const cors = require("cors");
const { exec } = require("child_process");

const app = express();
app.use(cors());
app.use(express.json());

app.post("/run", (req, res) => {
  const { variables } = req.body;
  const command = `python3 backend/mainp.py ${variables.join(" ")}`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error ejecutando script: ${stderr}`);
      return res
        .status(500)
        .json({ output: `Error al ejecutar el script: ${stderr}` });
    }
    console.log(`Salida del script: ${stdout}`);
    res.json({ output: stdout.trim() });
  });
});

app.listen(4002, () => {
  console.log("Servidor en puerto 4002");
});
