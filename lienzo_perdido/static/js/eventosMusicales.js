fetch('http://127.0.0.1:5000/api/eventos')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos recibidos de la API
    console.log(data);

    const tabla = document.getElementById('nuevos');
    const tbody = tabla.querySelector('section');
    

    data.forEach((registro) => {
      const lineaDivisora = document.createElement('div');
      lineaDivisora.classList.add('linea');
      const nuevaSeccion = document.createElement('section');
      nuevaSeccion.classList.add('expo');
      const celdaNombre = document.createElement('h3');
      const alinear = document.createElement('div');
      alinear.classList.add('alinear');
      const palabraFecha = document.createElement('h4');
      const celdaFecha = document.createElement('p');
      celdaFecha.classList.add('fecha');
      const celdaDescripcion = document.createElement('p');
      celdaNombre.textContent = registro.nombre ? registro.nombre.trim() : '';

      palabraFecha.textContent = "Fecha: ";
      celdaFecha.textContent = registro.fecha ? registro.fecha.trim() : '';
      celdaDescripcion.textContent = registro.descripcion ? registro.descripcion.trim() : '';

      nuevaSeccion.appendChild(lineaDivisora);
      nuevaSeccion.appendChild(alinear);
      nuevaSeccion.appendChild(celdaNombre);

      alinear.appendChild(palabraFecha);
      alinear.appendChild(celdaFecha);
      
      nuevaSeccion.appendChild(celdaDescripcion);

      tbody.appendChild(nuevaSeccion);
    });
  })
  .catch(error => {
    // Manejo de errores en caso de que la petición falle
    console.error('Error:', error);
  });
