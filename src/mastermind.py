#Autor Danny Xie Li
#Tarea Programada 2
#Instituto Tecnologico de Costa Rica
#Profesor William Mata
#Versión 0.0.1
#Fecha de entrega 16/10/16

#-----------------
#Librerías Usadas
#-----------------

from os import startfile 
import random
import time
import tkinter.ttk as ttk 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

#-------------------
#Variables Globales 
#-------------------

#Se utiliza en la pantalla jugar
NombreJugador = "Danny"
DificultadConsultar = "" #Para consultar la dificultar en top 10 y detalle
dificultad = "Fácil" 
reloj="Si"
posicion="Derecha"
Panel="Colores"
Cronometro="Juego"
CuantoTiempo=1800 #Tiempo en segundos solo por juego
CuantoJugada=60 #Tiempo en segundos solo por jugada
#Parte juego
Elementos={'Números': ['uno.gif', 'dos.gif', 'tres.gif', 'cuatro.gif', 'cinco.gif', 'seis.gif'], 'Colores': ['Earth.gif', 'luna.gif', 'jupiter.gif', 'negro.gif', 'circulo.gif', 'oval.gif'], 'Letras': ['A.gif', 'B.gif', 'C.gif', 'D.gif', 'E.gif', 'F.gif'], 'Emoticones': ['tranquilo.gif', 'confundido.gif', 'enfermo.gif', 'sorprendido.gif', 'feliz.gif', 'ninja.gif']}
Jugada = []
TodasLasJugadas=[] #Se usa para cargar las jugadas.
PosicionX=0
#Función de tick se usa para configurar la hora, minutos y segundos
sec = 0
minute=00
hour=00
segundos=0
tiempo=0
JugadaOponente=[] #Jugada hecha por la compu
ListasDeJugadas=[]#Todas las jugadas hechos por la compu
InsertarX=50 #Para insertar imagenes en posiciones
InsertarY= 370 #Para insertar imagenes en posiciones
#Referencia no se usan
x1=50
y1=370
x2=82
y2=404
ListaConfiguración = [] #Se usa para cargar datos
DatosDeLosGanadores = [] #Se usa para cargar datos
xm1=280
ym1=390
xm2=294
ym2=404

#----------
#Funciones 
#----------

#----------------------------------------------------------------------------------------
#Descripción: La siguiente función carga la configuración almacenada a la variable global.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def CargarConfiguración():
    global ListaConfiguración 
    contenido = leerTodo("mastermind2016configuracion.txt")
    if contenido == "" :
        return contenido
        ListaConfiguración  = []
    else:
        ListaConfiguración  = eval(contenido)
        return eval(contenido)

#----------------------------------------------------------------------------------
#Descripción: La siguiente función asigna las variables la configuración guardada.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
    
def PonerConfiguración():
    global dificultad,reloj,posicion,Panel,Cronometro,CuantoTiempo,CuantoJugada,ListaConfiguración
    contenido = eval(leerTodo("mastermind2016configuracion.txt"))
    if contenido == "" :
        dificultad = "Fácil"
        reloj = "Si"
        posicion = "Derecha"
        Panel ="Colores"
        Cronometro = "Juego"
        CuantoTiempo = 1800
        CuantoJugada = 60
    else:
        dificultad = contenido[0]
        reloj =  contenido[1]
        posicion=contenido[2]
        Panel = contenido[3]
        Cronometro =  contenido[4]
        CuantoTiempo = contenido[5]
        CuantoJugada = contenido[6]

#-----------------------------------------------------------------------------------        
#Descripción: La siguiente funcion sobrescribe el archivo y guarda la configuración.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.
        
def SobreescribeConfi():
    global dificultad,reloj,posicion,Panel,Cronometro,CuantoTiempo,CuantoJugada
    lista= [dificultad,reloj,posicion,Panel,Cronometro,CuantoTiempo,CuantoJugada]
    archivo = open ("mastermind2016configuracion.txt", "w")  #Abre el archivo y la operación es sólo escritura.
    archivo.write (str(lista))  #El contenido leído se lo asigna a la variable.
    archivo.close() #Se cierra el archivo.

#---------------------------------------------------------------------------
#Descricpción: La siguiente función abre el manual de usuario de mastermind.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.

def ManualMasterMind():
    startfile("manual_de_usuario_mastermind.pdf")
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna el contenido leído en un archivo en formato string, cuando se le digite la entrada que es el nombre del archivo en formato string.
#Entradas: Un string.
#Salidas: Un string.
#Restricciones: Sólo en formato string.

def leerTodo (nombreArchivo):
    archivo = open (nombreArchivo, "r+")  #Abre el archivo y la operación es sólo escritura.
    contenido = archivo.read ()  #El contenido leído se lo asigna a la variable.
    archivo.close() #Se cierra el archivo.
    return contenido

#--------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función carga todos los datos del documento y loo asigna a la variable global.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def CargarGanadoresDeLaBase(): 
    global DatosDeLosGanadores
    contenido = leerTodo("mastermind2016top10.txt")
    if contenido == "" :
        return contenido
        DatosDeLosGanadores = []
    else:
        DatosDeLosGanadores = eval(contenido)
        return eval(contenido)

#--------------------------------------------------------------------------------------
#Descripción: La siguiente función sobreescribe un archivo toma una lista del ganador.
#Entradas: Una lista.
#Salidas: Ninguna.
#Restricciones: Ninguna.
    
def SobreescribeGanador(listaganador):
    global DatosDeLosGanadores, dificultad
    print(DatosDeLosGanadores)
    actualizado = AgregarSegunNivel(dificultad,DatosDeLosGanadores,listaganador)
    DatosDeLosGanadores = actualizado
    archivo = open ("mastermind2016top10.txt", "w")  #Abre el archivo y la operación es sólo escritura.
    archivo.write (str(actualizado))  #El contenido leído se lo asigna a la variable.
    archivo.close() #Se cierra el archivo.

#----------------------------------------------------------------------------------------
#Descripción: La siguiente función agrega una lista según en el nivel que desea agregar.
#Entradas: Un string y dos listas.
#Salidas: Una lista.
#Restricciones: Sólo string en la primera posición y las dos siguientes listas.
    
def AgregarSegunNivel(nivel,lista,listaganador): #formato de listaganador [1,2,3,4]
    listadelnivel= SóloNivel(lista,nivel)
    new = ListaSustituto(listadelnivel,listaganador)
    print(new)
    lista.remove(SóloNivel(lista,nivel))
    lista.append(new)
    return lista

#--------------------------------------------------------------------------------------------------
#Descripción: La siguiente función deja la lista que posea un menor tiempo de la lista del ganador.
#Entradas: Dos listas.
#Salidas: Una lista.
#Restricciones: Sólo listas.

def ListaSustituto(listanivel,listanueva): #formato listanivel["Facil",[["Pedro",12,12]]]
    newlist = []
    
    if listanivel[1] != []:
        for i in listanivel[1]:
            if i[0] == listanueva[0]:
                if i[1] >= listanueva[1]:
                    newlist =newlist + [listanueva]
                    continue
            else:
                newlist =newlist + [i]
        print("hollllllla",[listanivel[0],newlist+[listanueva]])
        return [listanivel[0],newlist+[listanueva]]
    else:
        return [listanivel[0],[listanueva]]

#-----------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista del nivel a partir de una lista de sublistas de niveles. 
#Entradas: Una lista y un string.
#Salidas: Una lista.
#Restricciones: Sólo listas y strings.

def SóloNivel(lista,nivel):
    for i in lista:
        if i[0] == nivel:
            return i
        else:
            continue

#------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función reinicia el tiempo del cronómetro si es Juego no lo hace si es jugada si lo hace al precionar el boton de calificar.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def JugadaConTiempo():
    global sec,minute,hour, segundos,Cronometro
    if Cronometro == "Juego":
        return
    else:
        sec=0
        minute=0
        hour=0
        segundos=0

#------------------------------------------------------------------------------------
#Descripción: La siguiente función cuenta la cantidad de listas que hay en una lista.
#Entradas: Una lista.
#Salidas: Un entero.
#Restricciones: Sólo listas dentro de listas.

def ContarListas(lista):
    cont=0
    for i in lista:
        cont=cont+1
    return cont

#--------------------------------------------------------------------------------------------------------------------------------
#Descripción: Esta función cuenta la cantidad de jugadas que tiene la variable si son 8,6,7 listas dependiendo de la dificultad.
#Entradas: Ninguna.
#Salidas: Valor booleano.
#Restricciones: Ninguna.

def Maximo():
    global dificultad,TodasLasJugadas
    if dificultad == "Fácil":
        if ContarListas(TodasLasJugadas) == 8:
            return True
        else:
            return False
    if dificultad == "Medio":
        if ContarListas(TodasLasJugadas) == 7:
            return True
        else:
            return False
    if dificultad == "Difícil":
        if ContarListas(TodasLasJugadas) == 6:
            return True
        else:
            return False

#------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna un valor booleano de que si dos listas son iguales o si ganó.
#Entradas: Dos listas.
#Salidas: Un valor booleano.
#Restricciones: Sólo listas.
        
def Correcto(lista,lista2):
    cont=0
    for i in lista:
        if i == lista2[cont]:
            cont=cont+1
            continue
        else:
            return False
    return True

#--------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función carga los datos que se encuentra en el archivo "AppContactosInfo.txt" y se lo asigna a la variable global.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.
    
def CargarListaDeJugadas():
    global ListasDeJugadas  #Utiliza la variable global ListasDeContactos
    archivo=leerTodo("JugadasDMasterMind.txt") #Utiliza la función leerTodo del archivo "AppContactosInfo.txt"
    if archivo == "" :
        ListasDeJugadas = []
    else:
        ListasDeJugadas = eval(archivo) #Se le asigna los datos que se encuentra en la variable a la variable global.
        print(ListasDeJugadas)

#------------------------------------------------------------------------
#Descripción: La siguiente función borra todo el contenido de un archivo.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
        
def Sobrescribir():
    global ListasDeJugadas  #Utiliza la variable global ListasDeContactos
    ListasDeJugadas = JugadaOponente + ListasDeJugadas
    archivo = open ("JugadasDMasterMind.txt", "w")  #Abre el archivo y la operación es sólo escritura.
    archivo.write (str(ListasDeJugadas))  #El contenido leído se lo asigna a la variable.
    archivo.close() #Se cierra el archivo.

#--------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función revisa de que sea diferente las jugadas que insertó y las jugadas que se encuentran guardadas.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def Diferente():
    JugadaOponente1()
    global ListasDeJugadas,JugadaOponente

    if ContarListas(ListasDeJugadas) >= 100:
        JugadaOponente1()
    else:
        while JugadaOponente in ListasDeJugadas:
            JugadaOponente1()
        print(JugadaOponente)

#----------------------------------------------------------------------        
#Descripción: La siguiente función se crea la jugada de la computadora.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def JugadaOponente1():
    global JugadaOponente
    JugadaOponente2=[]
    for i in range(4):
        n=random.randint(1,6)
        JugadaOponente2 = JugadaOponente2 + [n]
    JugadaOponente = JugadaOponente+[JugadaOponente2]
    print(JugadaOponente)

#---------------------------------------------------------------------------------------------------
#Descripción: La siguiente función carga los datos del archivo de top 10 de los jugadores ganadores.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def CargarGanadoresDeLaBase(): #colocarlo en la pantalla principal del juego
    global DatosDeLosGanadores
    contenido = leerTodo("mastermind2016top10.txt")
    if contenido == "" :
        return contenido
        DatosDeLosGanadores = []
    else:
        DatosDeLosGanadores = eval(contenido)
        return eval(contenido)

#--------------------------------------------------------------------------------------
#Descripcion: La siguiente funcion crea una jugada creada por la computadora.
#Entradas: Un entero.
#Salidas: Una lista.
#Restricciones: Solo enteros posibles.

def InsertarJugada(n):
    global Jugada
    
    Jugada = Jugada + [n]

#------------------------------------------------------------------------------------------
#Descripción: La siguiente funcion cuenta la cantidad de listas que hay en una lista.
#Entradas:Una lista
#Salidas: un entero positivo.
#Restricciones: Solo enteros positivos.
    
def Contar(lista):
    cont=0
    for i in lista:
        cont=cont+1
    return cont

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente funcion toma la variable global la lista y cuenta la cantidad de elementos que hay, si hay 4 elementos o no.
#Entradas: Ninguno.
#Salidas: Un valor booleano.
#Restricciones: Ninguno.

def HayCuatro():
    global Jugada
    if Contar(Jugada)>= 4:
        return True
    else:
        return False

#---------------------------------------------------------------------------------
#Descripción: La siguiente función crea una combinación de 4 digitos en una lista.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
            
def Combinación():
    lista=[]
    while len(lista)<4:
        n=random.randint(0,3)
        if n in lista:
            continue
        else:
            lista=lista+[n]
            continue
    return lista

#---------------------------------------------------------------------------------------------
#Descripción: La siguiente función cuetala cantidad de números repetidos que hay en una lista.
#Entradas: Una lista y un número.
#Salidas: Un entero.
#Restricciones: Sólo listas y números.

def ContarRepetido(dig,lista):
    cont=0
    for i in lista:
        if i == dig:
            cont=cont+1
        else:
            continue
    return cont

#------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función asigna a la variable la posición en el eje x según la posición que este si es izquierda o derecha.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def PosicionDeLosElementos():
    global posicion, PosicionX
    if posicion == "Derecha":
        PosicionX = 400
    else:
        PosicionX = 20

#------------------------------------------------------------------------------------------
#Descripción: La siguiente función convierte un string de segundos a este formato 00:00:00.
#Entradas: Un string.
#Salidas: Un string.
#Restricciones: Sólo strings.
    
def ConvertirStringATiempo(string):
    num = int(string)
    hour = num //3600
    minuto = num //60
    segundos = num%60
    return str(hour)+":"+str(minuto)+":"+str(segundos)

#---------------------------------------------------------------------------------------------------
#Descripción: La siguiente función muestra un mensaje de error, pidiendole que digite la dificultad.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def EscribaDifi():
    messagebox.showerror("Error","Digite la dificultad")

#-------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función recibe un string y cuenta la cantidad de letras que tiene ese string.
#Entradas: Un string.
#Salidas: Un número entero.
#Restricciones: Sólo strings.

def ContarString(nombre):
    cont=0
    for i in nombre:
        cont=cont+1
    return cont

#--------------------------------------------------------------------------------------
#Descripción:La siguiente función retorna una ventana de error cuando no digita tiempo.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def MensajeDeError():
    messagebox.showerror("Error","Ponga cuanto tiempo desea")
    
#----------------------------------------------------------------------------------
#Descripción: La siguiente función cierra la ventana, según el string que le ponga.
#Entradas: Un string, nombre del archivo.
#Salidas: Ninguna.
#Restricciones: Sólo strings.

def Cerrar(nombre):
    nombre.withdraw()

#---------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna un cuadro de texto diciendo un error que no escribió el nombre.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def EscribaNombre():
    messagebox.showerror("Error","Escriba un nombre")

#-----------------------
#Ventana de Jugar
#-----------------------

def VentanaJugar():

    global Panel,Elementos,PosicionX,NombreJugador,dificultad
    #---------------------------------------------------------------------------
    #Descripción: La siguiente función califica la jugada y aumenta el eje x, y. 
    #Entradas: Ninguno.
    #Salidas: Ventanas de error.
    #Restricciones: Ninguno.

    def Calificar():
        
        global JugadaOponente,Jugada,InsertarX,InsertarY,TodasLasJugadas,xm1,ym1,xm2,ym2
        
        if len(JugadaOponente) == 0:
            return messagebox.showerror("Error","Debe iniciar el juego")
        if Maximo() == True:
            return messagebox.showerror("Error","Ya perdistes")
        else:
            JugadaOponente2=JugadaOponente[0]
            if HayCuatro() == True:
                JugadaConTiempo()
                if Correcto(Jugada,JugadaOponente2):
                    GanoConTiempoJuego()
                    InsertarX=50 #Para insertar imagenes en posiciones
                    InsertarY= 370 #Para insertar imagenes en posiciones
                    Jugada = []
                    TodasLasJugadas=[]
                    JugadaOponente=[]
                    xm1=280
                    ym1=390
                    xm2=294
                    ym2=404
                    messagebox.showinfo("Ganó","Ganastes el juego")
                    return ventanaJugar.destroy()
                else:
                    CalificarPonerCirculos()
                    TodasLasJugadas=[Jugada]+TodasLasJugadas
                    InsertarX = 50
                    InsertarY = InsertarY-50
                    Jugada = []
                    return
            if HayCuatro() == False:
                return messagebox.showerror("Error","Debe seleccionar 4 elementos")
            else:
                TodasLasJugadas=[Jugada]+TodasLasJugadas
                Jugada = []
                InsertarX = 50
                InsertarY = InsertarY-50

    #---------------------------------------------------------------------------
    #Descripción: La siguiente función es el complemento de la función calificar.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def Calificar_aux():
        global Jugada,JugadaOponente,InsertarX,InsertarY,TodasLasJugadas
        JugadaOponente2=JugadaOponente[0]
        if HayCuatro() == True:
            if Correcto(Jugada,JugadaOponente2):
                return messagebox.showinfo("Ganó","Ganastes el juego")
            else:
                CalificarPonerCirculos()
                TodasLasJugadas=[Jugada]+TodasLasJugadas
                InsertarX = 50
                InsertarY = InsertarY-50
                Jugada = []
                return
        if HayCuatro() == False:
            return messagebox.showerror("Error","Debe seleccionar 4 elementos")
        else:
            TodasLasJugadas=[Jugada]+TodasLasJugadas
            Jugada = []
            InsertarX = 50
            InsertarY = InsertarY-50

    #-------------------------------------------------------------------------------------------
    #Descripción: La siguiente función crea la cantidad de circulos según la dificultad. 
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def Dificultad():
        global dificultad
        if dificultad == "Fácil":
            CrearCirculos(200,232,8) #Utiliza la función crear circulos.
            CrearCirculos(150,182,8) #Utiliza la función crear circulos.
            CrearCirculos(100,132,8) #Utiliza la función crear circulos.
            CrearCirculos(50,82,8) #Utiliza la función crear circulos.
            Jugadas(8)
            CrearMiniCirculos(260,370,274,384,8)
            CrearMiniCirculos(280,370,294,384,8)
            CrearMiniCirculos(260,390,274,404,8)
            CrearMiniCirculos(280,390,294,404,8)
            return
        if dificultad == "Medio" :
            CrearCirculos(200,232,7) #Utiliza la función crear circulos.
            CrearCirculos(150,182,7) #Utiliza la función crear circulos.
            CrearCirculos(100,132,7) #Utiliza la función crear circulos.
            CrearCirculos(50,82,7) #Utiliza la función crear circulos.
            Jugadas(7)
            CrearMiniCirculos(260,370,274,384,7)
            CrearMiniCirculos(280,370,294,384,7)
            CrearMiniCirculos(260,390,274,404,7)
            CrearMiniCirculos(280,390,294,404,7)
            return
        if dificultad == "Difícil":
            CrearCirculos(200,232,6) #Utiliza la función crear circulos.
            CrearCirculos(150,182,6) #Utiliza la función crear circulos.
            CrearCirculos(100,132,6) #Utiliza la función crear circulos.
            CrearCirculos(50,82,6) #Utiliza la función crear circulos.
            Jugadas(6) 
            CrearMiniCirculos(260,370,274,384,6)
            CrearMiniCirculos(280,370,294,384,6)
            CrearMiniCirculos(260,390,274,404,6)
            CrearMiniCirculos(280,390,294,404,6)
            return

    #-------------------------------------------------------------------------------
    #Descripción: La siguiente función le asigna los elementos que se va a utilizar.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
            
    def PanelElementos():
        global Panel,Elementos,posicion
        Lista = Elementos[Panel]
        print(Lista)
        if posicion == "Derecha":
            x=375
            y=300
            Imagen1=PhotoImage(file=Lista[0])
            BotonImagen1=Button(ventanaJugar,image=Imagen1).place(x=375,y=300)
            Imagen2=PhotoImage(file=Lista[1])
            BotonImagen2=Button(ventanaJugar,image=Imagen2).place(x=375,y=250)
            Imagen3=PhotoImage(file=Lista[2])
            BotonImagen3=Button(ventanaJugar,image=Imagen3).place(x=375,y=200)
            Imagen4=PhotoImage(file=Lista[3])
            BotonImagen4=Button(ventanaJugar,image=Imagen4).place(x=375,y=150)
            Imagen5=PhotoImage(file=Lista[4])
            BotonImagen5=Button(ventanaJugar,image=Imagen5).place(x=375,y=100)
            Imagen6=PhotoImage(file=Lista[5])
            BotonImagen6=Button(ventanaJugar,image=Imagen6).place(x=375,y=50)

    #------------------------------------------------------------------------------------       
    #Descripción: La siguiente funcion crea los circulos segun los valores que le digita.
    #Entradas: Eje x1, eje x2 y la cantidad de circulos.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def CrearCirculos(x,x2,n):
            yu=370 #Se le asigna a una variable 20.
            yd=404 #Se le asigna a una variable 54.
            for i in range(n): #Iteracion.
                canvas.create_oval(x,yu,x2,yd,fill="CHARTREUSE3") #Crea circulos con el color lemon chiffon.
                yu=yu-50 #Se le asigna a una variable la suma de 50.
                yd=yd-50 #Se le asigna a una variable la suma de 50.
                print("Aui",yu,yd)

    #---------------------------------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente funcion cra canvas de numeros que corresponde a los numeros de jugadas segun la dificultad o la cantidad de filas.
    #Entradas: Un entero.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
                
    def Jugadas(n):
        lista="12345678"
        x=30
        y=385
        for i in range(n):
            canvas.create_text(x,y,text=lista[0],fill="white",font=("comic sans ms",18))
            y=y-50
            lista=lista[1:]

    #-------------------------------------------------------------------------------
    #Descripción: La siguiente funcion crea los minicirculos que hay para calificar.
    #Entradas: 4 numeros son los ejes y el quinto numero es la cantidad de circulos.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
            
    def CrearMiniCirculos(x,y,x1,y1,n):
            for i in range(n): #Iteracion.
                canvas.create_oval(x,y,x1,y1,fill="white") #Crea circulos con el color lemon chiffon.
                y=y-50 #Se le asigna a una variable la suma de 50.
                y1=y1-50 #Se le asigna a una variable la suma de 50.

    #------------------------------------------------------------------------------------------------
    #Descripción: La siguiente función le asigna el valor de los variables a otros viables globales.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
                
    def ConfigurarVariables():
        global sec,hour,minute,segundos,tiempo,CuantoJugada,CuantoTiempo,Cronometro,finaliza
        if reloj == "Si":
            if Cronometro == "Juego":
                tiempo = CuantoTiempo
                finaliza=CuantoTiempo
            if Cronometro == "Jugada":
                tiempo = CuantoJugada
                finaliza=CuantoJugada
        else:
            Label(ventanaJugar,bg="#3C3B37",height=6,width=25,font=("Helvetica",13)).place(x=520, y=360)#3C3B37

    #------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente función simula un cronómetro y cambia los valores de las variables globales.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
            
    def tick():
        global sec,hour,minute,segundos,tiempo,CuantoJugada,CuantoTiempo
        
        if tiempo == segundos:
            return messagebox.showerror("Perdistes","Juego Terminado")
        else:
            sec = sec + 1 #sec+1
            segundos = segundos + 1
            if (sec>=60):
                sec=0
                minute+=1
            if (minute >=60):
                minute=0
                hour+=1
        EtiquetaCronometro['text'] = str(hour)+":"+str(minute)+":"+str(sec)
        EtiquetaCronometro.after(1000, tick)
        
    #----------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente función convierte los segundos en formato horas, minutos y segundos en formato string.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
        
    def TiempoEnSegundos():
        global tiempo
        segundos = str(tiempo%60)
        minutos = str(tiempo//60)
        hora = str(tiempo//3600)
        total=hora+":"+minutos+":"+segundos
        Finaliza.set(total)

    #----------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente función termina el juego y reinicia uno nuevo.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
        
    def TerminarJuego():
        global InsertarX,InsertarY,Jugada,TodasLasJugadas,JugadaOponente,xm1,ym1,xm2,ym2
        variable = messagebox.askquestion("Estás seguro", "Estás seguro de terminar el juego ")
        if variable == "yes":
            Dificultad()
            InsertarX=50 #Para insertar imagenes en posiciones
            InsertarY= 370 #Para insertar imagenes en posiciones
            Jugada = []
            TodasLasJugadas=[]
            JugadaOponente=[]
            xm1=280
            ym1=390
            xm2=294
            ym2=404
            Button(ventanaJugar,text="Iniciar Juego",command=IniciarGame,relief=FLAT).place(x=520,y=300)
            ventanaJugar.destroy()
            VentanaJugar()
        else:
            return
        
    #------------------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente funcion elimina un elemento cuando el usuario habia seleccionado un elemento del panel
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def Eliminar():
        global InsertarX,InsertarY,Jugada
        if Contar(Jugada)>=1:
            InsertarX=InsertarX-50
            Label(canvas,image=ImagenVacío,relief=FLAT,bg="brown").place(x=InsertarX,y=InsertarY)
            Jugada=Jugada[1:]
        else:
            return

    #-----------------------------------------------------------------------
    #Descripción: La siguiente funcion inserta un elemento 1 al juego.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
    
    
    def Insertar1():
        global InsertarY,InsertarX
        if Maximo():
            return messagebox.showinfo("Juego terminado","Ya perdistes")
        else:
        
            if HayCuatro():
                return messagebox.showerror("Error","Por favor presione el botón de calificar")
            else:
                Label(canvas,image=Imagen1,relief=FLAT,bg="brown").place(x=InsertarX,y=InsertarY)
                InsertarX=InsertarX+50
                InsertarJugada(1)

    #-----------------------------------------------------------------------------------------------
    #Descripción: En la siguiente funcion le inserta un elemento en el juego, el elemento 2.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
                
    def Insertar2():
        global InsertarY,InsertarX
        if Maximo():
            return messagebox.showinfo("Juego terminado","Ya perdistes")
        else:
            
            if HayCuatro():
                return messagebox.showerror("Error","Por favor presione el botón de calificar")
            else:
                Label(canvas,image=Imagen2,relief=FLAT,bg="brown").place(x=InsertarX,y=InsertarY)
                InsertarX=InsertarX+50
                InsertarJugada(2)

    #--------------------------------------------------------------------
    #Descripción: La siguiente funcion le inserta un elemento 3 al juego.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna
                
    def Insertar3():
        global InsertarY,InsertarX
        if Maximo():
            return messagebox.showinfo("Juego terminado","Ya perdistes")
        else:
            
            if HayCuatro():
                return messagebox.showerror("Error","Por favor presione el botón de calificar")
            else:
                Label(canvas,image=Imagen3,relief=FLAT,bg="brown").place(x=InsertarX,y=InsertarY)
                InsertarX=InsertarX+50
                InsertarJugada(3)

    #--------------------------------------------------------------------
    #Descripción: La siguiente funcion le inserta un elemento 4 al juego.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna
                
    def Insertar4():
        global InsertarY,InsertarX
        if Maximo():
            return messagebox.showinfo("Juego terminado","Ya perdistes")
        else: 
            if HayCuatro():
                return messagebox.showerror("Error","Por favor presione el botón de calificar")
            else:
                Label(canvas,image=Imagen4,relief=FLAT,bg="brown").place(x=InsertarX,y=InsertarY)
                InsertarX=InsertarX+50
                InsertarJugada(4)

    #--------------------------------------------------------------------
    #Descripción: La siguiente funcion le inserta un elemento 5 al juego.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna 
                
    def Insertar5():
        global InsertarY,InsertarX
        if Maximo():
            return messagebox.showinfo("Juego terminado","Ya perdistes")
        else:
            if HayCuatro():
                return messagebox.showerror("Error","Por favor presione el botón de calificar")
            else:
                Label(canvas,image=Imagen5,relief=FLAT,bg="brown").place(x=InsertarX,y=InsertarY)
                InsertarX=InsertarX+50
                InsertarJugada(5)

    #--------------------------------------------------------------------
    #Descripción: La siguiente funcion le inserta un elemento 6 al juego.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna
                               
    def Insertar6():
        global InsertarY,InsertarX
        
        if Maximo():
            return messagebox.showinfo("Juego terminado","Ya perdistes")
        else:
            if HayCuatro():
                return messagebox.showerror("Error","Por favor presione el botón de calificar")
            else:
                Label(canvas,image=Imagen6,relief=FLAT,bg="brown").place(x=InsertarX,y=InsertarY)
                InsertarX=InsertarX+50
                InsertarJugada(6)
                print(NombreJugador,"+++")

    #-------------------------------------------------------------------------------------------
    #Descripción: La siguiente funcion es el complemento de la función calificar poner circulos.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna
    
    def ParteDos(x,x1,Posibles,Jugada,Oponente):
        global ym2,ym1
        Y1=ym1
        Y2=ym2
        cont=2
        while cont != 4:
            if Jugada[Posibles[cont]] == Oponente[Posibles[cont]]:
                canvas.create_oval(x,Y1,x1,Y2,fill="black")
                Y1=Y1-20
                Y2=Y2-20
                cont=cont+1
                continue
            
            if Jugada[Posibles[cont]] in Oponente:
                canvas.create_oval(x,Y1,x1,Y2,fill="yellow")
                Y1=Y1-20
                Y2=Y2-20
                cont=cont+1
                continue
            else:
                cont=cont+1
                continue
        ym2=ym2-50
        ym1=ym1-50

    #-----------------------------------------------------------------------
    #Descripción: La siguiente funcion califica la jugada poniendo circulos.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna
        
    def CalificarPonerCirculos():
        global Jugada,JugadaOponente,xm1,ym1,xm2,ym2
        X1=xm1
        Y1=ym1
        X2=xm2
        Y2=ym2
        Oponente=JugadaOponente[0]
        cont=0
        Posibles=Combinación()
        while cont < 2:
            print(cont)
            if Jugada[Posibles[cont]] == Oponente[Posibles[cont]]:
                canvas.create_oval(X1,Y1,X2,Y2,fill="black")
                Y1=Y1-20
                Y2=Y2-20
                cont=cont+1
                continue
            if Jugada[Posibles[cont]] in Oponente:
                canvas.create_oval(X1,Y1,X2,Y2,fill="yellow")
                Y1=Y1-20
                Y2=Y2-20
                cont=cont+1
                continue
            else:
                cont=cont+1
                continue
        return ParteDos(xm1-20,xm2-20,Posibles,Jugada,Oponente)

    #-----------------------------------------------------------------------------------------------
    #Descripción: La siguiente funcion retorna una lista del ganador contra el juego con cronómetro.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna
    
    def GanoConTiempoJuego():
        global Jugada,segundos,dificultad,NombreJugador,Cronometro,JugadaOponente,CuantoTiempo,reloj
        if reloj == "Si":
            if Cronometro == "Juego":
            
                if segundos < CuantoTiempo: #modificar la varaible CuantoTiempo
                    hora= time.strftime("%X")
                    fecha = time.strftime("%x")
                    listaganador=[NombreJugador,segundos,tuple(Jugada),hora,fecha]
                    print(listaganador)
                    SobreescribeGanador(listaganador)
                    return listaganador
        else:
            return


    #--------------------------------------------------
    #Descripción: La siguiente funcion inicia el juego.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna

    def IniciarGame():
        global reloj,Cronometro,CuantoTiempo,CuantoJugada,tiempo
        CargarListaDeJugadas()
        Diferente()
        Sobrescribir()
        if reloj == "Si":
            tick()
            Label(ventanaJugar,relief=FLAT,bg="#3C3B37",width=11,height=3).place(x=520,y=300)
        else:
            return
        
    ventanaJugar = Toplevel(celular) #Abre una ventana
    ventanaJugar.title("DMaster Mind") #Titulo
    icono = ventanaJugar.iconbitmap("IconoDMasterMind.ico") #Icono de la ventana.
    ventanaJugar.geometry("750x500") #Tamano de la ventana.
    ventanaJugar.config(bg = "peru") #Color de la ventana.
    mini = Frame(ventanaJugar,bg = '#3C3B37',width = 300,height = 300).place(x = 500,y = 270)#Mini ventana.
    mini2 = Frame(ventanaJugar,bg = "#3C3B37",width = 300,height = 250).place(x = 500,y = 0)#Mini ventana.
    canvas = Canvas(ventanaJugar,width = 310,height = 420,bg = "brown",relief = RAISED)#Dibujo de la ventana.
    canvas.place(x = 70,y = 20) #Ubicarlo en las coordenadas 30, 80.
    etiqueta6 = Label(ventanaJugar,text = "Nombre",bg = "#3C3B37 ",fg = "ghost white",font = ("Helvetica",20)).place(x = 500, y = 30) #Se crea una etiqueta y se lo asigna a una variable
    EtiquetaDifi = Label(ventanaJugar,text = NombreJugador,bg = "#3C3B37 ",fg = "ghost white",font = ("Helvetica",15) ).place(x = 600, y = 85) #Se crea una etiqueta y se lo asigna a una variable
    Finaliza = StringVar() #lo define como una variable string
    etiqueta10 = Label(ventanaJugar,text="Finaliza",bg="honeydew2",font=("Helvetica",13)).place(x=670, y=360) #Se crea una etiqueta y se lo asigna a una variable
    #contenia mini en vez de ventanaJugar
    EtiquetaCronometro=Label(ventanaJugar, font=('ubuntu', 18, 'bold'), bg='#3C3B37', fg='white', bd=0)#Se crea una etiqueta y se lo asigna a una variable
    EtiquetaCronometro.place(x=530, y=400)#Se ubica la etiqueta.
    etiqueta9 = Label(ventanaJugar,text = "Cronómetro",bg = "honeydew2",font = ("Helvetica",13)).place(x=520, y=360) #Se crea una etiqueta y se lo asigna a una variable
    EtiquetaFinaliza = Label(ventanaJugar,textvariable=Finaliza,font=('ubuntu', 18, 'bold'), bg='#3C3B37', fg='white', bd=0).place(x=660, y=415)#Se crea una etiqueta y se lo asigna a una variable
    PosicionDeLosElementos() #Utiliza la función
    ConfigurarVariables() #Utiliza la función para configurar.
    TiempoEnSegundos() #Utiliza la función
    #contenia mini en vez de ventanaJugar
    etiqueta8 = Label(ventanaJugar,text = "Dificultad",bg = "#3C3B37",fg = "ghost white",font = ("Helvetica",20)).place(x = 500, y = 145) #Se crea una etiqueta y se lo asigna a una variable
    EtiquetaDifi = Label(ventanaJugar,text = dificultad,bg = "#3C3B37",fg = "ghost white",font = ("Helvetica",15)).place(x = 600, y = 195) #Se crea una etiqueta y se lo asigna a una variable
    Button(ventanaJugar,text="Terminar Juego",command=TerminarJuego,relief=FLAT).place(x=650,y=300) #Se crea un boton y se lo asigna a una variabre.
    Button(ventanaJugar,text="Iniciar Juego",command=IniciarGame,relief=FLAT).place(x=520,y=300) #Se crea un boton y se lo asigna a una variabre.
    Yes = PhotoImage(file="exito.gif") #Se le asigna una imagen
    No = PhotoImage(file = "error.gif") #Se le asigna una imagen
    Button(ventanaJugar,image=Yes,command=Calificar,relief=FLAT,bg="peru").place(x=450,y=405) #Se crea un boton y se lo asigna a una variabre.
    BotonNo = Button(ventanaJugar,image=No,command=Eliminar,relief=FLAT,bg="peru").place(x=400,y=405) #Se crea un boton y se lo asigna a una variabre.
    ImagenVacío = PhotoImage(file="Empty.gif") #Se le asigna una imagen
    #Los elementos que se van a usar
    Lista = Elementos[Panel] #Utiliza la variable global
    Imagen1=PhotoImage(file=Lista[0]) #Se le asigna la imagen que contiene la varoiable global.
    BotonImagen1=Button(ventanaJugar,image=Imagen1,command=Insertar1,bg="peru",relief=FLAT).place(x=PosicionX,y=300) #Se crea un boton y se lo asigna a una variabre.
    Imagen2=PhotoImage(file=Lista[1]) #Se le asigna la imagen que contiene la varoiable global.
    BotonImagen2=Button(ventanaJugar,image=Imagen2,command=Insertar2,bg="peru",relief=FLAT).place(x=PosicionX,y=250) #Se crea un boton y se lo asigna a una variabre.
    Imagen3=PhotoImage(file=Lista[2]) #Se le asigna la imagen que contiene la varoiable global.
    BotonImagen3=Button(ventanaJugar,image=Imagen3,command=Insertar3,bg="peru",relief=FLAT).place(x=PosicionX,y=200) #Se crea un boton y se lo asigna a una variabre.
    Imagen4=PhotoImage(file=Lista[3]) #Se le asigna la imagen que contiene la varoiable global.
    BotonImagen4=Button(ventanaJugar,image=Imagen4,command=Insertar4,bg="peru",relief=FLAT).place(x=PosicionX,y=150) #Se crea un boton y se lo asigna a una variabre.
    Imagen5=PhotoImage(file=Lista[4]) #Se le asigna la imagen que contiene la varoiable global.
    BotonImagen5=Button(ventanaJugar,image=Imagen5,command=Insertar5,bg="peru",relief=FLAT).place(x=PosicionX,y=100) #Se crea un boton y se lo asigna a una variabre.
    Imagen6=PhotoImage(file=Lista[5]) #Se le asigna la imagen que contiene la varoiable global.
    BotonImagen6=Button(ventanaJugar,image=Imagen6,command=Insertar6,bg="peru",relief=FLAT).place(x=PosicionX,y=50) #Se crea un boton y se lo asigna a una variabre.
    Dificultad() #Utiliza la función para crear circulos.
    ventanaJugar.mainloop() 

#------------------------
#Ventana de configuración
#------------------------

def VentanaConfigurar():

    #-------------------------------------
    #Funciones de la ventana configuración
    #-------------------------------------

    #--------------------------------------------------------------------
    #Descripción: La siguiente función cierra la ventana de configuración.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
    
    def CerrarConfiguración():
        ventanaConfigurar.withdraw()

    #------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente función retorna un cuadro de mensaje que le indica la cantidad de tiempo que debe poner.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
    
    def MensajeDeError():
        messagebox.showerror("Error","Ponga cuanto tiempo desea")

    #---------------------------------------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente función se activa cuando el usuario toca el botón de aceptar, y se le asigna la configuración configurado por el usuario.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
        
    def AceptarLaConfiguración():
        
        global dificultad,reloj,posicion,Panel,Cronometro,CuantoTiempo,CuantoJugada
        if Cual.get() != "" :
            dificultad = Cual.get()
        if Elemento.get() != 0:
            if Elemento.get() == 1:
                Panel="Colores"
            if Elemento.get() == 2:
                Panel="Letras"
            if Elemento.get() == 3:
                Panel="Números"
            if Elemento.get() == 4:
                Panel="Emoticones"
        if Posicion.get() !=0:
            if Posicion.get() == 1:
                posicion  = "Izquierda"
            if Posicion.get() == 2:
                posicion  = "Derecha"
        if Valor.get() == 1:
            reloj="Si"
            if Cro.get() == 0:
                Cronometro="Juego"
                if int(segundos.get()) != 0 or int(minutos.get()) != 0 or int(hora.get()) != 0:
                    total=int(segundos.get())+int(minutos.get())*60+int(hora.get())*3600
                    CuantoTiempo = total
                else:
                    return MensajeDeError()
            if Cro.get() == 1:
                Cronometro="Jugada"
                if int(segundosJugada.get()) != 0 or int(minutosJugada.get()) != 0 or int(horaJugada.get()) != 0:
                    total=int(segundosJugada.get())+int(minutosJugada.get())*60+int(horaJugada.get())*3600
                    CuantoJugada = total
                else:
                    return MensajeDeError()
        if Valor.get() == 2:
            reloj="No"
            CuantoTiempo = 0
            CuantoJugada = 0            
        print(dificultad,reloj,posicion,Panel,Cronometro,CuantoTiempo,CuantoJugada)
        SobreescribeConfi()
        CerrarConfiguración()

    #------------------------------------------------------------------------------
    #Descripción: La siguiente función define la dificultad con un rango de números.
    #Entradas: Un número flotante.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def DefinirDificultad(value):
        
        valor=float(value)
        if 0<valor<33:
            
            Cual.set("Fácil")
        if 33 < valor <66:
            
            Cual.set("Medio")
            
        if 66<valor<100:
            
            Cual.set("Difícil")

    #---------------------
    #Ventana configuración
    #---------------------
    
    ventanaConfigurar = Toplevel(celular) #Se crea una ventana.
    ventanaConfigurar.title("DMaster Mind") #Titulo de la ventana.
    ventanaConfigurar.geometry("310x700") #Tamaño de la ventana.
    ventanaConfigurar.maxsize(310,550) #El tamaño máximo que se puede agrandar o minimizar la pantalla.
    ventanaConfigurar.config(bg = "DeepSkyBlue4") #Configura el color de la ventana.
    no = PhotoImage(file = "error.gif") #A la imagen de equis o no se le asigna a la variable no.
    si = PhotoImage(file = "exito.gif") #A la imagen de check o si se le asigna a la variable si.
    EtiquetaConsulta = Label(ventanaConfigurar,bg = "DeepSkyBlue2",width = 50,height = 4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    TextoNombre = Label(ventanaConfigurar,text="Configurar",fg="white",relief=FLAT,bg="DeepSkyBlue2",font=("systemfixed",11,"bold")).place(x=110,y=25) #Se le asigna una etiqueta a la variable.
    notebook = ttk.Notebook(ventanaConfigurar,height = 306,width = 290) #Sea un nootebook dentro de la ventana.
    notebook.place(x=7,y=90) #Ubica el nootebook en esa posición x,y.
    fram1 = Frame(notebook,bg="light sky blue",relief = GROOVE,bd = 1)#Se crea ventanillas para el nootebook o cuaderno
    fram1.pack(fill=BOTH, expand = True) #Se empaca 
    fram2 = Frame(notebook,bg="light sky blue",relief = GROOVE,bd = 1) #Se crea ventanillas para el nootebook o cuaderno
    fram2.place(x=10,y=10)#Se empaca
    fram3 = Frame(notebook,bg="light sky blue",relief = GROOVE,bd = 1) #Se crea ventanillas para el nootebook o cuaderno
    fram3.place(x=10,y=10)#Lo ubica en el eje x a 10 pxeles y en el eje y a 10 pixeles.
    fram4 = Frame(notebook,bg="light sky blue",relief = GROOVE,bd = 1) #Se crea una etiqueta o Tab.
    fram4.pack(fill = BOTH, expand = True)
    tab2 = notebook.add(fram2,text = "Dificultad",padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de consultar.
    tab1 = notebook.add(fram1,text = "Reloj",padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    tab3 = notebook.add(fram3,text = "Posición",padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de eliminar. 
    tab4 = notebook.add(fram4,text = "Elementos",padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de modificar.
    BotonSi=Button(ventanaConfigurar,image=si,command=AceptarLaConfiguración,bg="DeepSkyBlue4",relief=FLAT).place(x=70,y=460) #Se crea un boton con la variable de la imagen si, aceptar.
    BotonNo=Button(ventanaConfigurar,command=CerrarConfiguración,image=no,bg="DeepSkyBlue4",relief=FLAT).place(x=200,y=460) #Se crea un boton con la variable de la imagen no, de cancelar.
    segundos = IntVar() #Se le asigna el valor de string a una variable.
    minutos = IntVar() #Se le asigna el valor de string a una variable.
    hora = IntVar() #Se le asigna el valor de string a una variable.
    ttk.Combobox(fram1,textvariable = hora,values =[0,1,2],width = 2).place(x=70,y=250) #Se le agrega un combobox, al frame de reloj.
    ttk.Combobox(fram1,textvariable = minutos,values =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59],width = 2).place(x=120,y=250) #Se le asigna un combobox con los valores de los minutos.
    ttk.Combobox(fram1,textvariable = segundos,values =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59],width = 2).place(x=170,y=250) #Se le asigna un combobox con los valores de los segundos.
    segundosJugada = IntVar() #Se le asigna el valor de string a una variable.
    minutosJugada = IntVar() #Se le asigna el valor de string a una variable.
    horaJugada = IntVar() #Se le asigna el valor de string a una variable.
    ttk.Combobox(fram1,textvariable = horaJugada,values =[0,1,2],width = 2).place(x=70,y=170) #Se le agrega un combobox, al frame de reloj.
    ttk.Combobox(fram1,textvariable = minutosJugada,values =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59],width = 2).place(x=120,y=170) #Se le asigna un combobox con los valores de los minutos.
    ttk.Combobox(fram1,textvariable = segundosJugada,values =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59],width = 2).place(x=170,y=170) #Se le asigna un combobox con los valores de los segundos.                                                                                                                                                                                                                                                                                                                                                                                                                     
    dificultad =IntVar() #Se le asigna una variable entero.
    Cual=StringVar() #Se le asigna una variable string.
    ttk.Scale(fram2, from_=0, to_=100, length=200,variable=dificultad,command= DefinirDificultad ).place(x=35,y=70) #Se define un widget scala.
    TextoDificultad = Label(fram2,height=1,width=10,text="Dificultad",fg="white",relief=FLAT,bg="light sky blue",font=("systemfixed",11,"bold")).place(x=8,y=20) #Se le asigna una etiqueta a la variable.
    TextoDificultad1 = Label(fram2,textvariable=Cual,fg="white",relief=FLAT,bg="light sky blue",font=("systemfixed",8,"bold")).place(x=110,y=110) #Se le asigna una etiqueta a la variable.
    Descripcion = Label(fram2,text="Descripción",fg="white",relief=FLAT,bg="light sky blue",font=("systemfixed",8,"bold")).place(x=20,y=160) #Se le asigna una etiqueta a la variable.
    Facil = Label(fram2,text="Fácil",fg="white",relief=FLAT,bg="light sky blue",font=("systemfixed",8,"bold")).place(x=20,y=180) #Se le asigna una etiqueta a la variable.
    Medio = Label(fram2,text="Medio",fg="white",relief=FLAT,bg="light sky blue",font=("systemfixed",8,"bold")).place(x=20,y=200) #Se le asigna una etiqueta a la variable.
    Dificil = Label(fram2,text="Difícil",fg="white",relief=FLAT,bg="light sky blue",font=("systemfixed",8,"bold")).place(x=20,y=220) #Se le asigna una etiqueta a la variable.
    FacilDes = Label(fram2,text="8 Jugadas permitidas",fg="white",relief=FLAT,bg="light sky blue",font=("systemfixed",8,"bold")).place(x=100,y=180) #Se le asigna una etiqueta a la variable.
    MedioDes = Label(fram2,text="7 Jugadas permitidas",fg="white",relief=FLAT,bg="light sky blue",font=("systemfixed",8,"bold")).place(x=100,y=200) #Se le asigna una etiqueta a la variable.
    DificilDes = Label(fram2,text="6 Jugadas permitidas",fg="white",relief=FLAT,bg="light sky blue",font=("systemfixed",8,"bold")).place(x=100,y=220) #Se le asigna una etiqueta a la variable.
    Valor = IntVar()#Se le asigna una variable entero.
    Cro = IntVar()#Se le asigna una variable entero.
    TextoReloj = Label(fram1,height=1,width=10,text="Reloj",fg="white",relief=FLAT,bg="light sky blue",font=("systemfixed",11,"bold")).place(x=8,y=20) #Se le asigna una etiqueta a la variable.
    Radiobutton(fram1,bg="light sky blue",variable=Valor,value=1,text="Si",fg="white").place(x=80,y=80) #Se le coloca un radiobutton al frame de reloj
    Radiobutton(fram1,bg="light sky blue",variable=Valor,value=2,text="No",fg="white").place(x=140,y=80)#Se le coloca un radiobutton al frame de reloj
    Radiobutton(fram1,bg="light sky blue",text="Cronómetro por jugada",variable=Cro,value=1).place(x=50,y=130)#Se le coloca un radiobutton al frame de reloj
    Radiobutton(fram1,bg="light sky blue",text="Cronómetro por juego",variable=Cro,value=0).place(x=50,y=200)#Se le coloca un radiobutton al frame de reloj
    Posicion = IntVar()#Se le asigna una variable entero.
    TextoPosición = Label(fram3,text="Posición del panel de elementos",fg="white",relief=FLAT,bg="light sky blue",font=("systemfixed",11,"bold")).place(x=8,y=20) #Se le asigna una etiqueta a la variable.
    Radiobutton(fram3,bg="light sky blue",variable=Posicion,value=1,text="Izquierda",fg="white").place(x=50,y=80)#Se le coloca un radiobutton al frame de reloj
    Radiobutton(fram3,bg="light sky blue",variable=Posicion,value=2,text="Derecha",fg="white").place(x=140,y=80)#Se le coloca un radiobutton al frame de reloj
    Elemento=IntVar()#Se le asigna una variable entero.
    Radiobutton(fram4,bg="light sky blue",value=1,variable=Elemento,text="Colores",fg="white").place(x=10,y=10)#Se le coloca un radiobutton al frame de reloj
    Radiobutton(fram4,bg="light sky blue",value=2,variable=Elemento,text="Letras",fg="white").place(x=10,y=80)#Se le coloca un radiobutton al frame de reloj
    Radiobutton(fram4,bg="light sky blue",value=3,variable=Elemento,text="Números",fg="white").place(x=10,y=150)#Se le coloca un radiobutton al frame de reloj
    Radiobutton(fram4,bg="light sky blue",value=4,variable=Elemento,text="Emoticones",fg="white").place(x=10,y=220)#Se le coloca un radiobutton al frame de reloj
    Verde = PhotoImage(file = "Earth.gif") #A la imagen se le asigna a la variable.
    Blanco = PhotoImage(file = "luna.gif") #A la imagen se le asigna a la variable.
    Amarillo = PhotoImage(file = "jupiter.gif") #A la imagen se le asigna a la variable.
    Negro = PhotoImage(file = "negro.gif") #A la imagen se le asigna a la variable.
    Naranja = PhotoImage(file = "circulo.gif") #A la imagen se le asigna a la variable.
    Azul = PhotoImage(file = "oval.gif") #A la imagen se le asigna a la variable.
    Label(fram4,image=Verde,bg="light sky blue").place(x=20,y=40) #Se le asigna una etiqueta a la variable.
    Label(fram4,image=Blanco,bg="light sky blue").place(x=60,y=40) #Se le asigna una etiqueta a la variable.
    Label(fram4,image=Amarillo,bg="light sky blue").place(x=100,y=40) #Se le asigna una etiqueta a la variable.
    Label(fram4,image=Negro,bg="light sky blue").place(x=140,y=40) #Se le asigna una etiqueta a la variable.
    Label(fram4,image=Naranja,bg="light sky blue").place(x=180,y=40) #Se le asigna una etiqueta a la variable.
    Label(fram4,image=Azul,bg="light sky blue").place(x=220,y=40) #Se le asigna una etiqueta a la variable.
    uno = PhotoImage(file = "uno.gif") #A la imagen se le asigna a la variable.
    dos = PhotoImage(file = "dos.gif") #A la imagen se le asigna a la variable.
    tres = PhotoImage(file = "tres.gif") #A la imagen se le asigna a la variable.
    cuatro = PhotoImage(file = "cuatro.gif") #A la imagen se le asigna a la variable.
    cinco = PhotoImage(file = "cinco.gif") #A la imagen se le asigna a la variable.
    seis = PhotoImage(file = "seis.gif") #A la imagen se le asigna a la variable.
    Label(fram4,image=uno,bg="light sky blue").place(x=20,y=180)#Se le asigna una etiqueta a la variable.
    Label(fram4,image=dos,bg="light sky blue").place(x=60,y=180)#Se le asigna una etiqueta a la variable.
    Label(fram4,image=tres,bg="light sky blue").place(x=100,y=180)#Se le asigna una etiqueta a la variable.
    Label(fram4,image=cuatro,bg="light sky blue").place(x=140,y=180)#Se le asigna una etiqueta a la variable.
    Label(fram4,image=cinco,bg="light sky blue").place(x=180,y=180)#Se le asigna una etiqueta a la variable.
    Label(fram4,image=seis,bg="light sky blue").place(x=220,y=180)#Se le asigna una etiqueta a la variable.
    tranquilo = PhotoImage(file = "tranquilo.gif")#A la imagen se le asigna a la variable.
    Label(fram4,image=tranquilo,bg="light sky blue").place(x=20,y=245)#Se le asigna una etiqueta a la variable.
    confundido=PhotoImage(file="confundido.gif")#A la imagen se le asigna a la variable.
    Label(fram4,image=confundido,bg="light sky blue").place(x=60,y=245)#Se le asigna una etiqueta a la variable.
    enfermo=PhotoImage(file="enfermo.gif")#A la imagen se le asigna a la variable.
    Label(fram4,image=enfermo,bg="light sky blue").place(x=100,y=245)#Se le asigna una etiqueta a la variable.
    sorprendido=PhotoImage(file="sorprendido.gif")#A la imagen se le asigna a la variable.
    Label(fram4,image=sorprendido,bg="light sky blue").place(x=140,y=245)#Se le asigna una etiqueta a la variable.
    feliz=PhotoImage(file="feliz.gif")#A la imagen se le asigna a la variable.
    Label(fram4,image=feliz,bg="light sky blue").place(x=180,y=245)#Se le asigna una etiqueta a la variable.
    ninja=PhotoImage(file="ninja.gif")#A la imagen se le asigna a la variable.
    Label(fram4,image=ninja,bg="light sky blue").place(x=220,y=245)#Se le asigna una etiqueta a la variable.
    A=PhotoImage(file="A.gif")#A la imagen se le asigna a la variable.
    Label(fram4,image=A,bg="light sky blue").place(x=20,y=110)#Se le asigna una etiqueta a la variable.
    B=PhotoImage(file="B.gif")#A la imagen se le asigna a la variable.
    Label(fram4,image=B,bg="light sky blue").place(x=60,y=110)#Se le asigna una etiqueta a la variable.
    C=PhotoImage(file="C.gif")#A la imagen se le asigna a la variable.
    Label(fram4,image=C,bg="light sky blue").place(x=100,y=110)#Se le asigna una etiqueta a la variable.
    D=PhotoImage(file="D.gif")#A la imagen se le asigna a la variable.
    Label(fram4,image=D,bg="light sky blue").place(x=140,y=110)#Se le asigna una etiqueta a la variable.
    E=PhotoImage(file="E.gif")#A la imagen se le asigna a la variable.
    Label(fram4,image=E,bg="light sky blue").place(x=180,y=110)#Se le asigna una etiqueta a la variable.
    F=PhotoImage(file="F.gif")#A la imagen se le asigna a la variable.
    Label(fram4,image=F,bg="light sky blue").place(x=220,y=110)#Se le asigna una etiqueta a la variable.
    ventanaConfigurar.mainloop() #Espera hasta que el usuario haga un evento.

#---------------------------------
#Ventana Acerca de la aplicación
#---------------------------------

def VentanaAcercaDe():
    
    ventanaAcercaDe = Toplevel(celular) #Se crea una ventana.
    ventanaAcercaDe.title("DMaster Mind") #Titulo de la ventana.
    ventanaAcercaDe.geometry("310x700") #Tamano de la ventana.
    ventanaAcercaDe.maxsize(310,550) #El tamano mÃ¡ximo que se puede agrandar o minimizar la pantalla.
    ventanaAcercaDe.config(bg = "DeepSkyBlue4") #Configura el color de la ventana.
    EtiquetaAcercaDe = Label(ventanaAcercaDe,bg = "DeepSkyBlue2",width = 50,height = 4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    TextoAcercaDe = Label(ventanaAcercaDe,text="Acerca de",fg="white",relief=FLAT,bg="DeepSkyBlue2",font=("systemfixed",11,"bold")).place(x=120,y=25) #Se le asigna una etiqueta a la variable.
    titulo2 = Label(ventanaAcercaDe,text="Actualizaciones",fg="white",relief=FLAT,width=25,height=2,bg="orange",font=("ms sans Serif",10,"bold")).place(x=40,y=100) #Se le asigna una etiqueta a la variable.
    titulo3 = Label(ventanaAcercaDe,text="Nombre de la APP",fg="white",relief=FLAT,bg="orange",width=25,height=2,font=("ms sans Serif",10,"bold")).place(x=40,y=260) #Se le asigna una etiqueta a la variable.
    title5 = Label(ventanaAcercaDe,text="DMaster Mind",fg="white",relief=FLAT,width=25,height=2,bg="RoyalBlue4",font=("ms sans Serif",8,"bold")).place(x=70,y=300) #Se le asigna una etiqueta a la variable
    title = Label(ventanaAcercaDe,text="Proximamente",fg="white",relief=FLAT,width=25,height=2,bg="RoyalBlue4",font=("ms sans Serif",8,"bold")).place(x=70,y=140) #Se le asigna una etiqueta a la variable.
    titulo4 = Label(ventanaAcercaDe,text="Versión",fg="white",relief=FLAT,bg="orange",width=25,height=2,font=("ms sans Serif",10,"bold")).place(x=40,y=180) #Se le asigna una etiqueta a la variable.
    title2 = Label(ventanaAcercaDe,text="0.0.1",fg="white",relief=FLAT,width=25,height=2,bg="RoyalBlue4",font=("ms sans Serif",8,"bold")).place(x=70,y=220) #Se le asigna una etiqueta a la variable
    titulo5 = Label(ventanaAcercaDe,text="Fecha de creación",fg="white",relief=FLAT,width=25,height=2,bg="orange",font=("ms sans Serif",10,"bold")).place(x=40,y=340) #Se le asigna una etiqueta a la variable.
    title3 = Label(ventanaAcercaDe,text="16 de Octubre del 2016",fg="white",relief=FLAT,width=25,height=2,bg="RoyalBlue4",font=("ms sans Serif",8,"bold")).place(x=70,y=380) #Se le asigna una etiqueta a la variable
    titulo7 = Label(ventanaAcercaDe,text="Creador",fg="white",relief=FLAT,bg="orange",width=25,height=2,font=("ms sans Serif",10,"bold")).place(x=40,y=420) #Se le asigna una etiqueta a la variable.
    title4 = Label(ventanaAcercaDe,text="Danny Xie Li",fg="white",relief=FLAT,width=25,height=2,bg="RoyalBlue4",font=("ms sans Serif",8,"bold")).place(x=70,y=460) #Se le asigna una etiqueta a la variable
    ventanaAcercaDe.mainloop() #Espera que el usuario interactue con la pantalla

#--------------------
#Parte de Top 10
#--------------------

#-----------------------------------------------------------------------
#Descripción: La siguiente función retorna sólo el tiempo de las listas.
#Entradas: Un string y una lista.
#Salidas: Una lista.
#Restricciones: Sólo strings y listas.
        
def SóloPorTiempo(dificultadConsultar,DatosDeLosGanadores):
    
    ListaNivel = SóloNivel(DatosDeLosGanadores,dificultadConsultar)#Formato de DatosDeLosGanadores [ ["Fácil",[["Juan",12,12,12,12],["Pedro",122,144,155,166]]],["Medio",[]],["Dificil",[]] ]
    LosPrimeros10 = []
    for i in ListaNivel[1]:
        LosPrimeros10 = LosPrimeros10 + [i[1]]
        print(i)
    return LosPrimeros10

#-------------------------------------------------------------------------------------
#Descripción: La siguiente función ordena los tiempos segun los jugadores que tiene.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.

def OrdenarTiempos(lista): #[12,3254,32]
    ListaTiempo = []
    l = lista
    for i in range(len(lista)):
        ListaTiempo = [max(l)] + ListaTiempo 
        l.remove(max(l))
    return ListaTiempo

#------------------------------------------------------------------------------------------
#Descripción: La siguiente funcion ordena la lista segun el tiempo que duro completandolo.
#Entradas: Una lista y un string.
#Salidas: Una lista.
#Restricciones: Sólo listas y strings.

def OrdenadoListo(DatosDeLosGanadores,dificultadConsultar):
    
    ListaNivel = SóloNivel(DatosDeLosGanadores,dificultadConsultar)
    Time = OrdenarTiempos(SóloPorTiempo(dificultadConsultar,DatosDeLosGanadores))
    lista = []
    for i in Time:
        for j in ListaNivel[1]:
            if j[1] == i:
                lista = lista + [j]
            else:
                continue
    return lista #Formato [['Juan', 12, 12, 12, 12], ['Pedro', 122, 144, 155, 166]]

#-----------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna solo la lista que posea el nivel que estaba buscando.
#Entradas: Una lista y un string.
#Salidas: Una lista.
#Restricciones: Sólo listas y strings.

def SóloNivel(lista,nivel):
    for i in lista:
        if i[0] == nivel:
            return i
        else:
            continue
        
#-----------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función abre una ventana pidiendo el nombre de la dificultad que desea consultar.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.
    
def NombreDelDificultad():

    #-------------------------------------------------------------------------
    #Descripción: La siguiente función acepta el nombre que digitó el usuario.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
    
    def AceptarDificultad():
        global DificultadConsultar
        if Difi.get() == "":
            return EscribaDifi()
        if Difi.get() == "Fácil" or Difi.get() == "Medio" or Difi.get() == "Difícil":
            DificultadConsultar = Difi.get()
            print("Nombre de la dificultad", DificultadConsultar)
            VentanaDifi.destroy()
            VentanaTop10()
        else:
            return messagebox.showerror("Error","Escriba una dificultad. Puede ser Fácil, Medio, Difícil.")

    #--------------------------------------------------------------------------
    #Descripción: La siguiente función cierra la ventana de Ventana dificultad.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def Cerrar():
        VentanaDifi.withdraw()
    
    VentanaDifi = Toplevel(celular)# Toplevel(VentanaDMasterMind)
    no = PhotoImage(file = "error.gif") #A la imagen de equis o no se le asigna a la variable no.
    si = PhotoImage(file = "exito.gif") #A la imagen de check se le asigna a la variable si.
    VentanaDifi.geometry("205x300")#Tamano de la ventana.
    VentanaDifi.title("DMaster Mind") #Titulo de la ventana.
    VentanaDifi.config(bg="DeepSkyBlue4") #Configura el color de la ventana.
    VentanaDifi.maxsize(305,400) #Tamano maximo de la ventana.
    icono = VentanaDifi.iconbitmap("IconoDMasterMind.ico") #Icono de la ventana.   "ms sans Serif"
    EtiquetaNombre = Label(VentanaDifi,bg="DeepSkyBlue2",width=50,height=4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    TextoNombre = Label(VentanaDifi,text="Digite la dificultad",fg="white",relief=FLAT,bg="DeepSkyBlue2",font=("systemfixed",11,"bold")).place(x=45,y=25) #Se le asigna una etiqueta a la variable.    NombreJugador = StringVar()
    Difi = StringVar() #Le asigna una variable string a la variable.
    CampoDifi = Entry(VentanaDifi,relief=FLAT,textvariable =Difi).place(x=40,y=140) #Le asigna un espacio en blanco a una variable.
    BotonSi=Button(VentanaDifi,image=si,command=AceptarDificultad,bg="DeepSkyBlue4",relief=FLAT).place(x=50,y=250) #Se crea un boton con la variable de la imagen si, aceptar.
    BotonNo=Button(VentanaDifi,image=no,command=Cerrar,bg="DeepSkyBlue4",relief=FLAT).place(x=120,y=250) #Se crea un boton con la variable de la imagen no, de cancelar.
    VentanaDifi.mainloop()

#-----------------------------
#Ventana de Top 10 Resumen
#-----------------------------
    
def VentanaTop10():
    global DificultadConsultar

    #--------------------------------------------------------------------------
    #Descripción: La siguiente función cierra la ventana de Ventana de top 10 resumen.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
    
    def CerrarVentanaTop10():
        VentanaTop10Resumen.withdraw()

    #------------------------------------------------------------------------------------
    #Descripción: La siguiente función agrega información a la ventana de Top 10 resumen.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def AgregarTop10():
        global DatosDeLosGanadores,DificultadConsultar
        lista = OrdenadoListo(DatosDeLosGanadores,DificultadConsultar) ###Falta carga los datpos y sustituir los valores por valores globales 
        fila = 1
        cont = 0
        Label(frameDeCanvas1,fg = "black",text = "Jugador",font = ("ms sans Serif",10,"bold")).grid(row=0,column=2)
        Label(frameDeCanvas1,fg = "black",text = "Tiempo",font = ("ms sans Serif",10,"bold")).grid(row=0,column=3)
               
        for i in lista:
            if cont == 10:
                return
            else:
                Label(frameDeCanvas1,fg = "black",text = i[0],font = ("ms sans Serif",10,"bold")).grid(row=fila,column=2)
                Label(frameDeCanvas1,fg = "black",text = i[1],font = ("ms sans Serif",10,"bold")).grid(row=fila,column=3)
                fila = fila + 1
                cont = cont + 1

    #--------------------------------------------------------------------------------
    #Descripción: La siguiente función configura el scrollbar esperando algún evento.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def EventosConsultar(eventos):
        canvasConsultar.configure(scrollregion=canvasConsultar.bbox("all"),width=250,height=280)
    
    VentanaTop10Resumen = Toplevel(celular)
    VentanaTop10Resumen.title("DMaster Mind") #Titulo de la ventana.
    VentanaTop10Resumen.geometry("310x550") #Tamano de la ventana.
    VentanaTop10Resumen.maxsize(310,550) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    VentanaTop10Resumen.config(bg = "DeepSkyBlue4") #Configura el color de la ventana.
    EtiquetaTop10 = Label(VentanaTop10Resumen,bg = "DeepSkyBlue2",width = 50,height = 4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    TextoTop10 = Label(VentanaTop10Resumen,text="Top 10 Resumen",fg="white",relief=FLAT,bg="DeepSkyBlue2",font=("systemfixed",11,"bold")).place(x=90,y=25) #Se le asigna una etiqueta a la variable.
    no = PhotoImage(file = "error.gif") #A la imagen de equis o no se le asigna a la variable no.
    si = PhotoImage(file = "exito.gif") #A la imagen de check se le asigna a la variable si.
    botonSi = Button(VentanaTop10Resumen,comman=CerrarVentanaTop10,image=si,bg="DeepSkyBlue4",relief=FLAT).place(x=70,y=480) #Se le asigna un boton a una variable.
    botonNo = Button(VentanaTop10Resumen,command=CerrarVentanaTop10,image=no,bg="DeepSkyBlue4",relief=FLAT).place(x=200,y=480) #Se le asigna un boton a una variable.
    notebook = ttk.Notebook(VentanaTop10Resumen,height=320,width=290) #Sea un nootebook dentro de la ventana.
    notebook.place(x=7,y=110) #Ubica el nootebook en esa posición x,y.
    fram1 = Frame(notebook,relief = GROOVE,bd = 1)#Se crea ventanillas para el nootebook o cuaderno
    fram1.pack(fill=BOTH, expand = True) #Se empaca 
    canvasConsultar = Canvas(fram1,width = 500,height = 200) #Se crea una ventana dentro del fram1
    frameDeCanvas1 = Frame(canvasConsultar) #Se crea una ventana dentro del canvas.
    Barra1=Scrollbar(fram1,orient = "vertical",command = canvasConsultar.yview) #Se crea un scrollbar.
    canvasConsultar.configure(yscrollcommand = Barra1.set) #Se configura el scrollbar.
    Barra1.pack(side = "right",fill = "y") #Se empaca el scrollbar.
    canvasConsultar.pack(side = "left") #Se empaca el canvas o ventana creado.
    canvasConsultar.create_window((0,0),window = frameDeCanvas1,anchor = 'nw') #Se crea una ventana en el canvas.
    frameDeCanvas1.bind("<Configure>",EventosConsultar) #En la ventana del canvas espera hasta que ocurra un evento y llama a la función EventosConsultar.
    tab1 = notebook.add(fram1,text = "Top 10",padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    AgregarTop10() #Utiliza la función para  agregar datos.
    VentanaTop10Resumen.mainloop() #Espera hasta que la ventana se cierre o el usuario interactúe en el.           
    
#-----------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función abre una ventana pidiendo el nombre de la dificultad que desea consultar.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.
    
def NombreDelDificultadDetalle():

    #-------------------------------------------------------------------------
    #Descripción: La siguiente función acepta el nombre que digitó el usuario.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
    
    def AceptarDificultad():
        global DificultadConsultar
        if Difi.get() == "":
            return EscribaDifi()
        if Difi.get() == "Fácil" or Difi.get() == "Medio" or Difi.get() == "Difícil":
            DificultadConsultar = Difi.get()
            print("Nombre de la dificultad", DificultadConsultar)
            VentanaDifiDetalle.destroy()
            VentanaDetalle()
        else:
            return messagebox.showerror("Error","Escriba una dificultad. Puede ser Fácil, Medio, Difícil.")

    #--------------------------------------------------------------------------
    #Descripción: La siguiente función cierra la ventana de Ventana dificultad.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def Cerrar():
        VentanaDifiDetalle.withdraw()
    
    VentanaDifiDetalle = Toplevel(celular)# Toplevel(VentanaDMasterMind)
    no = PhotoImage(file = "error.gif") #A la imagen de equis o no se le asigna a la variable no.
    si = PhotoImage(file = "exito.gif") #A la imagen de check se le asigna a la variable si.
    VentanaDifiDetalle.geometry("205x300") #Configura el tamano de la ventana.
    VentanaDifiDetalle.title("DMaster Mind") #Titulo de la ventana.
    VentanaDifiDetalle.config(bg="DeepSkyBlue4") #Configura el color de la ventana.
    VentanaDifiDetalle.maxsize(305,400) #El tamano maximo de la ventana.
    icono = VentanaDifiDetalle.iconbitmap("IconoDMasterMind.ico") #Icono de la ventana.   "ms sans Serif"
    EtiquetaNombre = Label(VentanaDifiDetalle,bg="DeepSkyBlue2",width=50,height=4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    TextoNombre = Label(VentanaDifiDetalle,text="Digite la dificultad",fg="white",relief=FLAT,bg="DeepSkyBlue2",font=("systemfixed",11,"bold")).place(x=45,y=25) #Se le asigna una etiqueta a la variable.    NombreJugador = StringVar()
    Difi = StringVar() #Le asigna una variable string a una variable.
    CampoDifi = Entry(VentanaDifiDetalle,relief=FLAT,textvariable =Difi).place(x=40,y=140) #Le asigna un campo de texto a una variable.
    BotonSi=Button(VentanaDifiDetalle,image=si,command=AceptarDificultad,bg="DeepSkyBlue4",relief=FLAT).place(x=50,y=250) #Se crea un boton con la variable de la imagen si, aceptar.
    BotonNo=Button(VentanaDifiDetalle,image=no,command=Cerrar,bg="DeepSkyBlue4",relief=FLAT).place(x=120,y=250) #Se crea un boton con la variable de la imagen no, de cancelar.
    VentanaDifiDetalle.mainloop()


#--------------------------
#Ventana de Top 10 detalles
#--------------------------

def VentanaDetalle():
    
    #--------------------------------------------------------------------------
    #Descripción: La siguiente función agrega elementos(labels) a la pantalla. 
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
    
    def AgregarTopDetalle10():
        global DificultadConsultar,DatosDeLosGanadores
        lista =OrdenadoListo(DatosDeLosGanadores,DificultadConsultar)
        fila=20
        cont=0
        Label(frameDeCanvas1,fg="black",text="Nombre",font=("ms sans Serif",8,"bold")).place(x=-3,y=0)#.grid(row=0,column=0)
        Label(frameDeCanvas1,fg="black",text="Tiempo",font=("ms sans Serif",8,"bold")).place(x=50,y=0)
        Label(frameDeCanvas1,fg="black",text="Jugada",font=("ms sans Serif",8,"bold")).place(x=97,y=0)
        Label(frameDeCanvas1,fg="black",text="Hora",font=("ms sans Serif",8,"bold")).place(x=144,y=0)
        Label(frameDeCanvas1,fg="black",text="Fecha",font=("ms sans Serif",8,"bold")).place(x=191,y=0)
        for i in lista:
            if cont == 10:
                return
            else:
                Label(frameDeCanvas1,fg="black",text=i[0],font=("ms sans Serif",10,"bold")).place(x=-3,y=fila)#.grid(row=0,column=0)
                Label(frameDeCanvas1,fg="black",text=ConvertirStringATiempo(i[1]),font=("ms sans Serif",5,"bold")).place(x=50,y=fila)
                Label(frameDeCanvas1,fg="black",text=i[2],font=("ms sans Serif",5,"bold")).place(x=97,y=fila)
                Label(frameDeCanvas1,fg="black",text=i[3],font=("ms sans Serif",5,"bold")).place(x=144,y=fila)
                Label(frameDeCanvas1,fg="black",text=i[4],font=("ms sans Serif",5,"bold")).place(x=191,y=fila)
                fila=fila+20
                cont=cont+1
                
    #-------------------------------------------------------------------------------------------
    #Descripción: La siguiente función configura el scrollbar de la pantalla de top 10 detalles.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
                
    def EventosConsultar(eventos):
        canvasConsultar.configure(scrollregion=canvasConsultar.bbox("all"),width=250,height=280)

    #---------------------------------------------------------------------------
    #Descripción: La siguiente función cierra la ventana de ventanadetalletop10.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def CerrarDetalle():
        VentanaDetalleTop10.withdraw()

    #-------------------------------------
    #Código de la ventana para top detalle
    #-------------------------------------
        
    VentanaDetalleTop10 = Toplevel(celular)
    VentanaDetalleTop10.title("DMaster Mind") #Titulo de la ventana.
    VentanaDetalleTop10.geometry("350x550") #Tamano de la ventana.
    VentanaDetalleTop10.maxsize(550,600) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    VentanaDetalleTop10.config(bg = "DeepSkyBlue4") #Configura el color de la ventana.
    EtiquetaTop10 = Label(VentanaDetalleTop10,bg = "DeepSkyBlue2",width = 100,height = 4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    TextoTop10 = Label(VentanaDetalleTop10,text="Top 10 Detalle",fg="white",relief=FLAT,bg="DeepSkyBlue2",font=("systemfixed",11,"bold")).place(x=130,y=25) #Se le asigna una etiqueta a la variable.
    no = PhotoImage(file = "error.gif") #A la imagen de equis o no se le asigna a la variable no.
    si = PhotoImage(file = "exito.gif") #A la imagen de check se le asigna a la variable si.
    botonSi = Button(VentanaDetalleTop10,command=CerrarDetalle,image=si,bg="DeepSkyBlue4",relief=FLAT).place(x=100,y=480) #Se le asigna un boton a una variable.
    botonNo = Button(VentanaDetalleTop10,command=CerrarDetalle,image=no,bg="DeepSkyBlue4",relief=FLAT).place(x=230,y=480) #Se le asigna un boton a una variable.
    notebook = ttk.Notebook(VentanaDetalleTop10,height=320,width=320) #Sea un nootebook dentro de la ventana.
    notebook.place(x=7,y=110) #Ubica el nootebook en esa posición x,y.
    fram1 = Frame(notebook,relief = GROOVE,bd=1)#Se crea ventanillas para el nootebook o cuaderno
    fram1.pack(fill=BOTH, expand = True) #Se empaca 
    canvasConsultar = Canvas(fram1,width = 600,height = 800) #Se crea una ventana dentro del fram1
    frameDeCanvas1 = Frame(canvasConsultar,width=900,height=500) #Se crea una ventana dentro del canvas.
    Barra1=Scrollbar(fram1,orient = "vertical",command = canvasConsultar.yview) #Se crea un scrollbar.
    canvasConsultar.configure(yscrollcommand = Barra1.set) #Se configura el scrollbar.
    Barra1.pack(side = "right",fill = "y") #Se empaca el scrollbar.
    canvasConsultar.pack(side = "left") #Se empaca el canvas o ventana creado.
    canvasConsultar.create_window((0,0),window = frameDeCanvas1,anchor = 'nw') #Se crea una ventana en el canvas.
    frameDeCanvas1.bind("<Configure>",EventosConsultar) #En la ventana del canvas espera hasta que ocurra un evento y llama a la función EventosConsultar.
    AgregarTopDetalle10() #Utiliza la función para agregar datos a la ventana.
    tab1 = notebook.add(fram1,text = "Top 10 detalles",padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    VentanaDetalleTop10.mainloop() #Esperar hasta que la ventana se cierre o interactue en el.

#-------------------------------------
#Ventana para pedir nombre del jugador
#-------------------------------------

def NombreDelJugador():
    
    #Descripción: La siguiente función recoge el nombre escrito por el usuario.
    #Entradas: Ninguna.
    #Salidas:  Ninguna.
    #Restricciones: Ninguna.
    
    def AceptarNombre():
        global NombreJugador
        if Name.get() == "":
            return EscribaNombre()
        if 1 >= ContarString(Name.get()) or ContarString(Name.get()) >30:
            return messagebox.showerror("Error","Escriba un nombre entre 2 a 30 letras")
        else:
            NombreJugador = Name.get()
            print("Nombre del jugador", NombreJugador)
            PonerConfiguración()
            VentanaNombre.withdraw()
            return VentanaJugar()

    #Descripción: La siguiente función cierra la ventana de VentanaNombre.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
    
    def Cerrar():
        VentanaNombre.withdraw()

    
    #--------------------------------------------
    #Código de la ventana para obtener el nombre.
    #--------------------------------------------
    
    VentanaNombre = Toplevel(celular)
    no = PhotoImage(file = "error.gif") #A la imagen de equis o no se le asigna a la variable no.
    si = PhotoImage(file = "exito.gif") #A la imagen de check se le asigna a la variable si.
    VentanaNombre.geometry("205x300") #Tamano de la imagen.
    VentanaNombre.title("DMaster Mind") #Titulo de la ventana.
    VentanaNombre.config(bg="DeepSkyBlue4") #Configura la ventana a ese color.
    VentanaNombre.maxsize(305,400) #Tamano máximo de la ventana.
    icono = VentanaNombre.iconbitmap("IconoDMasterMind.ico") #Icono de la ventana.   "ms sans Serif"
    EtiquetaNombre = Label(VentanaNombre,bg="DeepSkyBlue2",width=50,height=4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    TextoNombre = Label(VentanaNombre,text="Digite el nombre",fg="white",relief=FLAT,bg="DeepSkyBlue2",font=("systemfixed",11,"bold")).place(x=45,y=25) #Se le asigna una etiqueta a la variable.    NombreJugador = StringVar()
    Name=StringVar() #Se le asigna una variable un valor string
    CampoNombre = Entry(VentanaNombre,relief=FLAT,textvariable = Name).place(x=40,y=140)
    BotonSi=Button(VentanaNombre,image=si,command=AceptarNombre,bg="DeepSkyBlue4",relief=FLAT).place(x=50,y=250) #Se crea un boton con la variable de la imagen si, aceptar.
    BotonNo=Button(VentanaNombre,image=no,command=Cerrar,bg="DeepSkyBlue4",relief=FLAT).place(x=120,y=250) #Se crea un boton con la variable de la imagen no, de cancelar.
    VentanaNombre.mainloop() #La ventana se espera hasta que el ususario digite algo.

#----------------------------------
#Ventana Principal de DMaster Mind
#----------------------------------
    
def VentanaDMasterMind():
    
    #--------------------------------------------------------------
    #Descripción: La siguiente función cierra la ventana del juego.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def CerrarDMaster():
        VentanaDMasterMind.withdraw()
        
    VentanaDMasterMind = Toplevel(celular)#Abre una ventana.
    VentanaDMasterMind.geometry("640x550") #Tamaño de la ventana.
    VentanaDMasterMind.title("DMaster Mind") #Titulo de la ventana.
    VentanaDMasterMind.maxsize(640,550) #Tamaño maximo de la ventana.
    icono = VentanaDMasterMind.iconbitmap("IconoDMasterMind.ico") #Icono de la ventana.
    dibujo = Canvas(VentanaDMasterMind) #Ventana de dibujos.
    dibujo.pack(expand=True, fill=BOTH) #Empaca la ventana de dibujo.
    pintura = Image.open("Fondo-DMaster-Mind.png") #Imagen.
    Fondo = ImageTk.PhotoImage(pintura) #Agregarle la imagen al fondo de la pantalla.
    dibujo.img = Fondo #Imagen en la pantalla de dibujo.
    dibujo.create_image(0, 0, anchor=NW, image=Fondo) #Crea la imagen en la pantalla.
    Copa = PhotoImage(file="Copa.gif") #Le asigna un objeto imagen a la variable.
    Button(dibujo,image=Copa,command=NombreDelDificultadDetalle,bg="white",relief=FLAT,cursor="hand1").place(x=530,y=395)#Se crea un boton.
    Caja = Image.open("Box.png") #Se abre una imagen y se lo asina a la variable.
    Box = ImageTk.PhotoImage(Caja) #Se crea una imagen y se lo asigna a la variable.
    Button(dibujo,image=Box,command=VentanaConfigurar,bg="white",relief=FLAT,cursor="hand1").place(x=-30,y=435) #Se crea un boton.
    libro = Image.open("libro.png") #Se abre una imagen y se lo asigna a la variable.
    Book = ImageTk.PhotoImage(libro) #Se crea una imagen y se lo asigna a la variable.
    Button(dibujo,image=Book,bg="white",command=VentanaAcercaDe,relief=FLAT,cursor="hand1").place(x=-50,y=20)#Se crea un boton.
    Play = PhotoImage(file="Play.gif") #Se crea una imagen .gif y se lo asigna a la variable.
    Button(dibujo,command=NombreDelJugador,image=Play,bg="IndianRed1",relief=FLAT,cursor="hand1").place(x=215,y=380) #Se crea un botón.
    Salida = Image.open("Salida.png")#Se abre una imagen y se lo asigna a la variable.
    Out = ImageTk.PhotoImage(Salida)#Se crea una imagen y se lo asigna a la variable.
    Button(dibujo,image=Out,command=CerrarDMaster,bg="white",relief=FLAT,cursor="hand1").place(x=220,y=240)#Se crea un boton.
    Reloj = Image.open("reloj.png")#Se abre una imagen y se lo asigna a la variable.
    Clock = ImageTk.PhotoImage(Reloj)#Se crea una imagen y se lo asigna a la variable.
    Button(dibujo,image=Clock,command=NombreDelDificultad,bg="white",relief=FLAT,cursor="hand1").place(x=325,y=200)#Se crea un boton.
    Ayudar = Image.open("ayudar.png")#Se crea una imagen y se lo asigna a la variable.
    Help = ImageTk.PhotoImage(Ayudar)#Se abre una imagen y se lo asigna a la variable.
    Button(dibujo,image=Help,bg="white",command=ManualMasterMind,relief=FLAT,cursor="hand1").place(x=20,y=300)#Se crea un boton.
    CargarGanadoresDeLaBase() #Utiliza la función para cargar todos los datos de los ganadores.
    CargarListaDeJugadas() #Utiliza la función para cargar todas las jugadas al juego.
    VentanaDMasterMind.mainloop() #Se mantiene hasta que ocurra un evento.


celular = Tk() #Se crea una ventana.
celular.title("Apps") #Titulo de la ventana.
iconoCelular = celular.iconbitmap("telefono-inteligente.ico") #Icono de la ventana.
celular.geometry("310x550") #Tamano de la ventana.
ImagenDContact=PhotoImage(file="DContactImagen.gif")
MasterMind = PhotoImage(file="tablero.gif")
dibujo=Canvas(celular) #Ventana de dibujos.
dibujo.pack(expand=True, fill=BOTH) #Empaca la ventana de dibujo.
botonMaster = Button(dibujo,image=MasterMind,command=VentanaDMasterMind,relief=FLAT,bg="white smoke").place(x=100,y=30)
celular.maxsize(310,550) #El tamano máximo que se puede agrandar o minimizar la pantalla.
boton=Button(dibujo,image=ImagenDContact,relief=FLAT,bg="white smoke").place(x=30,y=30)
celular.mainloop()
