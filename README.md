# Python Exercises

Small command-line programs I wrote while learning Python. Each one runs on its own with only the standard library.

| Program | What it does |
|---------|--------------|
| [`atm.py`](atm.py) | ATM simulation: check balance, deposit and withdraw, with input validation |
| [`password_validator.py`](password_validator.py) | Checks a password against security rules and tells you exactly which ones it fails |

## Running

```bash
python3 atm.py
python3 password_validator.py
```

## Example

```
Enter your password: hello
Password is invalid. It needs:
  - at least 8 characters
  - an uppercase letter
  - a number
  - a special character (!@#$%^&*()-_=+[]{};:,.?/)
```

For a bigger project, see [personal-finance-tracker](https://github.com/DaniKabbani/personal-finance-tracker).
