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

        container.resizable(False, False) 
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
            container, text="Alta", command=self.alta_usuario
        )
        self.button_quit = ttk.Button(container, text="Salir", command=container.destroy)
        self.button_borrar = ttk.Button(container, text="Baja", command=self.baja_usuario)

        self.error_message_nombre_de_usuario = ttk.Label(container, foreground="red")
        self.error_message_nombre = ttk.Label(container, foreground="red")
        self.error_message_edad = ttk.Label(container, foreground="red")
        self.error_message_password = ttk.Label(container, foreground="red")
        self.error_message_repetir_password = ttk.Label(container, foreground="red")
        self.error_message_formulario_invalido = ttk.Label(container, foreground="red")
        self.table_usuarios = ttk.Treeview(container)
        self.item_selected = []

    def build(self):
        self.grid()

        self.label_nombre_usuario.grid(row=0, column=0, sticky="e")
        self.entry_nombre_usuario.grid(row=0, column=1, sticky="w")
        self.error_message_nombre_de_usuario.grid(row=0, column=2, sticky="w")
        self.entry_nombre_usuario.focus_set()

        self.label_nombre.grid(row=1, column=0, sticky="e")
        self.entry_nombre.grid(row=1, column=1, sticky="w")
        self.error_message_nombre.grid(row=1, column=2, sticky="w")

        self.label_edad.grid(row=2, column=0, sticky="e")
        self.entry_edad.grid(row=2, column=1, sticky="w")
        self.error_message_edad.grid(row=2, column=2, sticky="w")

        self.label_password.grid(row=3, column=0, sticky="e")
        self.entry_password.grid(row=3, column=1, sticky="w")
        self.error_message_password.grid(row=3, column=2, sticky="w")
        
        self.label_repetir_password.grid(row=4, column=0, sticky="e")
        self.entry_repetir_password.grid(row=4, column=1, sticky="w")
        self.error_message_repetir_password.grid(row=4, column=2, sticky="w")

        self.error_message_formulario_invalido.grid()
        self.button_borrar.grid(row=7, column=1, sticky="e")
        self.button_guardar.grid(row=5, column=1, sticky="e")
        
        self.table_usuarios.grid(row=6, column=0, columnspan=2, sticky="w")
        self.table_usuarios["columns"] = (
            "nombre_usuario",
            "nombre",
            "edad",
            "password",
        )

        self.table_usuarios.column("#0", width=0, stretch=0)
        self.table_usuarios.column("nombre_usuario", anchor=CENTER, width=80)
        self.table_usuarios.column("nombre", anchor=CENTER, width=80)
        self.table_usuarios.column("edad", anchor=CENTER, width=80)
        self.table_usuarios.column("password", anchor=CENTER, width=80)

        self.table_usuarios.heading("#0", text="", anchor=CENTER)
        self.table_usuarios.heading(
            "nombre_usuario", text="Nombre Usuario", anchor=CENTER
        )
        self.table_usuarios.heading("nombre", text="Nombre", anchor=CENTER)
        self.table_usuarios.heading("edad", text="Edad", anchor=CENTER)
        self.table_usuarios.heading("password", text="Password", anchor=CENTER)
        self._carga_tabla()

    def _carga_tabla(self, lineas=base_de_datos):
        for k, v in lineas.items():
            values = tuple([k] + list(v.values()))
            self.table_usuarios.insert(
                parent="", index="end", iid=k, text="", values=values
            )

    def validar_nombre_usario(self, nombre_usuario):
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
        if self.entry_password.get() != repetir_password:
            self.error_message_repetir_password[
                "text"
            ] = "Error: Passwords y repetir password no son iguales."
            return False
        self.error_message_repetir_password["text"] = ""
        return True

    def es_formulario_valido(self):

        return all(
            [
                self.entry_nombre_usuario.validate(),
                self.entry_nombre.validate(),
                self.entry_edad.validate(),
                self.entry_password.validate(),
                self.entry_repetir_password.validate()
            ]
        )

    def blanquear_campos(self):
        self.entry_nombre_usuario.delete(0, "end")
        self.entry_nombre.delete(0, "end")
        self.entry_edad.delete(0, "end")
        self.entry_password.delete(0, "end")
        self.entry_repetir_password.delete(0, "end")

    def alta_usuario(self):
        if self.es_formulario_valido():
            print(self.entry_nombre_usuario.get())
            linea = { self.entry_nombre_usuario.get():{
                "nombre": self.entry_nombre.get(),
                "edad": self.entry_edad.get(),
                "password": self.entry_password.get(),
                }
            }
            base_de_datos.update(linea)
            self._carga_tabla(linea)
            self.blanquear_campos()
            self.entry_nombre_usuario.focus_set()
            self.error_message_formulario_invalido[
                "text"
            ] = ""
        else:
            print(base_de_datos)
            self.error_message_formulario_invalido.grid(row=5, column=2)
            self.error_message_formulario_invalido[
                "text"
            ] = "Formulario invalido  corrija errores!!"

    def baja_usuario(self):
        for nombre_usuario in self.table_usuarios.selection():
            if nombre_usuario in base_de_datos:
                del base_de_datos[nombre_usuario]
                self.table_usuarios.delete(nombre_usuario)
                self.entry_nombre_usuario.focus_set()
                print(f"se borro con éxito el usuario {nombre_usuario}")
            else:
                print(f"Usuario seleccionado {nombre_usuario} no existe")

    def modificar_usuario(self):
        info = {
            "nombre": self.entry_nombre,
            "edad": self.entry_error,
            "password": self.entry_password,
        }
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
        self.title("ABM de Usuario")


if __name__ == "__main__":
    app = App()
    frame = MainFrame(app, padding=100)

    frame.build()
    app.mainloop()
