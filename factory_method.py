from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process(self):
        pass


class CreditCardPayment(Payment):
    def process(self):
        print("credit card payment")


class PayPalPayment(Payment):
    def process(self):
        print("paypal payment")


class PaymentFactory:
    @abstractmethod
    def create_payment(self):
        pass


class CreditCardFactory(PaymentFactory):
    def create_payment(self):
        return CreditCardPayment()


class PayPalFactory(PaymentFactory):
    def create_payment(self):
        return PayPalPayment()


if __name__ == "__main__":
    credit_factory = CreditCardFactory()
    paypal_factory = PayPalFactory()

    credit_factory.create_payment().process()
    paypal_factory.create_payment().process()
