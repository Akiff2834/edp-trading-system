class Event:
    def __init__(self, payload=None):
        self.payload = payload if payload else {}

    def event_name(self):
        raise NotImplementedError("Alt sınıflar event_name tanımlamalı!")
