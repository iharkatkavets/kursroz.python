#!/usr/bin/env python

from .user_input import *
from .load_utils import *
from .date_utils import *
from .list_utils import *
from .item_metadata import *
from .report_generator import *

def main():
    invoice_title = read_str("Enter invoice title: ")
    date_format = '%Y/%m/%d'
    issue_date_prompt = "Enter invoice date (YYYY/MM/DD): "
    invoice_issue_date = read_date(issue_date_prompt, date_format)
    money_receive_prompt = "Enter money receive date (YYYY/MM/DD): "
    money_receive_date = read_date(money_receive_prompt, date_format)
    invoice_value_prompt = "Enter invoce ($) value: "
    invoice_value = read_double(invoice_value_prompt)

    day_before_invoice_issue = day_before(invoice_issue_date)
    day_before_money_receive = day_before(money_receive_date)

    rates = load_tabel_a()

    item0 = select_item(rates, day_before_invoice_issue)
    invoice_issue_rate = None
    invoice_issue_table = None
    if item0 is not None: 
        invoice_issue_rate = load_exchange_rate(item0.xml_url)
        invoice_issue_table = item0.title
    if invoice_issue_rate is None:
        print(f'Can\'t load rate for {date_str(day_before_invoice_issue)}')
        prompt = f'Enter exchage rate for date {date_str(day_before_invoice_issue)}'
        invoice_issue_rate = read_double(prompt)
    if invoice_issue_table is None:
        print(f'Can\'t load tabel for {date_str(day_before_invoice_issue)}')
        prompt = f'Enter exchange tabel for date {date_str(day_before_invoice_issue)}'
        invoice_issue_rate = read_str(prompt)


    item1 = select_item(rates, day_before_money_receive)
    money_receive_rate = None
    money_receive_table = None
    if item1 is not None:
        money_receive_rate = load_exchange_rate(item1.xml_url)
        money_receive_table = item1.title
    if money_receive_rate is None:
        print(f'Can\'t load rate for {date_str(day_before_invoice_issue)}')
        prompt = f'Enter exchage rate for date {date_str(day_before_money_receive)}'
        money_receive_rate = read_double(prompt)
    if money_receive_table is None:
        print(f'Can\'t load tabel for {date_str(day_before_invoice_issue)}')
        prompt = f'Enter exchage tabel for date {date_str(day_before_money_receive)}'
        money_receive_table = read_str(prompt)


    assert invoice_issue_rate is not None
    assert money_receive_rate is not None

    report = ReportBuilder.report()\
    .with_invoice_title(invoice_title)\
    .with_invoice_value(invoice_value)\
    .with_invoice_issue_date(invoice_issue_date)\
    .with_money_receive_date(money_receive_date)\
    .with_exchange_rate_invoice_issue(invoice_issue_rate)\
    .with_exchange_table_invoice_issue(invoice_issue_table)\
    .with_exchange_rate_money_receive(money_receive_rate)\
    .with_exchange_table_money_receive(money_receive_table)\
    .generate()
    print(report)

if __name__ == '__main__':
    main()
