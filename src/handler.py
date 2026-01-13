from telegram import Update
from telegram.ext import ContextTypes
from src.pertanyaan import QUESTIONS
from src.prediksi import predict

ASKING = range(len(QUESTIONS))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bot Prediksi Penyakit Jantung.\n"
        "Gunakan /predict untuk mulai."
    )

async def start_predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    context.user_data["step"] = 0

    key, question = QUESTIONS[0]
    await update.message.reply_text(question)
    return ASKING[0]

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    step = context.user_data["step"]

    try:
        value = float(update.message.text)
    except ValueError:
        await update.message.reply_text("Input harus angka. Ulangi.")
        return ASKING[step]

    key, _ = QUESTIONS[step]
    context.user_data[key] = value
    step += 1

    if step >= len(QUESTIONS):
        data = {k: context.user_data[k] for k, _ in QUESTIONS}
        result = predict(data)

        await update.message.reply_text(
            f"Hasil Prediksi Penyakit Jantung: {result}"
        )
        context.user_data.clear()
        return -1

    context.user_data["step"] = step
    _, next_question = QUESTIONS[step]
    await update.message.reply_text(next_question)

    return ASKING[step]
