import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
            host = '127.0.0.1',
            port = 3306,
            database = 'flight_game',
            user = 'leo',
            password = 'salasana',
            autocommit = True
            )

def get_airport_coordinates(icao_code):
    query = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao_code}'"
    cursor = connection.cursor()
    cursor.execute(query)
    output = cursor.fetchone()
    return output





def run_airport_distance():
    icao_code1 = input("Enter the ICAO code of the first airport: ").upper()
    icao_code2 = input("Enter the ICAO code of the second airport: ").upper()

    coords1 = get_airport_coordinates(icao_code1)
    coords2 = get_airport_coordinates(icao_code2)

    distance_km = distance.distance(coords1, coords2).km
    print(f"Distance between {icao_code1} and {icao_code2}: {distance_km:.2f} kilometers")

run_airport_distance()
