"""PaperGPT main function."""

import time
import schedule
from typing import NoReturn
from multiprocessing import Process
from scrappers import schedule_scrape
from configs.configurations import config


if __name__ == '__main__':
    # schedule all the modules according
    # to user provided timeouts
    scheduled_processes: list[Process] = schedule_scrape(config['modules'])

    # start the scheduled processes
    for proc in scheduled_processes:
        proc.start()

    # wait for the scheduled processes
    for proc in scheduled_processes:
        proc.join()

    # p = Process(target=timer_process, args=(config,))
    # p.start()
    # p.join()