terminales_no_terminales = ["id", "num", "int", "float", "char", ",", ";", "+", "-", "*", "/", "(", ")", "=", "$", "P", "Tipo", "V", "A", "Exp", "E", "Term", "T", "F"]
ESTADOS = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14", "q15", "q16", "q17", "q18", "q19", "q20", "q21", "q22", "q23", "q24", "q25", "q26", "q27", "q28", "q29", "q30", "q31", "q32", "q33", "q34", "q35", "q36", "q37", "q38", "q39", "q40", "q41", "q42", "q43", "q44"]

tabla = [
    #"id", "num", "int", "float", "char", ",", ";",  "+",  "-",  "*",  "/",  "(", ")",  "=", "$", "P", "Tipo", "V", "A", "Exp", "E", "Term", "T", "F"]
    ["q7",  "",   "q4",   "q5",    "q6",  "",  "",   "",   "",   "",   "",   "",  "",   "",  "", "q1", "q2",    "","q3",  "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "",  "",   "", "P0", "",   "",     "", "",   "",   "",    "",   "",  "" ],
    ["q8",  "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "",  "",   "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "",  "",   "", "P2", "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["P3",  "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "",  "",   "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["P4",  "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "",  "",   "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["P5",  "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "",  "",   "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "",  "",  "q9", "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "", "q11","q12", "",   "",   "",   "",   "",  "",   "", "P1",  "",   "",  "q10","",   "",   "",    "",   "",  ""],
    ["q18","q19",  "",     "",      "",   "",  "",  "q14","q15", "",   "", "q20", "",   "",  "",  "",   "",     "", "",   "q13","",    "q16", "","q17"],
    ["P1",  "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "",  "",   "", "P1",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["q21", "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "",  "",   "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["q7",  "",   "q4",    "q5",    "q6",   "",  "",   "",   "",   "",   "",   "",  "",   "","P7","q22","q2",    "","q3",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "","q23",  "",   "",   "",   "",   "",  "",   "", "P8", "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["q18","q19",  "",     "",      "",   "",  "",   "",   "",   "",   "", "q20", "",   "",  "",  "",   "",     "", "",   "",   "",   "q24", "", "q17"],
    ["q18","q19",  "",     "",      "",   "",  "",   "",   "",   "",   "", "q20", "",   "",  "",  "",   "",     "", "",   "",   "",   "q25", "", "q17"],
    ["",    "",    "",     "",      "",   "", "P14","q27","q28", "",   "",   "", "P14", "",  "",  "",   "",     "", "",   "", "q26",   "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P18","P18","P18","q30","q31", "", "P18", "",  "",  "",   "",     "", "",   "",   "",    "", "q29", ""],
    ["",    "",    "",     "",      "",   "", "P19","P19","P19","P19","P19", "", "P19", "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P20","P20","P20","P20","P20", "", "P20", "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["q18","q19",  "",     "",      "",   "",  "",  "q14","q15", "",   "", "q20", "",   "",  "",  "",   "",     "", "",   "q32", "",   "q16","q29","q17"],
    ["",    "",    "",     "",      "", "q11","q12", "",   "",   "",   "",   "",  "",   "",  "",  "",   "",   "q33","",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "",  "",   "", "P7", "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "",  "",   "", "P8", "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P14","q27","q28", "",   "",   "", "P14", "",  "",  "",   "",     "", "",   "", "q35",   "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P14","q27","q28", "",   "",   "", "P14", "",  "",  "",   "",     "", "",   "", "q36",   "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P11", "",   "",   "",   "",   "", "P11", "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["q18","q19",  "",     "",      "",   "",  "",   "",   "",   "",   "", "q20", "",   "",  "",  "",   "",     "", "",   "",   "",  "q36",  "q29", "q17"],
    ["q18","q19",  "",     "",      "",   "",  "",   "",   "",   "",   "", "q20", "",   "",  "",  "",   "",     "", "",   "",   "",  "q37",  "", "q17"],
    ["",    "",    "",     "",      "",   "", "P15","P15","P15", "",   "",   "", "P15", "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["q18","q19",  "",     "",      "",   "",  "",   "",   "",   "",   "", "q20", "",   "",  "",  "",   "",     "", "",   "",   "",    "",   "", "q38"],
    ["q18","q19",  "",     "",      "",   "",  "",   "",   "",   "",   "", "q20", "",   "",  "",  "",   "",     "", "",   "",   "",    "",   "", "q40"],
    ["",    "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "", "q40", "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "",  "",   "",   "",   "",   "",   "",  "",   "", "P6", "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P9",  "",   "",   "",   "",   "", "P9",  "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P10", "",   "",   "",   "",   "", "P10", "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P14","q27","q28", "",   "",   "", "P14", "",  "",  "",   "",     "", "",   "", "q41",   "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P14","P17","q28", "",   "",   "", "P14", "",  "",  "",   "",     "", "",   "", "q42",   "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P18","P18","P18","q30","q31", "", "P18", "",  "",  "",   "",     "", "",   "",   "",    "", "q44", ""],
    ["",    "",    "",     "",      "",   "", "P18","P18","P18","q30","q31", "", "P18", "",  "",  "",   "",     "", "",   "",   "",    "", "q45", ""],
    ["",    "",    "",     "",      "",   "", "P21","P21","P21","P21","P21", "", "P21", "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P12", "",   "",   "",   "",   "", "P12", "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P13", "",   "",   "",   "",   "", "P12", "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P16","P16","P16", "",   "",   "", "P16", "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""],
    ["",    "",    "",     "",      "",   "", "P17","P17","P17", "",   "",   "", "P17", "",  "",  "",   "",     "", "",   "",   "",    "",   "",  ""]
]

producciones = {
    "P0": ("P'", "P",2),
    "P1": ("P", "Tipo Id V",6),
    "P2": ("P", "A",2),
    "P3": ("Tipo", "int",2),
    "P4": ("Tipo", "float",2),
    "P5": ("Tipo", "char",2),
    "P6": ("V", ", id V",6),
    "P7": ("V", "; P",4),
    "P8": ("A", "id = Exp ;",8),
    "P9": ("Exp", "+ Term E",6),
    "P10": ("Exp", "- Term E",6),
    "P11": ("Exp", "Term E",4),
    "P12": ("E", "+ Term E",6),
    "P13": ("E", "- Term E",6),
    "P14": ("E", "€",0),
    "P15": ("Term", "F T",4),
    "P16": ("T", "* F T",6),
    "P17": ("T", "/ F T",6),
    "P18": ("T", "€",0),
    "P19": ("F", "id",2),
    "P20": ("F", "num",2),
    "P21": ("F", "( Exp )",6),
}
pila = []
colum = "" 
fil = ""
pila.append("$")
pila.append("q0")
estado_actual = ""
def analisis(tokens, estado_actual):
    for token in tokens:
        if token == pila[-1]:
            pila_str = ",".join(map(str, pila))
            print("Entrada "+token+" pila: ("+pila_str+" ) la cadena se acepta")
            break
        #print("1--- "+estado_actual)
        #estado_actual = pila[-1]
        accion = obtener_fila_columna(estado_actual,token)
        if accion == "":
            print(pila)
            raise ErrorSintactico(accion,estado_actual)
        #if Errores(accion,pila,estado_actual,lexema,tokens,contador,token):
        #    raise ErrorSintactico(accion,pila,estado_actual,lexema,token)
        print("estado actual: "+estado_actual +" accion: "+accion)
        # si la accion es produccion
        if accion in producciones:
            pila_str = ",".join(map(str, pila))
            acciones = producciones[accion]
            acciones_str = ' '.join(map(str, acciones))
            print("Entrada "+token+" pila: ("+pila_str+" ) "+accion+":"+acciones_str)
            for x in range(0,acciones[2]):
                pila.pop()
            if acciones[0] == "P'":
                pila.pop()
            else:
                accion = obtener_fila_columna(pila[-1],acciones[0])
                pila.append(acciones[0])
                pila.append(accion)
                estado_actual = accion
                #print(pila)
                #print("estado actual: "+estado_actual+" accion "+accion)
            estado_actual = analisis([token],estado_actual)
                
        else:
            pila_str = ", ".join(map(str, pila))
            print("Entrada "+token+" pila: ("+pila_str+") Desplaza "+token+" a la pila y estado:"+accion)
            #moverse al siguiente estado y pasar a siguiente token
            pila.append(token)
            pila.append(accion)
            #print(pila)
            print("sig estado actual: "+estado_actual+" accion: "+accion)
            estado_actual = accion
            #print("des estado actual: "+estado_actual)
    return estado_actual


def obtener_fila_columna(estado_actual, token):
    fil = None
    colum = None

    for columna, item in enumerate(terminales_no_terminales):
        if token == item:
            colum = columna
            break

    for fila, estado in enumerate(ESTADOS):
        if estado_actual == estado:
            fil = fila
            break

    return tabla[fil][colum]

class ErrorSintactico(Exception):
    def __init__(self, accion, estado_actual):
        self.accion = accion
        self.pila = pila
        self.estado_actual = estado_actual
        #self.lexemas = lexemas
        #self.tokens = tokens
        #self.contador = contador
        #self.token = token
        super().__init__(self.__str__())

    def __str__(self):
        valores_aceptados = []
        cont = 0
        if self.accion == "":
            for fila, estado in enumerate(ESTADOS):
                if self.estado_actual == estado:
                    filas = tabla[fila]
                    for elemento in filas:
                        if elemento != "":
                            valores_aceptados.append(terminales_no_terminales[cont])
                        cont += 1
            valores = ", ".join(map(str, valores_aceptados))
            mensaje = "Error sintáctico: se esperaba " + valores + " se obtuvo un: "
            return mensaje
        else:
            return "Error sintáctico desconocido"


'''
def Errores(accion,pila,estado_actual,lexemas,tokens,contador,token):
    valores_aceptados = []
    cont = 0
    if accion == "":
        for fila, estado in enumerate(ESTADOS):
            if estado_actual == estado:
                filas = tabla[fila]
                for elemento in filas:
                    if elemento != "":
                        valores_aceptados.append(terminales_no_terminales[cont])
                    cont += 1
        valores = ", ".join(map(str, valores_aceptados))
        print(pila)
        print("Error sintactico se esperaba: "+valores+" se obtuvo un: ")
        return True
    else:
        return False

    print(valores_aceptados)
    item = ""
    for lexema in lexemas:

        item = lexema
    if accion == "":
        if estado_actual == "q27":
            pila_str = ", ".join(map(str, pila))
            print("Pila: "+pila_str)
            print("Error sintactico se esperaba un termino pero se obtuvo un: "+token)
            return True
        elif estado_actual == "q40":
            pila_str = ", ".join(map(str, pila))
            print("Pila: "+pila_str)
            print("Error sintactico se esperaba un operando o ';' pero se obtuvo un: "+token)
            return True
        elif estado_actual == "q7":
            pila_str = ", ".join(map(str, pila))
            print("Pila: "+pila_str)
            print("Error sintactico se esperaba un '=' pero se obtuvo un: "+token)
            return True
        elif estado_actual == "q18":
            pila_str = ", ".join(map(str, pila))
            print("Pila: "+pila_str)
            print("Error sintactico se esperaba un operando pero se obtuvo un: "+token)
            return True
        elif estado_actual == "q13":
            pila_str = ", ".join(map(str, pila))
            print("Pila: "+pila_str)
            print("Error sintactico se esperaba un ';' pero se obtuvo un: "+token)
            return True
        elif estado_actual == "q32":
            pila_str = ", ".join(map(str, pila))
            print("Pila: "+pila_str)
            print("Error sintactico se esperaba un ) pero se obtuvo un: "+token)
            return True
        pila_str = ", ".join(map(str, pila))
        print("Pila: "+pila_str)
        print("Error sintactico se esperaba un "+token+" pero se obtuvo un: "+token)
        return True
        
    else:
        return False
        '''