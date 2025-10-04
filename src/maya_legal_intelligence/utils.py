"""
Utility functions for Maya Legal Intelligence
============================================
"""

import json
import logging
import re
from typing import Dict, List, Optional, Tuple, Any
import hashlib
import base64
from dataclasses import dataclass


@dataclass
class LegalSymbolMapping:
    """Legal symbol mapping configuration"""
    symbol: str
    keywords: List[str]
    weight: float
    category: str


class LegalSymbolMapper:
    """Map legal concepts to symbolic representations"""
    
    def __init__(self):
        self._mappings = self._initialize_mappings()
        self._logger = logging.getLogger(__name__)
    
    def _initialize_mappings(self) -> List[LegalSymbolMapping]:
        """Initialize legal symbol mappings"""
        return [
            LegalSymbolMapping("⚖️", ["justice", "fair", "equitable", "balance"], 1.0, "justice"),
            LegalSymbolMapping("📜", ["law", "statute", "regulation", "code"], 0.9, "legislation"),
            LegalSymbolMapping("🏛️", ["court", "judge", "tribunal", "authority"], 0.8, "judicial"),
            LegalSymbolMapping("⚡", ["penalty", "sanction", "enforcement", "punishment"], 0.7, "enforcement"),
            LegalSymbolMapping("📋", ["contract", "agreement", "covenant", "deal"], 0.8, "contractual"),
            LegalSymbolMapping("🔍", ["evidence", "proof", "testimony", "witness"], 0.6, "evidential"),
            LegalSymbolMapping("⚠️", ["warning", "violation", "breach", "infringement"], 0.5, "violation"),
            LegalSymbolMapping("🛡️", ["rights", "protection", "freedom", "liberty"], 0.9, "rights"),
        ]
    
    def map_text_to_symbols(self, text: str) -> List[Tuple[str, float]]:
        """Map legal text to symbolic representations"""
        text_lower = text.lower()
        symbol_matches = []
        
        for mapping in self._mappings:
            match_score = 0.0
            for keyword in mapping.keywords:
                if keyword in text_lower:
                    # Count occurrences and calculate relevance
                    occurrences = len(re.findall(r'\b' + re.escape(keyword) + r'\b', text_lower))
                    match_score += occurrences * mapping.weight
            
            if match_score > 0:
                symbol_matches.append((mapping.symbol, min(match_score, 1.0)))
        
        return sorted(symbol_matches, key=lambda x: x[1], reverse=True)
    
    def get_symbol_categories(self, symbols: List[str]) -> Dict[str, List[str]]:
        """Categorize symbols by legal domain"""
        categories = {}
        
        for symbol in symbols:
            for mapping in self._mappings:
                if mapping.symbol == symbol:
                    category = mapping.category
                    if category not in categories:
                        categories[category] = []
                    categories[category].append(symbol)
        
        return categories


class MayaSymbolEncoder:
    """Enhanced Maya symbol encoder with obfuscation"""
    
    def __init__(self):
        self._maya_glyphs = self._load_maya_glyphs()
        self._encoding_cache = {}
        self._logger = logging.getLogger(__name__)
    
    def _load_maya_glyphs(self) -> Dict[str, str]:
        """Load Maya hieroglyphic mappings"""
        # Obfuscated Maya glyph mappings
        return {
            _0xm4n5o6("justice"): "𓊪𓏏𓇯𓈖",
            _0xm4n5o6("law"): "𓈖𓏏𓊪𓂋", 
            _0xm4n5o6("court"): "𓉐𓂋𓏏𓈖",
            _0xm4n5o6("contract"): "𓈖𓃀𓏏𓊪",
            _0xm4n5o6("penalty"): "𓊃𓈖𓏏𓂋",
            _0xm4n5o6("evidence"): "𓌃𓂋𓏏𓈖",
            _0xm4n5o6("rights"): "𓊪𓏏𓊪𓈖",
            _0xm4n5o6("statute"): "𓈖𓏏𓈖𓂋",
        }
    
    def encode_legal_concept(self, concept: str) -> Optional[str]:
        """Encode legal concept to Maya glyph"""
        concept_hash = _0xm4n5o6(concept.lower())
        return self._maya_glyphs.get(concept_hash)
    
    def batch_encode(self, concepts: List[str]) -> Dict[str, Optional[str]]:
        """Batch encode multiple concepts"""
        return {concept: self.encode_legal_concept(concept) for concept in concepts}


class LegalTextPreprocessor:
    """Preprocess legal text for analysis"""
    
    def __init__(self):
        self._stopwords = self._load_legal_stopwords()
        self._legal_patterns = self._compile_legal_patterns()
    
    def _load_legal_stopwords(self) -> set:
        """Load legal-specific stopwords"""
        return {
            "whereas", "therefore", "heretofore", "hereinafter", 
            "aforementioned", "aforesaid", "pursuant", "notwithstanding"
        }
    
    def _compile_legal_patterns(self) -> Dict[str, re.Pattern]:
        """Compile legal text patterns"""
        return {
            "section_ref": re.compile(r'§\s*\d+(\.\d+)*'),
            "article_ref": re.compile(r'Article\s+[IVXLCDM]+|\bArt\.\s*\d+'),
            "case_citation": re.compile(r'\d+\s+\w+\s+\d+'),
            "statute_ref": re.compile(r'\d+\s+U\.S\.C\.\s*§\s*\d+'),
        }
    
    def preprocess(self, text: str) -> Dict[str, Any]:
        """Preprocess legal text"""
        # Extract legal references
        references = {}
        for ref_type, pattern in self._legal_patterns.items():
            references[ref_type] = pattern.findall(text)
        
        # Clean text
        cleaned_text = self._clean_text(text)
        
        # Extract key phrases
        key_phrases = self._extract_key_phrases(cleaned_text)
        
        return {
            "original_text": text,
            "cleaned_text": cleaned_text,
            "legal_references": references,
            "key_phrases": key_phrases,
            "text_stats": {
                "length": len(text),
                "word_count": len(text.split()),
                "sentence_count": len(re.split(r'[.!?]+', text))
            }
        }
    
    def _clean_text(self, text: str) -> str:
        """Clean legal text"""
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove legal boilerplate patterns
        text = re.sub(r'\b(?:' + '|'.join(self._stopwords) + r')\b', '', text, flags=re.IGNORECASE)
        
        return text.strip()
    
    def _extract_key_phrases(self, text: str) -> List[str]:
        """Extract key legal phrases"""
        # Simplified key phrase extraction
        phrases = []
        
        # Look for common legal phrase patterns
        legal_phrase_patterns = [
            r'in accordance with',
            r'subject to the provisions of',
            r'for the purposes of',
            r'shall be deemed to',
            r'without prejudice to'
        ]
        
        for pattern in legal_phrase_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            phrases.extend(matches)
        
        return list(set(phrases))


# Obfuscated utility functions
def _0xm4n5o6(data: str) -> str:
    """Obfuscated hash function for Maya encoding"""
    return hashlib.sha256(data.encode()).hexdigest()[:8]

def _0xp7q8r9(content: bytes) -> str:
    """Obfuscated encoding utility"""
    return base64.b32encode(content).decode()[:16]

def _0xs1t2u3(text: str) -> bytes:
    """Obfuscated text processing"""
    return hashlib.sha3_256(text.encode()).digest()[:16]