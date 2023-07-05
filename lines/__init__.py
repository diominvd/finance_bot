import config

keyboards_lines: dict = {
    'menu_keyboard': {
        'income': '📈 | Доход',
        'expense': '📉 | Расход',
        'profile': '👤 | Профиль',
        'settings': '⚙️ | Настройки'
    },
    'currencies_keyboard': {
        'RUB': {
            'title': '🇷🇺 | RUB (₽)',
            'callback_data': 'currency_RUB',
            'text': '₽'
        },
        'BYN': {
            'title': '🇧🇾 | BYN (Br)',
            'callback_data': 'currency_BYN',
            'text': 'Br'
        },
        'UAH': {
            'title': '🇺🇦 | UAH (₴)',
            'callback_data': 'currency_UAH',
            'text': '₴'
        },
        'KZT': {
            'title': '🇰🇿 | KZT (₸)',
            'callback_data': 'currency_KZT',
            'text': '₸'
        },
        'USD': {
            'title': '🇺🇸 | USD ($)',
            'callback_data': 'currency_USD',
            'text': '$'
        },
        'EUR': {
            'title': '🇪🇺 | EUR (€)',
            'callback_data': 'currency_EUR',
            'text': '€'
        },
        'cancel': {
            'title': 'Отмена',
            'callback_data': 'cancel',
        }
    }
}

commands_lines: dict = {
    'command_text_help': 'Список основных функций бота:\n\n'
                         '1. <b>Добавить операцию</b> - Позволяет добавить операцию с последующим выбором категории и суммы. '
                         'Операция сохраняется в базу данных.\n\n'
                         '2. <b>Последние операции</b> - Отображает последние 5 операций с возможностью '
                         'удалить последнюю добавленную операцию.\n\n'
                         '3. <b>Профиль</b> - Отображает вашу статистику по всем категориям за отчётный период.\n\n'
                         '4. <b>Настройки</b> - Дополнительные функции.\n'
                         '4.1 <b>Очистить историю операций</b> - Удаляет всю историю операций. При этом сбрасывается отчётный период. '
                         'Чтобы начать новый период добавьте новую операцию.',
    'command_text_info': f'<b>Finance Bot v{config.version}</b>.\n'
                         f'Исходный код проекта на Git Hub: clck.ru/34qJYm\n'
                         f'Официальная группа: @diominvdev\n'
                         f'Developer: @diominvd',
    'command_text_start': 'Добро пожаловать в Finance Bot 💲\n\n'
                          'Этот бот поможет вести учёт расходов. '
                          'Вы можете классифицировать все операции по категориям, '
                          'просматривать последние операции и формировать отчёт за определённый период.\n\n'
                          'Для получения дополнительной информации напишите команду "/help."',
}


first_start_lines: dict = {
    'error_text_incorrect_categories': 'Некорректный ввод. Повторите попытку.',
    'error_text_wrong_balance': 'Некорректное значение. Повторите попытку',

    'text_set_currency': 'Перед использованием настроим бота. Выберите валюту, которая будет использована в дальнейших операциях.',
    'text_set_balance': 'Отлично. Теперь укажите текущий баланс.',
    'text_set_income_categories': 'Теперь создадим категории для доходов. Отправьте список категорий в формате:\n\n'
                                  'название_категории emoji\n'
                                  'название_категории emoji\n\n'
                                  'Между название категории и emoji должен быть пробел.',
    'text_set_expense_categories': 'Теперь отправьте категории расходов в таком же формате, как и категории доходов.',
    'text_first_start_complete': 'Отлично. Первичная настройка завершена.'
}


income_lines: dict = {
    'text_choose_income_category': 'Выберите категорию для операции.'
}
