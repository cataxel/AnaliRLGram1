import parsimonious
from parsimonious.grammar import Grammar

# Definición de la gramática
grammar = Grammar(
    r"""
    start = token*
    token = keyword / float / integer / identifier / char / symbol
    keyword = ~"int|float|char"i
    float = integer ~"\.\d+"
    integer = ~"\d+"
    identifier = ~"[a-zA-Z_]\w*"
    char = "'" ~r"'"i
    symbol = ~"."
    """
)

# Parseador de tokens
class TokenParser(parsimonious.NodeVisitor):
    def generic_visit(self, node, visited_children):
        return visited_children or node

    def visit_keyword(self, node, _):
        return Token("KeyWord", node.text)

    def visit_float(self, node, _):
        return Token("Flotante", float(node.text))

    def visit_integer(self, node, _):
        return Token("Numero", int(node.text))

    def visit_identifier(self, node, _):
        return Token("Id", node.text)

    def visit_char(self, node, _):
        return Token("Character", node.text)

    def visit_symbol(self, node, _):
        return Token("Symbol", node.text)

# Clase de tokens
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.type}({self.value})"

# Función para analizar tokens
def parse_tokens(input):
    parse_tree = grammar.parse(input)
    return TokenParser().visit(parse_tree)

# Función para analizar tokens con espacios en blanco opcionales alrededor
def parse_tokens_with_spaces(input):
    input = input.strip()
    return [token for tokens in parse_tokens(input) for token in tokens]
