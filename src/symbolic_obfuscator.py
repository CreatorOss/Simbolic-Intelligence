#!/usr/bin/env python3
"""
Symbolic Obfuscator - Universal Code Protection System
Uses our four universal symbols (⟐⧈◈⟡) for advanced obfuscation

This obfuscator provides multiple layers of protection:
1. Symbol-based variable renaming
2. Control flow obfuscation
3. String encryption
4. Dead code insertion
5. Function signature obfuscation
"""

import ast
import base64
import random
import string
import hashlib
import zlib
from typing import Dict, List, Set, Any, Optional
import re

# Universal Symbols for Obfuscation
SYMBOLS = {
    'STRUCTURE': '⟐',  # For class/structure obfuscation
    'FLOW': '⧈',       # For function/flow obfuscation
    'DECISION': '◈',   # For conditional obfuscation
    'IMPACT': '⟡'      # For critical/impact obfuscation
}

class SymbolicObfuscator:
    """
    Advanced obfuscator using symbolic intelligence patterns
    """
    
    def __init__(self, obfuscation_level: int = 3):
        self.obfuscation_level = obfuscation_level  # 1-5 scale
        self.symbol_map: Dict[str, str] = {}
        self.string_map: Dict[str, str] = {}
        self.function_map: Dict[str, str] = {}
        self.class_map: Dict[str, str] = {}
        self.variable_map: Dict[str, str] = {}
        self.reserved_names = {
            'self', 'cls', '__init__', '__new__', '__del__', '__str__', '__repr__',
            'True', 'False', 'None', 'and', 'or', 'not', 'if', 'else', 'elif',
            'for', 'while', 'def', 'class', 'import', 'from', 'as', 'try',
            'except', 'finally', 'with', 'lambda', 'return', 'yield', 'break',
            'continue', 'pass', 'global', 'nonlocal', 'assert', 'del', 'is',
            'in', 'raise'
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
            
            if self.obfuscation_level >= 5:
                tree = self._advanced_obfuscation(tree)
            
            # Convert back to source
            obfuscated_code = ast.unparse(tree)
            
            # Add symbolic header
            header = self._generate_symbolic_header()
            
            return header + "\n\n" + obfuscated_code
            
        except Exception as e:
            print(f"Obfuscation error: {e}")
            return source_code
    
    def _generate_symbolic_header(self) -> str:
        """Generate symbolic protection header"""
        symbols = ''.join(SYMBOLS.values())
        encoded_symbols = base64.b64encode(symbols.encode()).decode()
        
        return f'''# {symbols} SYMBOLIC INTELLIGENCE PROTECTION {symbols}
# Protected by Universal Symbolic Obfuscation System
# Symbols: {encoded_symbols}
# Level: {self.obfuscation_level}
# Warning: Reverse engineering is protected by symbolic intelligence
{symbols * 3}'''
    
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
                    not node.id.startswith('__')):
                    
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
            
            def visit_Str(self, node):
                # Encode string using symbolic method
                encoded = self.parent._encode_string_symbolically(node.s)
                
                # Create decoder call
                decoder_call = ast.Call(
                    func=ast.Name(id=self.parent._get_decoder_name(), ctx=ast.Load()),
                    args=[ast.Str(s=encoded)],
                    keywords=[]
                )
                
                return decoder_call
            
            def visit_Constant(self, node):
                if isinstance(node.value, str) and len(node.value) > 2:
                    # Encode string using symbolic method
                    encoded = self.parent._encode_string_symbolically(node.value)
                    
                    # Create decoder call
                    decoder_call = ast.Call(
                        func=ast.Name(id=self.parent._get_decoder_name(), ctx=ast.Load()),
                        args=[ast.Constant(value=encoded)],
                        keywords=[]
                    )
                    
                    return decoder_call
                return node
        
        # Add decoder function to the tree
        decoder_func = self._create_symbolic_decoder()
        if isinstance(tree, ast.Module):
            tree.body.insert(0, decoder_func)
        
        transformer = StringObfuscator(self)
        return transformer.visit(tree)
    
    def _obfuscate_control_flow(self, tree: ast.AST) -> ast.AST:
        """Obfuscate control flow using symbolic patterns"""
        
        class ControlFlowObfuscator(ast.NodeTransformer):
            def __init__(self, parent):
                self.parent = parent
            
            def visit_If(self, node):
                # Add symbolic dummy conditions
                if random.random() < 0.3:  # 30% chance
                    dummy_var = self.parent._generate_symbolic_name('IMPACT', 'dummy')
                    
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
                    
                    # Insert dummy assignment before if statement
                    return [dummy_assign, self.generic_visit(node)]
                
                return self.generic_visit(node)
            
            def visit_For(self, node):
                # Add symbolic loop obfuscation
                if random.random() < 0.2:  # 20% chance
                    counter_var = self.parent._generate_symbolic_name('FLOW', 'counter')
                    
                    # Add counter initialization
                    counter_init = ast.Assign(
                        targets=[ast.Name(id=counter_var, ctx=ast.Store())],
                        value=ast.Constant(value=0)
                    )
                    
                    # Add counter increment in loop body
                    counter_incr = ast.AugAssign(
                        target=ast.Name(id=counter_var, ctx=ast.Store()),
                        op=ast.Add(),
                        value=ast.Constant(value=1)
                    )
                    
                    node.body.insert(0, counter_incr)
                    
                    return [counter_init, self.generic_visit(node)]
                
                return self.generic_visit(node)
        
        transformer = ControlFlowObfuscator(self)
        result = transformer.visit(tree)
        
        # Handle case where transformer returns a list
        if isinstance(result, list):
            if isinstance(tree, ast.Module):
                new_body = []
                for item in result:
                    if isinstance(item, list):
                        new_body.extend(item)
                    else:
                        new_body.append(item)
                tree.body = new_body
                return tree
        
        return result
    
    def _insert_dead_code(self, tree: ast.AST) -> ast.AST:
        """Insert symbolic dead code for confusion"""
        
        class DeadCodeInserter(ast.NodeTransformer):
            def __init__(self, parent):
                self.parent = parent
            
            def visit_Module(self, node):
                new_body = []
                
                for stmt in node.body:
                    new_body.append(stmt)
                    
                    # 20% chance to insert dead code after each statement
                    if random.random() < 0.2:
                        dead_code = self.parent._generate_dead_code()
                        new_body.extend(dead_code)
                
                node.body = new_body
                return node
        
        transformer = DeadCodeInserter(self)
        return transformer.visit(tree)
    
    def _advanced_obfuscation(self, tree: ast.AST) -> ast.AST:
        """Advanced obfuscation techniques"""
        
        class AdvancedObfuscator(ast.NodeTransformer):
            def __init__(self, parent):
                self.parent = parent
            
            def visit_BinOp(self, node):
                # Obfuscate simple arithmetic operations
                if isinstance(node.op, ast.Add) and random.random() < 0.3:
                    # Replace a + b with (a - (-b))
                    new_node = ast.BinOp(
                        left=node.left,
                        op=ast.Sub(),
                        right=ast.UnaryOp(op=ast.USub(), operand=node.right)
                    )
                    return self.generic_visit(new_node)
                
                return self.generic_visit(node)
            
            def visit_Compare(self, node):
                # Obfuscate comparisons
                if (len(node.ops) == 1 and 
                    isinstance(node.ops[0], ast.Eq) and 
                    random.random() < 0.2):
                    
                    # Replace a == b with not (a != b)
                    new_node = ast.UnaryOp(
                        op=ast.Not(),
                        operand=ast.Compare(
                            left=node.left,
                            ops=[ast.NotEq()],
                            comparators=node.comparators
                        )
                    )
                    return self.generic_visit(new_node)
                
                return self.generic_visit(node)
        
        transformer = AdvancedObfuscator(self)
        return transformer.visit(tree)
    
    def _generate_symbolic_name(self, symbol_type: str, original_name: str) -> str:
        """Generate obfuscated name using symbols"""
        symbol = SYMBOLS[symbol_type]
        
        # Create hash of original name
        name_hash = hashlib.md5(original_name.encode()).hexdigest()[:8]
        
        # Generate symbolic name
        if symbol_type == 'STRUCTURE':
            prefix = f"{symbol}S"
        elif symbol_type == 'FLOW':
            prefix = f"{symbol}F"
        elif symbol_type == 'DECISION':
            prefix = f"{symbol}D"
        else:  # IMPACT
            prefix = f"{symbol}I"
        
        # Combine with hash and random suffix
        random_suffix = ''.join(random.choices(string.ascii_letters, k=4))
        
        return f"{prefix}_{name_hash}_{random_suffix}"
    
    def _encode_string_symbolically(self, text: str) -> str:
        """Encode string using symbolic method"""
        # Convert to bytes
        text_bytes = text.encode('utf-8')
        
        # Compress
        compressed = zlib.compress(text_bytes)
        
        # Base64 encode
        encoded = base64.b64encode(compressed).decode()
        
        # Add symbolic markers
        symbols = ''.join(SYMBOLS.values())
        return f"{symbols[0]}{encoded}{symbols[-1]}"
    
    def _get_decoder_name(self) -> str:
        """Get symbolic decoder function name"""
        if not hasattr(self, '_decoder_name'):
            self._decoder_name = self._generate_symbolic_name('IMPACT', 'decoder')
        return self._decoder_name
    
    def _create_symbolic_decoder(self) -> ast.FunctionDef:
        """Create symbolic string decoder function"""
        decoder_name = self._get_decoder_name()
        
        # Create decoder function
        decoder_code = f'''
def {decoder_name}(encoded_str):
    import base64, zlib
    symbols = "{''.join(SYMBOLS.values())}"
    if encoded_str.startswith(symbols[0]) and encoded_str.endswith(symbols[-1]):
        clean_str = encoded_str[1:-1]
        decoded_bytes = base64.b64decode(clean_str.encode())
        decompressed = zlib.decompress(decoded_bytes)
        return decompressed.decode('utf-8')
    return encoded_str
'''
        
        return ast.parse(decoder_code).body[0]
    
    def _generate_dead_code(self) -> List[ast.stmt]:
        """Generate symbolic dead code"""
        dead_statements = []
        
        # Random variable assignment
        var_name = self._generate_symbolic_name('DECISION', 'dead')
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
                    targets=[ast.Name(id=self._generate_symbolic_name('FLOW', 'fake'), ctx=ast.Store())],
                    value=ast.Constant(value="fake")
                )
            ],
            orelse=[]
        )
        dead_statements.append(never_true)
        
        return dead_statements

def obfuscate_file(input_file: str, output_file: str, level: int = 3) -> bool:
    """
    Obfuscate a Python file using symbolic obfuscation
    """
    try:
        # Read source file
        with open(input_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Create obfuscator
        obfuscator = SymbolicObfuscator(obfuscation_level=level)
        
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
    Main obfuscation utility
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Symbolic Code Obfuscator')
    parser.add_argument('input', help='Input Python file')
    parser.add_argument('output', help='Output obfuscated file')
    parser.add_argument('--level', type=int, default=3, choices=[1,2,3,4,5],
                       help='Obfuscation level (1-5)')
    
    args = parser.parse_args()
    
    print("🔮 Symbolic Intelligence Obfuscator")
    print("=" * 50)
    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print(f"Level: {args.level}")
    print()
    
    success = obfuscate_file(args.input, args.output, args.level)
    
    if success:
        print("\n🎉 Obfuscation completed successfully!")
        print("   Your code is now protected by symbolic intelligence!")
    else:
        print("\n❌ Obfuscation failed!")

if __name__ == '__main__':
    main()