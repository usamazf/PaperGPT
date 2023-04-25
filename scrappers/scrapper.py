"""PaperGPT central scrapper module to handle scraping request."""

import json
from .base import ScrapperBase

# perform scraping using all the modules requested
def perform_scrape(_module: ScrapperBase, _parameters: dict):
        
        # perform the fetch request
        paper_list = _module.fetch_papers(_parameters)

        # process the output
        # currently test on a text file
        # would be replaced with a DB transaction in the
        # future updates.
        with open("outfile.txt", "w") as fout:
                json.dump(paper_list, fout)