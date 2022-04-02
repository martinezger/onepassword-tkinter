from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

base_de_datos = {
    "german7833": {
        'nombre': 'German',
        'edad': '12',
        'password': '###'
    },
    "carolina87": {
        'nombre': 'Carolina',
        'edad': '12',
        'password': 'pw?'
    }
}


nombre_de_usuario_error_message = ttk.Label(frm, foreground="red")
nombre_error_message = ttk.Label(frm, foreground="red")
edad_error_message = ttk.Label(frm, foreground="red")
password_error_message = ttk.Label(frm, foreground="red")


def validar_nombre_usario(nombre_usuario): 
    nombre_de_usuario_error_message.grid(row=0, column=2)
    if "" == nombre_usuario:
        pass
    elif nombre_usuario[0].isnumeric():
        nombre_de_usuario_error_message["text"] = "error: usuario no puede empezar con un número."
        return False
    
    if nombre_usuario in base_de_datos:
        nombre_de_usuario_error_message["text"] = "error: usuario ya existe."
        return False

    nombre_de_usuario_error_message["text"] = ""
    return True

def validar_nombre(nombre): 
    nombre_error_message.grid(row=1, column=2)
    if "" == nombre:
        pass
    elif not nombre.isalpha():
        nombre_error_message["text"] = "error: Nombre tiene que ser string alfabético"
        return False
    elif len(nombre) < 4:
        nombre_error_message["text"] = "error: nombre tiene que ser mayor a tres caracteres"
        return False
    
    nombre_error_message["text"] = ""
    return True

def validar_edad(edad):
    edad_error_message.grid(row=2, column=2)
    if "" == edad:
        pass
    elif not edad.isnumeric() or int(edad) < 1:
        edad_error_message['text'] = "error: Edad tiene que ser un valor numérico entero mayor a 0"     
        return False   
    edad_error_message['text'] = ""
    return True

def validar_password(password):
    password_error_message.grid(row=3, column=2)
    if "" == password:
        pass
    elif "?" not in list(password) and "#" not in list(password):
        password_error_message['text'] = "error: Password tiene que tener almenos uno de estos caracteres ?, #"
        return False
    password_error_message['text'] = ""
    return True

def validar_si_password_coincide(password, repetir_password):
    if password != repetir_password:
        print("Error: Passwords y repetir password no son iguales.")
        return False
    return True

def alta_usuario():
    base_de_datos[nombre_usuario.get()] = {
        "nombre": nombre,
        "edad": edad,
        "password": password,
    }
    print(base_de_datos)

def borrar_usuario(nombre_usuario):
    if nombre_usuario in base_de_datos:
        del base_de_datos[nombre_usuario]
        print(f"se borro con éxito el usuario {nombre_usuario}")
    else:
        print(f"Usuario ingresado {nombre_usuario} no existe")
        

def modificar_usuario(nombre_usuario, nombre, edad, password):
    info = {"nombre": nombre, "edad": edad, "password": password}
    base_de_datos[nombre_usuario] = info
    print(f"Se modificó con éxito el usuario: {nombre_usuario}")
    print(info)

def buscar_usuario(dato):
    dato = input("Ingrese usuario:")
    if dato in base_de_datos:
        print(base_de_datos[dato])
    else:
        print(f"NO se encuentra {dato}")

ttk.Label(frm, text="Nombre de Usuario: ").grid(row=0, column=0)
nombre_usuario = ttk.Entry(frm, validate="focusout", validatecommand=(root.register(validar_nombre_usario),"%P" )).grid(row=0, column=1)

ttk.Label(frm, text="Nombre: ").grid(row=1, column=0)
nombre = ttk.Entry(frm, validate="focusout", validatecommand=(root.register(validar_nombre), "%P" )).grid(row=1, column=1)

ttk.Label(frm, text="Edad: ").grid(row=2, column=0)
edad = ttk.Entry(frm, validate="focusout", validatecommand=(root.register(validar_edad),"%P" )).grid(row=2, column=1)

ttk.Label(frm, text="Password: ").grid(row=3, column=0)
password = ttk.Entry(frm, validate="focusout", validatecommand=(root.register(validar_password),"%P" )).grid(row=3, column=1)

ttk.Button(frm, text="guardar", command=alta_usuario).grid(row=4, column=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(row=4, column=1)

root.mainloop()
