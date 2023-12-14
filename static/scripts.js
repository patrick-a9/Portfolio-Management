function generateActionInputs() {
    const numActions = parseInt(document.getElementById('numActions').value);
    const actionInputsContainer = document.getElementById('actionInputs');

    // Limpiar el contenedor antes de generar nuevas entradas
    actionInputsContainer.innerHTML = '';

    for (let i = 1; i <= numActions; i++) {
        const inputLabel = document.createElement('label');
        inputLabel.textContent = `Ticker de la Acción ${i}:`;

        const inputTextbox = document.createElement('input');
        inputTextbox.type = 'text';
        inputTextbox.name = `action${i}`;
        inputTextbox.required = true;

        actionInputsContainer.appendChild(inputLabel);
        actionInputsContainer.appendChild(document.createElement('br')); // Salto de línea después de la etiqueta
        actionInputsContainer.appendChild(inputTextbox);
        actionInputsContainer.appendChild(document.createElement('br')); // Salto de línea después de la caja de texto
    }
}

function resetForm() {
    document.getElementById('numActions').value = '';
    document.getElementById('actionInputs').innerHTML = '';
}

async function submitPortfolio(event) {
    event.preventDefault();

    const numActions = parseInt(document.getElementById('numActions').value);
    const actions = [];

    for (let i = 1; i <= numActions; i++) {
        const inputTextbox = document.querySelector(`input[name="action${i}"]`);
        const actionValue = inputTextbox.value.trim();
        actions.push(actionValue);
    }

    // Enviar datos al servidor Flask
    try {
        const response = await fetch('/create_portfolio', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ actions }),
        });

        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }

        const data = await response.json();

        // Restablecer el formulario
        document.getElementById('numActions').value = '';
        for (let i = 1; i <= numActions; i++) {
            document.querySelector(`input[name="action${i}"]`).value = '';
        }

        // Restablecer el formulario personalizado
        resetForm();

        // Mostrar un mensaje al usuario
        alert('Portafolio enviado correctamente');

        console.log('Respuesta del servidor:', data);
        // Puedes realizar acciones adicionales aquí, por ejemplo, actualizar la interfaz de usuario
    } catch (error) {
        console.error('Error al enviar datos:', error);
        // Puedes mostrar un mensaje de error al usuario si es necesario
        alert('Error al enviar el portafolio. Por favor, inténtalo de nuevo.');
    }
}

async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const data = {
        username: username,
        password: password
    };

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            console.log('Login successful');
            console.log('Token:', result.token);
            // Lógica para realizar acciones después de un inicio de sesión exitoso
            showPortfolio();
        } else {
            console.error('Login failed:', result.message);
            alert('Credenciales incorrectas');
        }
    } catch (error) {
        console.error('Error during login:', error);
        alert('Error durante el inicio de sesión');
    }
}

async function register() {
    const newMail = document.getElementById('newMail').value;
    const newUsername = document.getElementById('newUsername').value;
    const newPassword = document.getElementById('newPassword').value;

    // Verificar si los campos de nombre de usuario y contraseña están vacíos
    if (!newUsername || !newPassword || !newMail) {
        alert('Debe proporcionar un correo, nombre de usuario y una contraseña.');
        return;
    }

    const data = {
        mail: newMail,
        username: newUsername,
        password: newPassword
    };

    try {
        const response = await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            console.log('Registro exitoso');
            console.log('Mensaje del servidor:', result.message);
            // Puedes redirigir a otra página o realizar acciones adicionales después del registro exitoso
        } else {
            console.error('Error en el registro:', result.message);
            alert('Error en el registro. Consulta la consola para más detalles.');
        }
    } catch (error) {
        console.error('Error durante el registro:', error);
        alert('Error durante el registro. Consulta la consola para más detalles.');
    }
}

function showPortfolio() {
    
    document.getElementById('loginContainer').style.display = 'none';
    document.getElementById('registerContainer').style.display = 'none';
    document.getElementById('portfolioContainer').style.display = 'block';
}

function logout() {
    // Restablecer o limpiar cualquier estado de sesión o información del usuario si es necesario

    // Redirigir al usuario a la página de inicio
    window.location.href = '/';
}

function resetForm() {
    document.getElementById('portfolioForm').reset();
    document.getElementById('actionInputs').innerHTML = '';
}

function scrollToTop() {
    // Obtener la posición actual de desplazamiento
    const currentPosition = window.scrollY;

    // Calcular la posición a la que se debe desplazar (en este caso, la parte superior)
    const targetPosition = 0;

    // Calcular la distancia que se debe desplazar en cada paso
    const distance = targetPosition - currentPosition;

    // Duración del desplazamiento suave (en milisegundos)
    const duration = 500;

    // Hora de inicio del desplazamiento
    let startTime;

    // Función de animación
    function animate(currentTime) {
        if (!startTime) startTime = currentTime;

        // Calcular el tiempo transcurrido desde el inicio
        const elapsedTime = currentTime - startTime;

        // Calcular la nueva posición de desplazamiento
        const newPosition = easeInOut(elapsedTime, currentPosition, distance, duration);

        // Desplazar a la nueva posición
        window.scrollTo(0, newPosition);

        // Continuar la animación si no ha alcanzado la duración total
        if (elapsedTime < duration) {
            requestAnimationFrame(animate);
        }
    }

    // Función de desplazamiento suave (ease-in-out)
    function easeInOut(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return (c / 2) * t * t + b;
        t--;
        return (-c / 2) * (t * (t - 2) - 1) + b;
    }

    // Iniciar la animación
    requestAnimationFrame(animate);
}