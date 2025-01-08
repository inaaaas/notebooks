import psycopg2

def init_db():
    db_name = "notebooks_db"
    db_user = "ina"
    db_password = "ina1234"
    db_host = "localhost"
    db_port = 5432

    try:
        conn = psycopg2.connect(
            dbname="postgres", user=db_user, password=db_password, host=db_host, port=db_port
        )
        conn.autocommit = True
        cursor = conn.cursor()

        try:
            cursor.execute(f"CREATE DATABASE {db_name};")
            print(f"База данных '{db_name}' успешно создана.")
        except psycopg2.errors.DuplicateDatabase:
            print(f"База данных '{db_name}' уже существует.")

        cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user};")
        print(f"Привилегии для пользователя '{db_user}' успешно назначены.")

    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    init_db()
