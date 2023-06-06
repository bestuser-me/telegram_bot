import logging
from dictionary import getdef
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
API_TOKEN = '6170406728:AAEq7yxZThAHcF7OpklchIz3GYo9FHLdmy0'

# Configure logging
logging.basicConfig(level=logging.INFO)
translator = Translator()
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum, Botimizga xush kelibsiz!\nWikipediani telegramni o'zidan ishlating va qiziqarli malumotlarni bilib oling")



@dp.message_handler()
async def tarjimon(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word = message.text
        else:
            word = translator.translate(message.text, dest='en').text
        lookup = getdef(word)
        if lookup:
            await message.reply(f"Word: {word} \nDefinitions:\n{lookup['defs']}")
            if lookup.get('sound'):
                await message.reply_voice(lookup['sound'])
        else:
            await message.reply('bunday so\'z topilmadi')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)