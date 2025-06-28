from flask import Flask, jsonify, render_template, request,url_for, flash,redirect  #1 funcion para mandar llamar las vistas
from flask_mysqldb import MySQL
import MySQLdb

from flask import Flask

app = Flask (__name__)
 #definir variables
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="1111Ivet**"
app.config['MYSQL_DB']="dbFlask"
app.config['MYSQL_PORT']=3306
app.secret_key ='mysecretkey'

mysql =MySQL(app)

#ruta inicio #2
@app.route('/')
def home():
    #PRACTICA 10- Se agregaron las siguientes lineas 
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('SELECT*FROM albums')
        consultatodo= cursor.fetchall()
        return render_template ('formulario.html', errores ={},albums=consultatodo) #Regresa un render_template a la vista de formular
        
    except Exception as e:
        print('Error al consultar todo: '+e)
        return render_template ('formulario.html', errores ={},albums=[]) #Lllega la respuesta vacía
    
        
    finally:
        cursor.close()  
        
 #PRACTICA 10- Se crea una ruta detalles    
@app.route('/detalle/<int:idAlbums>')
def detalle(idAlbums):
    
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('SELECT*FROM albums where idAlbums=%s', (idAlbums,))
        consultaId= cursor.fetchone() #obtiene un registro
        return render_template('consulta.html',album=consultaId) #Regresa un render_template a la vista de formular
        
    except Exception as e:
        print('Error al consultar por id: '+e)
        return redirect((url_for('home'))) #Lllega la respuesta vacía
    
    finally:
        cursor.close()  
 
 
 
 # Ruta formUpdate
@app.route('/editar/<int:idAlbums>')
def editar(idAlbums):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM albums WHERE idAlbums = %s', (idAlbums,))
        album = cursor.fetchone()
        if album:
            return render_template('formUpdate.html', album=album)
        else:
            flash('Álbum no encontrado')
            return redirect(url_for('home'))
    except Exception as e:
        print('Error al obtener álbum: ' + str(e))
        flash('Error al obtener el álbum')
        return redirect(url_for('home'))
    finally:
        cursor.close()  
        
              

#ruta consulta #3
@app.route('/consulta')
def consulta():
    return render_template ('consulta.html') #Regresa un render_template a la vista de consulta


#ruta para el insert    #continuacion de la practica
@app.route('/guardarAlbum', methods=['POST'])
def guardar():
#declarar un diccionario/lista de errores de validaciones
    errores= {}
    
    
    #obtener los datos a insertar de la vista
    album=request.form.get('txtTitulo','').strip() #si hay espacios en lo que se escribe, strip se encarga de quitar los espacios para evitar que se guarden
    artista=request.form.get('txtArtista','').strip()
    anio=request.form.get('txtAnio','').strip()
    
    if not album:
        errores['txtTitulo']='Nombre del album Obligatorio'
    if not artista:
        errores['txtArtista']='Artista es Obligatorio'
    if not anio:
        errores['txtAnio']='Año Obligatorio'
    elif not anio.isdigit() or int(anio)<1800 or int(anio)>2100:
        errores['txtAnio']='Ingresa un año valido'

    if not errores:
        try:
            cursor= mysql.connection.cursor()
            cursor.execute('insert into albums(album,artista,anio) values(%s,%s,%s)',(album,artista,anio)) #datos de la base de datos creada
            mysql.connection.commit()
            flash('Album guardado en la BD')
            return redirect(url_for('home'))

        except Exception as e:
            mysql.connection.rollback() # revierte en caso de que se haya echo algo y ocurra un error
            flash('Algo fallo:'+str(e))
            return  redirect(url_for('home'))
        
        finally:
            cursor.close()
            
    return render_template('formulario.html',errores=errores)
    #return render_template('consulta.html')
        

    
# Ruta para actualizar 
@app.route('/actualizarAlbum', methods=['POST'])
def actualizar():
    errores = {}

    # Obtener los datos del formulario
    idAlbum= request.form.get('idAlbums', '').strip()
    album = request.form.get('txtTitulo', '').strip()
    artista = request.form.get('txtArtista', '').strip()
    anio = request.form.get('txtAnio', '').strip()

    if not album:
        errores['txtTitulo'] = 'Nombre del álbum obligatorio'
    if not artista:
        errores['txtArtista'] = 'Artista es obligatorio'
    if not anio:
        errores['txtAnio'] = 'Año obligatorio'
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2100:
        errores['txtAnio'] = 'Ingresa un año válido'

    if not errores:
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(
                'UPDATE albums SET album=%s, artista=%s, anio=%s WHERE idAlbums=%s',
                (album, artista, anio, idAlbum)
            )
            mysql.connection.commit()
            flash('Álbum actualizado correctamente')
            return redirect(url_for('home'))

        except Exception as e:
            mysql.connection.rollback()
            flash('Algo fallo: ' + str(e))
            return redirect(url_for('home'))

        finally:
            cursor.close()

    return render_template('formUpdate.html', album=request.form, errores=errores)    
    
    
    
    
    
    
    
    
 #ruta para probar la conección  a MYSQL
@app.route('/DBcheck')
def DBcheck():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify(  { 'status':'ok','message' : 'Conetactado con exito' }  ),200
    except MySQLdb.MySQLError as e:
         return jsonify( {'status': 'error', 'message' : str(e)}),500   
    
    
if __name__ == '__main__':
    app.run(port=3000, debug = True)
    #probar las rutas  con el parametro (nombre)
    #Hay que buscar el camino correcto y los posibles errores