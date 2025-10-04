"""
Basic Usage Examples for Maya Legal Intelligence
==============================================
"""

from maya_legal_intelligence import MayaLegalAnalyzer, LegalDocumentProcessor


def example_basic_analysis():
    """Basic legal document analysis example"""
    
    # Sample legal text
    legal_text = """
    This Employment Agreement is entered into between the Company and the Employee.
    The Employee agrees to perform duties in accordance with company policies.
    Any violation of this agreement may result in termination and legal penalties.
    The Company shall provide fair compensation and maintain workplace justice.
    """
    
    # Initialize analyzer
    analyzer = MayaLegalAnalyzer()
    
    # Perform analysis
    result = analyzer.analyze_legal_document(legal_text)
    
    print("🏛️ Maya Legal Intelligence Analysis")
    print("=" * 50)
    print(f"Maya Symbols: {result['maya_encoding']['symbols']}")
    print(f"Legal Category: {result['maya_encoding']['category']}")
    print(f"Confidence: {result['maya_encoding']['confidence']:.2%}")
    print(f"Final Classification: {result['fusion_result']['final_category']}")


def example_document_processing():
    """Document file processing example"""
    
    # Initialize processor
    processor = LegalDocumentProcessor()
    
    # Create sample document
    sample_doc = "sample_contract.txt"
    with open(sample_doc, 'w') as f:
        f.write("""
        LEGAL SERVICES AGREEMENT
        
        This agreement establishes the terms for legal representation.
        The attorney shall provide competent legal services with justice and fairness.
        Client agrees to pay fees as specified in the fee schedule.
        Any disputes shall be resolved through appropriate court procedures.
        Evidence of performance shall be documented and maintained.
        """)
    
    # Process document
    result = processor.process_document(sample_doc)
    
    print("\n📄 Document Processing Result")
    print("=" * 50)
    print(f"File: {result['file_metadata']['path']}")
    print(f"Size: {result['file_metadata']['size']} bytes")
    print(f"Legal Symbols: {result['symbolic_analysis']['symbols']}")
    print(f"Domain: {result['symbolic_analysis']['classification']['domain']}")
    
    # Cleanup
    import os
    os.remove(sample_doc)


def example_batch_processing():
    """Batch processing example"""
    
    # Create sample documents
    documents = {
        "contract1.txt": "This contract establishes terms for service provision with penalties for breach.",
        "criminal_case.txt": "The defendant is charged with violation of criminal statutes requiring court judgment.",
        "constitutional.txt": "This amendment protects fundamental rights and freedoms of all citizens."
    }
    
    # Create files
    for filename, content in documents.items():
        with open(filename, 'w') as f:
            f.write(content)
    
    # Batch process
    processor = LegalDocumentProcessor()
    file_paths = list(documents.keys())
    
    batch_result = processor.batch_process(file_paths)
    
    print("\n📊 Batch Processing Results")
    print("=" * 50)
    print(f"Total Processed: {batch_result['total_processed']}")
    print(f"Successful: {batch_result['successful']}")
    print(f"Failed: {batch_result['failed']}")
    
    # Show individual results
    for doc_path, result in batch_result['batch_results'].items():
        if 'error' not in result:
            category = result['fusion_result']['final_category']
            confidence = result['fusion_result']['confidence']
            print(f"  {doc_path}: {category} ({confidence:.1%})")
    
    # Cleanup
    import os
    for filename in documents.keys():
        os.remove(filename)


def example_symbolic_mapping():
    """Symbolic mapping example"""
    
    from maya_legal_intelligence.utils import LegalSymbolMapper
    
    mapper = LegalSymbolMapper()
    
    legal_texts = [
        "The court shall ensure justice is served fairly",
        "This contract binds both parties to the agreement", 
        "Evidence must be presented to support the case",
        "Penalties apply for violation of these regulations"
    ]
    
    print("\n🔮 Symbolic Mapping Examples")
    print("=" * 50)
    
    for text in legal_texts:
        symbols = mapper.map_text_to_symbols(text)
        print(f"Text: {text[:40]}...")
        print(f"Symbols: {[s[0] for s in symbols[:3]]}")
        print()


if __name__ == "__main__":
    print("🚀 Maya Legal Intelligence - Usage Examples")
    print("=" * 60)
    
    example_basic_analysis()
    example_document_processing()
    example_batch_processing()
    example_symbolic_mapping()
    
    print("\n✅ All examples completed successfully!")