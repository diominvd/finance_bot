from config import bot_storage
from data import connection, cursor


def insert_new_user_into_database(user_id: int) -> None:
    try:
        cursor.execute(f'INSERT INTO users VALUES (?, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)',
                       (user_id,))
    except:
        print(f'> insert user {user_id} into database/users: error.')
    else:
        connection.commit()
        print(f'> insert user {user_id} into database/users: success.')


def insert_operation_into_database(user_id: int) -> None:
    # Fetch operation data from boot storage.
    category: str = bot_storage[user_id]['category']
    value: float = bot_storage[user_id]['value']
    date: str = bot_storage[user_id]['date']

    try:
        # Operation data -> database/operations.
        cursor.execute(f'INSERT INTO operations (user_id, category, value, date) VALUES (?, ?, ?, ?)',
                       (user_id, category, value, date))
        connection.commit()

        # Operation data -> database/users.
        cursor.execute(f'UPDATE users SET {category} = {category} + ?, total = total + ? WHERE user_id = ?',
                       (value, value, user_id))
        connection.commit()
    except:
        print(f'> storage -> {user_id} -> operation data -> database: error.')
    else:
        print(f'> storage -> {user_id} -> operation data -> database: success.')


def select_last_operations_from_database(user_id: int) -> list:
    try:
        cursor.execute(f'SELECT * FROM operations WHERE user_id = ? ORDER BY operation_id DESC LIMIT 5', (user_id,))
    except:
        print(f'> database -> {user_id} -> last operations: error.')
    else:
        last_operations: list = list(reversed(cursor.fetchall()))
        return last_operations


def delete_last_operation_from_database(user_id: int) -> list:
    # Fetch operation category and value for update database/users.
    cursor.execute(f'SELECT category, value FROM operations WHERE user_id =? ORDER BY operation_id DESC LIMIT 1',
                   (user_id,))
    operation_data = cursor.fetchall()[0]

    category: str = operation_data[0]
    value: float = operation_data[1]

    # Delete operation value from database/users.
    cursor.execute(f'UPDATE users SET {category} = {category} - ?, total = total - ? WHERE user_id = ?',
                   (value, value, user_id))
    connection.commit()

    # Delete last operation from database/operations.
    cursor.execute(f'DELETE FROM operations WHERE operation_id = (SELECT MAX(operation_id) FROM operations) and user_id = ?',
                   (user_id,))
    connection.commit()

    last_operations: list = select_last_operations_from_database(user_id=user_id)

    return last_operations
