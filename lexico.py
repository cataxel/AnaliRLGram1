import ply.lex as lex

# Lista de tokens
tokens = (
    'KeyWord',
    'Flotante',
    'Numero',
    'Id',
    'Character',
    'Symbol',
)

# Reglas de los tokens
def t_KeyWord(t):
    r'int|float|char'
    return t

def t_Flotante(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_Numero(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_Character(t):
    r"'.'"
    return t

def t_Id(t):
    r'[a-zA-Z_]\w*'
    return t

def t_Symbol(t):
    r'[,;+\-*/()=]'
    return t

# Caracteres ignorados (espacios y saltos de línea)
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    raise CaracterNoReconocidoError(t.value[0],t.lexpos)

# Construir el analizador léxico
def analisis(input):
    ana = lex.lex()
    ana.input(input)
    return ana


# clase para la excepcion de caracter no valido
class CaracterNoReconocidoError(Exception):
    def __init__(self, caracter, ubicacion):
        self.caracter = caracter
        self.ubicacion = ubicacion
        if caracter == "'":
            super().__init__(f"No se encontro la ' de cierre en la ubicacion: ",ubicacion)
        else:
            super().__init__(f"Carácter no reconocido: " + caracter+ " en ",ubicacion)
        