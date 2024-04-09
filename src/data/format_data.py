from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    LinkPreviewOptions,
    Update,
    helpers,
)

def shorten_address(wallet_address):
    return f"{wallet_address[0:4]}...{wallet_address[-5:-1]}"

def count_lower(string):
    upper = string.upper()
    count = 0
    for idx in range(len(upper)):
        if upper[idx] != string[idx]:
            count += 1
    return count+1

def format_table(data, time_period):
    wallets, stats = parse_data(data, time_period, "wallets"), parse_data(data, time_period, "stats")
    
    # Shorten wallet addresses
    shortened = [shorten_address(x) for x in wallets]
    # HTML formatting
    body = f"""📈 🏆     <b>Top Traders of ⏳{time_period}       🏆</b>📉\n
<b>Wallet</b>                      <b>PnL</b>       <b>% Gain</b>\n"""

    # Adding data for each trader
    
    for i, (wallet, (pnl, percentage_gain)) in enumerate(zip(shortened, stats), start=1):
        pnl_space = 12-len(pnl)
        if i>9:
            
            body += f'{i}. <code>{wallet}</code>{" "*count_lower(wallet)}{pnl}  {" "*(pnl_space)}{percentage_gain}\n'
        else:
            body += f"{i}. <code>{wallet}</code>{' '*count_lower(wallet)}{pnl}  {' '*(pnl_space)}{percentage_gain}\n"

 
    
    return body



def parse_data(data, time_period, select):
    if select == "wallets":
        wallets = []
        for trader_entry in data[time_period]:
            wallets.append([x for x in trader_entry.keys()][0])
        return wallets
    
    elif select == "stats":
        stats = [] #(PnL, Percentage Gain)
        for trader_entry in data[time_period]:
            stats_table = trader_entry[list(trader_entry.keys())[0]]
            stats.append((stats_table["PnL"], stats_table["Percentage Gain"]))
        return stats


