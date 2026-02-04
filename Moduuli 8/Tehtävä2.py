import mysql.connector

def get_airports_by_country(country_code):

    country = f"SELECT type, count(*) AS amount FROM airport WHERE iso_country = '{country_code}'  GROUP BY type ORDER BY amount DESC"
    cursor = connection.cursor()
    cursor.execute(country)
    output = cursor.fetchall()

    if cursor.rowcount > 0:
        print(f"Airports in {country_code}:")
        for line in output:
            print(f"{line[1]} {line[0]} airports")

    else:
        print(f"No airports found for country code {country_code}")
    return

connection = mysql.connector.connect(
            host = '127.0.0.1',
            port = 3306,
            database = 'flight_game',
            user = 'leo',
            password = 'salasana',
            autocommit = True
            )

def run_country_program():
    country_code = input("Enter the country code (e.g. FI for Finland): ").upper()
    get_airports_by_country(country_code)

run_country_program()

