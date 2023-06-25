import pydantic.main

keyboards: dict = {
    'menu_keyboard': {
        'add_operation': 'Добавить операцию',
        'last_operations': 'Последние операции',
        'profile': 'Профиль',
        'settings': 'Настройки'
    },
    'categories_keyboard': {
        'products': {
            'title': 'Продукты',
            'callback_data': 'category_products'
        },
        'cafes': {
            'title': 'Кафе',
            'callback_data': 'category_cafe'
        },
        'auto': {
            'title': 'Автомобиль',
            'callback_data': 'category_auto'
        },
        'transport': {
            'title': 'Транспорт',
            'callback_data': 'category_transport'
        },
        'home': {
            'title': 'Дом',
            'callback_data': 'category_home'
        },
        'entertainment': {
            'title': 'Развлечения',
            'callback_data': 'category_entertainment'
        },
        'sport': {
            'title': 'Спорт',
            'callback_data': 'category_sport'
        },
        'health': {
            'title': 'Здоровье',
            'callback_data': 'category_health'
        },
        'education': {
            'title': 'Образование',
            'callback_data': 'category_education'
        },
        'gifts': {
            'title': 'Подарки',
            'callback_data': 'category_gifts'
        },
        'beauty': {
            'title': 'Красота',
            'callback_data': 'category_beauty'
        },
        'clothes': {
            'title': 'Одежда',
            'callback_data': 'category_clothes'
        },
        'technic': {
            'title': 'Техника',
            'callback_data': 'category_technic'
        },
        'subscriptions': {
            'title': 'Подписки',
            'callback_data': 'category_subscriptions'
        },
        'menu': {
            'title': 'Главное меню',
            'callback_data': 'menu'
        }
    },
    'last_operations_keyboard': {
        'delete_last_operation': {
            'title': 'Удалить последнюю операцию',
            'callback_data': 'delete_last'
        },
        'menu': {
            'title': 'Главное меню',
            'callback_data': 'menu'
        }
    }
}

categories: dict = {
    'products': 'Продукты',
    'cafes': 'Кафе',
    'auto': 'Автомобиль',
    'transport': 'Транспорт',
    'home': 'Дом',
    'entertainment': 'Развлечения',
    'sport': 'Спорт',
    'health': 'Здоровье',
    'education': 'Образование',
    'gifts': 'Подарки',
    'beauty': 'Красота',
    'clothes': 'Одежда',
    'technic': 'Техника',
    'subscriptions': 'Подписки'
}

commands: dict = {
    'start_command_text': 'Добро пожаловать в Finance Bot 💲\n\n'
                          'Этот бот поможет вести учёт расходов. '
                          'Вы можете классифицировать все операции по категориям, '
                          'просматривать последние операции и формировать отчёт за определённый период.\n\n'
                          'Для получения дополнительной информации напишите команду "/help."',
    'help_command_text': 'Список основных функций бота:\n\n'
                         '1. <b>Добавить операцию</b> - Позволяет добавить операцию с последующим выбором категории и суммы.\n\n'
                         '2. <b>Последние операции</b> - Отображает последние 5 операций.\n\n'
                         '3. <b>Профиль</b> - Отображает вашу статистику по всем категориям.\n\n'
                         '4. <b>Настройки</b> - Дополнительные функции.'
}

def output_category(category: str = None) -> str:
    return f'Выбрана категория: {categories[category]}'

def operation_complete_output(user_id: int = None) -> str:
    from config import bot_storage
    return f'📌 Операция успешно добавлена.\n' \
           f'Категория: {categories[bot_storage[user_id]["category"]]}\n' \
           f'Сумма: {bot_storage[user_id]["value"]} ₽\n' \
           f'Дата создания: {bot_storage[user_id]["date"]}\n\n'


new_operation: dict = {
    'choose_operation_category': 'Пожалуйста, укажите категорию для операции.',
    'operation_category_chosen': output_category,
    'choose_operation_value': 'Пожалуйста, укажите сумму операции.',
    'incorrect_value': 'Неверное значение суммы операции. Повторите попытку.',
    'operation_complete': operation_complete_output
}

def output_last_operations(operations: list) -> str:
    message_text = f'Последние операции:\n'
    for operation in operations:
        operation_id: int = operation[0]
        user_id: int = operation[1]
        category: str = operation[2]
        value: float = operation[3]
        date: str = operation[4]
        message_text += f'{value} ₽ | {categories[category]} | {date}\n'
    return message_text


last_operations: dict = {
    'output_last_operations': output_last_operations,
    'last_operations_empty': 'Список последних операций пуст.'
}

other: dict = {
    'back_to_menu': 'Возвращаюсь в главное меню.'
}


