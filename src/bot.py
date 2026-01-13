from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
)
from src.handler import start, start_predict, handle_answer
from src.pertanyaan import QUESTIONS

def init_bot(token: str):
    app = ApplicationBuilder().token(token).build()

    conv = ConversationHandler(
        entry_points=[CommandHandler("predict", start_predict)],
        states={
            i: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer)]
            for i in range(len(QUESTIONS))
        },
        fallbacks=[],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv)

    return app
