const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const { exec } = require("child_process");
const fs = require("fs");

const app = express();
app.use(cors());
app.use(bodyParser.json({ limit: "10mb" }));

app.post("/run", async (req, res) => {
  const { variables, image } = req.body;
  const useCanvas = variables.includes("paint");

  if (useCanvas && image) {
    const buffer = Buffer.from(image.split(",")[1], "base64");
    fs.writeFileSync("backend/digit_canvas.png", buffer);
  }

  const command = `python3 backend/mainp.py ${variables.join(" ")}`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error ejecutando script: ${stderr}`);
      return res
        .status(500)
        .json({ output: `Error al ejecutar el script: ${stderr}` });
    }

    res.json({
      output: stdout.trim(),
      imageUrl: useCanvas ? "/predicted_image.png" : null,
    });
  });
});

app.listen(4002, () => {
  console.log("Servidor en puerto 4002");
});
