fetch('http://127.0.0.1:5000/api/eventos')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos recibidos de la API
    console.log(data);

    const tabla = document.getElementById('nuevos');
    const tbody = tabla.querySelector('section');

    data.forEach((registro) => {
      const nuevaSeccion = document.createElement('section');
      nuevaSeccion.classList.add('expo');
      const celdaNombre = document.createElement('h3');
      const celdaDescripcion = document.createElement('p');
      const celdaFecha = document.createElement('p');
      const imagen = document.createElement('img'); // Crear elemento para la imagen

      celdaNombre.textContent = registro.nombre ? registro.nombre.trim() : '';
      celdaDescripcion.textContent = registro.descripcion ? registro.descripcion.trim() : '';
      celdaFecha.textContent = registro.fecha ? registro.fecha.trim() : '';

      // Decodificar la imagen de bytes y asignarla a la propiedad src del elemento img
      const imageBytes = registro.imagen ? Uint8Array.from(atob(registro.imagen), c => c.charCodeAt(0)) : null;
      if (imageBytes) {
        const blob = new Blob([imageBytes], { type: 'image/jpeg' });
        const imageUrl = URL.createObjectURL(blob);
        imagen.src = imageUrl;
      }

      nuevaSeccion.appendChild(celdaNombre);
      nuevaSeccion.appendChild(celdaDescripcion);
      nuevaSeccion.appendChild(celdaFecha);
      nuevaSeccion.appendChild(imagen); // Agregar la imagen a la sección

      tbody.appendChild(nuevaSeccion);
    });
  })
  .catch(error => {
    // Manejo de errores en caso de que la petición falle
    console.error('Error:', error);
  });