import ply.lex as lex
import re 
import tkinter
import AnalizadorLexico
import AnalizadorSintactico


class App:
    def __init__(self,master):

        self.master = master
        self.empieza()
    

    def empieza(self):
         frame1 = tkinter.Frame(self.master)
         frame1.pack()

         self.entrada = tkinter.Text(frame1)
         self.entrada.grid(column=0,row=0)
        
         
         boton1 = tkinter.Button(frame1,text="Analizador léxico",anchor=tkinter.CENTER,command=self.enviaALexer)
         boton1.grid(column=0,row=1)

         boton2 = tkinter.Button(frame1,text="Analizador sintáctico",anchor=tkinter.CENTER,command=self.enviaAParser)
         boton2.grid(column=0,row=2)

    def enviaALexer(self):
        entrar = self.entrada.get(1.0,"end-1c")
        tokens = AnalizadorLexico.SiRetornaTokens(entrar)
        self.imprimirTokens(tokens)
    
    def imprimirTokens(self,lst):
        
        ventana2  = tkinter.Tk()
        ventana2.title("Tokens")
        ventana.geometry("500x450")

        for n in lst:
            etiqueta = tkinter.Label(ventana2,text=n)
            etiqueta.pack()
        
        
        
    def enviaAParser(self):
        entrar = self.entrada.get(1.0,"end-1c")
        AnalizadorSintactico.SiParse(entrar)

        
        



   
    


ventana = tkinter.Tk()
ventana.title("Analizador")
ventana.geometry("650x500")
interf = App(ventana)
ventana.mainloop()









"""



#TOKEN_ID: para los identificadores.
#TOKEN_FL: para los números float.
#TOKEN_INT: para los numeros Enteros
#TOKEN_KEY: para todas las palabras reservadas y símbolos. 
#TOKEN_STRING para las cadenas
tokens = ['TOKEN_ID','TOKEN_KEY','TOKEN_FL','TOKEN_INT','TOKEN_COMENT','TOKEN_STRING']

#Para definir los token se tiene que poner t_
#Para ingnorar las Tabulaciones
t_ignore = '\t'

t_TOKEN_STRING = r'\".*\"'
#token para los comentarios
t_TOKEN_COMENT = r'\#.*'

#a qui les ponemos palabras reservadas y simbolos a la variable  t_TOKEN_KEY
t_TOKEN_KEY = r'start|string|int|input|print|fun|true|false|if|else|float|\^|,|\+|\-|/|\*|;|\{|\}|\(|\)|=|=!|<|>|<=|>='

#es la expresion regular de identificadores  de token_ID
t_TOKEN_ID = r'[_A-Za-z][A-Za-z0-9_]*'
  
# Esta funcion Define un numero flotante o decimal    
def t_TOKEN_FL(t):
    r'\d+\.\d+'
    t.value=float(t.value)
    return t

# Esta funcion Define los numeros enteros
def t_TOKEN_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Si no detecta ningun token de los anteriores 
def t_error(t):
    print("Caracter ilegal: "+str(t.value[0]))
    t.lexer.skip(1)

# Es un salto de linea
def t_nuevaLinea(t):
    r'\n+'
    t.lexer.lineno+=len(t.value)

# Es para los espacios
def t_nonspace(t):
 r'\s+'
 pass

#se manda a llamar al medoto lex que deVuelve un objeto de tipo lexer que tiene metodos como:
#input,skip,token
analizador = lex.lex()

#es el codigo que tenemos que separar en tokens


data = '''
start(){
int var , var2;
var_1 = 23.5;
var_2 = var*2;
int var_3 = 10^2;
print(var_3,var2,var_1);
int árbol;
#comentario
string var_4;
var_4 = 'hola';
print(var_4);
}
'''


#data =  input("Ingrese el script")


#A qui mandamos lo que tiene la variable data alas funciones de token como parametros.
analizador.input(data)
#Se hace un ciclo infinito para llamar al metodo token hasta que devuelva none

lstTokens = []

while True:
    tok = analizador.token()
    lstTokens.append(tok)
    if not tok:
        break
    #print(tok) 
   

lstImprimir = []



for i in range(len(lstTokens)-1): 
    if lstTokens[i].type=='TOKEN_COMENT': 
        pass
    else:

        lstImprimir.append([lstTokens[i].type,None,lstTokens[i].value])


contId = 0

#enteros que identifican a los tokens
for i in range(len(lstImprimir)):
    if lstImprimir[i][1]==None:
        contId+=1
        lstImprimir[i][1] = contId
        for j in range(len(lstImprimir)):
            if lstImprimir[i][2]==lstImprimir[j][2]:
                lstImprimir[j][1] = contId
    

for i in range(len(lstImprimir)): 
    print(lstImprimir[i])

"""







