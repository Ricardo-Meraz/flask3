<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Predicción de Precio de Laptop</title>

    <script>
        function predecirPrecio(event) {
            event.preventDefault();

            const formData = new FormData(document.getElementById("formulario"));

            fetch("/predict", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    document.getElementById("resultado").innerText = data.error;
                } else {
                    document.getElementById("resultado").innerText =
                        "Precio estimado: $" + data.precio;
                }
            });
        }
    </script>
</head>
<body>

    <h1>Predicción de Precio de Laptop</h1>

    <form id="formulario" onsubmit="predecirPrecio(event)">

        <label>Marca:</label>
        <input type="text" name="brand" required>
        <br><br>

        <label>Velocidad Procesador (GHz):</label>
        <input type="number" step="0.1" name="processor_speed" required>
        <br><br>

        <label>RAM (GB):</label>
        <input type="number" name="ram_size" required>
        <br><br>

        <label>Almacenamiento (GB):</label>
        <input type="number" name="storage_capacity" required>
        <br><br>

        <label>Tamaño Pantalla:</label>
        <input type="number" step="0.1" name="screen_size" required>
        <br><br>

        <label>Peso (kg):</label>
        <input type="number" step="0.1" name="weight" required>
        <br><br>

        <input type="submit" value="Predecir">

    </form>

    <h2 id="resultado"></h2>

</body>
</html>