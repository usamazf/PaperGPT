"""PaperGPT ArvixScrapper class."""

from typing import List
import urllib, urllib.request
import feedparser
from .base import ScrapperBase

class ArvixScrapper(ScrapperBase):
    """ArvixScrapper class for PaperGPT to scrape arvix database."""
    
    def fetch_papers(self, args: dict) -> List[str]:
        """Return list of papers with provided keywords.
        Parameters
        ----------
        args : dict
            A dictionary of user arguments that are needed by current module
                
        Returns
        -------
        List[str]
            The list of papers with provided keywords.
        """
        # build a query list
        arvix_query = ""
        for keyword in args['title_keys']:
            keyword.replace(" ", "+")
            arvix_query += f"ti:{keyword}+OR+"
        for keyword in args['abstract_keys']:
            keyword.replace(" ", "+")
            arvix_query += f"abs:{keyword}+OR+"
        for keyword in args['other_keys']:
            keyword.replace(" ", "+")
            arvix_query += f"all:{keyword}+OR+"
        # build the arvix query URL
        query_url = f'http://export.arxiv.org/api/query?search_query={arvix_query[:-4]}&start=0&max_results=1'
        # make a post request to get papers
        response = urllib.request.urlopen(query_url).read()
        # parse the response received and create a paper list
        return self.parse_response(response)
        # return paper list
        return papers
    
    def __name__(self) -> str:
        """Return name of the current module."""
        return 'ARVIX'
    
    def __str__(self) -> str:
        """Return name of the current module."""
        return 'ARVIX'
    
    def name(self) -> str:
        """Return name of the current module."""
        return self.__name__()

    def parse_response(self, response) -> list[dict]:
        feed = feedparser.parse(response)
        
        # do we keep meta information?
        # not sure yet, need to figure out if
        # this might be useful or not

        # print out feed information
        # print(f'Feed title: {feed.feed.title}')
        # print(f'Feed last updated: {feed.feed.updated}') 
        
        # # print opensearch metadata
        # print(f'TotalResults for this query: {feed.feed.opensearch_totalresults}')
        # print(f'ItemsPerPage for this query: {feed.feed.opensearch_itemsperpage}')
        # print(f'StartIndex for this query: {feed.feed.opensearch_startindex}')
        
        # create an empty paper list
        paper_list = []

        # Run through each entry, and print out information
        for entry in feed.entries:
            current_paper = dict()
            current_paper["arxiv-id"] = entry.id.split('/abs/')[-1]
            current_paper["published"] = entry.published
            current_paper["title"] = entry.title
            # feedparser v4.1 only grabs the first author
            author_string = entry.author
            # grab the affiliation in <arxiv:affiliation> if present
            # - this will only grab the first affiliation encountered
            #   (the first affiliation for the first author)
            # Please email the list with a way to get all of this information!
            try:
                author_string += ' (%s)' % entry.arxiv_affiliation
            except AttributeError:
                pass
            current_paper["author"] = author_string
            # feedparser v5.0.1 correctly handles multiple authors, print them all
            # try:
            #     print('Authors:  %s' % ', '.join(author.name for author in entry.authors))
            # except AttributeError:
            #     pass
        
            # get the links to the abs page and pdf for this e-print
            for link in entry.links:
                if link.rel == 'alternate':
                    print('abs page link: %s' % link.href)
                elif link.title == 'pdf':
                    current_paper['pdflink'] =  link.href
            
            # The journal reference, comments and primary_category sections live under 
            # the arxiv namespace
            # try:
            #     journal_ref = entry.arxiv_journal_ref
            # except AttributeError:
            #     journal_ref = 'No journal ref found'
            # print('Journal reference: %s' % journal_ref)
            
            # try:
            #     comment = entry.arxiv_comment
            # except AttributeError:
            #     comment = 'No comment found'
            # print('Comments: %s' % comment)
            
            # Since the <arxiv:primary_category> element has no data, only
            # attributes, feedparser does not store anything inside
            # entry.arxiv_primary_category
            # This is a dirty hack to get the primary_category, just take the
            # first element in entry.tags.  If anyone knows a better way to do
            # this, please email the list!
            # print('Primary Category: %s' % entry.tags[0]['term'])
            
            # # Lets get all the categories
            # all_categories = [t['term'] for t in entry.tags]
            # print('All Categories: %s' % (', ').join(all_categories))
            
            # The abstract is in the <summary> element
            # print('Abstract: %s' %  entry.summary)
            current_paper["abstract"] = entry.summary
            
            # append this paper as new entry
            paper_list.append(current_paper)
        
        return paper_list
            