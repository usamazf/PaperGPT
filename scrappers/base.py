"""PaperGPT scrapper (abstract base class)."""

from abc import ABC, abstractmethod
from typing import List

class ScrapperBase(ABC):
    """Abstract base class for PaperGPT scrapper."""
    
    @abstractmethod
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
        raise NotImplementedError
    
    @abstractmethod
    def __name__(self) -> str:
        """Return name of the current module."""
        raise NotImplementedError    
    
    @abstractmethod
    def __str__(self) -> str:
        """Return name of the current module."""
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        """Return name of the current module."""
        raise NotImplementedError