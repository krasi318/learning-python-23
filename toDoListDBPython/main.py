import sqlite3
import datetime

# gets the current date so can be added to the task
current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
# setting up Data base
connection = sqlite3.connect("testing.db")
cur = connection.cursor()
# boolean for the while loop
ending = True

# creating the table
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    num INTEGER PRIMARY KEY AUTOINCREMENT,
    added_time TEXT,
    task_content TEXT
)
""")

# adding example task
# cur.execute("""
# INSERT INTO tasks (added_time, task_content)
# VALUES (?,?)
# """, (current_time, "Do the dishes"))


# func to print out the tasks
def print_tasks():
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    print("")
    for i in tasks:
        print(" ".join(str(x) for x in i))


# func for adding a task
def add_task():
    task_content = input("Enter task's content : ")
    with connection:
        cur.execute("""
        INSERT INTO tasks (added_time, task_content)VALUES (?,?)
        """, (current_time, task_content))


# func for deleting a task
def delete_task():
    done_task = input("Completed task's id : ")
    with connection:
        cur.execute("""
        DELETE FROM tasks WHERE num = ?
        """, (done_task,))


# func for upgrading the task's content
def update_task():
    tasks_num = input("Enter task's num")
    task_content = input("Enter task's updated content : ")
    with connection:
        cur.execute("UPDATE tasks SET task_content = ? WHERE num = ?", (task_content, tasks_num))


# this piece of the code is running the program
while ending:
    print_tasks()
    doing = input("Enter what do you want to do (ADD/DELETE/UPDATE/\033[91m" + "END" + "\033[0m) a task : ")
    match doing:
        case "ADD":
            add_task()
        case "DELETE":
            delete_task()
        case "UPDATE":
            update_task()
        case "END":
            ending = False
