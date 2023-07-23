fetch('http://127.0.0.1:5000/api/menu')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos recibidos de la API
    console.log(data);

    const tabla = document.getElementById('tablaMenu');
    const tbody = tabla.querySelector('tbody');

    data.forEach((registro) => {
      const fila = document.createElement('tr');
      const celdaID = document.createElement('td');
      const celdaNombre = document.createElement('td');
      const celdaDescripcion = document.createElement('td');
      const celdaTipo = document.createElement('td');
      const celdaPrecio = document.createElement('td');

      celdaID.textContent = registro.idMenu;
      celdaNombre.textContent = registro.nombre;
      celdaTipo.textContent = registro.tipo ;
      celdaPrecio.textContent = registro.precio ;
      celdaDescripcion.textContent = registro.descripcion;

      fila.appendChild(celdaID);
      fila.appendChild(celdaNombre);
      fila.appendChild(celdaTipo);
      fila.appendChild(celdaPrecio);
      fila.appendChild(celdaDescripcion);
   


      tbody.appendChild(fila);
    });
  })
  .catch(error => {
    // Manejo de errores en caso de que la petición falle
    console.error('Error:', error);
  });
