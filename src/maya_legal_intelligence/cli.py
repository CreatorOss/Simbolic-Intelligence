"""
Command Line Interface for Symbolic Legal Intelligence
=====================================================
"""

import json
import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from .analyzer import LegalDocumentProcessor
from .core import SymbolicLegalIntelligence, LEGAL_SYMBOLS


console = Console()


@click.group()
@click.version_option(version="1.0.0")
def main():
    """Symbolic Legal Intelligence - Universal Legal Document Analysis"""
    pass


@main.command()
@click.argument('document_path', type=click.Path(exists=True))
@click.option('--output', '-o', help='Output file path')
@click.option('--format', '-f', type=click.Choice(['json', 'yaml']), default='json', help='Output format')
@click.option('--config', '-c', help='Configuration file path')
def analyze(document_path: str, output: Optional[str], format: str, config: Optional[str]):
    """Analyze a legal document using symbolic intelligence"""
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("Analyzing legal document...", total=None)
        
        try:
            # Initialize processor
            processor = LegalDocumentProcessor(config)
            
            # Process document
            result = processor.process_document(document_path)
            
            progress.update(task, description="Analysis complete!")
            
            # Display results
            _display_analysis_result(result)
            
            # Save output if specified
            if output:
                _save_result(result, output, format)
                console.print(f"✅ Results saved to {output}", style="green")
                
        except Exception as e:
            console.print(f"❌ Analysis failed: {str(e)}", style="red")
            sys.exit(1)


@main.command()
@click.argument('text')
@click.option('--output', '-o', help='Output file path')
@click.option('--format', '-f', type=click.Choice(['json', 'yaml']), default='json', help='Output format')
def analyze_text(text: str, output: Optional[str], format: str):
    """Analyze legal text directly using symbolic intelligence"""
    
    try:
        processor = LegalDocumentProcessor()
        result = processor.process_text(text)
        
        _display_analysis_result(result)
        
        if output:
            _save_result(result, output, format)
            console.print(f"✅ Results saved to {output}", style="green")
            
    except Exception as e:
        console.print(f"❌ Analysis failed: {str(e)}", style="red")
        sys.exit(1)


@main.command()
@click.argument('directory_path', type=click.Path(exists=True))
@click.option('--output', '-o', help='Output directory path')
@click.option('--format', '-f', type=click.Choice(['json', 'yaml']), default='json', help='Output format')
@click.option('--config', '-c', help='Configuration file path')
def batch_analyze(directory_path: str, output: Optional[str], format: str, config: Optional[str]):
    """Batch analyze legal documents in a directory"""
    
    directory = Path(directory_path)
    legal_files = list(directory.glob("*.txt")) + list(directory.glob("*.md"))
    
    if not legal_files:
        console.print("❌ No legal documents found in directory", style="red")
        return
    
    with Progress(console=console) as progress:
        task = progress.add_task("Processing legal documents...", total=len(legal_files))
        
        processor = LegalDocumentProcessor(config)
        file_paths = [str(f) for f in legal_files]
        
        batch_result = processor.batch_process(file_paths)
        
        progress.advance(task, advance=len(legal_files))
    
    # Display summary
    _display_batch_summary(batch_result)
    
    # Save results if output specified
    if output:
        output_dir = Path(output)
        output_dir.mkdir(exist_ok=True)
        
        for file_path, result in batch_result["batch_results"].items():
            output_file = output_dir / f"{Path(file_path).stem}_analysis.{format}"
            _save_result(result, str(output_file), format)
        
        # Save batch summary
        summary_file = output_dir / f"batch_summary.{format}"
        _save_result(batch_result["batch_summary"], str(summary_file), format)
        
        console.print(f"✅ Batch results saved to {output}", style="green")


@main.command()
def demo():
    """Run a demonstration of Symbolic Legal Intelligence"""
    
    demo_text = """
    ARTICLE I - CONSTITUTIONAL PROVISIONS
    
    Section 1. All persons shall have the right to equal protection under the law.
    The court shall determine if any violation of constitutional rights has occurred.
    
    Section 2. Criminal penalties may include imprisonment not exceeding 10 years
    and fines up to $100,000 for violations of this statute.
    
    Procedural requirements: All motions must be filed within 30 days of the incident.
    The defendant shall have the right to legal representation throughout the process.
    """
    
    console.print(Panel.fit("⟐ Symbolic Legal Intelligence Demo", style="bold blue"))
    console.print("\n📜 Analyzing sample legal text...\n")
    
    processor = LegalDocumentProcessor()
    result = processor.process_text(demo_text, "demo_legal_document")
    
    _display_analysis_result(result)


@main.command()
def symbols():
    """Display the symbolic intelligence legend"""
    
    console.print(Panel.fit("⟐ Symbolic Legal Intelligence - Symbol Legend", style="bold blue"))
    console.print()
    
    table = Table(title="🔮 Universal Legal Symbols")
    table.add_column("Symbol", style="cyan", width=8)
    table.add_column("Name", style="green", width=12)
    table.add_column("Legal Meaning", style="yellow")
    table.add_column("Examples", style="white")
    
    symbol_info = {
        '⟐': ('STRUCTURE', 'Legal frameworks and foundations', 'Articles, Sections, Constitutional provisions'),
        '⧈': ('FLOW', 'Legal processes and procedures', 'Filing requirements, Procedural steps, Timelines'),
        '◈': ('DECISION', 'Critical legal decisions', 'Court rulings, Conditional clauses, Legal determinations'),
        '⟡': ('IMPACT', 'High-impact legal consequences', 'Penalties, Damages, Constitutional violations')
    }
    
    for symbol, (name, meaning, examples) in symbol_info.items():
        table.add_row(symbol, name, meaning, examples)
    
    console.print(table)
    console.print()
    console.print("✨ These symbols provide universal understanding of legal document structure and complexity!")


def _display_analysis_result(result: dict):
    """Display analysis result in a formatted way"""
    
    if "error" in result:
        console.print(f"❌ Error: {result['error']}", style="red")
        return
    
    # Analysis Summary
    if "analysis_summary" in result:
        summary = result["analysis_summary"]
        
        table = Table(title="📊 Legal Document Analysis Summary")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Total Elements", str(summary.get("total_elements", 0)))
        table.add_row("Primary Legal Domain", summary.get("primary_legal_domain", "Unknown"))
        table.add_row("Average Complexity", str(summary.get("average_complexity", 0)))
        table.add_row("Document Length", f"{summary.get('document_length', 0)} characters")
        
        console.print(table)
    
    # Symbol Distribution
    if "analysis_summary" in result and "symbol_distribution" in result["analysis_summary"]:
        symbol_dist = result["analysis_summary"]["symbol_distribution"]
        
        table = Table(title="⟐ Symbol Distribution")
        table.add_column("Symbol", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Count", style="yellow")
        table.add_column("Percentage", style="white")
        
        total = sum(symbol_dist.values()) if symbol_dist.values() else 1
        
        for symbol_name, count in symbol_dist.items():
            symbol = LEGAL_SYMBOLS.get(symbol_name, "?")
            percentage = f"{(count/total)*100:.1f}%"
            table.add_row(symbol, symbol_name, str(count), percentage)
        
        console.print(table)
    
    # Legal Insights
    if "legal_insights" in result:
        insights = result["legal_insights"]
        
        console.print(Panel(
            f"🎯 **Complexity Assessment:** {insights.get('complexity_assessment', 'Unknown')}\n"
            f"⚠️  **Risk Indicators:** {len(insights.get('legal_risk_indicators', []))} identified\n"
            f"📋 **Procedural Requirements:** {len(insights.get('procedural_requirements', []))} found\n"
            f"🔑 **Key Legal Concepts:** {len(insights.get('key_legal_concepts', []))} extracted",
            title="⚖️ Legal Analysis Insights",
            style="bold green"
        ))
        
        # Show risk indicators if any
        risk_indicators = insights.get('legal_risk_indicators', [])
        if risk_indicators:
            console.print("\n⚠️  **Risk Indicators:**")
            for risk in risk_indicators[:5]:  # Show top 5
                console.print(f"   • {risk}")


def _display_batch_summary(batch_result: dict):
    """Display batch processing summary"""
    
    summary = batch_result.get("batch_summary", {})
    
    table = Table(title="📊 Batch Processing Summary")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Total Documents", str(summary.get("total_documents", 0)))
    table.add_row("Successful Analyses", str(summary.get("successful_analyses", 0)))
    table.add_row("Failed Analyses", str(summary.get("failed_analyses", 0)))
    table.add_row("Success Rate", summary.get("success_rate", "0%"))
    
    console.print(table)
    
    # Aggregate statistics
    if "aggregate_statistics" in summary:
        agg_stats = summary["aggregate_statistics"]
        
        console.print(f"\n📈 **Aggregate Statistics:**")
        console.print(f"   Total Legal Elements: {agg_stats.get('total_legal_elements', 0)}")
        
        # Domain distribution
        domain_dist = agg_stats.get('domain_distribution', {})
        if domain_dist:
            console.print(f"   Legal Domains: {', '.join(f'{k}({v})' for k, v in domain_dist.items())}")


def _save_result(result: dict, output_path: str, format: str):
    """Save analysis result to file"""
    
    with open(output_path, 'w') as f:
        if format == 'json':
            json.dump(result, f, indent=2)
        else:  # yaml
            import yaml
            yaml.dump(result, f, default_flow_style=False)


if __name__ == "__main__":
    main()