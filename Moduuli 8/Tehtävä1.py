import mysql.connector

def fetch_airport_data(icao):

    airport = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(airport)
    output = cursor.fetchall()

    if cursor.rowcount > 0:
        for line in output:
            print(f"Airport name: {line[0]}\nLocation: {line[1]}")

    else:
        print(f"No airport found with ICAO code {icao}")
    return

connection = mysql.connector.connect(
            host = '127.0.0.1',
            port = 3306,
            database = 'flight_game',
            user = 'leo',
            password = 'salasana',
            autocommit = True
            )

icao = input("Enter the ICAO code of an airport: ").upper()
fetch_airport_data(icao)