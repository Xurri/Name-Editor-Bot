import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from transliterate import translit

# Инициализация объектов
# TOKEN = os.getenv('7432763375:AAExICjlVQRxOIK-W-OLSCpivRBLzIgD0NE')
bot = Bot(token='7432763375:AAExICjlVQRxOIK-W-OLSCpivRBLzIgD0NE')      
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

#Обработка /start

@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Напиши свои ФИО'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

# Обработка/Хэндлер на любые сообщения

@dp.message()
async def fio_latin(message: Message):
    fio = message.text
    transliterate_fio = translit(fio, language_code='ru', reversed=True)
    logging.info(f'ФИО пользователя: {fio}. Транслитерация: {transliterate_fio}')
    await message.answer(text=f'Транслитерация ФИО: {transliterate_fio}')

# Запуск процесса пуллинга

if __name__ == '__main__':
    dp.run_polling(bot)