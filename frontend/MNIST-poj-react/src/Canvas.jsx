import { useRef, useState, useEffect } from "react";

function Canvas({ onPredict }) {
  const canvasRef = useRef(null);
  const [isDrawing, setIsDrawing] = useState(false);

  useEffect(() => {
    resetCanvas(); // Inicializar con fondo blanco
  }, []);

  const resetCanvas = () => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
  };

  const startDrawing = (e) => {
    setIsDrawing(true);
    draw(e); // Evitar que el primer clic no dibuje
  };

  const draw = (e) => {
    if (!isDrawing) return;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    const x = (e.clientX - rect.left) * scaleX;
    const y = (e.clientY - rect.top) * scaleY;

    ctx.fillStyle = "black";
    ctx.beginPath();
    ctx.arc(x, y, 1, 0, Math.PI * 2);
    ctx.fill();
  };

  const stopDrawing = () => {
    setIsDrawing(false);
  };

  const clearCanvas = () => {
    resetCanvas(); // Usar la función para limpiar el canvas correctamente
  };

  const predictNumber = () => {
    const canvas = canvasRef.current;
    const imageData = canvas.toDataURL("image/png"); // Exportar imagen en Base64
    onPredict(imageData); // Enviar imagen al backend
  };

  return (
    <div className="cubo-orig">
      <canvas
        ref={canvasRef}
        width={28}
        height={28}
        style={{
          border: "1px solid black",
          background: "white",
          width: "280px",
          height: "280px",
          imageRendering: "pixelated",
        }}
        onMouseDown={startDrawing}
        onMouseMove={draw}
        onMouseUp={stopDrawing}
        onMouseOut={stopDrawing}
      />
      <button onClick={clearCanvas}>Limpiar</button>
      <button onClick={predictNumber}>Predecir</button>
    </div>
  );
}

export default Canvas;
