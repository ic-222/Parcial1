import pyodbc
from flask import Flask, render_template

app = Flask(__name__)

## CONECTAR BASE DE DATOS DESDE ACCESS
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\cuc\Documents\Parcial 1\Parcial 1\BaseDeDatos1.accdb;'
)

def conectar_bd():
    return pyodbc.connect(conn_str)

## APP
@app.route('/')
def listado_completo():
    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Estudiantes')
    estudiantes = cursor.fetchall()


    cursor.execute('SELECT Cursos.nombre_curso, Estudiantes.Nombre, Estudiantes.Apellido '
                   'FROM Cursos INNER JOIN Estudiantes ON Cursos.id_estudiante = Estudiantes.Id')
    cursos_con_estudiantes = cursor.fetchall()

    conn.close()

    return render_template('listado_completo.html', estudiantes=estudiantes, cursos_con_estudiantes=cursos_con_estudiantes)

if __name__ == '__main__':
    app.run(debug=True)

##
