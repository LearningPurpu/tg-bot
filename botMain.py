from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
import logging
import comandi


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main() -> None:
    application = Application.builder().token("8404456019:AAF-1wX9DR1kv97CsQLYSzaL1XxOSP-jfMM").build()

    application.add_handler(CommandHandler("start", comandi.start))
    application.add_handler(CommandHandler("max", comandi.insultaMax))
    application.add_handler(CommandHandler("info", comandi.info))

    application.run_polling()


if __name__ == "__main__":
    main()