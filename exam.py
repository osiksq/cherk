import sqlite3

def connect():
    return sqlite3.connect('db.sl3')

def register(login, password):
    conn = connect()
    try:
        conn.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, password))
        conn.commit()
        print("Регистрация успешна!")
    except sqlite3.IntegrityError:
        print("Этот логин уже занят!")
    except Exception as e:
        print("Ошибка: ", e)
    finally:
        conn.close()

def check(login, password):
    conn = connect()
    result = conn.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, password)).fetchone()
    conn.close()
    return result is not None

def user_exists(login):
    conn = connect()
    result = conn.execute("SELECT * FROM users WHERE login = ?", (login,)).fetchone()
    conn.close()
    return result is not None

def show_users():
    conn = connect()
    users = conn.execute("SELECT * FROM users").fetchall()
    print("Все пользователи:")
    for user in users:
        print(user)
    conn.close()

def main():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    if check(login, password):
        print("Вы вошли!")
        if input("Показать всех пользователей? (да/нет): ").lower() == "да":
            show_users()
    else:
        print("Неправильный логин или пароль.")
        if user_exists(login):
            print("Логин существует, но пароль неправильный.")
        else:
            if input("Хотите зарегистрироваться? (да/нет): ").lower() == "да":
                register(login, password)
                if input("Показать всех пользователей? (да/нет): ").lower() == "да":
                    show_users()

if __name__ == "__main__":
    main()