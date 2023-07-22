const formulario = document.querySelector('.formulario');

formulario.addEventListener('submit', e => {
    e.preventDefault();

    const username = document.querySelector('.username').value;
    const password = document.querySelector('.password').value;

    const alertaPrevia = document.querySelector('.alerta');
    if (alertaPrevia) {
        alertaPrevia.remove();
    }

    const alerta = document.createElement('div');
    alerta.classList.add('alerta');

    if (username === '' || password === '') {
        alerta.textContent = 'Todos los campos son obligatorios';
        alerta.classList.add('error');
    } else {
        if (username === 'admin' && password === 123){
            alerta.textContent = 'Credenciales no válidas';
            alerta.classList.add('error');
        }else{
        alerta.textContent = 'Todo bien';
        alerta.classList.add('exito');
        }
        
    }

   

    formulario.appendChild(alerta);
});
