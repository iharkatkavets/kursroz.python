from .date_utils import *

class ReportBuilder:
    def __init__(self):
        pass

    def with_invoice_title(self, invoice_title):
        self.invoice_title = invoice_title
        return self

    def with_invoice_value(self, invoice_value):
        self.invoice_value = invoice_value
        return self

    def with_invoice_issue_date(self, invoice_issue_date):
        self.invoice_issue_date = invoice_issue_date
        return self

    def with_money_receive_date(self, money_receive_date):
        self.money_receive_date = money_receive_date
        return self

    def with_exchange_rate_invoice_issue(self, rate):
        self.exchange_rate_invoice_issue = rate
        return self

    def with_exchange_table_invoice_issue(self, str):
        self.exchange_table_invoice_issue = str
        return self

    def with_exchange_rate_money_receive(self, rate):
        self.exchange_rate_money_receive = rate
        return self

    def with_exchange_table_money_receive(self, str):
        self.exchange_table_money_receive = str
        return self

    @classmethod
    def report(cls):
        return cls()

    def generate(self):
        return ReportGenerator(self).generate()


class ReportGenerator:
    def __init__(self, builder):
        self.invoice_title = builder.invoice_title
        self.invoice_value = builder.invoice_value
        self.invoice_issue_date = builder.invoice_issue_date
        self.money_receive_date = builder.money_receive_date
        self.exchange_rate_invoice_issue = builder.exchange_rate_invoice_issue
        self.exchange_table_invoice_issue = builder.exchange_table_invoice_issue
        self.exchange_rate_money_receive = builder.exchange_rate_money_receive
        self.exchange_table_money_receive = builder.exchange_table_money_receive

    def generate(self):
        self._begin()
        self._add_title()
        self._add_common_part()
        self._add_invoice_issue_exchanged_calculations()
        self._add_money_received_exchanged_calculations()
        self._add_exchange_differences()
        return self.result

    def _begin(self):
        self.result = ""

    def _add_title(self):
        self.result += f'Do Faktury {self.invoice_title}'

    def _add_common_part(self):
        self.result += f'\n\nFakturę sprzedażową na kwotę {self.invoice_value} USD '\
                f'wystawiłem {date_report_str(self.invoice_issue_date)}, a zapłatę otrzymałem '\
                f'{date_report_str(self.money_receive_date)}.'

    def _float(self, str):
        str_corrected = str.replace(',','.')
        floated = float(str_corrected)
        return floated

    def _round_to_4(self, float_value):
        return round(float_value, 4)

    def _round_to_2(self, float_value):
        return round(float_value, 2)

    def _invoice_issued_amount(self):
        return self._float(self.exchange_rate_invoice_issue)*self._float(self.invoice_value)

    def _money_receive_amount(self):
        return self._float(self.exchange_rate_money_receive)*self._float(self.invoice_value)

    def _exchange_differences(self):
        return self._invoice_issued_amount() - self._money_receive_amount()

    def _exchange_differences_str(self):
        if self._exchange_differences() > 0: 
            return f'ujemne różnice kursowe'
        else: 
            return f'dodatnia różnica kursowa'

    def _add_invoice_issue_exchanged_calculations(self):
        a = f'{self._float(self.exchange_rate_invoice_issue)}'
        b = f'{self._round_to_2(self._float(self.invoice_value))}'
        r = f'{self._round_to_4(self._invoice_issued_amount())}'
        formula = f'{a} x {b} = {r}'
        self.result += f'\n\nŚredni kurs NBP z ostatniego dnia roboczego poprzedzającego dzień uzyskania '\
                f'przychodu wyniósł {self.exchange_rate_invoice_issue}. ({self.exchange_table_invoice_issue})'\
                f'\n{formula} zł'

    def _add_money_received_exchanged_calculations(self):
        a = f'{self._float(self.exchange_rate_money_receive)}'
        b = f'{self._round_to_2(self._float(self.invoice_value))}'
        r = f'{self._round_to_4(self._money_receive_amount())}'
        formula = f'{a} x {b} = {r}'
        self.result += f'\n\nŚredni kurs NBP z ostatniego dnia roboczego poprzedzającego dzień otrzymania '\
                f'zapłatę wyniósł {self.exchange_rate_money_receive}. ({self.exchange_table_money_receive})'\
                f'\n{formula} zł'

    def _add_exchange_differences(self):
        a = f'{self._round_to_4(self._invoice_issued_amount())}'
        b = f'{self._round_to_4(self._money_receive_amount())}'
        r = f'{self._round_to_4(self._exchange_differences())}'
        formula = f'{a} - {b} = {r}'
        self.result += f'\n\n{formula} zl ({self._exchange_differences_str()})'


