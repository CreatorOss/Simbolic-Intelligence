"""
Test suite for Maya Legal Intelligence core functionality
=======================================================
"""

import pytest
import tempfile
import os
from unittest.mock import Mock, patch

from maya_legal_intelligence.core import (
    MayaLegalAnalyzer, 
    SymbolicLegalClassifier,
    MayaSymbolEncoder,
    LegalSymbol
)


class TestMayaSymbolEncoder:
    """Test Maya symbol encoding functionality"""
    
    def setup_method(self):
        self.encoder = MayaSymbolEncoder()
    
    def test_encode_basic_legal_text(self):
        """Test basic legal text encoding"""
        text = "The court shall ensure justice is served"
        result = self.encoder.encode(text)
        
        assert result.original_text == text
        assert len(result.encoded_symbols) > 0
        assert result.confidence_score >= 0.0
        assert result.legal_category in ["criminal_law", "commercial_law", "constitutional_law", "general_law"]
    
    def test_encode_empty_text(self):
        """Test encoding empty text"""
        result = self.encoder.encode("")
        
        assert result.original_text == ""
        assert len(result.encoded_symbols) == 0
        assert result.confidence_score == 0.0
    
    def test_legal_category_classification(self):
        """Test legal category classification"""
        criminal_text = "The defendant committed a crime and faces prosecution"
        commercial_text = "This contract establishes commercial agreement terms"
        constitutional_text = "This amendment protects fundamental constitutional rights"
        
        criminal_result = self.encoder.encode(criminal_text)
        commercial_result = self.encoder.encode(commercial_text)
        constitutional_result = self.encoder.encode(constitutional_text)
        
        assert criminal_result.legal_category == "criminal_law"
        assert commercial_result.legal_category == "commercial_law"
        assert constitutional_result.legal_category == "constitutional_law"


class TestSymbolicLegalClassifier:
    """Test symbolic legal classification"""
    
    def setup_method(self):
        # Mock the transformer model to avoid downloading
        with patch('maya_legal_intelligence.core.AutoTokenizer.from_pretrained') as mock_tokenizer, \
             patch('maya_legal_intelligence.core.AutoModel.from_pretrained') as mock_model:
            
            mock_tokenizer.return_value = Mock()
            mock_model.return_value = Mock()
            
            self.classifier = SymbolicLegalClassifier()
    
    def test_extract_legal_symbols(self):
        """Test legal symbol extraction"""
        text = "The court ensures justice through fair enforcement of penalties"
        symbols = self.classifier._extract_legal_symbols(text)
        
        expected_symbols = ["⚖️", "🏛️", "⚡", "⚠️"]
        for symbol in expected_symbols:
            assert symbol in symbols
    
    def test_symbolic_analysis(self):
        """Test symbolic analysis logic"""
        import torch
        
        # Mock embeddings
        embeddings = torch.randn(1, 768)
        symbols = ["⚖️", "🏛️"]
        
        result = self.classifier._symbolic_analysis(embeddings, symbols)
        
        assert "confidence" in result
        assert "domain" in result
        assert "symbol_count" in result
        assert result["symbol_count"] == len(symbols)


class TestMayaLegalAnalyzer:
    """Test main Maya Legal Analyzer"""
    
    def setup_method(self):
        with patch('maya_legal_intelligence.core.AutoTokenizer.from_pretrained'), \
             patch('maya_legal_intelligence.core.AutoModel.from_pretrained'):
            self.analyzer = MayaLegalAnalyzer()
    
    def test_analyze_legal_document(self):
        """Test complete legal document analysis"""
        document = """
        This employment contract establishes the terms of employment.
        The employee shall receive fair compensation and just treatment.
        Any violation may result in penalties as prescribed by law.
        """
        
        result = self.analyzer.analyze_legal_document(document)
        
        # Check structure
        assert "maya_encoding" in result
        assert "symbolic_analysis" in result
        assert "fusion_result" in result
        assert "analysis_metadata" in result
        
        # Check maya encoding
        maya_data = result["maya_encoding"]
        assert "symbols" in maya_data
        assert "confidence" in maya_data
        assert "category" in maya_data
        
        # Check fusion result
        fusion_data = result["fusion_result"]
        assert "final_category" in fusion_data
        assert "confidence" in fusion_data
        assert "fusion_score" in fusion_data
    
    def test_analyze_empty_document(self):
        """Test analysis of empty document"""
        result = self.analyzer.analyze_legal_document("")
        
        assert "maya_encoding" in result
        assert result["maya_encoding"]["confidence"] == 0.0
    
    def test_fusion_analysis(self):
        """Test fusion analysis logic"""
        from maya_legal_intelligence.core import MayaLegalEncoding
        
        # Create mock encoding
        maya_encoding = MayaLegalEncoding(
            original_text="test",
            encoded_symbols=["𓊪𓏏𓇯"],
            confidence_score=0.8,
            legal_category="criminal_law",
            jurisdiction="multi"
        )
        
        # Create mock symbolic analysis
        symbolic_analysis = {
            "symbols": ["⚖️"],
            "confidence": 0.7,
            "classification": {"domain": "criminal_law"}
        }
        
        result = self.analyzer._fuse_analysis(maya_encoding, symbolic_analysis)
        
        assert result["final_category"] == "criminal_law"
        assert result["confidence"] > 0.7  # Should get confidence boost
        assert "maya_symbols" in result
        assert "symbolic_elements" in result


class TestLegalSymbolEnum:
    """Test legal symbol enumeration"""
    
    def test_legal_symbol_values(self):
        """Test legal symbol enum values"""
        assert LegalSymbol.JUSTICE.value == "⚖️"
        assert LegalSymbol.STATUTE.value == "📜"
        assert LegalSymbol.AUTHORITY.value == "🏛️"
        assert LegalSymbol.ENFORCEMENT.value == "⚡"
    
    def test_all_symbols_unique(self):
        """Test that all legal symbols are unique"""
        symbols = [symbol.value for symbol in LegalSymbol]
        assert len(symbols) == len(set(symbols))


@pytest.fixture
def sample_legal_document():
    """Fixture providing sample legal document"""
    return """
    LEGAL SERVICES AGREEMENT
    
    This agreement is entered into between Client and Attorney.
    The Attorney shall provide competent legal representation with justice and fairness.
    Client agrees to pay legal fees as specified in the fee schedule.
    Any disputes shall be resolved through appropriate court procedures.
    Evidence of legal services shall be documented and maintained.
    Violation of this agreement may result in penalties under applicable law.
    """


def test_integration_full_analysis(sample_legal_document):
    """Integration test for full analysis pipeline"""
    with patch('maya_legal_intelligence.core.AutoTokenizer.from_pretrained'), \
         patch('maya_legal_intelligence.core.AutoModel.from_pretrained'):
        
        analyzer = MayaLegalAnalyzer()
        result = analyzer.analyze_legal_document(sample_legal_document)
        
        # Verify complete analysis structure
        assert all(key in result for key in [
            "maya_encoding", "symbolic_analysis", "fusion_result", "analysis_metadata"
        ])
        
        # Verify analysis quality
        assert result["maya_encoding"]["confidence"] > 0.0
        assert result["fusion_result"]["confidence"] > 0.0
        assert len(result["symbolic_analysis"]["symbols"]) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])