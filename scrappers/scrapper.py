"""PaperGPT central scrapper module to handle scraping request."""

import json
from .base import ScrapperBase
from database import DatabaseHandler
import datetime

# perform scraping using all the modules requested
def perform_scrape(_module: ScrapperBase, _parameters: dict):
        # print a debug message
        print(f"\n\nScraper called for module {_module.name()}\n\n")
        
        # perform the fetch request
        paper_list = _module.fetch_papers(_parameters)

        # process the output
        # currently test on a text file
        # would be replaced with a DB transaction in the
        # future updates.
        with open("outfile.txt", "w") as fout:
                json.dump(paper_list, fout)
        
        # prepare date to be inserted into the database
        tuple_list = []
        for item in paper_list:
                # (serial, title, publish_date, abstract, pdflink, author, entry_date, source)
                tuple_list.append(tuple([None, item['title'], item['published'], item['abstract'], item['pdflink'], item['author'], datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'), _module.name()]))
        
        # insert the prepared data into the database
        #db = DatabaseHandler()
        DatabaseHandler.insert_raw(tuple_list)
