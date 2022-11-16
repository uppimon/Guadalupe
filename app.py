import json

with open('elementos.json', 'r') as file:
 lista_elements = json.load(file)

    
{
        "id":1,
        "nombre":"Fabuloso",
        "Precio": 20,
        "cantidad": 5
    },
{
        "id": 2,
        "nombre":"Galletas",
        "Precio": 10,
        "cantidad": 2
    }



def add_element():
    #agrega los elementos
    id = int(input("Ingresa el ID "))
    nombre= input("Ingresa el nombre ")
    precio= int(input("ingresa el precio "))
    cantidad= int(input("Ingresa la cantidad "))#pedimos los valores 
    product = {#creamos el objeto 
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad#pasamos los parametros 
    }
    lista_elements
    lista_elements.append(product)#agregamos los parametros a la lista 
    pass

def remove_element():#elimina 
    #for buscar
    id=int(input("Ingresa el id a ELIMINAR "))
    found = find_element(id)
    if found:
        print(found)
        aceptar=input("Estas seguro de eliminar S/N")
        if aceptar == "s":
            lista_elements.remove(found)
            print("Elemento elminado")
    else:
        print(f"El elemento id {id} no existe")

def find_element(id):#busca 
    #for para buscar
    for element in lista_elements:
        if element['id'] == id:
            return element
        else:
            print("NO SE ENCUENTRA EL PRODUCTO")

def show_elements():#muestra 
    #for para iterar y mostrar 
    for element in lista_elements:#iterar todos los elementos de la lista 
        for key, value in element.items():#mostramos todos los elementos 
            print(f"{key} -> {value}")#lo imprime 
def guardar_lista():
    with open('elementos.json', 'w') as file:
        json.dump(lista_elements)
def edit_element():#edita 
    #for a find para buscar
    #editar
    id=int(input("Ingresa el id a editar "))
    found = find_element(id)#busca los elementos
    if found: 
        print(found)#lo imprime 
        index=lista_elements.index(found)
        nombre=input("Actualizar nombre , deja en blanco para conservar ")
        precio= int(input("ingresa el nuevo precio "))
        cantidad= int(input("Ingresa la cantidad nueva "))
        if nombre != '':
            lista_elements[index]['nombre'] = nombre
        if precio != '':
            lista_elements[index]['precio'] = precio
        if cantidad != '':
            lista_elements[index]['cantidad'] = cantidad
    else:
        print (f"El id que ingresaste {id} no existe ")
    '''nombre= input("Ingresa el nuevo nombre ")
    precio= int(input("ingresa el nuevo precio "))
    cantidad= int(input("Ingresa la cantidad nueva "))#pedimos los valores
    product = {#creamos el objeto 
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad#pasamos los parametros 
    }
    lista_elements.remove(found)#elimina lo que contiene 
    lista_elements.append(product)#agrega los nuevos elemntos'''

    


if __name__ == '__main__':
     message=f"Tienda de abarrotes DU:\n  Elige la opcion\n1=Agregar Producto\n2=Mostar Producto\n3=Buscar Producto\n4=Editar Producto\n5=eliminar\n6=salir\n"
     while True:
        option=int(input(message))
        #compara cada opcion y llama a la funcion correspondiente 
        if option == 1:
            print("Inserta un producto")
            add_element()
        elif option==2:
            print("Mostar todos los productos")
            show_elements()
        elif option==3:
            print("Buscar productos")
            id =int(input("Agrega el id a buscar "))
            found = find_element(id)
            if found:
                print(found)
            
        elif option==4:
            print("Editar producto")
            edit_element()
        elif option==5:
            print("Eliminar producto")
            remove_element()
        elif option == 6:
            print("BYE")
            break
        else:
            print("OPCION INCORRECTA ")
            