#!/usr/bin/env python3
"""
Symbolic Obfuscator V2 - Enhanced Universal Code Protection
Uses ASCII-safe symbolic patterns for maximum compatibility
"""

import ast
import base64
import random
import string
import hashlib
import zlib
import re
from typing import Dict, List, Set, Any, Optional

class SymbolicObfuscatorV2:
    """
    Enhanced obfuscator with ASCII-safe symbolic patterns
    """
    
    def __init__(self, obfuscation_level: int = 3):
        self.obfuscation_level = obfuscation_level
        self.symbol_map: Dict[str, str] = {}
        self.string_map: Dict[str, str] = {}
        self.function_map: Dict[str, str] = {}
        self.class_map: Dict[str, str] = {}
        self.variable_map: Dict[str, str] = {}
        
        # ASCII-safe symbolic patterns
        self.symbol_patterns = {
            'STRUCTURE': 'SYM_S',  # Structure symbol
            'FLOW': 'SYM_F',       # Flow symbol  
            'DECISION': 'SYM_D',   # Decision symbol
            'IMPACT': 'SYM_I'      # Impact symbol
        }
        
        self.reserved_names = {
            'self', 'cls', '__init__', '__new__', '__del__', '__str__', '__repr__',
            'True', 'False', 'None', 'and', 'or', 'not', 'if', 'else', 'elif',
            'for', 'while', 'def', 'class', 'import', 'from', 'as', 'try',
            'except', 'finally', 'with', 'lambda', 'return', 'yield', 'break',
            'continue', 'pass', 'global', 'nonlocal', 'assert', 'del', 'is',
            'in', 'raise', 'main', 'print', 'len', 'range', 'str', 'int',
            'float', 'list', 'dict', 'tuple', 'set'
        }
        
    def obfuscate_python_code(self, source_code: str) -> str:
        """
        Main obfuscation method for Python code
        """
        try:
            # Parse AST
            tree = ast.parse(source_code)
            
            # Apply obfuscation transformations
            if self.obfuscation_level >= 1:
                tree = self._obfuscate_names(tree)
            
            if self.obfuscation_level >= 2:
                tree = self._obfuscate_strings(tree)
            
            if self.obfuscation_level >= 3:
                tree = self._obfuscate_control_flow(tree)
            
            if self.obfuscation_level >= 4:
                tree = self._insert_dead_code(tree)
            
            # Convert back to source
            obfuscated_code = ast.unparse(tree)
            
            # Add symbolic header
            header = self._generate_symbolic_header()
            
            return header + "\n\n" + obfuscated_code
            
        except Exception as e:
            print(f"Obfuscation error: {e}")
            # Return original code with basic protection
            return self._add_basic_protection(source_code)
    
    def _add_basic_protection(self, source_code: str) -> str:
        """Add basic protection when AST parsing fails"""
        header = self._generate_symbolic_header()
        
        # Basic string obfuscation using regex
        protected_code = self._basic_string_obfuscation(source_code)
        
        return header + "\n\n" + protected_code
    
    def _basic_string_obfuscation(self, code: str) -> str:
        """Basic string obfuscation using regex"""
        def encode_string(match):
            string_content = match.group(1)
            if len(string_content) > 2:
                encoded = base64.b64encode(string_content.encode()).decode()
                return f'base64.b64decode("{encoded}").decode()'
            return match.group(0)
        
        # Add import for base64
        if 'import base64' not in code:
            code = 'import base64\n' + code
        
        # Replace string literals
        code = re.sub(r'"([^"]{3,})"', encode_string, code)
        code = re.sub(r"'([^']{3,})'", encode_string, code)
        
        return code
    
    def _generate_symbolic_header(self) -> str:
        """Generate symbolic protection header"""
        symbols = 'SYM_S_SYM_F_SYM_D_SYM_I'
        encoded_symbols = base64.b64encode(symbols.encode()).decode()
        
        return f'''# {symbols} SYMBOLIC INTELLIGENCE PROTECTION {symbols}
# Protected by Universal Symbolic Obfuscation System V2
# Symbols: {encoded_symbols}
# Level: {self.obfuscation_level}
# Warning: Reverse engineering is protected by symbolic intelligence
# {symbols}'''
    
    def _obfuscate_names(self, tree: ast.AST) -> ast.AST:
        """Obfuscate variable, function, and class names using symbols"""
        
        class NameObfuscator(ast.NodeTransformer):
            def __init__(self, parent):
                self.parent = parent
            
            def visit_FunctionDef(self, node):
                if node.name not in self.parent.reserved_names:
                    new_name = self.parent._generate_symbolic_name('FLOW', node.name)
                    self.parent.function_map[node.name] = new_name
                    node.name = new_name
                return self.generic_visit(node)
            
            def visit_ClassDef(self, node):
                if node.name not in self.parent.reserved_names:
                    new_name = self.parent._generate_symbolic_name('STRUCTURE', node.name)
                    self.parent.class_map[node.name] = new_name
                    node.name = new_name
                return self.generic_visit(node)
            
            def visit_Name(self, node):
                if (isinstance(node.ctx, ast.Store) and 
                    node.id not in self.parent.reserved_names and
                    not node.id.startswith('__') and
                    not node.id.startswith('SYM_')):
                    
                    if node.id not in self.parent.variable_map:
                        new_name = self.parent._generate_symbolic_name('DECISION', node.id)
                        self.parent.variable_map[node.id] = new_name
                    node.id = self.parent.variable_map[node.id]
                
                elif (isinstance(node.ctx, ast.Load) and 
                      node.id in self.parent.variable_map):
                    node.id = self.parent.variable_map[node.id]
                
                return node
        
        transformer = NameObfuscator(self)
        return transformer.visit(tree)
    
    def _obfuscate_strings(self, tree: ast.AST) -> ast.AST:
        """Obfuscate string literals using symbolic encoding"""
        
        class StringObfuscator(ast.NodeTransformer):
            def __init__(self, parent):
                self.parent = parent
            
            def visit_Constant(self, node):
                if isinstance(node.value, str) and len(node.value) > 3:
                    # Skip docstrings and very short strings
                    if not (hasattr(node, 'parent') and 
                           isinstance(getattr(node, 'parent', None), ast.Expr)):
                        
                        # Encode string using base64
                        encoded = base64.b64encode(node.value.encode()).decode()
                        
                        # Create decoder call
                        decoder_call = ast.Call(
                            func=ast.Attribute(
                                value=ast.Attribute(
                                    value=ast.Name(id='base64', ctx=ast.Load()),
                                    attr='b64decode',
                                    ctx=ast.Load()
                                ),
                                attr='decode',
                                ctx=ast.Load()
                            ),
                            args=[ast.Constant(value=encoded)],
                            keywords=[]
                        )
                        
                        return decoder_call
                return node
        
        # Add base64 import to the tree
        import_base64 = ast.Import(names=[ast.alias(name='base64', asname=None)])
        if isinstance(tree, ast.Module):
            tree.body.insert(0, import_base64)
        
        transformer = StringObfuscator(self)
        return transformer.visit(tree)
    
    def _obfuscate_control_flow(self, tree: ast.AST) -> ast.AST:
        """Obfuscate control flow using symbolic patterns"""
        
        class ControlFlowObfuscator(ast.NodeTransformer):
            def __init__(self, parent):
                self.parent = parent
                self.dummy_counter = 0
            
            def visit_If(self, node):
                # Add symbolic dummy conditions occasionally
                if random.random() < 0.2:  # 20% chance
                    self.dummy_counter += 1
                    dummy_var = f"SYM_D_dummy_{self.dummy_counter}"
                    
                    # Create dummy assignment
                    dummy_assign = ast.Assign(
                        targets=[ast.Name(id=dummy_var, ctx=ast.Store())],
                        value=ast.Constant(value=True)
                    )
                    
                    # Wrap original condition with dummy check
                    new_condition = ast.BoolOp(
                        op=ast.And(),
                        values=[
                            ast.Name(id=dummy_var, ctx=ast.Load()),
                            node.test
                        ]
                    )
                    
                    node.test = new_condition
                    
                    # Return both statements
                    return [dummy_assign, self.generic_visit(node)]
                
                return self.generic_visit(node)
        
        transformer = ControlFlowObfuscator(self)
        result = transformer.visit(tree)
        
        # Handle case where transformer returns a list
        if isinstance(result, list) and isinstance(tree, ast.Module):
            new_body = []
            for item in tree.body:
                if isinstance(item, list):
                    new_body.extend(item)
                else:
                    new_body.append(item)
            tree.body = new_body
        
        return tree
    
    def _insert_dead_code(self, tree: ast.AST) -> ast.AST:
        """Insert symbolic dead code for confusion"""
        
        class DeadCodeInserter(ast.NodeTransformer):
            def __init__(self, parent):
                self.parent = parent
                self.dead_counter = 0
            
            def visit_Module(self, node):
                new_body = []
                
                for stmt in node.body:
                    new_body.append(stmt)
                    
                    # 15% chance to insert dead code after each statement
                    if random.random() < 0.15:
                        dead_code = self.parent._generate_dead_code()
                        new_body.extend(dead_code)
                
                node.body = new_body
                return node
        
        transformer = DeadCodeInserter(self)
        return transformer.visit(tree)
    
    def _generate_symbolic_name(self, symbol_type: str, original_name: str) -> str:
        """Generate obfuscated name using ASCII-safe symbols"""
        pattern = self.symbol_patterns[symbol_type]
        
        # Create hash of original name
        name_hash = hashlib.md5(original_name.encode()).hexdigest()[:6]
        
        # Generate symbolic name
        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
        
        return f"{pattern}_{name_hash}_{random_suffix}"
    
    def _generate_dead_code(self) -> List[ast.stmt]:
        """Generate symbolic dead code"""
        dead_statements = []
        
        # Random variable assignment
        var_name = f"SYM_D_dead_{random.randint(1000, 9999)}"
        dead_assign = ast.Assign(
            targets=[ast.Name(id=var_name, ctx=ast.Store())],
            value=ast.Constant(value=random.randint(1, 100))
        )
        dead_statements.append(dead_assign)
        
        # Conditional that never executes
        never_true = ast.If(
            test=ast.Compare(
                left=ast.Constant(value=1),
                ops=[ast.Eq()],
                comparators=[ast.Constant(value=0)]
            ),
            body=[
                ast.Assign(
                    targets=[ast.Name(id=f"SYM_F_fake_{random.randint(100, 999)}", ctx=ast.Store())],
                    value=ast.Constant(value="fake_data")
                )
            ],
            orelse=[]
        )
        dead_statements.append(never_true)
        
        return dead_statements

def obfuscate_file_v2(input_file: str, output_file: str, level: int = 3) -> bool:
    """
    Obfuscate a Python file using symbolic obfuscation V2
    """
    try:
        # Read source file
        with open(input_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Create obfuscator
        obfuscator = SymbolicObfuscatorV2(obfuscation_level=level)
        
        # Obfuscate code
        obfuscated_code = obfuscator.obfuscate_python_code(source_code)
        
        # Write obfuscated file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(obfuscated_code)
        
        print(f"✅ Successfully obfuscated {input_file} -> {output_file}")
        print(f"   Obfuscation level: {level}")
        print(f"   Functions renamed: {len(obfuscator.function_map)}")
        print(f"   Classes renamed: {len(obfuscator.class_map)}")
        print(f"   Variables renamed: {len(obfuscator.variable_map)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error obfuscating {input_file}: {e}")
        return False

def main():
    """
    Main obfuscation utility V2
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Symbolic Code Obfuscator V2')
    parser.add_argument('input', help='Input Python file')
    parser.add_argument('output', help='Output obfuscated file')
    parser.add_argument('--level', type=int, default=3, choices=[1,2,3,4,5],
                       help='Obfuscation level (1-5)')
    
    args = parser.parse_args()
    
    print("🔮 Symbolic Intelligence Obfuscator V2")
    print("=" * 50)
    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print(f"Level: {args.level}")
    print()
    
    success = obfuscate_file_v2(args.input, args.output, args.level)
    
    if success:
        print("\n🎉 Obfuscation completed successfully!")
        print("   Your code is now protected by symbolic intelligence!")
    else:
        print("\n❌ Obfuscation failed!")

if __name__ == '__main__':
    main()