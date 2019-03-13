# coding=utf-8
import os
import random

def cls():
    try:
        os.system("cls")
        os.system("color D")
    except:
        pass      
cls()

print("""
 ______     __         ______        ______     __  __     ______     __    __     ______     __   __     ______     ______    
/\  __ \   /\ \       /\  ___\      /\  ___\   /\_\_\_\   /\  __ \   /\ "-./  \   /\  ___\   /\ "-.\ \   /\  ___\   /\  ___\   
\ \  __ \  \ \ \____  \ \  __\      \ \  __\   \/_/\_\/_  \ \  __ \  \ \ \-./\ \  \ \  __\   \ \ \-.  \  \ \  __\   \ \___  \  
 \ \_\ \_\  \ \_____\  \ \_____\     \ \_____\   /\_\/\_\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\  \ \_\\"\_\  \ \_____\  \/\_____\ 
  \/_/\/_/   \/_____/   \/_____/      \/_____/   \/_/\/_/   \/_/\/_/   \/_/  \/_/   \/_____/   \/_/ \/_/   \/_____/   \/_____/ 
                                                                                                                              
      #################################################################################################################  
      # Hola Ale, este es un programa que te pueda ayudar a estudiar y sacar una buena calificacion en tus examenes   #
      # que se aproximan, hechale ganas para que tu mama se sienta orgullosa y saque una lagrimita ;...) de felicidad #
      #################################################################################################################
      
      Bueno estas son las reglas y el procedimiento:
      
          - Se te iran mostrando de una en una las preguntas del examen salteadas  
          - Si te iran acumulando las respuestas correctar para darte un resultado final
          - Cada vez que no aciertes una respuesta se te mostrara la respuesta correcta.
          - Para selecionar una respuesta teclea la letra de su inciso.
          
      Ammmm... creo que es todo... Quieres comenzar ya ?
      
      tecle la opcion y despues Enter
      
      s = si, n = no
                                                
                                                                                                                              
                                                                                                                               """)
 
comenzar = input()

respuestasCorrectas = 0
respuestasIncorrectas = 0

    
##while(comenzar is 's'):
      
repetir = 's'
while(repetir is 's'):
    ################### Primera Preguntas ####################    
    preguntas = ["""¿Cada cuando el INEGI (Instituto Nacional de Estadística y Geografía) lleva a cabo el censo de población?
a.    Cada 5 años
c.    Cada 20 años    
b.    Cada 15 años
d.    Cada 10 años    

"""] 
    respuestas =['d']
    ############################################################
    
    #################### Segunda Preguntas ####################    
    preguntas.append("""Las zonas rurales son importantes para la economía del país ya que son productores de alimentos:
a.    ganaderos y agrícolas    
b.    pesquero y el cultivo    
c.    lechero y arquitecto
d.    agrícola y productos enlatados
""")
    respuestas.append('a')
    
    ############################################################
    
    ################### Tercera Preguntas ####################    
    preguntas.append("""Son algunas de las ventajas que disfrutan las poblaciones rurales.
a.    La contaminación y los productos enlatados
b.    Vivir en contacto con la naturaleza y obtener alimentos sanos
c.    Viajar en caballo y tener todos los servicios
d.    Tener cercano un hospital y una gasolinera
""")
    respuestas.append('b')
    
    ############################################################
    
    preguntas.append("""La cantidad de habitantes por kilómetro cuadrado se conoce como:
a.    población absoluta    c.    densidad de población
b.    población    d.    concentración de la población
""")
    respuestas.append('c')   
    ############################################################
    
    preguntas.append("""Es aquella que habita en el campo y se dedica a actividades como la agricultura y ganadería.
a.    población    
b.    población rural    
c.    población urbana
d.    densidad de población
""")
    respuestas.append('b')   
    ############################################################
    
    preguntas.append("""Tener disponibilidad de servicios, medios de comunicación y empleos es un beneficio de la:
a.    población    
b.    población rural    
c.    población urbana
d.    densidad de población
""")
    respuestas.append('c')   
    ############################################################
    
    preguntas.append("""El cambio de residencia de las personas fuera de su localidad, entidad o país se denomina:
a.    inmigrante    
b.    emigrante    
c.    migración temporal
d.    Migración

""")
    respuestas.append('d')   
    ############################################################
    
    preguntas.append("""Cuando una persona abandona el lugar donde habita se convierte en:
a.    inmigrante    
b.    Emigrante    
c.    migración temporal
d.    Migración
""")
    respuestas.append('b')   
    ############################################################
    
    preguntas.append("""Cuando se va a vivir a un lugar diferente del que habitaba se le considera:
a.    Inmigrante    c.    migración temporal
b.    Emigrante    d.    Migración

""")
    respuestas.append('a')   
    ############################################################
    
    preguntas.append("""Cuando la población o persona permanece poco tiempo fuera de su lugar de residencia se denomina como:
a.    migración externa    c.    migración interna
b.    migración definitiva    d.    migración temporal
""")
    respuestas.append('d')   
    ############################################################
    
    preguntas.append("""Cuando la población se desplaza de un país a otro se le conoce como
a.    migración externa    c.    migración interna
b.    migración definitiva    d.    migración temporal
""")
    respuestas.append('a')   
    ############################################################
    
    preguntas.append("""Cuando una persona se traslada de forma permanente a otro lugar se le llama:
a.    migración externa    c.    migración interna
b.    migración definitiva    d.    migración temporal
""")
    respuestas.append('b')
    
    ############################################################
    
    preguntas.append("""Se considera que la densidad de población es menor porque:
a.    hay 10 personas por m2    c.    hay más personas por cada m2
b.    hay una persona por m2     d.    hay pocas personas
""")
    respuestas.append('b')    

    ############################################################
    
    preguntas.append("""La distribución demográfica puede ser de tres tipos, ¿Cuáles son?
a.    Alta, media y baja    
b.    Fuerte, media y débil    
c.    Alta concentración, mediana concentración y dispersión
d.    Concentración extra, concentración normal y concentración ligera
""")
    respuestas.append('c')   
    
    ############################################################
    
    preguntas.append("""Son algunos servicios que se requieren y son indispensables en las ciudades:
a.    Flora y Fauna    
b.    Bibliotecas y centros culturales    
c.    Industrias y áreas densamente pobladas
d.    agua potable, drenaje y electricidad
""")
    respuestas.append('d')     
     
    ############################################################
     
    preguntas.append("""Para mejorar su situación económica, tener mejores servicios educativos y de salud, o más espacios recreativos y culturales, las personas: 
a.    se mudan a una zona rural    
b.    cambian de residencia    
c.    Crean nuevos objetivos
d.    cambian de ocupación
""")    
    respuestas.append('b')  
    
    ############################################################
     
    preguntas.append("""Es una de las actividades económicas más importantes para nuestro país:
a.    La pesca    
b.    La ganadería    
c.    El turismo
d.    La migración externa
""")    
    respuestas.append('c') 

    ############################################################
     
    preguntas.append("""¿Cuáles son algunos de los países de destino para los mexicanos emigrantes?
a.    E.U.A. y Canadá    
b.    Perú y Brasil    
c.    Canadá y Guatemala
d.    E. U. A. y Panamá
""")    
    respuestas.append('a') 
 
    ############################################################
     
    preguntas.append("""Representa una situación desfavorable para el desarrollo de las familias y las comunidades en localidades rurales.
a.    Las carreteras    c.    El crecimiento poblacional
b.    La migración    d.    El aislamiento

""")    
    respuestas.append('d')     
############################################################

    preguntas.append("""Son herencia de nuestros antepasados, y combinan las influencias culturales que ocurrieron y ocurren a lo largo de la historia del país.
a.    Tradiciones y costumbres    c.    Las tribus urbanas
b.    La combinación de prácticas culturales    d.    La celebración de la independencia de México
""")    
    respuestas.append('a') 
     
    len(preguntas)
    len(respuestas) 

    while(len(preguntas) != 0):
        cls()
        numPregunta = random.randint(0,len(preguntas)-1)
        print(preguntas[numPregunta])
        R = input()
        if(respuestas[numPregunta] is R ):
            respuestasCorrectas=respuestasCorrectas+1
            print("""
            
               _____ ____  _____  _____  ______ _____ _______ ____    _   _   _ 
      / ____/ __ \|  __ \|  __ \|  ____/ ____|__   __/ __ \  | | | | | |
     | |   | |  | | |__) | |__) | |__ | |       | | | |  | | | | | | | |
     | |   | |  | |  _  /|  _  /|  __|| |       | | | |  | | | | | | | |
     | |___| |__| | | \ \| | \ \| |___| |____   | | | |__| | |_| |_| |_|
      \_____\____/|_|  \_\_|  \_\______\_____|  |_|  \____/  (_) (_) (_)
                                                                        
                                                                        
    ... Da enter""")
            input()
        else:
            respuestasIncorrectas=respuestasIncorrectas+1
            print("""
            
            
            Te equivocasta Ale
                                          
                                      
                         CCCCCCCCCCCCC
                      CCC::::::::::::C
                    CC:::::::::::::::C
                   C:::::CCCCCCCC::::C
                  C:::::C       CCCCCC
     ::::::      C:::::C              
     ::::::      C:::::C              
     ::::::      C:::::C              
                 C:::::C              
                 C:::::C              
                 C:::::C              
     ::::::       C:::::C       CCCCCC
     ::::::        C:::::CCCCCCCC::::C
     ::::::         CC:::::::::::::::C
                      CCC::::::::::::C
                         CCCCCCCCCCCC           
                                                                       
                                        ... Da enter""")
            input()
        preguntas.pop(numPregunta)
        respuestas.pop(numPregunta)
    
    cls()
        
    print("Ale tuviste respuestas correctas = {}".format(respuestasCorrectas))
    print("Ale tuviste respuestas Incorrectas = {}".format(respuestasIncorrectas))            
    
    print("Quieres repitir el examen : s = si, n = no")
    repetir = input()
    



        

                                                                                                                     
                                                                                                                            