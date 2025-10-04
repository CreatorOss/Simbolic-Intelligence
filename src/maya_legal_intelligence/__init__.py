"""
Maya Legal Intelligence - Symbolic Intelligence for Legal Analysis
================================================================

A revolutionary legal technology platform that combines Maya hieroglyphic wisdom
with modern symbolic intelligence for comprehensive legal document analysis.

Author: BENNY HARIANTO
Email: creatoropensource@gmail.com
License: MIT
"""

__version__ = "0.1.0"
__author__ = "BENNY HARIANTO"
__email__ = "creatoropensource@gmail.com"
__license__ = "MIT"

# Try to import full version, fallback to lite version
try:
    from .core import MayaLegalAnalyzer, SymbolicLegalClassifier
    from .analyzer import LegalDocumentProcessor
    from .utils import MayaSymbolEncoder, LegalSymbolMapper
    
    __all__ = [
        "MayaLegalAnalyzer",
        "SymbolicLegalClassifier", 
        "LegalDocumentProcessor",
        "MayaSymbolEncoder",
        "LegalSymbolMapper",
    ]
except ImportError:
    # Fallback to lite version for testing
    from .core_lite import MayaLegalAnalyzerLite as MayaLegalAnalyzer
    from .core_lite import SymbolicLegalClassifierLite as SymbolicLegalClassifier
    from .core_lite import MayaSymbolEncoder
    
    __all__ = [
        "MayaLegalAnalyzer",
        "SymbolicLegalClassifier",
        "MayaSymbolEncoder",
    ]