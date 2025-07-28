from flask import Flask, jsonify
from flask_mysqldb import MySQL
import MySQLdb

from config import Config

mysql = MySQL()

def create_app():    
    app = Flask(__name__)
    app.config.from_object(Config) 
    mysql.init_app(app)
    
 
    from controllers.albumController import albumBP  
    app.register_blueprint(albumBP)
    
    @app.route('/DBcheck')
    def DB_check():
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT 1')
            cursor.close()  # ✅ Cerrar cursor
            return jsonify({'status': 'ok', 'message': 'Conectado con éxito'}), 200        
        except MySQLdb.MySQLError as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500 
    
    @app.errorhandler(404)
    def paginaNoE(e):
        return jsonify({'Cuidado: Error de capa 8! :c'}), 404

    @app.errorhandler(405)
    def metodoNoPermitido(e):
        return jsonify({'Revisa el método de envío de tu ruta (GET o POST'}), 405 
    
 
    return app

if __name__ == '__main__':
    app = create_app() 
    app.run(port=3000, debug=True)