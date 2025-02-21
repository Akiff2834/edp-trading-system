import random
from event_types.trade_events import TradeExecutedEvent

class TradeEngine:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.trade_history = []
        self.dispatcher.register_listener("trade_order", self.execute_trade)

    def execute_trade(self, payload):
        price = round(random.uniform(100, 500), 2)
        trade_record = {**payload, "price": price}
        self.trade_history.append(trade_record)
        print(f"[TRADE EXECUTED] {payload['quantity']} {payload['symbol']} {payload['order_type'].upper()} @ {price} USD")
        self.dispatcher.dispatch(TradeExecutedEvent(**trade_record))

    def show_trade_history(self):
        print("\n📜 Trade History")
        for trade in self.trade_history:
            print(f"{trade['trader_id']} | {trade['symbol']} | {trade['quantity']} units | {trade['order_type'].upper()} @ {trade['price']} USD")
