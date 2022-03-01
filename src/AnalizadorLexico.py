import ply.lex as lex
tokens = ['ID','LPARENT','RPARENT','LBRACKET','RBRACKET','PUNTOCOMA','MAS','MENOS',
        'MULTIPLICACION','DIVISION','IGUAL','FLOTANTE','ENTERO','CADENA','BOOLEANO']


reservadas = {
    'START' : 'start',
    'STRING' : 'string',
    'INT' : 'int',
    'FLOAT' : 'float',
    'BOOLEAN' : 'boolean',
    'IF' : 'if',
    'WHILE' : 'while',
    'FUN' : 'fun',
    'PRINT' : 'print',
    'INPUT' : 'input'
}

tokens = tokens+list(reservadas.keys())

t_ignore = '\t'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_PUNTOCOMA = r';'
t_MAS = r'\+'
t_MENOS = r'\-'
t_DIVISION = r'/'
t_MULTIPLICACION = r'\*'
t_IGUAL = r'='



def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value.upper(),'ID').upper()
    return t

def t_BOOLEANO(t):
    r'true | false'
    t.type = reservadas.get(t.value.upper(),'ID').upper()
    return t

def t_FLOTANTE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

def t_error(t):
    print("carcter ileagl"+t.value[0])

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ccode_nonspace(t):
    r'\s+'
    pass


cadena = '''
variable
'''



analizador = lex.lex()
def SiRetornaTokens(cad):   #Esta funcion es por si queremos mostrar el analisis lexico
    
    cadena=cad
    analizador.input(cad)




    ltk = []    

    while True:
        tok = analizador.token()
        if not tok : break
        ltk.append(tok)
    
    return ltk


