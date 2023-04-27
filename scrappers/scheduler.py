"""PaperGPT scrape scheduler module."""

import time
import schedule
from typing import NoReturn
from multiprocessing import Process
from .scrapper import perform_scrape

def run_schedule() -> NoReturn: 
    # keep running this module until
    # all scheduled jobs have finished
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)

def run_process(_module, module_configs) -> None: 
    schedule.every(module_configs["timeout"]).minutes.do(perform_scrape, _module, module_configs['userParams'])
    
    # print out log message for debugging purposes
    print(f"Info: Scheduled module {_module.name()} to run once every {module_configs['timeout']} hours.")
    
    # keep running this module until
    # all scheduled jobs have finished
    run_schedule()


def schedule_scrape(all_module_configs: dict) -> list[Process]:
    """PaperGPT scheduler to perform periodic scrapes of paper databases."""
    
    # make a list of processes to keep
    # track of all scheduled modules
    scheduled_processes = []

    # Module 1: arxiv db
    if (all_module_configs['arxiv']['useModule']):
        from scrappers.arxiv import ArxivScrapper
        _module = ArxivScrapper()
        scheduled_processes.append(Process(target=run_process, args=(_module, all_module_configs['arxiv'])))
    
    # Module 2: google-scholar db


    # return the list of scheduled process
    # and let main function deal with starting
    # these processes and waiting for the joins
    return scheduled_processes