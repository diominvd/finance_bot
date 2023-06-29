import aiogram.types
import pydantic.main

from config import dispatcher


from handlers.commands import help, start
dispatcher.include_routers(
    help.router,
    start.router
)

from handlers.last_operations import delete_last_operation, last_operations_command
dispatcher.include_routers(
    delete_last_operation.router,
    last_operations_command.router
)

from handlers.market import market_command
from handlers.market.add_ticker import add_new_ticker, add_ticker_command
from handlers.market.my_tickers import get_ticker_for_parsing, my_ticker_command
dispatcher.include_routers(
    market_command.router,
    add_new_ticker.router,
    add_ticker_command.router,
    get_ticker_for_parsing.router,
    my_ticker_command.router
)

from handlers.new_operation import add_operation_command, operation_category, operation_value
dispatcher.include_routers(
    add_operation_command.router,
    operation_category.router,
    operation_value.router
)

from handlers.other import incorrect_ticker, market_menu, menu
dispatcher.include_routers(
    incorrect_ticker.router,
    market_menu.router,
    menu.router
)

from handlers.profile import profile_command_handler
dispatcher.include_routers(
    profile_command_handler.router
)

from handlers.settings import delete_all_operations_handler, settings_command_handler
dispatcher.include_routers(
    delete_all_operations_handler.router,
    settings_command_handler.router
)

def fetch_user_id(obj: pydantic.main.ModelMetaclass) -> int:
    return int(obj.from_user.id)

def fetch_user_username(obj: pydantic.main.ModelMetaclass) -> str:
    return str(obj.from_user.username)


async def remove_callback_delay(callback_query: aiogram.types.CallbackQuery) -> None:
    await callback_query.answer(text=None,
                                show_alert=None)
    return None