import sqlite3
import sys

sys.path.insert(1, 'C:/Users/kpaci/PycharmProjects/pythonProject/learning-python-23/pyOOPlearning')
import person

connection = sqlite3.connect('mydatabase.db')

cur = connection.cursor()

# sql zaqvka suzdavashta table people
cur.execute("""
CREATE TABLE IF NOT EXISTS people (
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    job TEXT,
    salary INTEGER
)
""")


#sql zaqvki za vuvejdane na hora
# cur.execute("""
#     INSERT INTO people VALUES (
#             ("krasi","grigorov",19,"no job",0) <- vajno e tuk da ima (,) zapetai
#             ("robi","petrov",19,"sys admin",1500)
#             ("qvor","qjo",39,"rapper",1300)
# )
# """)
# cur.execute("""
#     INSERT INTO people VALUES
#         ("krasi","grigorov",19,"no job",0),
#         ("robi","petrov",19,"sys admin",1500),
#         ("qvor","qjo",39,"rapper",1300)
# """)

# metod za dobavqne na person kum bazata danni
def insert_person(per):
    with connection:
        cur.execute("INSERT INTO people VALUES (?,?,?,?,?)",
                    (per.name, per.age, per.height, per.salary, per.programming_lang))


def get_person_by_lname(lastname):
    with connection:
        cur.execute("""
        SELECT * FROM people WHERE last_name = ?
        """, (lastname,))
        print(cur.fetchall())


def update_salary(per, salary):
    with connection:
        cur.execute("""
        SELECT * FROM people WHERE first_name = ?
        """, (per,))
        per.salary = salary
        print(cur.fetchall())


def delete_person(lastname):
    with connection:
        cur.execute("""
           DELETE FROM people WHERE last_name = ?
           """, (lastname,))
        print(cur.fetchall())


# adding objs to our DB
special_person = person.Programmer("krasi", 20, 192, 2000, "py")
special_person1 = person.Programmer("Carl", 34, 168, 5000, "py")
print(special_person)

# insert_person(special_person)

# lasname = input("enter lastname for search : ")
# get_person_by_lname(lasname)

# salar = input("enter salary for change : ")
# update_salary(special_person, salar)

# lastname = input("enter lastname for deletion : ")
# delete_person(lastname)

# sql zaqvka s koqto da nqma povtarqshti se hora s purvo ime
cur.execute("""
DELETE FROM people
WHERE rowid NOT IN (
SELECT min(rowid)
FROM people
GROUP BY first_name

);
""")
connection.commit()
# sql zaqvka koqto printira vsichko ot nashata tablica
cur.execute("SELECT * FROM people")
names = cur.fetchall()
print("")


for i in names:
    print(" ".join(str(x) for x in i))
