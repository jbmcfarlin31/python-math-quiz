# python-math-quiz
A simple Python program that tests your math skills in different number bases (e.g. base 10, octal, hex)

# Prerequisites
Python version 3+ or higher

This uses Python's PrettyTable to tabulate score, so you will need to make sure it is installed.
```bash
pip install PTable prettytable

# note if using Python 3 you might have to run it like so:
pip3 install PTable prettytable

# Optionally, you can use the requirements.txt file to install related packages as well
pip3 install -r requirements.txt
```
# on windows:
```powershell
# for installing behind proxy
python -m pip install prettytable PTable --proxy=myproxy:80

# for installing regularily - you should probably use this one first
python -m pip install prettytable PTable

# Optionally, installing via the requirements.txt
python -m pip install prettytable PTable -r requirements.txt
