import random
from event_types.price_events import PriceUpdateEvent

class Exchange:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def update_price(self, symbol):
        price = round(random.uniform(100, 500), 2)  # Rastgele fiyat oluştur
        print(f"[Exchange] {symbol} fiyat güncellendi: {price} USD")
        event = PriceUpdateEvent(symbol, price)
        self.dispatcher.dispatch(event)
