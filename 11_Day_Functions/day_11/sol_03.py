# Declare una función llamada capitalize_list_items. Toma una lista como parámetro y devuelve una lista de
# elementos en mayúscula
convert = []


def capitalize_list_items(lista):
    for i in range(len(lista)):
        x = lista[i].upper()
        convert.append(x)
    return convert


print(capitalize_list_items(['a', 'b', 'c']))

# Declare una función llamada add_item. Toma una lista y los parámetros de un elemento. Devuelve una lista con el
# elemento agregado al final.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']


def add_item(lista, item):
    nueva = lista.copy()
    nueva.append(item)

    return nueva


print(food_staff)
print(add_item(food_staff, 'juna'))


# Declare una función llamada remove_item. Toma una lista y los parámetros de un elemento.
# Devuelve una lista con el elemento eliminado de ella.

def remove_item(lista, item):
    nueva = lista.copy()
    nueva.remove(item)
    return nueva


print(food_staff)
print(remove_item(food_staff, 'Mango'))


# Declare una función llamada sum_of_numbers. Toma un parámetro numérico y suma todos los números en ese rango.

def sum_of_numbers(numero):
    if numero == 1:
        return numero
    else:
        return numero + sum_of_numbers(numero - 1)


print(sum_of_numbers(100))
