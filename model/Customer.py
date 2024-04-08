
class Customer:

    def __init__(self, customer_id, first_name, last_name, bank_name, credit_card_number, amount_of_money):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.bank_name = bank_name
        self.credit_card_number = credit_card_number
        self.amount_of_money = amount_of_money

    def get_payment(self, salary: int):
        self.amount_of_money = self.amount_of_money + salary
