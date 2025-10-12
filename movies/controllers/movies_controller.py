from flask import jsonify, request
from database.connection import dbConnection
from config.config import config
from datetime import datetime

#obtener todas las peliculas
def get_movies():
    mydb, err = dbConnection()
    if mydb is None:
        return jsonify({ 'message': f'Error en la conexion {err}' }), 503
    try:
        cursor = mydb.cursor(dictionary=True)
        query = "SELECT * FROM movies"
        cursor.execute(query)
        movies = cursor.fetchall()
        cursor.close()
        mydb.close()
        return jsonify(movies), 200
    except Exception as ex:
        return jsonify({ 'message': f'Error al obtener las peliculas: {ex}' }), 400
    
#obtener las peliculas por id
def get_movie_by_id(movie_id):
    mydb, err = dbConnection()
    if mydb is None:
        return jsonify({ 'message': f'Error en la conexion {err}' }), 503
    try:
        cursor = mydb.cursor(dictionary=True)
        query = "SELECT * FROM movies WHERE id = %s"
        cursor.execute(query, (movie_id, ))
        movie = cursor.fetchone()
        cursor.close()
        mydb.close()
        if movie:
            return jsonify(movie), 200
        else:
            return jsonify({ 'message': 'Pelicula no encontrada' }), 404
    except Exception as ex:
        return jsonify({ 'message': f'Error al obtener pelicula: {ex}' }), 400

#crear nueva pelicula
def create_movie():
    data = request.json
    title = data.get('title')
    year = data.get('year')
    genre = data.get('genre')

    mydb, err = dbConnection()
    if mydb is None:
        return jsonify({'message': f'Error en la conexión: {err}'}), 503
    try:
        cursor = mydb.cursor()
        query = "INSERT INTO movies (title, year, genre) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, year, genre))
        movie_id = cursor.lastrowid
        mydb.commit()
        cursor.close()
        mydb.close()
        return jsonify({ 'message': 'Pelicula creada exitosamente', 'id': movie_id }), 201
    except Exception as ex:
        return jsonify({'message': f'Error al crear película: {ex}'}), 400
    
#actualizar pelicula
def update_movie(movie_id):
    data = request.json
    title = data.get('title')
    year = data.get('year')
    genre = data.get('genre')

    mydb, err = dbConnection()
    if mydb is None:
        return jsonify({'message': f'Error en la conexión: {err}'}), 503
    try:
        cursor = mydb.cursor()
        query = "UPDATE movies SET title=%s, year=%s, genre=%s WHERE id=%s"
        cursor.execute(query, (title, year, genre, movie_id))
        mydb.commit()
        cursor.close()
        mydb.close()
        return jsonify({'message': 'Película actualizada exitosamente'}), 200
    except Exception as ex:
        return jsonify({'message': f'Error al actualizar película: {ex}'}), 400
    
#eliminar pelicula
def delete_movie(movie_id):
    mydb, err = dbConnection()
    if mydb is None:
        return jsonify({'message': f'Error en la conexión: {err}'}), 503
    try:
        cursor = mydb.cursor()
        query = "DELETE FROM movies WHERE id=%s"
        cursor.execute(query, (movie_id,))
        mydb.commit()
        cursor.close()
        mydb.close()
        return jsonify({'message': 'Película eliminada exitosamente'}), 200
    except Exception as ex:
        return jsonify({'message': f'Error al eliminar película: {ex}'}), 400