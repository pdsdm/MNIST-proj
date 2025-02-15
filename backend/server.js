const express = require("express");
const cors = require("cors");
const { exec } = require("child_process");

const app = express();
app.use(cors());
app.use(express.json());

app.use("/static", express.static("static"));

app.post("/run", (req, res) => {
  const { variables } = req.body;
  const command = `python3 backend/mainp.py ${variables.join(" ")}`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      return res.status(500).json({ output: "Error al ejecutar el script" });
    }

    res.json({
      output: stdout.trim(),
      imageUrl: "http://localhost:4002/static/predicted_image.png",
    });
  });
});

app.listen(4002, () => {
  console.log("Servidor en puerto 4002");
});
