import mysql.connector
from geopy.distance import distance

def get_airport_coordinates(icao_code):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()
    if result is None:
        return None
    return result



