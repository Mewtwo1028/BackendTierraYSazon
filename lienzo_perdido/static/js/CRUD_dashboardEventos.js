fetch('http://127.0.0.1:5000/api/eventos')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos recibidos de la API
    console.log(data);

    const tabla = document.getElementById('tblEventos');
    const tbody = tabla.querySelector('tbody');

    data.forEach((registro) => {
      const fila = document.createElement('tr');
      const celdaID = document.createElement('td');
      const celdaNombre = document.createElement('td');
      const celdaDescripcion = document.createElement('td');
      const celdaFecha = document.createElement('td');
      const celdaImagen = document.createElement('td');
      const imagen=document.createElement('img');

            // Decodificar la imagen de bytes y asignarla a la propiedad src del elemento img
            const imageBytes = registro.imagen ? Uint8Array.from(atob(registro.imagen), c => c.charCodeAt(0)) : null;
            if (imageBytes) {
              const blob = new Blob([imageBytes], { type: 'image/jpeg' });
              const imageUrl = URL.createObjectURL(blob);
              imagen.src = imageUrl;
              imagen.style.width='100px';
            }


      celdaID.textContent = registro.idEvento;
      celdaNombre.textContent = registro.nombre ? registro.nombre.trim() : ''; 
      celdaDescripcion.textContent = registro.descripcion ? registro.descripcion.trim() : '';
      celdaFecha.textContent = registro.fecha ? registro.fecha.trim() : '';
      
      celdaImagen.appendChild(imagen);
      fila.appendChild(celdaID);
      fila.appendChild(celdaNombre);
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
