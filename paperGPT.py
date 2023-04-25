"""PaperGPT main function."""

import time
import schedule
from multiprocessing import Process
from scrappers import schedule_scrape
from configs.configurations import config


if __name__ == '__main__':
    schedule_scrape(config)
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)
    
    #p = Process(target=timer_process, args=(config,))
    #p.start()
    #p.join()