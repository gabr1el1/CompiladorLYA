
#PRIMERA VERSION
import ply.yacc as yacc #Necesitarémos usar la librería yacc
import re

from AnalizadorLexico import tokens 
'''
Se importan los tokens para que el analizador sintactico sepa que hacer 
con ellos 
'''


'''Estas son las producciones de la Gramatica Libre de Contexto que seguirá nuestro lenguaje deben
    ir con p_ antes de su nombre
'''
def p_program(p):
    '''program : START LPARENT RPARENT LBRACKET statementList RBRACKET '''
    print("program -> START LPARENT RPARENT LBRACKET statementList RBRACKET")

def p_statementList1(p):
    '''statementList : statement statementList'''
    print("statementList -> statement statementList")

def p_statementListEmpty(p):
    '''statementList : empty'''
    print("statementList -> nulo")


def p_statement(p): #Esta regla define un solo statement
    '''statement : ID IGUAL expression PUNTOCOMA'''
    print("statement -> ID IGUAL expression PUNTOCOMA")

#Por el momento definimos a una expresion como un ID o como un valor 
def p_expression1(p):
    '''expression : ID'''
    print("expression -> ID")

def p_expression2(p):
    '''expression : valor'''
    print("expression -> valor")

#Hemos definido los valores posibles en nuestro lenguaje
def p_valor1(p):
    '''valor : CADENA'''
    print("valor -> CADENA")

def p_valor2(p):
    '''valor : ENTERO'''
    print("valor -> ENTERO")

def p_valor3(p):
    '''valor : FLOTANTE'''
    print("valor -> FLOTANTE")

def p_statementEmpty(p): #Define si el statement está vacío
    '''statement : empty'''
    print("statement -> nulo")


def p_empty(p): 
    '''empty :'''
    pass

def p_error(p): #Esta regla define que hacer si ninguna de las anteriores pudo definir a los tokens
    print("Error de sintáxis" , p)


def SiParse(cadena): #Este metodo se llamara para hacer el analisis sintactico
    parser = yacc.yacc() #Construye el analizador sintáctico
    result = parser.parse(cadena) 

    #llama al metodo del analizador para construir el "árbol" que en realidad son las reglas que usa
                                                        

    print(result)

