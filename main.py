from aiogram import Dispatcher, types, executor
from congig import bot
from keyboards import *
from all_texts import *

first_time_write = True
dp = Dispatcher(bot)

@dp.callback_query_handler(text = "university_of_Lavkraft")
async def university_of_Lavkraft (call:types.callback_query):
    await call.message.answer(text= university_of_Lavkraft_text, reply_markup=university_kb)
    await call.answer()

@dp.callback_query_handler(text = "board_games_about_Lavkraft")
async def board_games_about_Lavkraft (call:types.callback_query):
    await call.message.answer(text= board_games_about_Lavkraft_text, reply_markup=board_games_kb)
    await call.answer()

@dp.callback_query_handler(text = "university_of_Lavkraft")
async def university_of_Lavkraft (call:types.callback_query):
    await call.message.answer(text= university_of_Lavkraft_text, reply_markup=university_kb)
    await call.answer()

@dp.callback_query_handler(text = "eldritch_gods")
async def eldritch_gods (call:types.callback_query):
    await call.message.answer(text= eldritch_gods_text)
    await call.answer()

@dp.callback_query_handler(text = "cities")
async def cities (call:types.callback_query):
    await call.message.answer(text= cities_text)
    await call.answer()

@dp.callback_query_handler(text = "species")
async def species (call:types.callback_query):
    await call.message.answer(text=species_text )
    await call.answer()

@dp.callback_query_handler(text = "horror_of_Archam_board_game")
async def horror_of_Archam_board_game (call:types.callback_query):
    await call.message.answer(text= horror_of_Archam_board_game_text )
    await call.answer()

@dp.callback_query_handler(text = "horror_of_Archam_card_game")
async def horror_of_Archam_card_game (call:types.callback_query):
    await call.message.answer(text=horror_of_Archam_card_game_text )
    await call.answer()

@dp.callback_query_handler(text = "call_of_Cthulhu_board_role_game")
async def eldritch_horror_board_game (call:types.callback_query):
    await call.message.answer(text= call_of_Cthulhu_board_role_game_text )
    await call.answer()

@dp.callback_query_handler(text = "mansions_of_madness_board_game")
async def mansions_of_madness_board_game (call:types.callback_query):
    await call.message.answer(text= mansions_of_madness_board_game_text)
    await call.answer()

@dp.message_handler()
async def first_message (msg: types.Message):
    global first_time_write
    if first_time_write == True:
        await msg.answer(text=start_text, reply_markup=menu_ikb)
        first_time_write = False


if  __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


                #Хватит писать в моем файле