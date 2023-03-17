import pandas as pd
from api.models import Bank, Branches


def fillBank():
    bank_data = pd.read_csv('../banks.csv')
    banks = [
        Bank(
            name = bank_data.ix[row]['name'],
            id = bank_data.ix[row]['id'],
        )
        for row in bank_data['id']
    ]

    Bank.objects.bulk_create(banks)
