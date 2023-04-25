"""PaperGPT scrapper (abstract base class)."""

from abc import ABC
from typing import List

class ScrapperBase(ABC):
    """Abstract base class for PaperGPT scrapper."""
    
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