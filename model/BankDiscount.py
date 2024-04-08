from overrides import overrides
from model.Bank import Bank
from model.CompanyCustomer import CompanyCustomer


class BankDiscount(Bank):

    def __init__(self, bank_id, bank_name, number_of_employees, amount_of_revenue, amount_of_expenses, bank_customers, bank_company_customers):
        super().__init__(bank_id, bank_name, number_of_employees, amount_of_revenue, amount_of_expenses, bank_customers)
        self.bank_company_customers = bank_company_customers

    @overrides
    def calculate_customer_money(self):
        customer_total_amount_of_money = 0
        for customer in self.bank_customers:
            customer_total_amount_of_money = customer_total_amount_of_money + customer.amount_of_money

        company_customer_total_amount_of_money = 0
        for company_customer in self.bank_company_customers:
            company_customer_total_amount_of_money = company_customer_total_amount_of_money + company_customer.amount_of_money

        return customer_total_amount_of_money + company_customer_total_amount_of_money

    def take_company_customer_payment(self, company_customer: CompanyCustomer, payment: int):
        for existing_company_customer in self.bank_company_customers:
            if company_customer.company_customer_id == existing_company_customer.company_customer_id:
                company_customer.amount_of_money = company_customer.amount_of_money - payment
                self.amount_of_revenue = self.amount_of_revenue + payment
