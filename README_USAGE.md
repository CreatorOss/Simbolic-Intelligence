# 🚀 Maya Legal Intelligence - Usage Guide

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/CreatorOss/maya-legal-intelligence.git
cd maya-legal-intelligence

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### Basic Usage

```python
from maya_legal_intelligence import MayaLegalAnalyzer

# Initialize analyzer
analyzer = MayaLegalAnalyzer()

# Analyze legal document
legal_text = """
This employment contract establishes terms between employer and employee.
The employee shall receive fair compensation and just treatment.
Any violation may result in legal penalties under applicable law.
"""

result = analyzer.analyze_legal_document(legal_text)

print(f"Legal Category: {result['fusion_result']['final_category']}")
print(f"Confidence: {result['fusion_result']['confidence']:.2%}")
print(f"Maya Symbols: {result['maya_encoding']['symbols']}")
print(f"Legal Symbols: {result['symbolic_analysis']['symbols']}")
```

### Command Line Interface

```bash
# Analyze a legal document
maya-legal analyze contract.txt

# Analyze text directly
maya-legal analyze-text "This contract establishes legal obligations"

# Batch process documents
maya-legal batch-analyze ./legal_documents/

# Run demonstration
maya-legal demo
```

### Document Processing

```python
from maya_legal_intelligence import LegalDocumentProcessor

# Initialize processor
processor = LegalDocumentProcessor()

# Process single document
result = processor.process_document("contract.txt")

# Batch process multiple documents
results = processor.batch_process(["doc1.txt", "doc2.txt", "doc3.txt"])
```

## Advanced Features

### Symbolic Mapping

```python
from maya_legal_intelligence.utils import LegalSymbolMapper

mapper = LegalSymbolMapper()
symbols = mapper.map_text_to_symbols("The court ensures justice through enforcement")
print(f"Legal Symbols: {[s[0] for s in symbols]}")
```

### Maya Encoding

```python
from maya_legal_intelligence.core import MayaSymbolEncoder

encoder = MayaSymbolEncoder()
encoding = encoder.encode("Legal contract with justice provisions")
print(f"Maya Symbols: {encoding.encoded_symbols}")
print(f"Legal Category: {encoding.legal_category}")
```

## Configuration

Create a `config.json` file:

```json
{
  "max_document_size": 1000000,
  "supported_formats": [".txt", ".md", ".json"],
  "output_format": "json",
  "enable_caching": true,
  "cache_dir": ".maya_cache"
}
```

## Examples

See the `examples/` directory for complete usage examples:

- `basic_usage.py` - Basic analysis examples
- `batch_processing.py` - Batch document processing
- `symbolic_analysis.py` - Advanced symbolic analysis
- `maya_encoding.py` - Maya hieroglyphic encoding

## API Reference

### MayaLegalAnalyzer

Main analyzer class for legal document analysis.

**Methods:**
- `analyze_legal_document(document: str) -> Dict[str, Any]`

### LegalDocumentProcessor

Document processing and file handling.

**Methods:**
- `process_document(document_path: str) -> Dict[str, Any]`
- `process_text(text: str) -> Dict[str, Any]`
- `batch_process(document_paths: List[str]) -> Dict[str, Any]`

### LegalSymbolMapper

Map legal concepts to symbolic representations.

**Methods:**
- `map_text_to_symbols(text: str) -> List[Tuple[str, float]]`
- `get_symbol_categories(symbols: List[str]) -> Dict[str, List[str]]`

## Legal Symbol Reference

| Symbol | Meaning | Keywords |
|--------|---------|----------|
| ⚖️ | Justice | justice, fair, equitable |
| 📜 | Statute | law, statute, regulation |
| 🏛️ | Authority | court, judge, authority |
| ⚡ | Enforcement | penalty, sanction, enforcement |
| 📋 | Contract | contract, agreement, covenant |
| 🔍 | Evidence | evidence, proof, testimony |
| ⚠️ | Penalty | fine, punishment, penalty |
| 🛡️ | Rights | rights, freedom, liberty |

## Maya Hieroglyphic Mappings

| Concept | Maya Symbol | Description |
|---------|-------------|-------------|
| Justice | 𓊪𓏏𓇯 | Ancient Maya justice symbol |
| Law | 𓈖𓏏𓊪 | Written law and regulation |
| Court | 𓉐𓂋𓏏 | Authority and judgment |
| Contract | 𓈖𓃀𓏏 | Agreement and covenant |
| Penalty | 𓊃𓈖𓏏 | Punishment and consequence |
| Evidence | 𓌃𓂋𓏏 | Proof and testimony |
| Rights | 𓊪𓏏𓊪 | Protection and freedom |
| Statute | 𓈖𓏏𓈖 | Written legal code |

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Memory Issues**: For large documents, increase memory limits
   ```python
   processor = LegalDocumentProcessor({"max_document_size": 5000000})
   ```

3. **Performance**: Enable caching for repeated analysis
   ```python
   processor = LegalDocumentProcessor({"enable_caching": True})
   ```

## Support

- **Documentation**: [Full Documentation](https://maya-legal-intelligence.readthedocs.io)
- **Issues**: [GitHub Issues](https://github.com/CreatorOss/maya-legal-intelligence/issues)
- **Email**: creatoropensource@gmail.com
- **LinkedIn**: [BENNY HARIANTO](https://www.linkedin.com/in/bennyharianto-024868383)

## License

MIT License - see LICENSE file for details.

---

**© 2025 Maya Legal Intelligence**  
*Revolutionary Legal Technology - Ancient Wisdom Meets Modern Innovation*