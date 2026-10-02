import re

pending_transactions = [
    {
        'Sender_Bank_Information': {
            'Name on account' : 'John Doe',
            'BIC': 'BOFIIE2DXXX',
            'IBAN': 'IE12BOFI 123456 78912345'
        },
        'Recipient_Bank_Information': {
            'Name on account' : 'Jane Smith',
            'BIC': 'CITIIE2DXXX',
            'IBAN': 'IE12CITI 123456 78912345'
        },
        'amount': 1000.00,
        'currency': 'EUR',
        'transfer_date': '2023-10-01',
        'description': 'Monthly salary transfer',
        

    },
    {
        'Sender_Bank_Information': {
            'BIC': 'BOFIIE2DXXX',
            'IBAN': 'IE12BOFI 123456 78912345'
        },
        'Recipient_Bank_Information': {
            'BIC': 'CITIIE2DXXX',
            'IBAN': 'IE12CITI 123456 78912345'
        },
        'amount': 2500.00,
        'currency': 'EUR',
        'transfer_date': '2023-10-02',
        'description': 'Gift transfer',
       
    },
    
    {
        'Sender_Bank_Information': {
            'Name on account' : 'Alice Johnson',
            'BIC': 'BOFIIE2DXXX',
            'IBAN': 'IE12BOFI 123456 78912345'
        },
        'Recipient_Bank_Information': {
            'Name on account' : 'Bob Brown',
            'BIC': 'CITIIE2DXXX',
            'IBAN': 'IE12CITI 123456 78912345'
        },
        'amount': 500.00,
        'currency': 'EUR',
        'transfer_date': '2023-10-03',
        'description': '',
        
    },
    
    {
        'Sender_Bank_Information': {
            'Name on account' : 'Charlie Davis',
            'BIC': 'BOFIIE2DXXX',
            'IBAN': 'IE12BOFI 123456 78912345'
        },
        'Recipient_Bank_Information': {
            'Name on account' : 'Diana Evans',
            'BIC': 'CITIIE2DXXX',
            'IBAN': 'IE12CITI 123456 78912345'
        },
        'amount': 12500.00,
        'currency': 'EUR',
        'transfer_date': '2023-10-04',
        'description': '',
       
    }
]


def validate_pending_transactions(
    Sender_Bank_Information, Recipient_Bank_Information, amount, currency, transfer_date, description
):
    constraints = {
        'Sender_Bank_Information': isinstance(Sender_Bank_Information, dict),
        'Recipient_Bank_Information': isinstance(Recipient_Bank_Information, dict),
        'amount': isinstance(amount, (int, float)) and amount > 0,
        'currency': isinstance(currency, str) and currency == 'EUR',
        # re.fullmatch checks if the transfer_date matches the format YYYY-MM-DD. \d{4} maps the four digits of the the year to the transfer_data constraint and the hyphen(-) maps to the hyphen in the transfer_data
        'transfer_date': isinstance(transfer_date, str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}', transfer_date),
        'description': isinstance(description, str)
    }
    return [key for key, value in constraints.items() if not value]



def find_fraudulent_transactions(data):
    
    # is_invalid is a boolean variable that is used to track whether any invalid transactions are found. If so, is_invalid will change to True, and the function will return False at the end as the function declares the information is invalid.
    is_invalid = False
    key_set =['Sender_Bank_Information', 'Recipient_Bank_Information', 'amount', 'currency', 'transfer_date', 'description']
    
    
    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue


        if set(dictionary.keys()) != set(key_set):
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        invalid_records = validate_pending_transactions(**dictionary)
        for key in invalid_records:
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            is_invalid = True

        if invalid_records:
            continue
        
        if dictionary['amount'] > 10000.00 and dictionary['description'] == '':
                print(f'Suspicious transaction detected, transaction number {index}: Amount exceeds threshold without a description. Please be advised this transaction must be reviewed by a member of staff before approval.')
                is_invalid = True
        
    if is_invalid:
        return False
    print('Valid transactions: All transactions are valid and meet the required criteria.')
    return True

print(find_fraudulent_transactions(pending_transactions))





