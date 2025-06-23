from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def function():
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor()
        query = """
        
        """
        cursor.execute(query,)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

