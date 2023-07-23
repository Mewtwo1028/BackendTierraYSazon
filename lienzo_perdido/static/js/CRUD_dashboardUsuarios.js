fetch('http://127.0.0.1:5000/api/usuarios')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos recibidos de la API
    console.log(data);

    const tabla = document.getElementById('tablaUsuarios');
    const tbody = tabla.querySelector('tbody');

    data.forEach((registro) => {
      const fila = document.createElement('tr');
      const celdaID = document.createElement('td');
      const celdaNombre = document.createElement('td');
      const celdaContra = document.createElement('td');

      celdaID.textContent = registro.id;
      celdaNombre.textContent = registro.nombre ? registro.nombre.trim() : '';
      celdaContra.textContent = registro.contra ? registro.contra.trim() : '';

      fila.appendChild(celdaID);
      fila.appendChild(celdaNombre);
      fila.appendChild(celdaContra);

      tbody.appendChild(fila);
    });
  })
  .catch(error => {
    // Manejo de errores en caso de que la petición falle
    console.error('Error:', error);
  });
