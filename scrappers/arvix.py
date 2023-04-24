"""PaperGPT arvix class."""
from scrapper import Scrapper
from typing import List
import urllib, urllib.request
import feedparser

class ArvixScrapper(Scrapper):
    """Abstract base class for PaperGPT scrapper."""
    
    def fetch_papers(self, title_keys: List[str], abstract_keys: List[str], other_keys: List[str]) -> List[str]:
        """Return list of papers with provided keywords.
        Parameters
        ----------
        title_keys : List[str]
                The list of keywords to search for in the title of the paper.
        abstract_keys : List[str]
                The list of keywords to search for in the abstract of the paper.
        other_keys : List[str]
                The list of keywords to search for in other parts of the paper.
                
        Returns
        -------
        List[str]
            The list of papers with provided keywords.
        """
        # build a query list
        arvix_query = ""
        for keyword in title_keys:
            keyword.replace(" ", "+")
            arvix_query += f"ti:{keyword}+OR+"
        for keyword in abstract_keys:
            keyword.replace(" ", "+")
            arvix_query += f"abs:{keyword}+OR+"
        for keyword in other_keys:
            keyword.replace(" ", "+")
            arvix_query += f"all:{keyword}+OR+"
        # build the arvix query URL
        query_url = f'http://export.arxiv.org/api/query?search_query={arvix_query[:-4]}&start=0&max_results=1000'
        # make a post request to get papers
        response = urllib.request.urlopen(query_url).read()
        # parse the response received and create a paper list
        return self.parse_response(response)
        # return paper list
        return papers
    
    def parse_response(self, response):
        feed = feedparser.parse(response)
        #with open('readme.xml', 'w') as f:
        #    f.write(response.encode('utf-8'))
        
        # print out feed information
        print(f'Feed title: {feed.feed.title}')
        print(f'Feed last updated: {feed.feed.updated}') 
        
        # print opensearch metadata
        print(f'TotalResults for this query: {feed.feed.opensearch_totalresults}')
        print(f'ItemsPerPage for this query: {feed.feed.opensearch_itemsperpage}')
        print(f'StartIndex for this query: {feed.feed.opensearch_startindex}')
        input()
        
        # Run through each entry, and print out information
        for entry in feed.entries:
            print('\n\ne-print metadata')
            print('arxiv-id: %s' % entry.id.split('/abs/')[-1])
            print('Published: %s' % entry.published)
            print('Title:  %s' % entry.title)
            
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
            
            print('Last Author:  %s' % author_string)
            
            # feedparser v5.0.1 correctly handles multiple authors, print them all
            try:
                print('Authors:  %s' % ', '.join(author.name for author in entry.authors))
            except AttributeError:
                pass
        
            # get the links to the abs page and pdf for this e-print
            for link in entry.links:
                if link.rel == 'alternate':
                    print('abs page link: %s' % link.href)
                elif link.title == 'pdf':
                    print('pdf link: %s' % link.href)
            
            # The journal reference, comments and primary_category sections live under 
            # the arxiv namespace
            try:
                journal_ref = entry.arxiv_journal_ref
            except AttributeError:
                journal_ref = 'No journal ref found'
            print('Journal reference: %s' % journal_ref)
            
            try:
                comment = entry.arxiv_comment
            except AttributeError:
                comment = 'No comment found'
            print('Comments: %s' % comment)
            
            # Since the <arxiv:primary_category> element has no data, only
            # attributes, feedparser does not store anything inside
            # entry.arxiv_primary_category
            # This is a dirty hack to get the primary_category, just take the
            # first element in entry.tags.  If anyone knows a better way to do
            # this, please email the list!
            print('Primary Category: %s' % entry.tags[0]['term'])
            
            # Lets get all the categories
            all_categories = [t['term'] for t in entry.tags]
            print('All Categories: %s' % (', ').join(all_categories))
            
            # The abstract is in the <summary> element
            print('Abstract: %s' %  entry.summary)


# test code for current module
if __name__=="__main__":
    test_keywords = [
        "FL",
        "FedML",
        "FML",
        "Federated+Learning",
        "Federated+Machine+Learning",
    ]
    # create a sample object of arvix scrapper
    arvix_scrapper = ArvixScrapper()
    papers = arvix_scrapper.fetch_papers(
                            title_keys = test_keywords,
                            abstract_keys = test_keywords,
                            other_keys = []
                    )
    
    #print(papers.read().decode('utf-8'))