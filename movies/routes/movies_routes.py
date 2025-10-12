from flask import Blueprint, request
from controllers.movies_controller import (
    get_movies,
    get_movie_by_id,
    create_movie,
    update_movie,
    delete_movie
)

movies_routes = Blueprint('movies', __name__)

#lista de peliculas
@movies_routes.route('/api/movies/listar', methods=['GET'])
def getMovies_route():
    return get_movies()

#pelicula por id
@movies_routes.route('/api/movies/buscar-por-id/<int:movie_id>', methods=['GET'])
def getMovie_route(movie_id):
    return get_movie_by_id(movie_id)

#crear pelicula
@movies_routes.route('/api/movies/crear', methods=['POST'])
def createMovie_route():
    return create_movie()

#actualizar pelicula
@movies_routes.route('/api/movies/actualizar/<int:movie_id>', methods=['PUT'])
def updateMovie_route(movie_id):
    return update_movie(movie_id)

#eliminar pelicula
@movies_routes.route('/api/movies/eliminar/<int:movie_id>', methods=['DELETE'])
def deleteMovie_route(movie_id):
    return delete_movie(movie_id)