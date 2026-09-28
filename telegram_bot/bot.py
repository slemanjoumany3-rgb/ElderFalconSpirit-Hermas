from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

class TelegramBot:
    def __init__(self, token, allowed_users, llm_callback, state):
        self.token = token
        self.allowed_users = allowed_users.split(",")
        self.llm = llm_callback
        self.state = state

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = str(update.effective_user.id)
        if user_id not in self.allowed_users:
            await update.message.reply_text("❌ Access denied.")
            return

        prompt = update.message.text
        reply = self.llm(prompt)
        await update.message.reply_text(reply)

    def run(self):
        app = ApplicationBuilder().token(self.token).build()
        app.add_handler(MessageHandler(filters.TEXT, self.handle_message))
        app.run_polling()
