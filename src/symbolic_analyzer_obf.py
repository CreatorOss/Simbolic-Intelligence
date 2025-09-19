#!/usr/bin/env python3
"""
Universal Symbolic Code Intelligence System - Obfuscated Core
Copyright (c) 2025 Benny Harianto
Email: creatoropensource@gmail.com
LinkedIn: www.linkedin.com/in/bennyharianto-024868383
Patent Pending - Trade Secret Protected
"""

import ast
import os
import sys
import json
import base64
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from collections import defaultdict

# Obfuscated symbol definitions
_S = {'A': '⟐', 'B': '⧈', 'C': '◈', 'D': '⟡'}
_K = [0x1A2B, 0x3C4D, 0x5E6F, 0x7890]  # Obfuscated complexity weights

@dataclass
class _CE:  # CodeElement (obfuscated)
    fp: str  # file_path
    n: str   # name
    s: str   # symbol
    sn: str  # symbol_name
    ls: int  # line_start
    le: int  # line_end
    cs: int  # complexity_score
    d: str   # description
    c: str   # code_snippet

class _PA(ast.NodeVisitor):  # PythonAnalyzer (obfuscated)
    def __init__(self, fp: str, sc: str):
        self.fp = fp
        self.sl = sc.split('\n')
        self.e: List[_CE] = []
        self._w = self._lw()  # Load weights (trade secret)
    
    def _lw(self):
        """Load obfuscated complexity weights - TRADE SECRET"""
        return {
            'class': _K[0] ^ 0x1000,
            'function': _K[1] ^ 0x2000,
            'if': _K[2] ^ 0x3000,
            'loop': _K[3] ^ 0x4000
        }
    
    def visit_ClassDef(self, node):
        """Classes are STRUCTURE ⟐"""
        e = _CE(
            fp=self.fp,
            n=node.name,
            s=_S['A'],
            sn='STRUCTURE',
            ls=node.lineno,
            le=getattr(node, 'end_lineno', node.lineno),
            cs=self._cc(node),  # Calculate complexity (obfuscated)
            d=f"Class {node.name} architectural boundary",
            c=self._gcs(node.lineno, getattr(node, 'end_lineno', node.lineno + 5))
        )
        self.e.append(e)
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        """Functions are FLOW ⧈ or DECISION ◈"""
        cx = self._cc(node)
        
        # Obfuscated decision logic
        if self._icd(node) and cx > (self._w['function'] >> 8):
            s, sn, d = _S['C'], 'DECISION', f"Complex decision logic in {node.name}"
        else:
            s, sn, d = _S['B'], 'FLOW', f"Function {node.name} data flow"
        
        e = _CE(
            fp=self.fp, n=node.name, s=s, sn=sn, ls=node.lineno,
            le=getattr(node, 'end_lineno', node.lineno), cs=cx, d=d,
            c=self._gcs(node.lineno, getattr(node, 'end_lineno', node.lineno + 10))
        )
        self.e.append(e)
        self.generic_visit(node)
    
    def visit_If(self, node):
        """Complex conditionals are DECISION ◈"""
        cx = self._cc(node)
        if cx > (self._w['if'] >> 10):  # Obfuscated threshold
            e = _CE(
                fp=self.fp, n=f"cond_L{node.lineno}", s=_S['C'], sn='DECISION',
                ls=node.lineno, le=getattr(node, 'end_lineno', node.lineno),
                cs=cx, d="Critical decision point", 
                c=self._gcs(node.lineno, getattr(node, 'end_lineno', node.lineno + 3))
            )
            self.e.append(e)
        self.generic_visit(node)
    
    def _cc(self, node) -> int:
        """Calculate complexity - PROPRIETARY ALGORITHM"""
        # Trade secret complexity calculation
        cx = 1
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For)):
                cx += (self._w['loop'] >> 12) + 1
            elif isinstance(child, ast.Try):
                cx += (self._w['function'] >> 11) + 2
            elif isinstance(child, ast.BoolOp):
                cx += len(child.values) * (self._w['if'] >> 13)
        
        # Proprietary normalization (trade secret)
        return min(cx * self._pn(), 20)  # Max complexity 20
    
    def _pn(self) -> float:
        """Proprietary normalization factor - TRADE SECRET"""
        # This contains trade secret normalization algorithm
        return 1.0 + (sum(_K) >> 16) / 1000.0
    
    def _icd(self, node) -> bool:
        """Is complex decision - TRADE SECRET LOGIC"""
        # Proprietary decision detection algorithm
        dump = ast.dump(node)
        keywords = ['if', 'elif', 'else', 'and', 'or', 'not']
        score = sum(dump.count(kw) for kw in keywords)
        return score > (self._w['if'] >> 14)
    
    def _gcs(self, start: int, end: int) -> str:
        """Get code snippet"""
        try:
            si = max(0, start - 1)
            ei = min(len(self.sl), end)
            return '\n'.join(self.sl[si:ei])
        except:
            return "Code unavailable"

class _SA:  # SymbolicAnalyzer (obfuscated)
    def __init__(self):
        self.e: List[_CE] = []
        self.fs = defaultdict(int)
        self._cfg = self._lc()  # Load config (trade secret)
    
    def _lc(self):
        """Load configuration - TRADE SECRET"""
        # Obfuscated configuration
        return {
            'impact_threshold': (_K[0] >> 8) + 3,
            'decision_threshold': (_K[1] >> 9) + 2,
            'flow_threshold': (_K[2] >> 10) + 1
        }
    
    def analyze_directory(self, directory: str) -> Dict[str, Any]:
        """Analyze directory with obfuscated processing"""
        for py_file in Path(directory).rglob('*.py'):
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    sc = f.read()
                
                tree = ast.parse(sc)
                analyzer = _PA(str(py_file), sc)
                analyzer.visit(tree)
                
                self.e.extend(analyzer.e)
                self.fs[str(py_file)] = len(analyzer.e)
                
            except Exception as e:
                print(f"Error analyzing {py_file}: {e}")
        
        return self._gr()  # Generate report (obfuscated)
    
    def _gr(self) -> Dict[str, Any]:
        """Generate report - PROPRIETARY PROCESSING"""
        sc = defaultdict(int)  # symbol_counts
        hie = []  # high_impact_elements
        
        for element in self.e:
            sc[element.sn] += 1
            if element.cs > self._cfg['impact_threshold']:
                hie.append(element)
        
        # Mark high complexity as IMPACT ⟡ (trade secret logic)
        for element in hie:
            if element.cs > (self._cfg['impact_threshold'] + 3):
                element.s = _S['D']
                element.sn = 'IMPACT'
                element.d += " - CRITICAL: High complexity detected"
        
        return {
            'summary': {
                'total_elements': len(self.e),
                'files_analyzed': len(self.fs),
                'symbol_distribution': dict(sc),
                'high_impact_count': len(hie),
                'analysis_signature': self._gas()  # Generate analysis signature
            },
            'elements': [asdict(e) for e in self.e],
            'file_stats': dict(self.fs),
            'metadata': {
                'analyzer_version': '1.0.0-obf',
                'copyright': 'Benny Harianto 2025',
                'patent_pending': True
            }
        }
    
    def _gas(self) -> str:
        """Generate analysis signature - TRADE SECRET"""
        # Proprietary signature generation
        data = f"{len(self.e)}{sum(self.fs.values())}{sum(_K)}"
        return base64.b64encode(data.encode()).decode()[:16]

def _gmr(report: Dict[str, Any]) -> str:
    """Generate markdown report - OBFUSCATED"""
    md = []
    md.append("# 🔮 Universal Symbolic Code Analysis Report")
    md.append("**Copyright (c) 2025 Benny Harianto - Patent Pending**\n")
    
    s = report['summary']
    md.append("## 📊 Analysis Summary\n")
    md.append(f"- **Total Elements**: {s['total_elements']}")
    md.append(f"- **Files Analyzed**: {s['files_analyzed']}")
    md.append(f"- **High Impact Elements**: {s['high_impact_count']}")
    md.append(f"- **Analysis Signature**: {s.get('analysis_signature', 'N/A')}\n")
    
    md.append("## 🎯 Universal Symbol Distribution\n")
    for sn, count in s['symbol_distribution'].items():
        symbol = _S.get(sn[0], '?')
        md.append(f"- {symbol} **{sn}**: {count}")
    
    md.append("\n## 🔬 Detailed Analysis\n")
    
    # Group elements by symbol
    ebs = defaultdict(list)  # elements_by_symbol
    for element in report['elements']:
        ebs[element['sn']].append(element)
    
    for sn, elements in ebs.items():
        symbol = _S.get(sn[0], '?')
        md.append(f"### {symbol} {sn} Elements\n")
        
        for element in sorted(elements, key=lambda x: x['cs'], reverse=True)[:5]:
            md.append(f"**{element['n']}** (Complexity: {element['cs']})")
            md.append(f"- File: `{element['fp']}`")
            md.append(f"- Lines: {element['ls']}-{element['le']}")
            md.append(f"- Description: {element['d']}")
            md.append("```python")
            md.append(element['c'][:200] + "..." if len(element['c']) > 200 else element['c'])
            md.append("```\n")
    
    md.append("---")
    md.append("*Generated by Universal Symbolic Code Intelligence System*")
    md.append("*Copyright (c) 2025 Benny Harianto*")
    md.append("*Email: creatoropensource@gmail.com*")
    md.append("*LinkedIn: www.linkedin.com/in/bennyharianto-024868383*")
    md.append("*Patent Pending - Proprietary Analysis Technology*")
    
    return '\n'.join(md)

def main():
    """Main entry point - OBFUSCATED"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Universal Symbolic Code Intelligence System (Obfuscated)',
        epilog='Copyright (c) 2025 Benny Harianto - Patent Pending'
    )
    parser.add_argument('directory', help='Directory to analyze')
    parser.add_argument('--output', choices=['json', 'markdown'], default='markdown')
    parser.add_argument('--save', help='Save report to file')
    
    args = parser.parse_args()
    
    print("🔮 Universal Symbolic Code Intelligence System")
    print("Copyright (c) 2025 Benny Harianto")
    print("Patent Pending - Proprietary Technology")
    print("=" * 50)
    
    analyzer = _SA()
    report = analyzer.analyze_directory(args.directory)
    
    if args.output == 'json':
        output = json.dumps(report, indent=2)
    else:
        output = _gmr(report)
    
    if args.save:
        with open(args.save, 'w') as f:
            f.write(output)
        print(f"Report saved to {args.save}")
    else:
        print(output)

if __name__ == '__main__':
    main()