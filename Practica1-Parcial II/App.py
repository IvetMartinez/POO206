from flask import Flask

app = Flask (__name__)

#ruta simple 1
@app.route('/')
def home():
    return 'Hola mundo FLASK'
#ruta con parametros  2
@app.route('/saludo/<nombre>')
def saludar(nombre): # puedes agregar el tipo de dato y el parametro (int:nombre)
    return 'Hola,' +nombre +'!!!'
 #ruta try-catch
@app.errorhandler(404)
def paginaNoEncontrada(e):
    return 'Cuidado : Error de capa 8 !!!',404
@app.errorhandler(405)
def metodonoP(e):
    return 'Revisa el metodo de envio de la ruta (GET o POST)!!!',405

 #ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'Soy el mismo recurso del servidor'
    
    #ruta POST
@app.route('/formulario', methods = ['POST'])
def formulario():
    return 'Hola soy un formulario' #No existe algo que haga el metodo
   
    
if __name__ == '__main__':
    app.run(port=3000, debug = True)
    #probar las rutas  con el parametro (nombre)
    #Hay que buscar el camino correcto y los posibles errores