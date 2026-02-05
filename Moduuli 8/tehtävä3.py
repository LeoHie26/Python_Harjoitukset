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

def get_airport_coordinates(icao_code1, icao_code2):
    coordinates1 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = {icao_code1}"
    coordinates2 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = {icao_code2}"
    cursor = connection.cursor()
    cursor.execute(coordinates1, coordinates2)
    output = cursor.fetchone()


    if cursor.rowcount > 0:
        print(distance.distance(coordinates1, coordinates2).km)
        for distance in output:
            print(f"Distance between {icao_code1} and {icao_code2}: {distance} kilometers")


def run_airport_distance():
    icao_code1 = input("Enter the ICAO code of the first airport: ").upper()
    icao_code2 = input("Enter the ICAO code of the second airport: ").upper()
    det_airport_coordinates(icao_code1, icao_code2)

run_airport_distance()
