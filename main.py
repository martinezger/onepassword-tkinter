from tkinter import *
from tkinter import ttk
import tkinter


base_de_datos = {
    "german7833": {"nombre": "German", "edad": "12", "password": "###"},
    "carolina87": {"nombre": "Carolina", "edad": "12", "password": "pw?"},
}


class MainFrame(ttk.Frame):
    def __init__(self, container, *args, **kwarg):

        super().__init__(container, *args, **kwarg)


        self._is_form_valid = [False]
        self.label_nombre_usuario = ttk.Label(text="Nombre de Usuario: ")
        self.entry_nombre_usuario = ttk.Entry(
            validate="focusout",
            validatecommand=(self.register(self.validar_nombre_usario), "%P"),
        )

        self.label_nombre = ttk.Label(container, text="Nombre: ")
        self.entry_nombre = ttk.Entry(
            container,
            validate="focusout",
            validatecommand=(self.register(self.validar_nombre), "%P"),
        )

        self.label_edad = ttk.Label(container, text="Edad: ")
        self.entry_edad = ttk.Entry(
            container,
            validate="focusout",
            validatecommand=(self.register(self.validar_edad), "%P"),
        )

        self.label_password = ttk.Label(container, text="Password: ")
        self.entry_password = ttk.Entry(
            container,
            validate="focusout",
            validatecommand=(self.register(self.validar_password), "%P"),
        )

        self.label_repetir_password = ttk.Label(container, text="Repetir Password: ")
        self.entry_repetir_password = ttk.Entry(
            container,
            validate="focusout",
            validatecommand=(self.register(self.validar_si_password_coincide), "%P"),
        )

        self.button_guardar = ttk.Button(
            container, text="guardar", command=self.alta_usuario
        )
        self.button_quit = ttk.Button(
            container, text="Quit", command=container.destroy
        )

        self.error_message_nombre_de_usuario = ttk.Label(container, foreground="red")
        self.error_message_nombre = ttk.Label(container, foreground="red")
        self.error_message_edad = ttk.Label(container, foreground="red")
        self.error_message_password = ttk.Label(container, foreground="red")
        self.error_message_repetir_password = ttk.Label(container, foreground="red")
        self.error_message_formulario_invalido = ttk.Label(container, foreground="red")

    
    def build(self):
        self.grid()
        self.label_nombre_usuario.grid(row=0, column=0)
        self.entry_nombre_usuario.grid(row=0, column=1)
        
        self.label_nombre.grid(row=1, column=0)
        self.entry_nombre.grid(row=1, column=1)
        
        self.label_edad.grid(row=2, column=0)
        self.entry_edad.grid(row=2, column=1)
        
        self.label_password.grid(row=3, column=0)
        self.entry_password.grid(row=3, column=1)

        self.label_repetir_password.grid(row=4, column=0)
        self.entry_repetir_password.grid(row=4, column=1)

        self.error_message_formulario_invalido.grid()    
        self.button_guardar.grid(row=5, column=0)   
        self.button_quit.grid(row=5, column=1)


    def validar_nombre_usario(self, nombre_usuario):

        self.error_message_nombre_de_usuario.grid(row=0, column=2)
        if "" == nombre_usuario:
            pass
        elif nombre_usuario[0].isnumeric():
            self.error_message_nombre_de_usuario[
                "text"
            ] = "error: usuario no puede empezar con un número."
            
            return False

        if nombre_usuario in base_de_datos:
            self.error_message_nombre_de_usuario["text"] = "error: usuario ya existe."
            return False

        self.error_message_nombre_de_usuario["text"] = ""
        return True

    def validar_nombre(self, nombre):
        self.error_message_nombre.grid(row=1, column=2)
        if "" == nombre:
            return False
        elif not nombre.isalpha():
            self.error_message_nombre[
                "text"
            ] = "error: Nombre tiene que ser string alfabético"
            return False
        elif len(nombre) < 4:
            self.error_message_nombre[
                "text"
            ] = "error: nombre tiene que ser mayor a tres caracteres"
            return False

        self.error_message_nombre["text"] = ""
        return True

    def validar_edad(self, edad):
        self.error_message_edad.grid(row=2, column=2)
        if "" == edad:
            return False
        elif not edad.isnumeric() or int(edad) < 1:
            self.error_message_edad[
                "text"
            ] = "error: Edad tiene que ser un valor numérico entero mayor a 0"
            return False
        self.error_message_edad["text"] = ""
        return True

    def validar_password(self, password):
        self.error_message_password.grid(row=3, column=2)
        if "" == password:
            return False
        elif "?" not in list(password) and "#" not in list(password):
            self.error_message_password[
                "text"
            ] = "error: Password tiene que tener almenos uno de estos caracteres ?, #"
            return False
        self.error_message_password["text"] = ""
        return True

    def validar_si_password_coincide(self, repetir_password):
        if "" == repetir_password:
            return False
        if self.entry_password["text"] != repetir_password:
            self.error_message_repetir_password["text"] = "Error: Passwords y repetir password no son iguales."
            return False
        self.error_message_repetir_password["text"] = "" 
        return True


    def es_formulario_valido(self):

        return all([self.entry_nombre_usuario.validate(), 
        self.entry_nombre.validate(),
        self.entry_edad.validate(),
        self.entry_password.validate()]
        )


    def alta_usuario(self):

        if self.es_formulario_valido():
            print(self.entry_nombre_usuario.get())
            base_de_datos[self.entry_nombre_usuario.get()] = {
                "nombre": self.entry_nombre.get(),
                "edad": self.entry_edad.get(),
                "password": self.entry_password.get(),
            }
        else:
            print(base_de_datos)
            self.error_message_formulario_invalido.grid(row=5, column=2)
            self.error_message_formulario_invalido["text"] = ("Formulario invalido  corrija errores!!")
            

    def borrar_usuario(self):
        if self.entry_nombre_usuario in base_de_datos:
            del base_de_datos[self.entry_nombre_usuario]
            print(f"se borro con éxito el usuario {self.entry_nombre_usuario}")
        else:
            print(f"Usuario ingresado {self.entry_nombre_usuario} no existe")

    def modificar_usuario(self):
        info = {"nombre": self.entry_nombre, "edad": self. entry_error, "password": self.entry_password}
        base_de_datos[self.entry_nombre_usuario] = info
        print(f"Se modificó con éxito el usuario: {self.entry_nombre_usuario}")
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
        self.title("My Awesome App")


if __name__ == "__main__":
    app = App()
    frame = MainFrame(app, padding=100)

    frame.build()
    app.mainloop()
