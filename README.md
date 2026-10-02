## Pending transaction validator


This python program is designed to flag suspicious transactions in an Irish banking and fintech environment. My aim was to build a program that attempts to stop fraud in banking transactions without the need for constant human supervision. 



## What my Pending Transaction Validator does

My program looks at each transaction and checks that:

1. It is a dictionary.
2. It has exactly the expected keys (no missing or extra ones).
3. Each value has the right type and format.
4. It is not suspicious: transfers of **10,000 or more with an empty description** are flagged.

If every transaction passes, my program prints `Valid format.` and returns `True`. If any transaction fails, it prints a message for each problem found and returns `False`.

## Requirements

- Python 3.6 or newer
- No external libraries (it only uses the built-in `re` module)




## Transaction format

Each transaction is a dictionary with these keys:

| Key | Type | Rule |
|---|---|---|
| `Sender_Bank_Information` | dict | Must be a dictionary (e.g. name, BIC, IBAN) |
| `Recipient_Bank_Information` | dict | Must be a dictionary (e.g. name, BIC, IBAN) |
| `amount` | int or float | Must be greater than 0 |
| `currency` | str | Must be `'EUR'` |
| `transfer_date` | str | Must look like `YYYY-MM-DD` |
| `description` | str | Must be a string (can be empty) |

Example:

```python
{
    'Sender_Bank_Information': {
        'Name on account': 'John Doe',
        'BIC': 'BOFIIE2DXXX',
        'IBAN': 'IE12BOFI 123456 78912345'
    },
    'Recipient_Bank_Information': {
        'Name on account': 'Jane Smith',
        'BIC': 'CITIIE2DXXX',
        'IBAN': 'IE12CITI 123456 78912345'
    },
    'amount': 1000.00,
    'currency': 'EUR',
    'transfer_date': '2023-10-01',
    'description': 'Monthly salary transfer'
}
```

## Functions

### `validate_pending_transactions(...)`

Checks the type and format of each field in one transaction. Returns a list of the field names that failed (an empty list means all fields are fine).

### `find_fraudulent_transactions(data)`

Takes a **list** of transactions and runs all the checks above on each one. It reports every problem it finds instead of stopping at the first one.

- Returns `True` if all transactions are valid and not suspicious.
- Returns `False` if any transaction has a problem.

## Usage

Check every transaction:

```python
print(find_fraudulent_transactions(pending_transactions))
```

Check a single transaction (wrap it in square brackets so it is a list):

```python
print(find_fraudulent_transactions([pending_transactions[3]]))
```

## Known limitations

- The date check only verifies the `YYYY-MM-DD` shape, so a value like `2023-99-99` would still pass.
- BIC and IBAN values are not validated.
- Only `EUR` is accepted as a currency.
- The 10,000 threshold is set directly in the code.
