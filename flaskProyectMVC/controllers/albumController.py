from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.albumModel import *

albumBP = Blueprint('albums', __name__)

#ruta de inicio (consulta todos)
@albumBP.route('/')
def home():
    try:
        albums = getAll()     
        return render_template('formulario.html', errores={}, albums = albums)
    except Exception as e:
        print(f"Error : {e}")
        return render_template('formulario.html', errores={}, albums = [])

#Ruta para guardar los albums
@albumBP.route('/guardarAlbum', methods = ['POST'])
def guardar():
    errores = {}

    titulo = request.form.get('txtTitulo', '').strip()
    artista = request.form.get('txtArtista', '').strip()
    anio = request.form.get('txtAnio', '').strip()
    
    if not titulo:
        errores['txtTitulo'] = 'Nombre del álbum obligatorio'
    if not artista:
        errores['txtArtista'] = 'Nombre del artista obligatorio'
    if not anio:
        errores['txtAnio'] = 'Año del álbum obligatorio'
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2100:
        errores['txtAnio'] = 'Ingresa un año válido'
        
    if not errores:
        try:  
            insertAlbum(titulo, artista, anio)
            flash('Album se guardó en BD')
            return redirect(url_for('albums.home'))
        except Exception as e:
            mysql.connection.rollback()
            flash( f'Algo falló: {str(e)}')
            return redirect(url_for('albums.home'))
            
    return render_template('formulario.html', errores = errores)    

#Ruta para ver detalles
@albumBP.route('/detalle/<int:id>')
def detalle(id):
    try:
        albums = getById(id)
        return render_template('consulta.html', albums = albums)
    except Exception as e:
        flash('Error al consultar el album: ' +  str(e))
        return redirect(url_for('albums.home'))
        
#Ruta para editar (mostrar formulario) 
@albumBP.route('/editaralbum/<int:id>', methods=['POST'])
def editar(id):
    try:
        albums = getById(id)
        return render_template('update.html', albums = albums)
    except Exception as e:
        flash('Error al consultar el album: ' +  str(e))
        return redirect(url_for('albums.home'))
        
#Ruta para actualizar 
@albumBP.route('/ActualizarAlbum/<int:id>', methods= ['POST'])
def actualizar(id):
    errores = {}

    titulo = request.form.get('ntxtTitulo', '').strip()
    artista = request.form.get('ntxtArtista', '').strip()
    anio = request.form.get('ntxtAnio', '').strip()
    
    if not titulo:
        errores['ntxtTitulo'] = 'Nombre del álbum obligatorio'
        
    if not artista:
        errores['ntxtArtista'] = 'Nombre del artista obligatorio'
        
    if not anio:
        errores['ntxtAnio'] = 'Año del álbum obligatorio'
        
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2050:
        errores['ntxtAnio'] = 'Ingresa un año válido'
        
    if not errores:
        try:
            updateAlbum(id, titulo, artista, anio)
            flash('Album actualizado correctamente')
            return redirect(url_for('albums.home'))
            
        except Exception as e:
            mysql.connection.rollback()
            flash( 'Error al actualizar:'+{str(e)})
            return redirect(url_for('albums.home'))    
    return redirect(url_for('albums.home'))
     
#Confirmación de la eliminación
@albumBP.route('/confirmadel/<int:id>')
def confirmareliminacion(id):
    try:
       albums = getById(id)
       return render_template('confirmDel.html', albums=albums)
    except Exception as e:
        flash('Error al consultar para eliminar:' + str(e))
        return redirect(url_for('albums.home'))
    
#Ruta para eliminar (soft delete)

@albumBP.route('/eliminaralbum/<int:id>' , methods=['POST'])
def eliminar(id):
    try:
       softDeleteAlbum(id)
       flash('Álbum eliminado (soft delete)')
       return redirect(url_for('albums.home'))
    except Exception as e:
        flash('Error al eliminar: ' + str(e))
        return redirect(url_for('albums.home'))
    
    