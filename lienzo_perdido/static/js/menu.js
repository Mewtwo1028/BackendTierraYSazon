fetch('http://127.0.0.1:5000/api/menu/entrada')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos recibidos de la API
    console.log(data);

    const menuEntradas = document.getElementById('entradas');
    const tbody = menuEntradas.querySelector('ul');
    

    data.forEach((registro) => {
      const entrada = document.createElement('li');
      const nombreEntrada = document.createElement('span');
      nombreEntrada.classList.add('nombre-platillo');
      const precioEntrada = document.createElement('span');
      precioEntrada.classList.add('precio');


      nombreEntrada.textContent = registro.nombre ? registro.nombre.trim(): '';
      precioEntrada.textContent = "$"+registro.precio;

      menuEntradas.appendChild(entrada);
      entrada.appendChild(nombreEntrada);
      entrada.appendChild(precioEntrada);
      tbody.appendChild(entrada);
    });
  })
  .catch(error => {
    // Manejo de errores en caso de que la petición falle
    console.error('Error:', error);
  });
