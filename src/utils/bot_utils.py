import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
import os
from data import format_data


BOT_API_KEY = os.environ.get("API_KEY")
#Setup logging module for debugging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
    
class SnifferBot:
    def __init__(self, trader_data):
        self.trader_data = trader_data


    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [InlineKeyboardButton("View Top Traders:", callback_data="1")],
        [
            InlineKeyboardButton("24 Hrs", callback_data="2"),
            InlineKeyboardButton("3D", callback_data="3"),
            InlineKeyboardButton("7D", callback_data="4"),
            InlineKeyboardButton("1M", callback_data="5")
            
        ],
        [InlineKeyboardButton("View Tracked Wallets", callback_data="6")],
        [InlineKeyboardButton("Bonk a Trader", callback_data="7")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
    
        await update.message.reply_text("Hi! Select an option below to track the top bonk traders.", reply_markup=reply_markup)

    async def buttonResponse(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #Parses the CallbackQuery and updates the message text
        query = update.callback_query
        await query.answer()
        if query.data == "2":
            #24Hrs
            message = format_data.format_table(self.trader_data, "24Hrs")
            await query.edit_message_text(text=message, parse_mode=ParseMode.HTML)
        if query.data == "3":
            #24Hrs
            message = format_data.format_table(self.trader_data, "3D")
            await query.edit_message_text(text=message, parse_mode=ParseMode.HTML)
        if query.data == "4":
            #24Hrs
            message = format_data.format_table(self.trader_data, "7D")
            await query.edit_message_text(text=message, parse_mode=ParseMode.HTML)
        if query.data == "5":
            #24Hrs
            message = format_data.format_table(self.trader_data, "1M")
            await query.edit_message_text(text=message, parse_mode=ParseMode.HTML)


    
    def bot_init(self):
        application = ApplicationBuilder().token(BOT_API_KEY).build()
        
        # Init handlers
        start_handler = CommandHandler('start', self.start_command)
        buttonClick_handler = CallbackQueryHandler(self.buttonResponse)
        
        # Add Handlers
        application.add_handler(start_handler)
        application.add_handler(buttonClick_handler)

        # Start Polling
        application.run_polling()   
     


