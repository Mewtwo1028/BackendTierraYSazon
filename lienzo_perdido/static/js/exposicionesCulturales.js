fetch('http://127.0.0.1:5000/api/exposiciones')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos recibidos de la API
    console.log(data);

    const tabla = document.getElementById('nuevos');
    const tbody = tabla.querySelector('section');
    

    data.forEach((registro) => {
      const lineaDivisora = document.createElement('div');
      const nuevaSeccion = document.createElement('section');
      const celdaNombre = document.createElement('h3');
      const alinear = document.createElement('div');
      const palabraFecha = document.createElement('h4');
      const celdaFecha = document.createElement('p');
      const celdaDescripcion = document.createElement('p');
      const celdaImagen = document.createElement('div');
      const imagen = document.createElement('img');

      //Agregar clase a los elementos
      lineaDivisora.classList.add('linea');
      nuevaSeccion.classList.add('expo');
      alinear.classList.add('alinear');
      celdaFecha.classList.add('fecha');
      celdaImagen.classList.add('imagen');
    
      celdaNombre.textContent = registro.nombre ? registro.nombre.trim() : '';
      palabraFecha.textContent = "Fecha: ";
      celdaDescripcion.textContent = registro.descripcion ? registro.descripcion.trim() : '';
      celdaFecha.textContent = registro.fecha ? registro.fecha.trim() : '';

      // Decodificar la imagen de bytes y asignarla a la propiedad src del elemento img
      const imageBytes = registro.imagen ? Uint8Array.from(atob(registro.imagen), c => c.charCodeAt(0)) : null;
      if (imageBytes) {
        const blob = new Blob([imageBytes], { type: 'image/jpeg' });
        const imageUrl = URL.createObjectURL(blob);
        imagen.src = imageUrl;
      }

      nuevaSeccion.appendChild(lineaDivisora);
      nuevaSeccion.appendChild(alinear);
      nuevaSeccion.appendChild(celdaNombre);
      nuevaSeccion.appendChild(celdaDescripcion);
      nuevaSeccion.appendChild(celdaImagen);
      celdaImagen.appendChild(imagen); // Agregar la imagen a la sección

      alinear.appendChild(palabraFecha);
      alinear.appendChild(celdaFecha);

      tbody.appendChild(nuevaSeccion);
    });
  })
  .catch(error => {
    // Manejo de errores en caso de que la petición falle
    console.error('Error:', error);
  });
