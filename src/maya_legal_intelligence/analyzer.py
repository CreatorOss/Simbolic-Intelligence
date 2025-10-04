"""
Legal Document Processor and Analyzer
=====================================
"""

import json
import logging
import os
from pathlib import Path
from typing import Dict, List, Optional, Union, Any
import hashlib
import base64

from .core import MayaLegalAnalyzer, LegalSymbol
from .utils import LegalSymbolMapper


class LegalDocumentProcessor:
    """Process and analyze legal documents"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.analyzer = MayaLegalAnalyzer()
        self.symbol_mapper = LegalSymbolMapper()
        self._config = self._load_config(config_path)
        self._logger = logging.getLogger(__name__)
    
    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration"""
        default_config = {
            "max_document_size": 1000000,  # 1MB
            "supported_formats": [".txt", ".md", ".json"],
            "output_format": "json",
            "enable_caching": True,
            "cache_dir": ".maya_cache"
        }
        
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    user_config = json.load(f)
                default_config.update(user_config)
            except Exception as e:
                self._logger.warning(f"Failed to load config: {e}")
        
        return default_config
    
    def process_document(self, document_path: str) -> Dict[str, Any]:
        """Process a legal document file"""
        try:
            # Validate file
            if not os.path.exists(document_path):
                raise FileNotFoundError(f"Document not found: {document_path}")
            
            # Check file size
            file_size = os.path.getsize(document_path)
            if file_size > self._config["max_document_size"]:
                raise ValueError(f"Document too large: {file_size} bytes")
            
            # Read document
            with open(document_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Process with analyzer
            analysis_result = self.analyzer.analyze_legal_document(content)
            
            # Add file metadata
            analysis_result["file_metadata"] = {
                "path": document_path,
                "size": file_size,
                "format": Path(document_path).suffix,
                "hash": self._calculate_file_hash(document_path)
            }
            
            # Cache result if enabled
            if self._config["enable_caching"]:
                self._cache_result(document_path, analysis_result)
            
            return analysis_result
            
        except Exception as e:
            self._logger.error(f"Document processing failed: {e}")
            return {"error": str(e), "status": "failed"}
    
    def process_text(self, text: str) -> Dict[str, Any]:
        """Process raw text content"""
        return self.analyzer.analyze_legal_document(text)
    
    def batch_process(self, document_paths: List[str]) -> Dict[str, Any]:
        """Process multiple documents"""
        results = {}
        
        for doc_path in document_paths:
            try:
                result = self.process_document(doc_path)
                results[doc_path] = result
            except Exception as e:
                results[doc_path] = {"error": str(e), "status": "failed"}
        
        return {
            "batch_results": results,
            "total_processed": len(document_paths),
            "successful": len([r for r in results.values() if "error" not in r]),
            "failed": len([r for r in results.values() if "error" in r])
        }
    
    def _calculate_file_hash(self, file_path: str) -> str:
        """Calculate file hash for caching"""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def _cache_result(self, document_path: str, result: Dict[str, Any]) -> None:
        """Cache analysis result"""
        try:
            cache_dir = Path(self._config["cache_dir"])
            cache_dir.mkdir(exist_ok=True)
            
            file_hash = self._calculate_file_hash(document_path)
            cache_file = cache_dir / f"{file_hash}.json"
            
            with open(cache_file, 'w') as f:
                json.dump(result, f, indent=2)
                
        except Exception as e:
            self._logger.warning(f"Caching failed: {e}")


def cli_main():
    """CLI entry point for legal document analysis"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Maya Legal Intelligence Analyzer")
    parser.add_argument("document", help="Path to legal document")
    parser.add_argument("--config", help="Configuration file path")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--format", choices=["json", "yaml"], default="json", help="Output format")
    
    args = parser.parse_args()
    
    # Initialize processor
    processor = LegalDocumentProcessor(args.config)
    
    # Process document
    result = processor.process_document(args.document)
    
    # Output result
    if args.output:
        with open(args.output, 'w') as f:
            if args.format == "json":
                json.dump(result, f, indent=2)
            else:  # yaml
                import yaml
                yaml.dump(result, f, default_flow_style=False)
    else:
        print(json.dumps(result, indent=2))


# Obfuscated functions for security
def _0x7g8h9i(data: bytes) -> str:
    """Obfuscated security function"""
    return base64.b85encode(data).decode()[:24]

def _0xj1k2l3(content: str) -> bytes:
    """Obfuscated encryption stub"""
    return hashlib.blake2b(content.encode(), digest_size=32).digest()