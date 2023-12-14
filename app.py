import sqlite3
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import sqlite3

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Lista para almacenar los tickers del portafolio
tickers_list = []

@app.route('/')
def inicio():
    """Ruta para la página de inicio.

    Renderiza la plantilla 'Portafolio.html' con la información de los portafolios del usuario.

    Returns:
    render_template: Plantilla 'Portafolio.html'.
    """
    # Verificar la autenticación del usuario
    if 'user_id' not in session:
        return render_template('Portafolio.html', user_portfolios=[])

    user_id = session['user_id']

    # Conectar a la base de datos
    conn = sqlite3.connect('api.sqlite')
    c = conn.cursor()

    try:
        # Obtener los portafolios asociados al usuario
        c.execute('SELECT id, tickers FROM Tickers WHERE user_id = ?', (user_id,))
        user_portfolios = c.fetchall()

        return render_template('Portafolio.html', user_portfolios=user_portfolios)
    except Exception as e:
        # Manejar errores aquí, por ejemplo, registrándolos en la consola
        print(f'Error al obtener portafolios: {e}')
        return render_template('Portafolio.html', user_portfolios=[])
    finally:
        conn.close()

@app.route('/create_portfolio', methods=['POST'])
def create_portfolio():
    """
    Ruta para crear un portafolio.

    Recibe datos JSON con una lista de acciones y las almacena en la base de datos de tickers apuntando al usuario que se logueó.

    Returns:
        jsonify: Respuesta JSON con éxito y la lista de tickers almacenados.
    """
    # Verificar la autenticación del usuario
    if 'user_id' not in session:
        return jsonify({'message': 'User not authenticated'}), 401

    user_id = session['user_id']
    
    data = request.get_json()
    actions = data.get('actions', [])

    # Limpiar la lista antes de agregar nuevos tickers
    tickers_list.clear()

    for action in actions:
        tickers_list.append(action)

    # Conectar a la base de datos
    conn = sqlite3.connect('api.sqlite')
    c = conn.cursor()

    try:
        # Insertar los tickers en la base de datos
        c.execute('INSERT INTO Tickers (user_id, tickers) VALUES (?, ?)', (user_id, ', '.join(tickers_list)))
        conn.commit()

        return jsonify({'success': True, 'tickers': tickers_list})
    except Exception as e:
        return jsonify({'message': 'Error during portfolio creation', 'error': str(e)}), 500
    finally:
        conn.close()

# Ruta para registro de usuarios
@app.route('/register', methods=['POST'])
def register():
    """
    Ruta para el registro de usuarios.

    Recibe datos JSON con nombre de usuario y contraseña.
    Verifica si el usuario ya existe, registra al usuario 
    en la base de datos y devuelve una respuesta JSON.

    Returns:
        jsonify: Respuesta JSON indicando el resultado del registro.
    """
    data = request.get_json()

    mail=data.get('mail')
    username = data.get('username')
    password = data.get('password')

    if not username or not password or not mail:
        return jsonify({'message': 'Must provide mail, username and password'}), 400

    # Conectar a la base de datos
    conn = sqlite3.connect('api.sqlite')
    c = conn.cursor()

    try:
        # Verificar si el usuario ya existe
        c.execute('SELECT * FROM Users WHERE username = ?', (username,))
        existing_user = c.fetchone()

        if existing_user:
            return jsonify({'message': 'User already exists'}), 400

        # Insertar nuevo usuario
        c.execute('INSERT INTO Users (mail,username, password) VALUES (?,?, ?)', (mail, username, password))

        # Guardar los cambios y cerrar la conexión a la base de datos
        conn.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Error during registration', 'error': str(e)}), 500
    finally:
        conn.close()

# Ruta para login de usuarios
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Must provide username and password'}), 400

    # Conectar a la base de datos
    conn = sqlite3.connect('api.sqlite')
    c = conn.cursor()

    # Consultar al usuario
    c.execute('SELECT * FROM Users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()

    # Si el usuario no existe o la contraseña es incorrecta, regresar error
    if not user:
        return jsonify({'message': 'Invalid username or password'}), 401

    user_id, user_name, *_ = user  # No almacenamos la contraseña en la respuesta

    # Almacenar información del usuario en la sesión
    session['user_id'] = user_id
    session['user_name'] = user_name

    # Consultar los tickers asociados con el usuario
    c.execute('SELECT tickers FROM Tickers WHERE user_id = ?', (user_id,))
    tickers_data = c.fetchone()

    tickers = tickers_data[0] if tickers_data else ''  # Obtener los tickers o establecer una cadena vacía

    return jsonify({'message': 'Login successful', 'user_id': user_id, 'user_name': user_name, 'tickers': tickers}), 200



if __name__ == '__main__':
    app.run(debug=True, port=5500)