import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="student_db",
    user="postgres",
    password="abhinand12",
    port="5432"
)

print("Database connected successfully!")

connection.close()