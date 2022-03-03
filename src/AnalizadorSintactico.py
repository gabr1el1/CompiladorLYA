
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


def p_statement1(p): #Esta regla define un solo statement
    '''statement : ID IGUAL expression PUNTOCOMA'''
    print("statement -> ID IGUAL expression PUNTOCOMA")

def p_statement2(p):
    '''statement : tipo idList PUNTOCOMA'''
    print("statement -> tipo idList PUNTOCOMA")


def p_tipo1(p):
    '''tipo : INT'''
    print("tipo -> INT")

def p_tipo2(p):
    '''tipo : FLOAT'''
    print("tipo -> FLOAT")

def p_tipo3(p):
    '''tipo : STRING'''
    print("tipo -> STRING")

def p_idList1(p):
    '''idList : ID'''
    print("idList -> ID")

def p_idList2(p):
    '''idList : idList COMA ID'''
    print("idList -> idList COMA ID")






def p_expression1(p):
    '''expression : term'''
    print("expression -> term")

def p_expression2(p):
    '''expression : addingOperator term'''
    print("expression -> addingOperator term")

def p_expression3(p):
    '''expression : expression addingOperator term'''
    print("expression -> expression addingOperator term")

def p_term1(p):
    '''term : factor'''
    print("term -> factor")


def p_term2(p):
    '''term : term multiplyingOperator factor'''
    
    print("term -> term multiplyingOperator factor")


def p_multiplyingOperator1(p):
    '''multiplyingOperator : MULTIPLICACION'''
    print("multiplyingOperator -> MULTIPLICACION")

def p_multiplyingOperator2(p):
    '''multiplyingOperator : DIVISION '''
    print("multiplyingOperator -> DIVISION")

def p_addingOperator1(p):
    '''addingOperator : MAS '''
    print("addingOperator -> MAS")

def p_addingOperator2(p):
    '''multiplyingOperator : MENOS '''
    print("addingOperator-> MENOS")

def p_factor1(p):
    '''factor : ID '''
    print("factor -> ID")

def p_factor2(p):
    '''factor : numero '''
    print("factor -> ENTERO")

def p_factor3(p):
    '''factor : LPARENT expression RPARENT '''
    print("factor -> LPARENT expression RPARENT")

def p_numero1(p):
    '''numero : ENTERO'''
    print("numero -> ENTERO")

def p_numero2(p):
    '''numero : FLOTANTE'''
    print("numero -> FLOTANTE")




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

