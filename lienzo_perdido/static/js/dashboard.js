


//obtener los datos de la bd
fetch('http://10.11.4.96:5000/api/menu')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos recibidos de la API
    console.log(data[0]);
  })
  .catch(error => {
    // Manejo de errores en caso de que la petición falle
    console.error('Error:', error);
  });

  //Click chidoris en los botones, para los formularios
  const toggleButton = document.getElementById("toggleButton");
  const formulario = document.getElementById("formulario");

  toggleButton.addEventListener("click", () => {
      formulario.classList.toggle("formulario-visible");
  });

  var formularioI = document.getElementById("formulario INSERT");
  var formularioU = document.getElementById("formulario Update");
  var formularioD = document.getElementById("formulario Delete");

  function toggleFormInsert() {
    var formulario = document.getElementById("formulario INSERT");
    formularioU.style.display = "none";
    formularioD.style.display = "none";
    if (formulario.style.display === "block") {
        formulario.style.display = "none";
    } else {
        formulario.style.display = "block";
    }
    
  }

  function toggleFormUpdate() {
    var formulario = document.getElementById("formulario Update");
    formularioD.style.display = "none";
    formularioI.style.display = "none";
    if (formulario.style.display === "block") {
      formulario.style.display = "none";
  } else {
      formulario.style.display = "block";
  }
 
  }

  function toggleFormDelete() {
    var formulario = document.getElementById("formulario Delete");
    formularioI.style.display = "none";
    formularioU.style.display = "none";
    if (formulario.style.display === "block") {
      formulario.style.display = "none";
  } else {
      formulario.style.display = "block";
  }
  }

  //Obtener y setear el id de un renglón seleccionado para el CRUD
  document.querySelector()


  // document.querySelector("#tblEventos").addEventListener("click", (e) => {
  //   target = e.target;
  //   if (target.classList.contains("edit")) {
  //     selectedRow = target.parentElement.parentElement;
  //     document.querySelector("#idEvento").value =
  //       selectedRow.children[0].textContent;
        
  //       console.log(document.querySelector("#idEvento").value);
  //   }
  // });
  console.log(document.querySelector("#idEvento").value = selectedRow.children[0].textContent);