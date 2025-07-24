from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
import logging




async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Ciao {update.message.from_user.first_name} ecco una lista utile di comandi:\n/start\n/max\n/start")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Sono Viva, {update.message.from_user.first_name}")


async def insultaMax(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Max Sei un coglione")