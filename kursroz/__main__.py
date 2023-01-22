#!/usr/bin/env python

from user_input import *
from ex_rates_provider import *


def main():
    user_input = UserInput()
    date_format = '%Y/%m/%d'
    issue_date_prompt = "Enter invoice date YYYY/MM/DD: "
    invoice_issue_date = user_input.readDate(issue_date_prompt, date_format)
    money_receive_prompt = "Enter money receive date (YYYY/MM/DD): "
    money_receive_date = user_input.readDate(money_receive_prompt, date_format)
    invoce_value_prompt = "Enter invoce $ value: "
    invoice_value = user_input.readDouble(invoce_value_prompt)

    rates = ExRatesProvider().load()

    print(invoice_issue_date)
    print(money_receive_date)
    print(invoice_value)
    print(rates)

if __name__ == '__main__':
    main()
