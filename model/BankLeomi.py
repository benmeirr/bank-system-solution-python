from overrides import overrides
from model.Bank import Bank

class BankLeomi(Bank):

    def __init__(self, bank_id, bank_name, number_of_employees, amount_of_revenue, amount_of_expenses, bank_customers):
        super().__init__(bank_id, bank_name, number_of_employees, amount_of_revenue, amount_of_expenses, bank_customers)

    @overrides
    def calculate_customer_money(self):
        customer_total_amount_of_money = 0
        for customer in self.bank_customers:
            customer_total_amount_of_money = customer_total_amount_of_money + customer.amount_of_money
        return self.amount_of_revenue - customer_total_amount_of_money
