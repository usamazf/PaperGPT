"""PaperGPT central scrapper module to handle scraping request."""

import json
from .base import ScrapperBase
from database import DatabaseHandler

# perform scraping using all the modules requested
def perform_scrape(_module: ScrapperBase, _parameters: dict):
        # print a debug message
        print(f"Scraper called for module {_module}")
        
        # perform the fetch request
        paper_list = _module.fetch_papers(_parameters)

        # process the output
        # currently test on a text file
        # would be replaced with a DB transaction in the
        # future updates.
        with open("outfile.txt", "w") as fout:
                json.dump(paper_list, fout)
        
        # insert into database
        tuple_list = []
        for item in paper_list:
                tuple_list.append(tuple([None, item['title'], item['published'], item['abstract'], 'no_link', item['author'], 'no_date', 'ARVIX']))
                # (serial, title, publish_date, abstract, pdflink, author, entry_date, source)
        db = DatabaseHandler()
        db.insert_raw(tuple_list)
