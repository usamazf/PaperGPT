"""PaperGPT scrapper (abstract base class)."""

from abc import ABC
from typing import List


class Scrapper(ABC):
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