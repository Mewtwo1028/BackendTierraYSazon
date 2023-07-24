fetch('http://127.0.0.1:5000/api/exposiciones')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos recibidos de la API
    console.log(data);

    const tabla = document.getElementById('tablaExposiciones');
    const tbody = tabla.querySelector('tbody');

    data.forEach((registro) => {
      const fila = document.createElement('tr');
      const celdaID = document.createElement('td');
      const celdaDescripcion = document.createElement('td');
      const celdaFecha = document.createElement('td');
      const celdaImagen = document.createElement('td');

      const img=document.createElement('img');
      img.src=registro.imagen;
      img.style.width = '50px'; 

      celdaID.textContent = registro.idExposicionCultural;
      celdaDescripcion.textContent = registro.descripcion ? registro.descripcion.trim() : '';
      celdaFecha.textContent = registro.fecha ? registro.fecha.trim() : '';
      celdaImagen.appendChild(img);

      fila.appendChild(celdaID);
      fila.appendChild(celdaDescripcion);
      fila.appendChild(celdaFecha);
      fila.appendChild(celdaImagen);

      tbody.appendChild(fila);
    });
  })
  .catch(error => {
    // Manejo de errores en caso de que la petición falle
    console.error('Error:', error);
  });
