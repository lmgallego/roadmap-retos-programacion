'''

EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos

'''

def saludo():
    print('Hola como estás')

saludo()

# Con retorno
def saludo1():
    return "Hola como estas"

print(saludo1())

# Con argumentos

def saludo_argu(nombre):
    print(f'Hola {nombre}')

saludo_argu('Pedro')

def saludo_argu2(nombre='Python'):
    print(f'Hola {nombre}')
    
saludo_argu2()

# con retorno y argumentos
def saludo_argu3(saludo, nombre):
    return f'{saludo}, {nombre}'

print(saludo_argu3('Hola', 'Pascual'))

# Con retorno y varios valores
def saludo_argu4(saludo, nombre):
    return "Hola", "Python"

# Con un número variable de argumentos
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")
        
variable_arg_greet("Python", "Angel", "Mouredev", "Comunidad")

# Con un número  variable de argumentos con palabras clave
def variable_arg_greet2(**names):
    for name in names:
        print(f"Hola, {name}!")
        
variable_arg_greet2(Python="Python", Angel="Angel", Mouredev="Mouredev", Comunidad="Comunidad")


def cadena(texto1, texto2):
    cont = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + texto2)
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else:
            print(i)
            cont += 1
    return cont

print(cadena("Python", "Mouredev"))