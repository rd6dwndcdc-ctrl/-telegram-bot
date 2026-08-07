from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os
TOKEN=os.getenv('BOT_TOKEN')
ADMIN=int(os.getenv('ADMIN_ID'))
async def h(update:Update, ctx:ContextTypes.DEFAULT_TYPE):
 u=update.effective_user
 t=update.message.text or ''
 await update.message.reply_text('✅ تم إرسال رسالتك، سيتم الرد عليك قريبًا.')
 msg=f'📩 رسالة جديدة\n\n👤 {u.full_name}\n🆔 {u.id}\n🔗 @{u.username}\n\n💬 {t}'
 await ctx.bot.send_message(ADMIN,msg)
app=Application.builder().token(TOKEN).build();app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,h));app.run_polling()