import os
from dotenv import load_dotenv
from src.bot import init_bot

load_dotenv()

app = init_bot(os.getenv("BOT_TOKEN"))
app.run_polling()
