from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

menu_ikb = InlineKeyboardMarkup()

start_b1 = InlineKeyboardButton(text="Вселенная Лавкрафта",callback_data="university_of_Lavkraft")
start_b2 = InlineKeyboardButton(text="Настольные игры по Лавкрафту", callback_data="board_games_about_Lavkraft")
start_b3 = InlineKeyboardButton(text="rfg", callback_data="et")


menu_ikb.add(start_b1, start_b2, start_b3)


board_games_kb = InlineKeyboardMarkup()

board_games_b1 = InlineKeyboardButton(text="Ужас Аркхема",callback_data="horror_of_Arkham_board_game")
board_games_b2 = InlineKeyboardButton(text="Карточный ужас Аркхема",callback_data="horror_of_Arkham_card_game")
board_games_b3 = InlineKeyboardButton(text="Древний ужас", callback_data="eldritch_horror_board_game")
board_games_b4 = InlineKeyboardButton(text="Особняки безумия",callback_data="mansions_of_madness_board_game")
board_games_b5 = InlineKeyboardButton(text="Зов Ктулху",callback_data="call_of_Ctulchu_board_role_game")

board_games_kb.add(board_games_b1, board_games_b2, board_games_b3, board_games_b4, board_games_b5)


university_kb = InlineKeyboardMarkup()

university_b1 = InlineKeyboardButton(text="Древние боги", callback_data="eldritch_gods")
university_b2 = InlineKeyboardButton(text="Города", callback_data="cities")
university_b3 = InlineKeyboardButton(text="Виды", callback_data="species")

university_kb.add(university_b1, university_b2, university_b3)


