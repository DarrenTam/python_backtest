from __future__ import print_function
class Event(object): """
Event is base class providing an interface for all subsequent (inherited) events, that will trigger further events in the
trading infrastructure. """
pass



class MarketEvent(Event): 
    def __init__(self):
        """
        Initialises the MarketEvent. """
        self.type = "MARKET"
        
class SignalEvent(Event): """
Handles the event of sending a Signal from a Strategy object. This is received by a Portfolio object and acted upon.
"""
def __init__(self, strategy_id, symbol, datetime, signal_type, strength):
    self.type = "SIGNAL" 
    self.strategy_id = strategy_id 
    self.symbol = symbol
    self.datetime = datetime 
    self.signal_type = signal_type 
    self.strength = strength

class OrderEvent(Event):
    def __init__(self, symbol, order_type, quantity, direction):
        self.type = "ORDER"
        self.symbol = symbol 
        self.order_type = order_type 
        self.quantity = quantity 
        self.direction = direction
    def print_order(self): 
        print("Order: Symbol=%s, Type=%s, Quantity=%s, Direction=%s" %(self.symbol, self.order_type, self.quantity, self.direction) )
        
class FillEvent(Event):
    
    def __init__(self, timeindex, symbol, exchange, quantity, direction, fill_cost, commission=None):
        self.type = "FILL"
        self.timeindex = timeindex 
        self.symbol = symbol
        self.exchange = exchange 
        self.quantity = quantity 
        self.direction = direction 
        self.fill_cost = fill_cost
        if commission is None:
            self.commission = self.calculate_ib_commission()
        else:
            self.commission = commission

    def calculate_ib_commission(self):
        if self.quantity <= 500:
            full_cost = max(1.3, 0.013 * self.quantity) 
        else: # Greater than 500
            full_cost = max(1.3, 0.008 * self.quantity) 
        return full_cost