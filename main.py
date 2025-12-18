from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from credits import API_TG
from AI import responce_ai
import asyncio

bot = Bot(token=API_TG)
dp = Dispatcher()

class State(StatesGroup):
    waitIdea = State()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💡 Получить идею 💡")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

@dp.message(CommandStart())
async def send_idea(message: Message, state: FSMContext):
    await message.answer("Привет. Я бот который поможет придумать идею для твоего проекта.\nЧтобы придумать идею введи '/idea' или используй клавиатуру.", reply_markup=keyboard)


@dp.message(Command('idea'))
@dp.message(F.text == "💡 Получить идею 💡")
async def send_idea(message: Message, state: FSMContext):
    await state.set_state(State.waitIdea)
    await message.answer("Опишите подробнее...\nПример: 'Я пишу на языке Python. Хочу написать telegram бота но не знаю какого.'")

@dp.message(State.waitIdea)
async def generate_idea(message: Message, state: FSMContext):
    await message.answer("🕐 Обрабатываю ваш запрос...")
    result = await responce_ai(message.text)
    await message.answer(result)
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())