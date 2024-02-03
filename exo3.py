import sqlite3

# Creer la base de donnée
def create_database():
    
    conn = sqlite3.connect("missing_numbers.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS missing_numbers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number INTEGER
        )
    ''')

    conn.commit()
    conn.close()

# Inserer dans la base de donnée
def insert_missing_numbers(numbers):
    
    conn = sqlite3.connect("missing_numbers.db")
    cursor = conn.cursor()

    for number in numbers:
        cursor.execute("INSERT INTO missing_numbers (number) VALUES (?)", (number,))

    conn.commit()
    conn.close()

# Premiere proposition
def missing_hunter1(chain):
    missing_numbers = [i for i in range(2,chain[-1]) if i not in chain]
    create_database()
    insert_missing_numbers(missing_numbers)
    return missing_numbers


# Deuxieme proposition
def missing_hunter2(chain):
    all_numbers = set(range(1, max(chain) + 1))
    missing_numbers = list(all_numbers - set(chain))
    return missing_numbers

# Afficher le contenu de la base de donnée
def display_database_contents():

    conn = sqlite3.connect("missing_numbers.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM missing_numbers")
    rows = cursor.fetchall()

    print("Contenu de la table missing_numbers:")
    for row in rows:
        print(row)

    conn.close()

display_database_contents()

chain1 = [1,2,3,4,6,7,11]
missing_hunter1(chain1)