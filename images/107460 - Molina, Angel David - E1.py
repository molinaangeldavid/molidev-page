# Dieguito Presidente 
# Recientemente en Argentina se desarrollaron las elecciones presidenciales en las cuales Diego 
# Acosta ha sido elegido presidente. Un portal de información nos solicita armar un software capaz 
# de procesar las estadísticas de esta elección y para futuras elecciones. En esta elección Dieguito 
# Acosta solo compitió contra Serafin Vertido, pero nos solicitan que nuestro software se adapte a 
# cualquier cantidad de candidatos posibles.  
# Para ellos nos brindan 2 archivos donde poseen información importante para poder cumplir nuestro 
# objetivo. 
# poblacion.csv 
# contiene cada una de las provincias, la cantidad de población urbana y la cantidad de población rural 
# votos.csv 
# contiene en cada fila el nombre del candidato, la provincia y la cantidad de votos positivos obtenidos 
# El software debe permitir hacer lo siguiente: 
# 1.  Procesar la información provista por el portal para luego ser utilizada en el resto de las 
# opciones. 
# 2.  Ingresar un nuevo registro en el archivo de votos provisto por el portal limitándose a las 
# provincias provistas en el archivo de poblacion. 
# 3.  Determinar el candidato que mayor voto de población rural obtuvo indicando las 5 provincias 
# donde obtuvo mayor cantidad ordenadas por la cantidad de dichos votos. 
# 4.  Determinar las 5 provincias que tienen mayor población urbana y de las mismas indicar 
# como fue la distribución % de votos de los candidatos, incluyendo como “3º candidato” a 26
# los votos no positivos. 
# 5.  Imprimir el escrutinio definitivo de cada una de las provincias en un archivo separado para 
# cada una llamado con su nombre y extensión txt (por ejemplo: tucuman.txt) indicando el 
# candidato, el % de votos obtenidos, y una estimación de cuantos votos fueron de población 
# rural y cuantos de urbana. 
# Ej: Si tenemos la provincia A que tiene 20.000 habitantes distribuidos en 5.000 rurales y 
# 15.000 urbanos tendríamos un 25% de población rural y 75% de población urbana. 
# Supongamos que el Candidato D sacó 12000 votos, podríamos estimar que obtuvo 3000 
# votos rurales y 9000 votos urbanos. Mientras tanto el Candidato E sacó 6000 votos, 
# estimando 1500 rurales y 4500 urbanos. El archivo provinciaA.txt quedaría con el siguiente 
# contenido: 
# Candidato D, 60, 3000, 9000 
# Candidato E, 30, 1500, 4500 
# No positivos, 10, 500, 1500 
 
# Aclaración 1: Debe utilizar funciones para resolver cada uno de los puntos 
# Aclaración 2: Es obligatorio usar try-except por lo menos en un lugar y justificar su uso 
# Aclaración 3: Es obligatorio el uso de un diccionario y una lista como mínimo 
# Aclaración 4: Debe existir un menú para poder llamar a las opciones a gusto del usuario

import csv,os,time

def validar_opcion_menu()->int:
    opcion = input('Ingrese una opcion: ')
    while not (opcion.isnumeric() and int(opcion)>=1 and int(opcion)<=6):
        opcion = input('ERROR. Ingrese de nuevo: ') 
    opcion = int(opcion)
    return opcion

def procesar_archivos()->dict:
    poblacion = {}
    votos = []
    with open('poblacion.csv', newline='',encoding='utf-8')as archivo_poblacion:
        csv_reader = csv.reader(archivo_poblacion,delimiter=',')
        for dato1 in csv_reader:
            poblacion[dato1[0]] = dato1[1:len(dato1)]
    with open('votos.csv', newline='',encoding='utf-8')as archivo_votos:
        csv_reader = csv.reader(archivo_votos,delimiter=';')
        for dato2 in csv_reader:
            votos.append(dato2)
    return poblacion,votos   

def cargar_registro(votos,poblacion)->None:

    provincias = []
    for provincia in poblacion.keys():
        provincias.append(provincia)
    candidato = input('Ingrese el candidato a las presidenciales: ')
    provincia_candidato = input('Ingrese la provincia donde se registraron los votos: ')
    while provincia_candidato not in provincias:
        print('Ingresaste una provincia incorrecta')
        provincia_candidato = input('Ingrese de nuevo la provincia: ')
    votos_positivos = int(input('Ingrese (CON NUMEROS) la cantidad de votos positivos: '))
    votos.append([candidato,provincia_candidato,votos_positivos])
    with open('votos.csv','a')as archivo_votos:
        csv_writer = csv.writer(archivo_votos,delimiter=';')
        csv_writer.writerow([candidato,provincia_candidato,votos_positivos])
    print(votos)    
    print('\tCarga realizada\n')            

def porcentaje_poblacional(poblacion)->dict:
    porcentaje_habitantes = {}
    for key, habitantes in poblacion.items():
        total = int(habitantes[0]) + int(habitantes[1])
        porcentaje_urbano = (int(habitantes[0])*100)/total
        porcentaje_rural = (int(habitantes[1])*100)/total
        porcentaje_habitantes[key] = [
            ['urbana',porcentaje_urbano],
            ['rural',porcentaje_rural],
        ]
    return porcentaje_habitantes    

def candidato_mayor_voto(votos,poblacion)->None:
    # 3.  Determinar el candidato que mayor voto de población rural obtuvo indicando las 5 provincias 
    # donde obtuvo mayor cantidad ordenadas por la cantidad de dichos votos. 

    porc_pobla = porcentaje_poblacional(poblacion)
    print(porc_pobla)
    for voto_provincial in votos:
        pass

def poblacion_urbana(votos,poblacion)->None:
    # 4.  Determinar las 5 provincias que tienen mayor población urbana y de las mismas indicar 
    # como fue la distribución % de votos de los candidatos, incluyendo como “3º candidato” a 
    # los votos no positivos.     
    porc_pobla = porcentaje_poblacional(poblacion)
    top5_poblacion = sorted(porc_pobla.items(),key=lambda x:x[1][0][1],reverse=True)
    contador = 0
    print('\n=====Top 5 provincias con mayor poblacion urbana=====')
    for i in top5_poblacion:
        contador += 1
        if contador < 6:
            print(f'\t{i[0]}')

def menu(opcion,poblacion,votos)->None:
    if opcion == 2:

        # El planteo está OK, pero al cargar un nuevo registor de votos, no se respeta
        # la estructura de datos del tipo: 
        #
        # --> ['nombre_candidato', 'provincia', 'cant_votos']
        #
        # Y se está registrando con esta otra estructura: 
        # --> ['nombre_candidato', 'provincia', cant_votos]
        #
        # @author Leonel Abel Chaves   

        cargar_registro(votos,poblacion)
    elif opcion == 3:

        # El planteo está a medias, se debería obtener el porcentaje de la
        # población rural y urbana a nivel nacional, con el fin de poder luego
        # determinar, de todos los votos obtenidos por los candidatos, 
        # quien tuvo una mayor incidencia en el voto rural
        #
        # Una vez hecho el punto anterior, se debía determinar la cantidad
        # del voto rural obtenido por el candidato, en cada provincia, y armar
        # el top5 de provincias.
        #
        # @author Leonel Abel Chaves 

        candidato_mayor_voto(votos,poblacion)
    elif opcion == 4:

        # El planteo está mal, el top5 se debería armar de acuerdo a la
        # cantidad de población urbana, y no al porcentaje con respecto 
        # a la población total de la provincia.
        #
        # Sumado a esto, falta mostrar el % de distribución de los votos
        # entre los candidatos, sumando a un 3° candidato a los votos no
        # positivos
        #
        # @author Leonel Abel Chaves   

        poblacion_urbana(votos,poblacion)
    elif opcion == 5:

        # No está hecho
        #
        # @author Leonel Abel Chaves   

        pass

def main()->None:
    datos_procesados_poblacion = {}
    datos_procesados_votos = []
    init_inicio = False
    while not init_inicio:
        print('''
            ===================================================================
            ======================= ESCRUTINIO PRESIDENCIAL =======================
            ===================================================================\n
            1. PROCESAR ARCHIVOS
            2. CARGAR UN NUEVO REGISTRO
            3. CANDIDATO DE MAYOR VOTO
            4. MOSTRAR POBLACION URBANA Y DISTRIBUCION PORCENTUAL DE LOS VOTOS
            5. GUARDAR ESCRITINIO DEFINITIVO
            6. SALIR DEL PROGRAMA
        ''')
        opcion = validar_opcion_menu()
        if opcion == 1:
            # El Try-except se utiliza en esta estructura para que ejecute el proceso de los archivos, caso que no encuentre los archivos.csv. Entonces saltara un error personalizado de que no pudo abrir el archivo buscado. En caso que si haya encontrado los archivos, estos se guardaran y entonces se ejecutara el else. Porque no ha encontrado ningun problema en los archivos
            try:
                print('Procesado...')
                datos_procesados_poblacion, datos_procesados_votos = procesar_archivos() 
            except IOError:
                return print('El archivo no se pudo leer')
            else:         
                print('Archivo procesado con exito')
                init_menu = False
                while not init_menu:
                    opcion = validar_opcion_menu()
                    menu(opcion,datos_procesados_poblacion,datos_procesados_votos)
                    if opcion == 6:
                        init_menu = True
                        init_inicio = True
                        return init_menu   
        if opcion == 6:
            init_inicio = True
            print('Saliendo del programa...')
        elif opcion >=2 and opcion <=5:
            print('No has procesado ningun archivo')
            time.sleep(1)
            os.system('clear')    
main()
