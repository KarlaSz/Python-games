import sqlite3

#otworzenie polaczenia do bazy
connection = sqlite3.connect('todo.db')

def create_table(connection):
    try:
        cur = connection.cursor()
        # zapytania SQL z 3 """ bo wtedy wszystko co bedzie miedzy nimi to py wezmie to jako calosc
        cur.execute("""CREATE TABLE task(task text)""")
    except:
        pass
    

def show_tasks(connection):
    cur = connection.cursor()
    cur.execute("""SELECT rowid,task FROM task""")
    result = cur.fetchall()
    
    for row in result:
        print(str(row[0]) + ' - ' + row[1])
    


def add_task(connection):
    print('dodajemy zadanie')
    task = input("Wpisz treść zadania: ")
    if task == "0":
        print("Powrót do menu")
    else:
        cur = connection.cursor()
        # ? dla kazdego wartosci ktora chcemy dodac do bazt to uzywamy ?
        cur.execute("""INSERT INTO task(task) VALUES(?)""", (task,))
        #do trwalego zapisywania danych w tabeli
        connection.commit()
        print("Dodano zadanie!")


def delete_task(connection):
    task_index = int(input("Podaj indeks zadania do usunięcia: "))
    
    cur = connection.cursor()
    #rowcount wlasciwosc ktora zwraca ilosc wierszy ktore zostlay usuniete 
    rows_deleted = cur.execute("""DELETE FROM task WHERE rowid=?""", (task_index,)).rowcount
    connection.commit()
    
    if rows_deleted == 0:
        print('Zadanie nie istnieje.')
    else:
        print('Usunięto zadanie.')

    print("Usunięto zadanie!")

create_table(connection)

while True:
    print()
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wyjdź")

    user_choice = int(input("Wybierz liczbę: "))
    print()
    if user_choice == 1:
        show_tasks(connection)

    if user_choice == 2:
        add_task(connection)

    if user_choice == 3:
        delete_task(connection)

    if user_choice == 4:
        break

#zamkniecie polaczenia do bazy
connection.close()
