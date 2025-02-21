from event_dispatcher import EventDispatcher
from modules.exchange import Exchange
from modules.trader import Trader
from modules.trade_engine import TradeEngine

# Olay yöneticisini başlat
dispatcher = EventDispatcher()

# Ajanları oluştur
exchange = Exchange(dispatcher)
trader = Trader("Trader_1", dispatcher)
trade_engine = TradeEngine(dispatcher)

# Olayları simüle et
exchange.update_price("BTC")
trader.place_order("BTC", 2, "buy")
exchange.update_price("BTC")
trade_engine.show_trade_history()
