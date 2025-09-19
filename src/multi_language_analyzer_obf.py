#!/usr/bin/env python3
"""
Multi-Language Universal Symbolic Code Intelligence System - Obfuscated
Copyright (c) 2025 Benny Harianto
Email: creatoropensource@gmail.com
LinkedIn: www.linkedin.com/in/bennyharianto-024868383
Patent Pending - Trade Secret Protected
"""

import os
import sys
import json
import re
import base64
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from collections import defaultdict

# Obfuscated symbols and constants
_SYM = {'A': '⟐', 'B': '⧈', 'C': '◈', 'D': '⟡'}
_KEYS = [0x2A3B, 0x4C5D, 0x6E7F, 0x8091]  # Obfuscated complexity keys
_LANG_PATTERNS = {
    'py': ['*.py'],
    'js': ['*.js', '*.jsx', '*.ts', '*.tsx'],
    'java': ['*.java'],
    'go': ['*.go'],
    'cs': ['*.cs'],
    'rs': ['*.rs'],
    'php': ['*.php'],
    'kt': ['*.kt']
}

@dataclass
class _EL:  # Element (obfuscated)
    fp: str    # file_path
    n: str     # name
    s: str     # symbol
    sn: str    # symbol_name
    ls: int    # line_start
    le: int    # line_end
    cs: int    # complexity_score
    d: str     # description
    c: str     # code_snippet
    l: str     # language
    f: str     # framework
    et: str    # element_type

class _LD:  # LanguageDetector (obfuscated)
    @staticmethod
    def detect_language(fp: str, content: str = "") -> str:
        """Detect programming language - PROPRIETARY ALGORITHM"""
        ext = Path(fp).suffix.lower()
        
        # Obfuscated language detection
        lang_map = {
            '.py': 'python',
            '.js': 'javascript', '.jsx': 'javascript',
            '.ts': 'typescript', '.tsx': 'typescript',
            '.java': 'java',
            '.go': 'go',
            '.cs': 'csharp',
            '.rs': 'rust',
            '.php': 'php',
            '.kt': 'kotlin'
        }
        
        base_lang = lang_map.get(ext, 'unknown')
        
        # Content-based detection (trade secret)
        if content and base_lang == 'unknown':
            return _LD._detect_by_content(content)
        
        return base_lang
    
    @staticmethod
    def _detect_by_content(content: str) -> str:
        """Content-based language detection - TRADE SECRET"""
        # Proprietary content analysis
        patterns = {
            'python': [r'def\s+\w+\(', r'import\s+\w+', r'from\s+\w+\s+import'],
            'javascript': [r'function\s+\w+\(', r'const\s+\w+\s*=', r'=>\s*{'],
            'java': [r'public\s+class\s+\w+', r'public\s+static\s+void\s+main'],
            'go': [r'func\s+\w+\(', r'package\s+\w+', r'import\s+\('],
        }
        
        scores = {}
        for lang, lang_patterns in patterns.items():
            score = sum(len(re.findall(pattern, content)) for pattern in lang_patterns)
            scores[lang] = score
        
        return max(scores, key=scores.get) if scores else 'unknown'

class _FA:  # FrameworkAnalyzer (obfuscated)
    @staticmethod
    def detect_framework(content: str, language: str) -> str:
        """Framework detection - PROPRIETARY ALGORITHM"""
        # Obfuscated framework patterns
        fw_patterns = {
            'python': {
                'django': [r'from\s+django', r'Django', r'models\.Model'],
                'flask': [r'from\s+flask', r'Flask\(', r'@app\.route'],
                'fastapi': [r'from\s+fastapi', r'FastAPI\(', r'@app\.(get|post)']
            },
            'javascript': {
                'react': [r'import.*React', r'useState', r'useEffect', r'jsx'],
                'express': [r'express\(\)', r'app\.get\(', r'app\.post\('],
                'nodejs': [r'require\(', r'module\.exports', r'process\.']
            },
            'java': {
                'spring': [r'@SpringBootApplication', r'@RestController', r'@Service'],
                'hibernate': [r'@Entity', r'@Table', r'SessionFactory']
            },
            'go': {
                'gin': [r'gin\.Default\(\)', r'gin\.Engine', r'c\.JSON\('],
                'gorilla': [r'mux\.NewRouter\(\)', r'gorilla/mux']
            }
        }
        
        if language not in fw_patterns:
            return 'none'
        
        for framework, patterns in fw_patterns[language].items():
            if any(re.search(pattern, content, re.IGNORECASE) for pattern in patterns):
                return framework
        
        return 'none'

class _LA:  # LanguageAnalyzer (obfuscated base class)
    def __init__(self, fp: str, content: str):
        self.fp = fp
        self.content = content
        self.lines = content.split('\n')
        self.language = _LD.detect_language(fp, content)
        self.framework = _FA.detect_framework(content, self.language)
        self._weights = self._load_weights()  # Trade secret weights
    
    def _load_weights(self) -> Dict[str, int]:
        """Load obfuscated complexity weights - TRADE SECRET"""
        return {
            'class': _KEYS[0] ^ 0x1111,
            'function': _KEYS[1] ^ 0x2222,
            'condition': _KEYS[2] ^ 0x3333,
            'loop': _KEYS[3] ^ 0x4444
        }
    
    def analyze(self) -> List[_EL]:
        """Analyze code - PROPRIETARY METHOD"""
        elements = []
        
        # Language-specific analysis
        if self.language == 'python':
            elements.extend(self._analyze_python())
        elif self.language in ['javascript', 'typescript']:
            elements.extend(self._analyze_javascript())
        elif self.language == 'java':
            elements.extend(self._analyze_java())
        elif self.language == 'go':
            elements.extend(self._analyze_go())
        else:
            elements.extend(self._analyze_generic())
        
        # Apply proprietary post-processing
        return self._post_process(elements)
    
    def _analyze_python(self) -> List[_EL]:
        """Python analysis - TRADE SECRET IMPLEMENTATION"""
        elements = []
        
        # Class detection
        for i, line in enumerate(self.lines):
            if re.match(r'^\s*class\s+(\w+)', line):
                match = re.match(r'^\s*class\s+(\w+)', line)
                if match:
                    elements.append(_EL(
                        fp=self.fp, n=match.group(1), s=_SYM['A'], sn='STRUCTURE',
                        ls=i+1, le=i+1, cs=self._calc_complexity(line, 'class'),
                        d=f"Python class {match.group(1)}", c=line.strip(),
                        l=self.language, f=self.framework, et='class'
                    ))
        
        # Function detection
        for i, line in enumerate(self.lines):
            if re.match(r'^\s*def\s+(\w+)', line):
                match = re.match(r'^\s*def\s+(\w+)', line)
                if match:
                    complexity = self._calc_complexity(line, 'function')
                    symbol = _SYM['C'] if complexity > 5 else _SYM['B']
                    symbol_name = 'DECISION' if complexity > 5 else 'FLOW'
                    
                    elements.append(_EL(
                        fp=self.fp, n=match.group(1), s=symbol, sn=symbol_name,
                        ls=i+1, le=i+1, cs=complexity,
                        d=f"Python function {match.group(1)}", c=line.strip(),
                        l=self.language, f=self.framework, et='function'
                    ))
        
        return elements
    
    def _analyze_javascript(self) -> List[_EL]:
        """JavaScript/TypeScript analysis - TRADE SECRET"""
        elements = []
        
        # Function detection
        patterns = [
            r'function\s+(\w+)\s*\(',
            r'const\s+(\w+)\s*=\s*\(',
            r'(\w+)\s*:\s*function\s*\(',
            r'(\w+)\s*=>\s*{'
        ]
        
        for i, line in enumerate(self.lines):
            for pattern in patterns:
                match = re.search(pattern, line)
                if match:
                    name = match.group(1)
                    complexity = self._calc_complexity(line, 'function')
                    
                    elements.append(_EL(
                        fp=self.fp, n=name, s=_SYM['B'], sn='FLOW',
                        ls=i+1, le=i+1, cs=complexity,
                        d=f"JavaScript function {name}", c=line.strip(),
                        l=self.language, f=self.framework, et='function'
                    ))
                    break
        
        return elements
    
    def _analyze_java(self) -> List[_EL]:
        """Java analysis - TRADE SECRET"""
        elements = []
        
        # Class detection
        for i, line in enumerate(self.lines):
            match = re.search(r'class\s+(\w+)', line)
            if match:
                elements.append(_EL(
                    fp=self.fp, n=match.group(1), s=_SYM['A'], sn='STRUCTURE',
                    ls=i+1, le=i+1, cs=self._calc_complexity(line, 'class'),
                    d=f"Java class {match.group(1)}", c=line.strip(),
                    l=self.language, f=self.framework, et='class'
                ))
        
        # Method detection
        for i, line in enumerate(self.lines):
            match = re.search(r'(public|private|protected).*\s+(\w+)\s*\(', line)
            if match and 'class' not in line:
                method_name = match.group(2)
                complexity = self._calc_complexity(line, 'function')
                
                elements.append(_EL(
                    fp=self.fp, n=method_name, s=_SYM['B'], sn='FLOW',
                    ls=i+1, le=i+1, cs=complexity,
                    d=f"Java method {method_name}", c=line.strip(),
                    l=self.language, f=self.framework, et='method'
                ))
        
        return elements
    
    def _analyze_go(self) -> List[_EL]:
        """Go analysis - TRADE SECRET"""
        elements = []
        
        # Function detection
        for i, line in enumerate(self.lines):
            match = re.search(r'func\s+(\w+)\s*\(', line)
            if match:
                func_name = match.group(1)
                complexity = self._calc_complexity(line, 'function')
                
                elements.append(_EL(
                    fp=self.fp, n=func_name, s=_SYM['B'], sn='FLOW',
                    ls=i+1, le=i+1, cs=complexity,
                    d=f"Go function {func_name}", c=line.strip(),
                    l=self.language, f=self.framework, et='function'
                ))
        
        # Struct detection
        for i, line in enumerate(self.lines):
            match = re.search(r'type\s+(\w+)\s+struct', line)
            if match:
                struct_name = match.group(1)
                elements.append(_EL(
                    fp=self.fp, n=struct_name, s=_SYM['A'], sn='STRUCTURE',
                    ls=i+1, le=i+1, cs=self._calc_complexity(line, 'class'),
                    d=f"Go struct {struct_name}", c=line.strip(),
                    l=self.language, f=self.framework, et='struct'
                ))
        
        return elements
    
    def _analyze_generic(self) -> List[_EL]:
        """Generic analysis for unsupported languages"""
        elements = []
        
        # Basic pattern detection
        for i, line in enumerate(self.lines):
            if len(line.strip()) > 50:  # Complex lines
                elements.append(_EL(
                    fp=self.fp, n=f"complex_line_{i+1}", s=_SYM['C'], sn='DECISION',
                    ls=i+1, le=i+1, cs=3,
                    d="Complex code line", c=line.strip(),
                    l=self.language, f=self.framework, et='line'
                ))
        
        return elements
    
    def _calc_complexity(self, line: str, element_type: str) -> int:
        """Calculate complexity - PROPRIETARY ALGORITHM"""
        base = 1
        
        # Complexity indicators (trade secret)
        indicators = {
            'if': 2, 'else': 1, 'elif': 2, 'while': 2, 'for': 2,
            'try': 2, 'catch': 2, 'switch': 3, 'case': 1,
            '&&': 1, '||': 1, 'and': 1, 'or': 1
        }
        
        for indicator, weight in indicators.items():
            base += line.lower().count(indicator) * weight
        
        # Element type modifier (trade secret)
        type_modifier = {
            'class': self._weights['class'] >> 12,
            'function': self._weights['function'] >> 13,
            'method': self._weights['function'] >> 13
        }.get(element_type, 1)
        
        return min(base * type_modifier, 20)  # Max complexity 20
    
    def _post_process(self, elements: List[_EL]) -> List[_EL]:
        """Post-process elements - PROPRIETARY ENHANCEMENT"""
        # Mark high complexity as IMPACT
        for element in elements:
            if element.cs > 8:
                element.s = _SYM['D']
                element.sn = 'IMPACT'
                element.d += " - HIGH IMPACT"
        
        return elements

class _MLA:  # MultiLanguageAnalyzer (obfuscated)
    def __init__(self):
        self.elements: List[_EL] = []
        self.file_stats: Dict[str, int] = {}
        self.language_stats: Dict[str, int] = {}
        self._config = self._load_config()  # Trade secret config
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration - TRADE SECRET"""
        return {
            'max_files': 10000,
            'max_file_size': 1024 * 1024,  # 1MB
            'supported_languages': list(_LANG_PATTERNS.keys()),
            'analysis_signature': self._generate_signature()
        }
    
    def _generate_signature(self) -> str:
        """Generate analysis signature - TRADE SECRET"""
        data = f"MLA-{sum(_KEYS)}-2025-BH"
        return base64.b64encode(data.encode()).decode()[:16]
    
    def analyze_directory(self, directory: str) -> Dict[str, Any]:
        """Analyze directory - PROPRIETARY COORDINATION"""
        self.elements = []
        self.file_stats = {}
        self.language_stats = {}
        
        # Find all supported files
        files = self._find_files(directory)
        
        print(f"🔮 Found {len(files)} files to analyze")
        
        # Analyze each file
        for file_path in files:
            try:
                self._analyze_file(file_path)
            except Exception as e:
                print(f"Error analyzing {file_path}: {e}")
        
        return self._generate_report()
    
    def _find_files(self, directory: str) -> List[str]:
        """Find supported files - OPTIMIZED SEARCH"""
        files = []
        directory_path = Path(directory)
        
        for lang_patterns in _LANG_PATTERNS.values():
            for pattern in lang_patterns:
                files.extend(directory_path.rglob(pattern))
        
        # Filter and convert to strings
        valid_files = []
        for file_path in files:
            if file_path.is_file() and file_path.stat().st_size < self._config['max_file_size']:
                valid_files.append(str(file_path))
        
        return valid_files[:self._config['max_files']]
    
    def _analyze_file(self, file_path: str) -> None:
        """Analyze single file - PROPRIETARY PROCESSING"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read()
            except Exception:
                return
        except Exception:
            return
        
        # Analyze with language-specific analyzer
        analyzer = _LA(file_path, content)
        elements = analyzer.analyze()
        
        # Add to results
        self.elements.extend(elements)
        self.file_stats[file_path] = len(elements)
        
        # Update language stats
        if analyzer.language != 'unknown':
            self.language_stats[analyzer.language] = self.language_stats.get(analyzer.language, 0) + 1
    
    def _generate_report(self) -> Dict[str, Any]:
        """Generate comprehensive report - PROPRIETARY AGGREGATION"""
        # Calculate statistics
        total_elements = len(self.elements)
        files_analyzed = len(self.file_stats)
        
        # Symbol distribution
        symbol_counts = defaultdict(int)
        for element in self.elements:
            symbol_counts[element.sn] += 1
        
        # Language distribution
        language_counts = defaultdict(int)
        framework_counts = defaultdict(int)
        
        for element in self.elements:
            language_counts[element.l] += 1
            if element.f != 'none':
                framework_counts[element.f] += 1
        
        # High impact analysis
        high_impact = [e for e in self.elements if e.sn == 'IMPACT']
        
        return {
            'summary': {
                'total_elements': total_elements,
                'files_analyzed': files_analyzed,
                'languages_detected': len(self.language_stats),
                'frameworks_detected': len([f for f in framework_counts.keys() if f != 'none']),
                'symbol_distribution': dict(symbol_counts),
                'language_distribution': dict(language_counts),
                'framework_distribution': dict(framework_counts),
                'high_impact_count': len(high_impact),
                'analysis_signature': self._config['analysis_signature']
            },
            'elements': [asdict(e) for e in self.elements],
            'file_stats': self.file_stats,
            'language_stats': self.language_stats,
            'metadata': {
                'analyzer_version': '2.0.0-obf-ml',
                'copyright': 'Benny Harianto 2025',
                'patent_pending': True,
                'trade_secret_protected': True
            }
        }

def generate_markdown_report(report: Dict[str, Any]) -> str:
    """Generate markdown report - ENHANCED FORMATTING"""
    summary = report['summary']
    
    md = []
    md.append("# 🔮 Multi-Language Universal Symbolic Code Analysis Report")
    md.append("**Copyright (c) 2025 Benny Harianto - Patent Pending**")
    md.append("**Email**: creatoropensource@gmail.com")
    md.append("**LinkedIn**: www.linkedin.com/in/bennyharianto-024868383\n")
    
    # Executive Summary
    md.append("## 📊 Executive Summary\n")
    md.append(f"- **Total Elements Analyzed**: {summary['total_elements']:,}")
    md.append(f"- **Files Processed**: {summary['files_analyzed']:,}")
    md.append(f"- **Programming Languages**: {summary['languages_detected']}")
    md.append(f"- **Frameworks Detected**: {summary['frameworks_detected']}")
    md.append(f"- **High Impact Elements**: {summary['high_impact_count']}")
    md.append(f"- **Analysis Signature**: `{summary.get('analysis_signature', 'N/A')}`\n")
    
    # Language Distribution
    md.append("## 🌍 Programming Language Distribution\n")
    lang_dist = summary.get('language_distribution', {})
    total_lang_elements = sum(lang_dist.values())
    
    for language, count in sorted(lang_dist.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_lang_elements * 100) if total_lang_elements > 0 else 0
        md.append(f"- **{language.title()}**: {count:,} elements ({percentage:.1f}%)")
    md.append("")
    
    # Framework Distribution
    framework_dist = summary.get('framework_distribution', {})
    if framework_dist:
        md.append("## 🔧 Framework Distribution\n")
        for framework, count in sorted(framework_dist.items(), key=lambda x: x[1], reverse=True):
            md.append(f"- **{framework.title()}**: {count:,} elements")
        md.append("")
    
    # Symbol Distribution
    md.append("## 🎯 Universal Symbol Distribution\n")
    symbol_dist = summary.get('symbol_distribution', {})
    total_symbols = sum(symbol_dist.values())
    
    for symbol_name, count in symbol_dist.items():
        symbol = _SYM.get(symbol_name[0], '?')
        percentage = (count / total_symbols * 100) if total_symbols > 0 else 0
        md.append(f"- {symbol} **{symbol_name}**: {count:,} ({percentage:.1f}%)")
    md.append("")
    
    # Top Elements by Symbol
    elements = report.get('elements', [])
    
    for symbol_name in ['IMPACT', 'DECISION', 'FLOW', 'STRUCTURE']:
        symbol_elements = [e for e in elements if e.get('sn') == symbol_name]
        
        if symbol_elements:
            symbol = _SYM.get(symbol_name[0], '?')
            md.append(f"## {symbol} Top {symbol_name} Elements\n")
            
            # Sort by complexity and show top 10
            top_elements = sorted(symbol_elements, key=lambda x: x.get('cs', 0), reverse=True)[:10]
            
            for i, element in enumerate(top_elements, 1):
                name = element.get('n', 'Unknown')
                complexity = element.get('cs', 0)
                language = element.get('l', 'unknown')
                framework = element.get('f', 'none')
                file_path = element.get('fp', '')
                
                md.append(f"### {i}. {name} (Complexity: {complexity})")
                md.append(f"- **Language**: {language.title()}")
                if framework != 'none':
                    md.append(f"- **Framework**: {framework.title()}")
                md.append(f"- **File**: `{file_path}`")
                md.append(f"- **Type**: {element.get('et', 'unknown').title()}")
                md.append(f"- **Description**: {element.get('d', '')}")
                
                # Code snippet
                code = element.get('c', '')
                if code:
                    md.append(f"```{language}")
                    md.append(code[:200] + "..." if len(code) > 200 else code)
                    md.append("```")
                md.append("")
    
    # Footer
    md.append("---")
    md.append("## 📞 Contact Information")
    md.append("- **Creator**: Benny Harianto")
    md.append("- **Email**: creatoropensource@gmail.com")
    md.append("- **LinkedIn**: [www.linkedin.com/in/bennyharianto-024868383](https://www.linkedin.com/in/bennyharianto-024868383)")
    md.append("- **Patent Status**: Pending")
    md.append("- **License**: MIT with Commercial Licensing Available")
    md.append("")
    md.append("*Generated by Universal Symbolic Code Intelligence System*")
    md.append("*Proprietary Multi-Language Analysis Technology*")
    md.append("*Trade Secret Protected Algorithms*")
    
    return '\n'.join(md)

def main():
    """Main entry point - OBFUSCATED MULTI-LANGUAGE ANALYZER"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Multi-Language Universal Symbolic Code Intelligence System',
        epilog='Copyright (c) 2025 Benny Harianto - Patent Pending'
    )
    parser.add_argument('directory', help='Directory to analyze')
    parser.add_argument('--output', choices=['json', 'markdown'], default='markdown')
    parser.add_argument('--save', help='Save report to file')
    
    args = parser.parse_args()
    
    print("🔮 Multi-Language Universal Symbolic Code Intelligence System")
    print("Copyright (c) 2025 Benny Harianto")
    print("Email: creatoropensource@gmail.com")
    print("LinkedIn: www.linkedin.com/in/bennyharianto-024868383")
    print("Patent Pending - Trade Secret Protected")
    print("=" * 60)
    
    analyzer = _MLA()
    report = analyzer.analyze_directory(args.directory)
    
    if args.output == 'json':
        output = json.dumps(report, indent=2)
    else:
        output = generate_markdown_report(report)
    
    if args.save:
        with open(args.save, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"\n✅ Report saved to {args.save}")
    else:
        print("\n" + output)

if __name__ == '__main__':
    main()