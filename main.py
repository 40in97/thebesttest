from pydantic import BaseModel, ValidationError
import config
import logging
import asyncio
from aiogram.filters.command import Command,CommandStart
from aiogram import Bot, Dispatcher, types,F,Router
from aiogram.types.message import ContentType, Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo


bot = Bot(token=config.TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Открыть веб-страницу",web_app=WebAppInfo(url='https://rawcdn.githack.com/40in97/thebesttest/4655090b3ac7e9fd96a7b37673c4090e2c5b853c/index.html'))]
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Привет,мой друг!", reply_markup=keyboard)


PRICE = {
    '1': [types.LabeledPrice(label='Item1', amount=100000)],
    '2': [types.LabeledPrice(label='Item2', amount=200000)],
    '3': [types.LabeledPrice(label='Item3', amount=300000)],
    '4': [types.LabeledPrice(label='Item4', amount=400000)],
    '5': [types.LabeledPrice(label='Item5', amount=500000)],
    '6': [types.LabeledPrice(label='Item6', amount=600000)]
}

@dp.message(F.web_app_data)
async def buy_process(web_app_message):
    await bot.send_invoice(web_app_message.chat.id,
                           title='Laptop',
                           description='Description',
                           provider_token='pay_token',
                           currency='rub',
                           need_email=True,
                           prices=PRICE[f'{web_app_message.web_app_data.data}'],
                           start_parameter='example',
                           payload='some_invoice')

@dp.pre_checkout_query(lambda query: True)
async def pre_checkout_process(pre_checkout: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)

@dp.message(F.types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await bot.send_message(message.chat.id, 'Платеж прошел успешно!')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())