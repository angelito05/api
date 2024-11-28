from flask import Flask, jsonify, request
import conf as db

app = Flask(__name__)

def get_db_connection():
    return db.conexion

# Ruta para mostrar datos en formato JSON directamente en la pantalla
@app.route('/')
def show_json():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM proveedor')
    rows = cursor.fetchall()
    cursor.close()

    # Obtener los nombres de las columnas
    column_names = [description[0] for description in cursor.description]

    # Convertir filas a lista de diccionarios para enviarlo como JSON
    data = [dict(zip(column_names, row)) for row in rows]

    return jsonify(data)

# Ruta para buscar proveedores
@app.route('/buscar_proveedor', methods=['GET'])
def buscar_proveedor():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Obtener los parámetros de búsqueda desde la URL
    nombre = request.args.get('nombre')

    query = 'SELECT * FROM proveedor WHERE 1=1'
    params = []

    if nombre:
        query += ' AND nombre LIKE ?'
        params.append(f'%{nombre}%')
    cursor.execute(query, params)
    rows = cursor.fetchall()
    cursor.close()

    # Obtener los nombres de las columnas
    column_names = [description[0] for description in cursor.description]

    # Convertir filas a lista de diccionarios
    data = [dict(zip(column_names, row)) for row in rows]

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=4000)
