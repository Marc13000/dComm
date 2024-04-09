from utils import bot_utils
from data import api_data

def main():
    top_trader_data = api_data.return_api_data()
    snifferbot = bot_utils.SnifferBot(top_trader_data).bot_init()

if __name__ == "__main__":
    main()