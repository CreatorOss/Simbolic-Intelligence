"""
Basic Usage Examples for Symbolic Legal Intelligence
===================================================
"""

from maya_legal_intelligence import SymbolicLegalIntelligence, LegalDocumentProcessor, LEGAL_SYMBOLS


def example_basic_analysis():
    """Basic legal document analysis example using symbolic intelligence"""
    
    # Sample legal text
    legal_text = """
    ARTICLE I - CONSTITUTIONAL RIGHTS
    
    Section 1. All citizens shall have equal protection under the law.
    The court must determine if constitutional violations have occurred.
    
    Section 2. Criminal penalties may include imprisonment up to 10 years
    and fines not exceeding $50,000 for violations of federal statutes.
    
    Procedural Requirements:
    - All motions must be filed within 30 days
    - Defendants shall have right to legal counsel
    - Evidence must be presented according to established procedures
    """
    
    # Initialize analyzer
    analyzer = SymbolicLegalIntelligence()
    
    # Perform analysis
    elements = analyzer.analyze_legal_document("sample_legal_doc.txt", legal_text)
    
    print("⟐ Symbolic Legal Intelligence Analysis")
    print("=" * 50)
    print(f"Total Elements Found: {len(elements)}")
    print()
    
    # Display by symbol type
    for symbol_name, symbol in LEGAL_SYMBOLS.items():
        symbol_elements = [e for e in elements if e.symbol_name == symbol_name]
        if symbol_elements:
            print(f"{symbol} {symbol_name} ({len(symbol_elements)} elements):")
            for element in symbol_elements[:3]:  # Show first 3
                print(f"   • {element.name} (complexity: {element.complexity_score})")
            print()


def example_document_processing():
    """Document file processing example"""
    
    # Initialize processor
    processor = LegalDocumentProcessor()
    
    # Create sample document
    sample_doc = "sample_legal_contract.txt"
    with open(sample_doc, 'w') as f:
        f.write("""
        LEGAL SERVICES AGREEMENT
        
        ARTICLE I - SCOPE OF SERVICES
        Section 1.1. Attorney shall provide competent legal representation.
        Section 1.2. Client agrees to cooperate fully with legal procedures.
        
        ARTICLE II - COMPENSATION
        Section 2.1. Client shall pay fees as specified in Schedule A.
        Section 2.2. Payment must be made within 30 days of invoice.
        
        ARTICLE III - TERMINATION
        Section 3.1. Either party may terminate with 30 days written notice.
        Section 3.2. Upon termination, all pending matters shall be resolved.
        
        PENALTIES: Violation of this agreement may result in damages
        up to $25,000 and immediate termination of services.
        """)
    
    # Process document
    result = processor.process_document(sample_doc)
    
    print("\n📄 Document Processing Result")
    print("=" * 50)
    
    if "error" not in result:
        summary = result["analysis_summary"]
        print(f"File: {result['file_metadata']['path']}")
        print(f"Size: {result['file_metadata']['size']} bytes")
        print(f"Total Elements: {summary['total_elements']}")
        print(f"Primary Domain: {summary['primary_legal_domain']}")
        print(f"Average Complexity: {summary['average_complexity']}")
        print()
        
        print("Symbol Distribution:")
        for symbol_name, count in summary['symbol_distribution'].items():
            symbol = LEGAL_SYMBOLS[symbol_name]
            print(f"   {symbol} {symbol_name}: {count}")
        
        print()
        print("Legal Insights:")
        insights = result["legal_insights"]
        print(f"   Complexity: {insights['complexity_assessment']}")
        print(f"   Risk Indicators: {len(insights['legal_risk_indicators'])}")
        print(f"   Key Concepts: {len(insights['key_legal_concepts'])}")
    
    # Cleanup
    import os
    os.remove(sample_doc)


def example_batch_processing():
    """Batch processing example"""
    
    # Create sample documents
    documents = {
        "constitutional_law.txt": """
        AMENDMENT XIV - EQUAL PROTECTION
        Section 1. No State shall deny any person equal protection of the laws.
        The Supreme Court shall have jurisdiction to review constitutional violations.
        Penalties for constitutional violations may include federal intervention.
        """,
        
        "criminal_code.txt": """
        CRIMINAL CODE SECTION 187 - HOMICIDE
        Any person who unlawfully kills another shall be guilty of murder.
        Penalties: Imprisonment for 25 years to life or death penalty.
        Procedural requirements: Defendant must be informed of charges within 48 hours.
        """,
        
        "commercial_contract.txt": """
        COMMERCIAL SALES AGREEMENT
        Section 1. Seller agrees to deliver goods according to specifications.
        Section 2. Buyer shall pay within 30 days of delivery.
        Breach of contract may result in damages up to $100,000.
        """
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
    
    summary = batch_result["batch_summary"]
    print(f"Total Documents: {summary['total_documents']}")
    print(f"Successful: {summary['successful_analyses']}")
    print(f"Failed: {summary['failed_analyses']}")
    print(f"Success Rate: {summary['success_rate']}")
    print()
    
    print("Aggregate Statistics:")
    agg_stats = summary["aggregate_statistics"]
    print(f"   Total Elements: {agg_stats['total_legal_elements']}")
    print(f"   Domains: {', '.join(agg_stats['domain_distribution'].keys())}")
    print()
    
    # Show individual results
    for doc_path, result in batch_result['batch_results'].items():
        if 'error' not in result:
            analysis = result['analysis_summary']
            print(f"📄 {doc_path}:")
            print(f"   Domain: {analysis['primary_legal_domain']}")
            print(f"   Elements: {analysis['total_elements']}")
            print(f"   Complexity: {analysis['average_complexity']}")
    
    # Cleanup
    import os
    for filename in documents.keys():
        os.remove(filename)


def example_symbolic_analysis():
    """Symbolic analysis example showing all four symbols"""
    
    complex_legal_text = """
    UNITED STATES CONSTITUTION - ARTICLE I
    
    Section 8. The Congress shall have Power:
    - To regulate Commerce among the several States
    - To establish Post Offices and post Roads
    - To declare War and maintain armed Forces
    
    CRIMINAL PENALTIES: Violation of federal commerce regulations
    may result in imprisonment up to 20 years and fines up to $1,000,000.
    
    PROCEDURAL REQUIREMENTS:
    1. All cases must be filed in federal district court
    2. Defendants shall have right to jury trial
    3. Appeals must be filed within 30 days of judgment
    
    JUDICIAL REVIEW: The Supreme Court shall determine the constitutionality
    of all federal legislation and may declare laws unconstitutional.
    """
    
    analyzer = SymbolicLegalIntelligence()
    elements = analyzer.analyze_legal_document("complex_legal_doc.txt", complex_legal_text)
    
    print("\n🔮 Symbolic Analysis Examples")
    print("=" * 50)
    
    # Group by symbol type
    symbol_groups = {}
    for element in elements:
        symbol_name = element.symbol_name
        if symbol_name not in symbol_groups:
            symbol_groups[symbol_name] = []
        symbol_groups[symbol_name].append(element)
    
    # Display each symbol type
    for symbol_name, symbol in LEGAL_SYMBOLS.items():
        if symbol_name in symbol_groups:
            group_elements = symbol_groups[symbol_name]
            print(f"\n{symbol} {symbol_name} - {len(group_elements)} elements:")
            
            for element in group_elements:
                print(f"   • {element.name}")
                print(f"     Complexity: {element.complexity_score}")
                print(f"     Description: {element.description}")
                print()


if __name__ == "__main__":
    print("🚀 Symbolic Legal Intelligence - Usage Examples")
    print("=" * 60)
    
    example_basic_analysis()
    example_document_processing()
    example_batch_processing()
    example_symbolic_analysis()
    
    print("\n✅ All examples completed successfully!")
    print("🔮 Symbolic Intelligence provides universal understanding of legal documents!")
    print("⟐ ⧈ ◈ ⟡ - Four symbols for complete legal analysis")