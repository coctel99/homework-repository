"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75
order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""
from abc import ABC, abstractmethod


class Discount(ABC):
    @staticmethod
    @abstractmethod
    def get_discount_rate() -> float:
        pass


class MorningDiscount(Discount):
    @staticmethod
    def get_discount_rate() -> float:
        return 0.25


class ElderDiscount(Discount):
    @staticmethod
    def get_discount_rate() -> float:
        return 0.4


class Order:
    discount: Discount

    def __init__(self, price):
        self.price = price

    def set_discount(self, discount: type(Discount)) -> None:
        """
        Set order discount
        :param discount: Type of discount to apply
        """
        self.discount = discount

    def get_final_price(self) -> float:
        """
        Get order final price
        :return: If objects has discount, return price with discount
        applied, else return original price
        """
        if not getattr(self, "discount", None):
            return self.price
        return self.price - self.price * self.discount.get_discount_rate()
