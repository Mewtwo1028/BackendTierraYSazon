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

  fetch('http://127.0.0.1:5000/api/menu/platillo')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos recibidos de la API
    console.log(data);

    const menuPlatillo = document.getElementById('platillos');
    const tbody = menuPlatillo.querySelector('ul');
    

    data.forEach((registro) => {
      const platillo = document.createElement('li');
      const nombrePlatillo = document.createElement('span');
      nombrePlatillo.classList.add('nombre-platillo');
      const precioPlatillo = document.createElement('span');
      precioPlatillo.classList.add('precio');


      nombrePlatillo.textContent = registro.nombre ? registro.nombre.trim(): '';
      precioPlatillo.textContent = "$"+registro.precio;

      menuPlatillo.appendChild(platillo);
      platillo.appendChild(nombrePlatillo);
      platillo.appendChild(precioPlatillo);
      tbody.appendChild(platillo);
    });
  })
  .catch(error => {
    // Manejo de errores en caso de que la petición falle
    console.error('Error:', error);
  });

  fetch('http://127.0.0.1:5000/api/menu/bebida')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos recibidos de la API
    console.log(data);

    const menuBebida = document.getElementById('bebidas');
    const tbody = menuBebida.querySelector('ul');
    

    data.forEach((registro) => {
      const bebida = document.createElement('li');
      const nombreBebida = document.createElement('span');
      nombreBebida.classList.add('nombre-platillo');
      const precioBebida = document.createElement('span');
      precioBebida.classList.add('precio');


      nombreBebida.textContent = registro.nombre ? registro.nombre.trim(): '';
      precioBebida.textContent = "$"+registro.precio;

      menuBebida.appendChild(bebida);
      bebida.appendChild(nombreBebida);
      bebida.appendChild(precioBebida);
      tbody.appendChild(bebida);
    });
  })
  .catch(error => {
    // Manejo de errores en caso de que la petición falle
    console.error('Error:', error);
  });

  fetch('http://127.0.0.1:5000/api/menu/postre')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos recibidos de la API
    console.log(data);

    const menuPostre = document.getElementById('postres');
    const tbody = menuPostre.querySelector('ul');
    

    data.forEach((registro) => {
      const postre = document.createElement('li');
      const nombrePostre = document.createElement('span');
      nombrePostre.classList.add('nombre-platillo');
      const precioPostre = document.createElement('span');
      precioPostre.classList.add('precio');


      nombrePostre.textContent = registro.nombre ? registro.nombre.trim(): '';
      precioPostre.textContent = "$"+registro.precio;

      menuPostre.appendChild(postre);
      postre.appendChild(nombrePostre);
      postre.appendChild(precioPostre);
      tbody.appendChild(postre);
    });
  })
  .catch(error => {
    // Manejo de errores en caso de que la petición falle
    console.error('Error:', error);
  });