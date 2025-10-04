"""
Symbolic Legal Intelligence - Universal Legal Document Analysis
==============================================================

Revolutionary legal document analysis using proven symbolic intelligence
framework (⟐, ⧈, ◈, ⟡) for universal understanding of legal content.

Author: BENNY HARIANTO
Email: creatoropensource@gmail.com
License: MIT
"""

__version__ = "1.0.0"
__author__ = "BENNY HARIANTO"
__email__ = "creatoropensource@gmail.com"
__license__ = "MIT"

# Import core components
from .core import SymbolicLegalIntelligence, LEGAL_SYMBOLS, LegalElement
from .analyzer import LegalDocumentProcessor

__all__ = [
    "SymbolicLegalIntelligence",
    "LegalDocumentProcessor", 
    "LEGAL_SYMBOLS",
    "LegalElement",
]