"""
Command Line Interface for Maya Legal Intelligence
=================================================
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
from .core import MayaLegalAnalyzer


console = Console()


@click.group()
@click.version_option(version="0.1.0")
def main():
    """Maya Legal Intelligence - Symbolic Legal Analysis Platform"""
    pass


@main.command()
@click.argument('document_path', type=click.Path(exists=True))
@click.option('--output', '-o', help='Output file path')
@click.option('--format', '-f', type=click.Choice(['json', 'yaml']), default='json', help='Output format')
@click.option('--config', '-c', help='Configuration file path')
def analyze(document_path: str, output: Optional[str], format: str, config: Optional[str]):
    """Analyze a legal document"""
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("Analyzing document...", total=None)
        
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
    """Analyze legal text directly"""
    
    try:
        analyzer = MayaLegalAnalyzer()
        result = analyzer.analyze_legal_document(text)
        
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
        task = progress.add_task("Processing documents...", total=len(legal_files))
        
        processor = LegalDocumentProcessor(config)
        results = {}
        
        for file_path in legal_files:
            try:
                result = processor.process_document(str(file_path))
                results[str(file_path)] = result
                progress.advance(task)
            except Exception as e:
                console.print(f"❌ Failed to process {file_path}: {str(e)}", style="red")
                results[str(file_path)] = {"error": str(e)}
    
    # Display summary
    _display_batch_summary(results)
    
    # Save results if output specified
    if output:
        output_dir = Path(output)
        output_dir.mkdir(exist_ok=True)
        
        for file_path, result in results.items():
            output_file = output_dir / f"{Path(file_path).stem}_analysis.{format}"
            _save_result(result, str(output_file), format)
        
        console.print(f"✅ Batch results saved to {output}", style="green")


@main.command()
def demo():
    """Run a demonstration of Maya Legal Intelligence"""
    
    demo_text = """
    This contract establishes the terms and conditions for the provision of legal services.
    The parties agree to the following terms: justice shall be served fairly and equitably.
    Any violation of this agreement may result in penalties as prescribed by law.
    Evidence of breach must be presented to the appropriate court authority.
    """
    
    console.print(Panel.fit("🏛️ Maya Legal Intelligence Demo", style="bold blue"))
    console.print("\n📜 Analyzing sample legal text...\n")
    
    analyzer = MayaLegalAnalyzer()
    result = analyzer.analyze_legal_document(demo_text)
    
    _display_analysis_result(result)


def _display_analysis_result(result: dict):
    """Display analysis result in a formatted way"""
    
    if "error" in result:
        console.print(f"❌ Error: {result['error']}", style="red")
        return
    
    # Maya Encoding Results
    if "maya_encoding" in result:
        maya_data = result["maya_encoding"]
        
        table = Table(title="🏛️ Maya Hieroglyphic Analysis")
        table.add_column("Aspect", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Symbols Found", " ".join(maya_data.get("symbols", [])))
        table.add_row("Confidence", f"{maya_data.get('confidence', 0):.2%}")
        table.add_row("Legal Category", maya_data.get("category", "Unknown"))
        table.add_row("Jurisdiction", maya_data.get("jurisdiction", "Unknown"))
        
        console.print(table)
    
    # Symbolic Analysis Results
    if "symbolic_analysis" in result:
        symbolic_data = result["symbolic_analysis"]
        
        table = Table(title="🔮 Symbolic Intelligence Analysis")
        table.add_column("Aspect", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Legal Symbols", " ".join(symbolic_data.get("symbols", [])))
        table.add_row("Confidence", f"{symbolic_data.get('confidence', 0):.2%}")
        table.add_row("Legal Domain", symbolic_data["classification"].get("domain", "Unknown"))
        
        console.print(table)
    
    # Fusion Results
    if "fusion_result" in result:
        fusion_data = result["fusion_result"]
        
        console.print(Panel(
            f"🎯 **Final Classification:** {fusion_data.get('final_category', 'Unknown')}\n"
            f"🎯 **Confidence Score:** {fusion_data.get('confidence', 0):.2%}\n"
            f"🎯 **Fusion Score:** {fusion_data.get('fusion_score', 0):.2%}",
            title="⚖️ Fusion Analysis Result",
            style="bold green"
        ))


def _display_batch_summary(results: dict):
    """Display batch processing summary"""
    
    total = len(results)
    successful = len([r for r in results.values() if "error" not in r])
    failed = total - successful
    
    table = Table(title="📊 Batch Processing Summary")
    table.add_column("Metric", style="cyan")
    table.add_column("Count", style="green")
    
    table.add_row("Total Documents", str(total))
    table.add_row("Successfully Processed", str(successful))
    table.add_row("Failed", str(failed))
    table.add_row("Success Rate", f"{(successful/total)*100:.1f}%")
    
    console.print(table)


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