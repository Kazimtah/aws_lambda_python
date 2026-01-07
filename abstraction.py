from abc import ABC, classmethod
class Payment:
    @classmethod
    def proces_payment(self):
        pass 

class Creditecardpayment(Payment):
    def proces_payment(self):
        pass

class StripPayment(Payment):
    def proces_payment(self):
        pass


class PayballPayment(Payment):
    def proces_payment(self):
        pass