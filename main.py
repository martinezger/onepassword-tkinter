from tkinter import *
from tkinter import ttk
import tkinter



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


class MainFrame(ttk.Frame):

    def __init__(self, container):


        super().__init__(container)

        ttk.Label(container, text="Nombre de Usuario: ").grid(row=0, column=0)
        self.nombre_usuario = ttk.Entry(container, validate="focusout", validatecommand=(self.validar_nombre_usario,"%P" )).grid(row=0, column=1)

        ttk.Label(container, text="Nombre: ").grid(row=1, column=0)
        self.nombre = ttk.Entry(container, validate="focusout", validatecommand=(self.validar_nombre, "%P" )).grid(row=1, column=1)

        ttk.Label(container, text="Edad: ").grid(row=2, column=0)
        self.edad = ttk.Entry(container, validate="focusout", validatecommand=(self.validar_edad,"%P" )).grid(row=2, column=1)

        ttk.Label(container, text="Password: ").grid(row=3, column=0)
        self.password = ttk.Entry(container, validate="focusout", validatecommand=(self.validar_password,"%P" )).grid(row=3, column=1)

        self.btn_guardar = ttk.Button(container, text="guardar", command=self.alta_usuario).grid(row=4, column=0)
        self.btn_quit = ttk.Button(container, text="Quit", command=container.destroy).grid(row=4, column=1)

        self.nombre_de_usuario_error_message = ttk.Label(container, foreground="red")
        self.nombre_error_message = ttk.Label(container, foreground="red")
        self.edad_error_message = ttk.Label(container, foreground="red")
        self.password_error_message = ttk.Label(container, foreground="red")
    
    def validar_nombre_usario(self): 
        self.nombre_de_usuario_error_message.grid(row=0, column=2)
        if "" == self.nombre_usuario:
            pass
        elif self.nombre_usuario[0].isnumeric():
            self.nombre_de_usuario_error_message["text"] = "error: usuario no puede empezar con un número."
            return False
        
        if self.nombre_usuario in base_de_datos:
            self.nombre_de_usuario_error_message["text"] = "error: usuario ya existe."
            return False

        self.nombre_de_usuario_error_message["text"] = ""
        return True

    def validar_nombre(self): 
        self.nombre_error_message.grid(row=1, column=2)
        if "" == self.nombre:
            pass
        elif not self.nombre.isalpha():
            self.nombre_error_message["text"] = "error: Nombre tiene que ser string alfabético"
            return False
        elif len(self.nombre) < 4:
            self.nombre_error_message["text"] = "error: nombre tiene que ser mayor a tres caracteres"
            return False
        
        self.nombre_error_message["text"] = ""
        return True

    def validar_edad(self):
        self.edad_error_message.grid(row=2, column=2)
        if "" == self.edad:
            pass
        elif not self.edad.isnumeric() or int(self.edad) < 1:
            self.edad_error_message['text'] = "error: Edad tiene que ser un valor numérico entero mayor a 0"     
            return False   
        self.edad_error_message['text'] = ""
        return True

    def validar_password(self):
        self.password_error_message.grid(row=3, column=2)
        if "" == self.password:
            pass
        elif "?" not in list(self.password) and "#" not in list(self.password):
            self.password_error_message['text'] = "error: Password tiene que tener almenos uno de estos caracteres ?, #"
            return False
        self.password_error_message['text'] = ""
        return True

    def validar_si_password_coincide(self):
        if self.password != self.repetir_password:
            print("Error: Passwords y repetir password no son iguales.")
            return False
        return True

    def alta_usuario(self):
        base_de_datos[self.nombre_usuario.get()] = {
            "nombre": self.nombre,
            "edad": self.edad,
            "password": self.password,
        }
        print(base_de_datos)

    def borrar_usuario(self):
        if self.nombre_usuario in base_de_datos:
            del base_de_datos[self.nombre_usuario]
            print(f"se borro con éxito el usuario {self.nombre_usuario}")
        else:
            print(f"Usuario ingresado {self.nombre_usuario} no existe")
            

    def modificar_usuario(self):
        info = {"nombre": self.nombre, "edad": self.edad, "password": self.password}
        base_de_datos[self.nombre_usuario] = info
        print(f"Se modificó con éxito el usuario: {self.nombre_usuario}")
        print(info)

    def buscar_usuario(dato):
        dato = input("Ingrese usuario:")
        if dato in base_de_datos:
            print(base_de_datos[dato])
        else:
            print(f"NO se encuentra {dato}")

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('My Awesome App')
       

if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()

