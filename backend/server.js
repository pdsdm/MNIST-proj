const express = require("express");
const cors = require("cors");
const { exec } = require("child_process");

const app = express();
app.use(express.json());
app.use(cors());

app.post("/predict", (req, res) => {
  exec("python3 backend/script/predict.py", (error, stdout, stderr) => {
    if (error) {
      res.status(500).json({ error: stderr });
    } else {
      res.json({ prediction: stdout.trim() });
    }
  });
});

app.listen(4002, () =>
  console.log("Servidor corriendo en http://localhost:4002")
);
