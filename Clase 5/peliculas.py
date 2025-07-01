"""
IMPORTANTE: debí usar móduos pero para explicarlo era más fácil todo junto (perdón).
Generé una clase Peliculas para poder guardar lo que levanto de un archivo. A lo que levanto
le elimino el primer elemento leido porque es el header (se que lo trae).
Luego me veo obligado a hacer unas peripecias ya que "split" no se lleva con comillas ni
dobles ni simples (calculo que el profe lo sabe y se "olvidó" de mencionarlo) y como el tema
era sin el módulo de CSV hubo que quemar neuonas. Use "regular expressions" (eso si me
ayudó ChatGPT porque hoy por hoy me supera) y si solo sacaba comillas y había comas internas
daba destrozos (igual en algún caso que, se lo puso adrede, pasa). Luego saco comillas (las que
sea) y ahi puedo hacer el "split" para luego volver a poner comillas (si las tenía).
"""
import re # "regulars expressions" (gracias ChatGPT)
from collections import defaultdict

class Pelicula: # Defino la clase de películas
    def __init__(self, id="", 
                       title="", 
                       certificate="", 
                       duration=0, 
                       genre="", 
                       rate="", 
                       metascore="", 
                       description="", 
                       cast="", 
                       info=""):        

        self.id = str(id).strip() if id is not None else ""
        self.title = str(title).strip() if title is not None else ""
        self.certificate = str(certificate).strip() if certificate is not None else ""

        if duration == None or duration == "": # Redundante pero por si es None o similares
            duration = 0
        else:
            duration = str(duration).strip() # Acá hago así por si es numérico

        if isinstance(duration, (int, float, str)): # Redundante también pero soy paranóico
            # Verifico el valor porque si o si necesito que sea númeríco
            # para cálculos más adelante
            try:
                self.duration = int(float(duration)) # Primero a float que es menos conflictivo

            except ValueError:
                self.duration = 0
        else:
            self.duration = 0
        
        self.genre = str(genre).strip() if genre is not None else ""
        self.rate = str(rate).strip() if rate is not None else ""
        self.metascore = str(metascore).strip() if metascore is not None else ""
        self.description = str(description).strip() if description is not None else ""
        self.cast = str(cast).strip() if cast is not None else ""
        self.info = str(info).strip() if info is not None else ""

def leer_archivo(archivo: str, modo: str = "r", encoding: str = "utf-8") -> list:
    with open(archivo, mode=modo, encoding=encoding) as f:
        lineas = f.readlines() # Lee todas las líneas (porque son pocas sino readline() es mejor)
        return list(lineas[1:]) # devuelvo la lista (omito el header que se que es la primera línea)
                                # redundante el list() pero vengo de FUERTEMENTE tipificados

# Esta caí en ayuda del Sr. ChatGPT ya que las "regular expressions"
# me superan en este nivel (soy principiante en Python).
def proteger_comas_en_entre_comillas(linea: str, marcador: str = ',', reemplazo: str = '⧙') -> str:
    # Reemplaza comas internas dentro de comillas 
    # dobles o simples por un firulete (⧙)
    def reemplazo_interno(match):
        texto = match.group(0)
        return texto.replace(marcador, reemplazo)
    
    # Para comillas dobles: "..."
    linea = re.sub(r'"[^"]*"', reemplazo_interno, linea)

    # Para comillas simples: '...'
    linea = re.sub(r"'[^']*'", reemplazo_interno, linea)
    
    # Cargo la línea ya normalizada
    return str(linea) # No "strip" porque mantengo lo que se levantó

# Reemplazo las comillas dobles y simples por caracteres específicos
# que pueden ser asignados o tomados por defecto
def reemplazar_comillas(texto: str, doble: str = '§', simple: str = '¤') -> str:
    return str(texto.replace('"', doble).replace("'", simple))

# Restauro las comillas dobles y simples buscando caracteres específicos
# que pueden ser asignados o tomados por defecto
def restaurar_comillas(texto: str, doble: str = '§', simple: str = '¤') -> str:
    return str(texto.replace(doble, '"').replace(simple, "'"))

# Reemplazo el caracter (firulete '⧙') que usé para cambiar dentro de comillas
# (usando "regular expressions" que el profe tiró para ver quien caía)
def restaurar_comas(texto, marcador='⧙') -> str:
    return str(texto.replace(marcador, ','))

# Conviero la cadena pasada a int tomando del inicio hasta donde llegue
# como duración en minutos 
# ej: "120 min", "90min", "95min7") dará (120, 90, 95) respectivamente
def minutos(texto) -> int:
    if texto == None:
        texto = ''

    # Verifico si paso un número
    if isinstance(texto, (int, float)):
        texto = str(texto)

    # Elimino caracteres innecesarios
    texto = texto.strip()        
    
    # Defino variable de retorno de valor
    valor = ""

    # Recorro la cadena hasta encontrar un no numérico
    for caracter in str(texto).strip():
        if caracter.isdigit(): # isdigit() toma sólo número de 0 a 9 (no puntos ni comas)
            valor += caracter
        else:
            break

    return int(valor) if valor else 0 # Si es vacío/None asume 0

#
# Cuerpo principal del programa
#

# Contabilizo errores porque el profe puso unas trampas caza-bobos
# y bombas lógicas (no lo iba a hacer fácil)
mensajes = list()
errores = 0
registros = 0

# Creo una lista de películas
peliculas = list()

# Leo todas las líneas del archivo
lineas = leer_archivo("IMDB_TOP1000.csv")

# Recorro las líneas leidas
for linea in lineas: # Podría haber invocado directo a la función pero así es más legible
    # Incremento cantidad total de registros
    registros +=1

    # Remuevo las comillas dobles y simples
    # ya que molestan al "split" y da "cositas raras"
    linea = proteger_comas_en_entre_comillas(linea.strip())  # esto es clave
    linea = reemplazar_comillas(linea) # prodía unir con la de arriba pero así es más claro

    # Hago "slipt" ya sin miedo a efectos indeseados (unos pocos pueden haber igual)
    campos = linea.split(",") # separo los campos

    # Restauro las comillas (si las hubiera) y las comas en los campos
    campos = [restaurar_comas(restaurar_comillas(campo)).strip() for campo in campos]

    # Por las dudas evaluo la cantidad de campos por problemas de comas
    # que insisto fue ADREDE que el profe las dejó !!!!!
    if len(campos) != 10:
        errores += 1
        mensajes.append(f"Error en línea {registros}: {campos[1]}")
        continue # No sigo porque hay errores en recuperación 
                 # (salto al siguiente registro si hubiera)

    # Instancio una variables para llenar con los valores recuperados
    pelicula = Pelicula()

    # Cargo los valores de la pelicula
    pelicula.id = campos[0] if campos[0] is not None else "" # Evaluo esto por None
    pelicula.title = campos[1] if campos[1] is not None else ""
    pelicula.certificate = campos[2] if campos[2] is not None else ""
    pelicula.duration = minutos(str(campos[3])) # lo convieto a int o 0 si no se puede
    pelicula.genre = campos[4] if campos[4] is not None else ""
    pelicula.rate = campos[5] if campos[5] is not None else ""
    pelicula.metascore = campos[6] if campos[6] is not None else ""
    pelicula.description = campos[7] if campos[7] is not None else ""
    pelicula.cast = campos[8] if campos[8] is not None else ""
    pelicula.info = campos[9] if campos[9] is not None else ""

    # Agrego la pelicula a la lista de peliculas
    peliculas.append(pelicula)

# Calculo las estadisticas pedidas
cantidad_peliculas_ok = len(peliculas)
mas_larga = max(peliculas, key=lambda p: p.duration)
mas_corta = min(peliculas, key=lambda p: p.duration)
tiempo_promedio = int(sum(p.duration for p in peliculas) / cantidad_peliculas_ok)

# Agrupo las películas por género
generos  = defaultdict(list)
for pelicula in peliculas:
    genero = pelicula.genre.strip()
    generos[genero].append(pelicula)

# Contabilizo las películas por género
peliculas_por_genero = {} # Diccionario "genero / cantidad"
for genero, lista in generos.items():
    cantidad = len(lista)
    peliculas_por_genero[genero] = {"cantidad": cantidad}

# Muesto los valores solicitados
print("-" * 50)
print(f"Cantidad de películas: {cantidad_peliculas_ok} (de {registros})")
print(f"Película más larga: {mas_larga.title} con {mas_larga.duration} minutos")
print(f"Película más corta: {mas_corta.title} con {mas_corta.duration} minutos")
print(f"Promedio de duración: {tiempo_promedio} minutos")

# Muesto cantidad de errores y los mensajes de donde ocurrieron
# (si es que hubo errores)
if errores != 0:
    porcentaje_error = errores / registros * 100
    porcentaje_ok = 100 - porcentaje_error

    print("-" * 50)
    print(f"Cantidad de errores {errores} sobre {registros} registros totales")
    print("-" * 50)

    for error in mensajes:
        print(error) 

    print("-" * 50)
    print(f"Porcentaje de errores: {porcentaje_error:.2f} % ({porcentaje_ok:.2f} % ok)")

# Muestro resumen por género
print("-" * 50)
print("Resumen de películas por género")
print("-" * 50)

for genero in sorted(peliculas_por_genero.items(), key=lambda x: x[0]):
    print(genero[0].replace('"', "").replace("'", "") + ":", genero[1]['cantidad'], "películas")

print("-" * 50)