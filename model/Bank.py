from abc import ABC, abstractmethod
from model.Customer import Customer

class Bank(ABC):

    @abstractmethod
    def __init__(self, bank_id, bank_name, number_of_employees, amount_of_revenue, amount_of_expenses, bank_customers):
        self.bank_id = bank_id
        self.bank_name = bank_name
        self.number_of_employees = number_of_employees
        self.amount_of_revenue = amount_of_revenue
        self.amount_of_expenses = amount_of_expenses
        self.bank_customers = bank_customers

    @abstractmethod
    def calculate_customer_money(self):
        pass

    def take_payment(self, customer: Customer, payment: int):
        for existing_customer in self.bank_customers:
            if customer.customer_id == existing_customer.customer_id:
                customer.amount_of_money = customer.amount_of_money - payment
                self.amount_of_revenue = self.amount_of_revenue + payment

    def increase_revenue(self, revenue_to_add: int):
        self.amount_of_revenue = self.amount_of_revenue + revenue_to_add

    def increase_expenses(self, expenses_to_increase: int):
        self.amount_of_expenses = self.amount_of_expenses + expenses_to_increase

