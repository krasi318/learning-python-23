import sqlite3


i = 0
connection = sqlite3.connect('mydatabase.db')

cur = connection.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS people (
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    job TEXT,
    salary INTEGER
)
""")
#
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


# connection.commit()

names = cur.execute("SELECT * FROM people")


for row in names:
    print(" ".join(str(x) for x in row))
