class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_apellido(self, apellido):
        self._apellido = apellido

    def __str__(self):
        return f"{self._apellido}, {self._nombre}"
    
    
class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha):
        self._titulo = titulo
        self._autor = autor  # tipo Persona
        self._isbn = isbn
        self._paginas = paginas
        self._edicion = edicion
        self._editorial = editorial
        self._ciudad = ciudad
        self._pais = pais
        self._fecha = fecha

    def get_titulo(self): 
        return self._titulo
    def get_autor(self): 
        return self._autor
    def get_isbn(self): 
        return self._isbn
    def get_paginas(self): 
        return self._paginas
    def get_edicion(self): 
        return self._edicion
    def get_editorial(self): 
        return self._editorial
    def get_ciudad(self): 
        return self._ciudad
    def get_pais(self): 
        return self._pais
    def get_fecha(self): 
        return self._fecha

    def set_titulo(self, titulo): 
        self._titulo = titulo
    def set_autor(self, autor): 
        self._autor = autor
    def set_isbn(self, isbn): 
        self._isbn = isbn
    def set_paginas(self, paginas): 
        self._paginas = paginas
    def set_edicion(self, edicion): 
        self._edicion = edicion
    def set_editorial(self, editorial): 
        self._editorial = editorial
    def set_ciudad(self, ciudad): 
        self._ciudad = ciudad
    def set_pais(self, pais): 
        self._pais = pais
    def set_fecha(self, fecha): 
        self._fecha = fecha


    def leer_informacion(self):
        self._titulo = input("Título: ")
        self.nombre = input("Nombre del autor: ")
        self.apellido = input("Apellido del autor: ")
        self._autor = Persona(nombre, apellido)
        self._isbn = input("ISBN: ")
        self._paginas = int(input("Número de páginas: "))
        self._edicion = input("Edición: ")
        self._editorial = input("Editorial: ")
        self._ciudad = input("Ciudad: ")
        self._pais = input("País: ")
        self._fecha = input("Fecha de edición: ")

    def mostrar_informacion(self):
        print(f"Título: {self._titulo} {self._edicion} edición")
        print(f"Autor: {self._autor}")
        print(f"ISBN: {self._isbn}")
        print(f"{self._editorial}, {self._ciudad} ({self._pais})")
        print(f"{self._fecha}")
        print(f"{self._paginas} páginas")