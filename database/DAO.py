from database.DB_connect import DBConnect
from model.race import Race


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllSeasons():
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor()
        query = """
                select distinct year
                from seasons
        """
        cursor.execute(query,)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllRaces(season):
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select *
                from races r
                where r.year = %s
                """

        cursor.execute(query,(season,))

        for row in cursor:
            result.append(Race(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(year):
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor()
        query = """
                select r1.raceId, r2.raceId, count(distinct rs2.driverId)
                from races r1, races r2, results rs1, results rs2
                where r1.raceId = rs1.raceId 
                and r2.raceId = rs2.raceId
                and r1.raceId < r2.raceId
                and rs1.statusId = 1
                and rs2.statusId = 1
                and rs1.driverId = rs2.driverId
                and r1.year = %s 
                and r2.year = %s
                group by r1.raceId, r2.raceId
                """

        cursor.execute(query,(year,year))

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result