from database.connection import getConnection

class Review:
    def __init__(self, id, user_id, movie_id, comment, rating):
        self.id = id
        self.user_id = user_id
        self.movie_id = movie_id
        self.comment = comment
        self.rating = rating
    
    @staticmethod
    def create(user_id, movie_id, comment, rating):
        mydb, err = getConnection()
        if mydb is None:
            return None, f"Error en la conexion: {err}"
        try:
            cursor = mydb.cursor()
            query = "INSERT INTO reviews (user_id, movie_id, comment, rating) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (user_id, movie_id, comment, rating))
            mydb.commit()
            review_id = cursor.lastrowid
            cursor.close()
            mydb.close()
            return review_id, None
        except Exception as ex:
            return None, str(ex)
        
    @staticmethod
    def get_all():
        mydb, err = getConnection()
        if mydb is None:
            return None, f"Error en la conexion: {err}"
        try:
            cursor = mydb.cursor(dictionary=True)
            cursor.execute("SELECT * FROM reviews")
            reviews = cursor.fetchall()
            cursor.close()
            mydb.close()
            return reviews, None
        except Exception as ex:
            return None, str(ex)
    
    @staticmethod
    def get_by_id(review_id):
        mydb, err = getConnection()
        if mydb is None:
            return None, f"Error en la conexión: {err}"
        try:
            cursor = mydb.cursor(dictionary=True)
            cursor.execute("SELECT * FROM reviews WHERE id = %s", (review_id,))
            review = cursor.fetchone()
            cursor.close()
            mydb.close()
            return review, None
        except Exception as ex:
            return None, str(ex)
        
    @staticmethod
    def update(review_id, comment=None, rating=None):
        mydb, err = getConnection()
        if mydb is None:
            return f"Error en la conexión: {err}"
        try:
            cursor = mydb.cursor()
            fields = []
            values = []
            if comment is not None:
                fields.append("comment = %s")
                values.append(comment)
            if rating is not None:
                fields.append("rating = %s")
                values.append(rating)
            values.append(review_id)
            query = f"UPDATE reviews SET {', '.join(fields)} WHERE id = %s"
            cursor.execute(query, tuple(values))
            mydb.commit()
            cursor.close()
            mydb.close()
            return None
        except Exception as ex:
            return str(ex)

    @staticmethod
    def delete(review_id):
        mydb, err = getConnection()
        if mydb is None:
            return f"Error en la conexión: {err}"
        try:
            cursor = mydb.cursor()
            cursor.execute("DELETE FROM reviews WHERE id = %s", (review_id,))
            mydb.commit()
            cursor.close()
            mydb.close()
            return None
        except Exception as ex:
            return str(ex)