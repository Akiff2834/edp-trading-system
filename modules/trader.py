from event_types.trade_events import TradeOrderEvent

class Trader:
    def __init__(self, trader_id, dispatcher):
        self.trader_id = trader_id
        self.dispatcher = dispatcher

    def place_order(self, symbol, quantity, order_type):
        print(f"[Trader {self.trader_id}] {quantity} {symbol} için {order_type.upper()} emri verdi.")
        event = TradeOrderEvent(self.trader_id, symbol, quantity, order_type)
        self.dispatcher.dispatch(event)