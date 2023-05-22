import time
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = "6172664683:AAHxMzJz_XzJxi-_cAfcwiGBPSa6A9xrtvQ"
MSG = "Привет! Чем сегодня займемся?"
MSG2 = "Какие задачи ставишь на завтра?"
MSG3 = "Слушай, отличная идея, напиши подробности @ml_steve, он одобрит)"
MSG4 = """SteevE bot(V_0.1,5)> создан с несколькими целями:\n
            1)Сейчас он может задавать вопросы, но ему пока до фени, что Вы отвечаете, т.к. ему несколько часов отроду, он еще маленький
            В последующих версиях бот будет поддерживать диалог на ограниченные темы и станет незаменимым помочником и бизнес-ассистентом
            2)Бот научится ставить задачи на нужную дату и напоминать о них в нужное время 
            3)Уже готова функция приглашения на тусы, всю необходимую информацию бот уже готов отправлять пользователю. Спасибо за внимание"""
MSG5 = "Ты ж умница! Заходи по ссылке https://www.doors-treasures.ru . Если у тебя уже есть аккаунт тут, напиши @ml_steve в личку свой ник в игре и мы с тобой оформим каточку"




bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}, {time.asctime()}')

    await message.reply(f"Привет, {user_full_name}!")
    await bot.send_message(user_id, MSG.format(user_name))

@dp.message_handler(commands=['task'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}, {time.asctime()}')

    await bot.send_message(user_id, MSG2.format(user_name))

    @dp.message_handler(commands=['party'])
    async def start_handler(message: types.Message):
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        user_full_name = message.from_user.full_name
        logging.info(f'{user_id=} {user_full_name=}, {time.asctime()}')

        await bot.send_message(user_id, MSG3.format(user_name))

    @dp.message_handler(commands=['diplom'])
    async def start_handler(message: types.Message):
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        user_full_name = message.from_user.full_name
        logging.info(f'{user_id=} {user_full_name=}, {time.asctime()}')

        await bot.send_message(user_id, MSG4.format(user_name))\


    @dp.message_handler(commands=['man4kin'])
    async def start_handler(message: types.Message):
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        user_full_name = message.from_user.full_name
        logging.info(f'{user_id=} {user_full_name=}, {time.asctime()}')

        await bot.send_message(user_id, MSG5.format(user_name))


if __name__ == '__main__':
    executor.start_polling(dp)