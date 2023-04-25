from scrappers import ArvixScrapper

"""PaperGPT mian function."""
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