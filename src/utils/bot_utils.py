import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, helpers
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
import os
import time
from data import format_data


BOT_API_KEY = os.environ.get("API_KEY")
#Setup logging module for debugging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
    
class SnifferBot:
    def __init__(self, trader_data):
        self.trader_data = trader_data
        self.TRACK_WALLET = 0 


    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.message.reply_text('Operation cancelled.')
        return ConversationHandler.END
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE, from_callback_query=False):
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
        
        message_text = "Hi! Select an option below to track the top bonk traders."
        if from_callback_query:
            query = update.callback_query
            await query.edit_message_text(text=message_text, reply_markup=reply_markup)
        else:
            await update.message.reply_text(message_text, reply_markup=reply_markup)

    async def buttonResponse(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #Parses the CallbackQuery and updates the message text

        keyboard = [[InlineKeyboardButton("Track a Wallet", callback_data="8")],
            [InlineKeyboardButton("Back", callback_data="0")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query = update.callback_query
        await query.answer()
        if query.data == "2":
            #24Hrs
            message = format_data.format_table(self.trader_data, "24Hrs")
            await query.edit_message_text(text=message, parse_mode=ParseMode.HTML,reply_markup=reply_markup)
        elif query.data == "3":
            #24Hrs
            message = format_data.format_table(self.trader_data, "3D")
            await query.edit_message_text(text=message, parse_mode=ParseMode.HTML,reply_markup=reply_markup)
        elif query.data == "4":
            #24Hrs
            message = format_data.format_table(self.trader_data, "7D")
            await query.edit_message_text(text=message, parse_mode=ParseMode.HTML,reply_markup=reply_markup)
        elif query.data == "5":
            #24Hrs
            message = format_data.format_table(self.trader_data, "1M")
            await query.edit_message_text(text=message, parse_mode=ParseMode.HTML,reply_markup=reply_markup)
        elif query.data == "8":
            await self.prompt_for_wallet_rank(update, context)
        
        elif query.data[0]=="w":
            keyboard = [
            [InlineKeyboardButton("Trade (BAG) on BonkBot", url="https://t.me/bonkbot_bot?start=ref_nxk03_ca_D8r8XTuCrUhLheWeGXSwC3G92RhASficV3YA7B2XWcLv")]
        ]
            reply_markup2 = InlineKeyboardMarkup(keyboard)
            await query.message.reply_text(f"Tracking Wallet as: 'wallet1'")
            time.sleep(3)
            await query.message.reply_text(f"'wallet1' just swapped 4.000 SOL for 32528.32 catwifbag (BAG)", reply_markup=reply_markup2)

        elif query.data == "0":
            await self.start_command(update, context, from_callback_query=True)
            
            

    async def prompt_for_wallet_rank(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        query = update.callback_query
        keyboard = [[InlineKeyboardButton("1", callback_data="w1"), 
                     InlineKeyboardButton("2", callback_data="w2")
                     ,InlineKeyboardButton("3", callback_data="w3")
                     ,InlineKeyboardButton("4", callback_data="w4"), 
                     InlineKeyboardButton("5", callback_data="w5"),
                     ],
                     [
                     InlineKeyboardButton("6", callback_data="w6"),
                     InlineKeyboardButton("7", callback_data="w7"),
                     InlineKeyboardButton("8", callback_data="w8"),
                     InlineKeyboardButton("9", callback_data="w9"),
                     InlineKeyboardButton("10", callback_data="w10")
                     ],
            [InlineKeyboardButton("Back", callback_data="0")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.answer()
        await query.message.reply_text("Please enter the rank of the wallet you want to track (1-10):", reply_markup=reply_markup)
        return self.TRACK_WALLET
    
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
     


