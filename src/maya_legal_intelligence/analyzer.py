"""
Legal Document Processor with Symbolic Intelligence
==================================================
"""

import json
import logging
import os
from pathlib import Path
from typing import Dict, List, Optional, Union, Any
import hashlib
import base64

from .core import SymbolicLegalIntelligence, LEGAL_SYMBOLS


class LegalDocumentProcessor:
    """Process and analyze legal documents using symbolic intelligence"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.analyzer = SymbolicLegalIntelligence()
        self._config = self._load_config(config_path)
        self._logger = logging.getLogger(__name__)
    
    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration"""
        default_config = {
            "max_document_size": 5000000,  # 5MB for legal documents
            "supported_formats": [".txt", ".md", ".json"],
            "output_format": "json",
            "enable_caching": True,
            "cache_dir": ".legal_analysis_cache",
            "legal_domains": ["constitutional", "criminal", "civil", "commercial", "administrative"]
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
        """Process a legal document file using symbolic intelligence"""
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
            
            # Process with symbolic intelligence analyzer
            elements = self.analyzer.analyze_legal_document(document_path, content)
            
            # Generate comprehensive analysis
            analysis_result = self._generate_analysis_report(document_path, content, elements)
            
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
    
    def process_text(self, text: str, source_name: str = "direct_input") -> Dict[str, Any]:
        """Process raw legal text content"""
        try:
            elements = self.analyzer.analyze_legal_document(source_name, text)
            return self._generate_analysis_report(source_name, text, elements)
        except Exception as e:
            self._logger.error(f"Text processing failed: {e}")
            return {"error": str(e), "status": "failed"}
    
    def batch_process(self, document_paths: List[str]) -> Dict[str, Any]:
        """Process multiple legal documents"""
        results = {}
        
        for doc_path in document_paths:
            try:
                result = self.process_document(doc_path)
                results[doc_path] = result
            except Exception as e:
                results[doc_path] = {"error": str(e), "status": "failed"}
        
        # Generate batch summary
        batch_summary = self._generate_batch_summary(results)
        
        return {
            "batch_results": results,
            "batch_summary": batch_summary
        }
    
    def _generate_analysis_report(self, source: str, content: str, elements: List) -> Dict[str, Any]:
        """Generate comprehensive legal analysis report"""
        
        # Symbol distribution
        symbol_counts = {}
        for symbol_name in LEGAL_SYMBOLS.keys():
            symbol_counts[symbol_name] = len([e for e in elements if e.symbol_name == symbol_name])
        
        # Complexity analysis
        complexity_scores = [e.complexity_score for e in elements]
        avg_complexity = sum(complexity_scores) / len(complexity_scores) if complexity_scores else 0
        
        # Legal domain analysis
        domain_counts = {}
        for element in elements:
            domain = element.legal_domain
            domain_counts[domain] = domain_counts.get(domain, 0) + 1
        
        # Determine primary legal domain
        primary_domain = max(domain_counts, key=domain_counts.get) if domain_counts else "unknown"
        
        return {
            "source": source,
            "analysis_summary": {
                "total_elements": len(elements),
                "primary_legal_domain": primary_domain,
                "average_complexity": round(avg_complexity, 2),
                "document_length": len(content),
                "symbol_distribution": symbol_counts,
                "domain_distribution": domain_counts
            },
            "symbolic_analysis": {
                "structure_elements": [e for e in elements if e.symbol_name == "STRUCTURE"],
                "flow_elements": [e for e in elements if e.symbol_name == "FLOW"],
                "decision_elements": [e for e in elements if e.symbol_name == "DECISION"],
                "impact_elements": [e for e in elements if e.symbol_name == "IMPACT"]
            },
            "legal_insights": {
                "complexity_assessment": self._assess_complexity(avg_complexity),
                "legal_risk_indicators": self._identify_risk_indicators(elements),
                "procedural_requirements": self._extract_procedural_requirements(elements),
                "key_legal_concepts": self._extract_key_concepts(elements)
            },
            "elements": [
                {
                    "name": e.name,
                    "symbol": e.symbol,
                    "symbol_name": e.symbol_name,
                    "line": e.line_start,
                    "complexity": e.complexity_score,
                    "description": e.description,
                    "type": e.element_type,
                    "domain": e.legal_domain
                } for e in elements
            ],
            "analysis_metadata": {
                "analyzer_version": "1.0.0",
                "analysis_timestamp": self._get_timestamp(),
                "symbolic_intelligence_version": "proven"
            }
        }
    
    def _assess_complexity(self, avg_complexity: float) -> str:
        """Assess document complexity level"""
        if avg_complexity <= 3:
            return "Low - Simple legal document"
        elif avg_complexity <= 8:
            return "Moderate - Standard legal complexity"
        elif avg_complexity <= 15:
            return "High - Complex legal document"
        else:
            return "Very High - Highly complex legal document"
    
    def _identify_risk_indicators(self, elements: List) -> List[str]:
        """Identify potential legal risk indicators"""
        risk_indicators = []
        
        # High-impact elements indicate potential risks
        impact_elements = [e for e in elements if e.symbol_name == "IMPACT"]
        if len(impact_elements) > 5:
            risk_indicators.append("High number of impact elements detected")
        
        # Complex decision elements
        complex_decisions = [e for e in elements if e.symbol_name == "DECISION" and e.complexity_score > 10]
        if complex_decisions:
            risk_indicators.append("Complex decision points requiring careful review")
        
        # Criminal law indicators
        criminal_elements = [e for e in elements if e.legal_domain == "criminal"]
        if criminal_elements:
            risk_indicators.append("Criminal law elements present")
        
        return risk_indicators
    
    def _extract_procedural_requirements(self, elements: List) -> List[str]:
        """Extract procedural requirements from flow elements"""
        requirements = []
        
        flow_elements = [e for e in elements if e.symbol_name == "FLOW"]
        for element in flow_elements:
            if any(word in element.name.lower() for word in ['shall', 'must', 'required']):
                requirements.append(element.description)
        
        return requirements[:10]  # Limit to top 10
    
    def _extract_key_concepts(self, elements: List) -> List[str]:
        """Extract key legal concepts"""
        concepts = []
        
        # Structure elements often contain key concepts
        structure_elements = [e for e in elements if e.symbol_name == "STRUCTURE"]
        for element in structure_elements:
            concepts.append(element.name)
        
        # High-complexity elements
        complex_elements = [e for e in elements if e.complexity_score > 10]
        for element in complex_elements:
            concepts.append(element.name)
        
        return list(set(concepts))[:15]  # Unique concepts, limit to 15
    
    def _generate_batch_summary(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate summary for batch processing"""
        total = len(results)
        successful = len([r for r in results.values() if "error" not in r])
        failed = total - successful
        
        # Aggregate statistics
        total_elements = 0
        domain_counts = {}
        symbol_counts = {}
        
        for result in results.values():
            if "error" not in result:
                total_elements += result.get("analysis_summary", {}).get("total_elements", 0)
                
                # Aggregate domains
                domain_dist = result.get("analysis_summary", {}).get("domain_distribution", {})
                for domain, count in domain_dist.items():
                    domain_counts[domain] = domain_counts.get(domain, 0) + count
                
                # Aggregate symbols
                symbol_dist = result.get("analysis_summary", {}).get("symbol_distribution", {})
                for symbol, count in symbol_dist.items():
                    symbol_counts[symbol] = symbol_counts.get(symbol, 0) + count
        
        return {
            "total_documents": total,
            "successful_analyses": successful,
            "failed_analyses": failed,
            "success_rate": f"{(successful/total)*100:.1f}%" if total > 0 else "0%",
            "aggregate_statistics": {
                "total_legal_elements": total_elements,
                "domain_distribution": domain_counts,
                "symbol_distribution": symbol_counts
            }
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
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        import datetime
        return datetime.datetime.now().isoformat()


def cli_main():
    """CLI entry point for legal document analysis"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Symbolic Legal Intelligence Analyzer")
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