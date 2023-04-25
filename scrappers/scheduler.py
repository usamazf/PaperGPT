"""PaperGPT scrape scheduler module."""

import schedule
from .scrapper import perform_scrape

def schedule_scrape(config: dict) -> None:
    print(config)
    
    # Module 1: arvix db
    if (config['arvix']['UseModule']):
        from scrappers.arvix import ArvixScrapper
        _module = ArvixScrapper()
        schedule.every(config['arvix']["Timeout"]).minutes.do(perform_scrape, _module, config['arvix']['UserParams'])

    # Module 2: google-scholar db