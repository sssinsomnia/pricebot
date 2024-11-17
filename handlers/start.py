from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

# функция для реагирования на команду /start
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, <b>{message.from_user.full_name}</b>! Бот запущен")