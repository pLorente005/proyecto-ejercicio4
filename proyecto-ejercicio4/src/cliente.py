import re

class Cliente:
    def __init__(self, nombre: str, correo: str, telefono: str = ""):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def actualizar_datos(self, nombre: str = None, correo: str = None, telefono: str = None):
        if nombre:
            self.nombre = nombre
        if correo and self._es_correo_valido(correo):
            self.correo = correo
        if telefono:
            self.telefono = telefono

    def _es_correo_valido(self, correo: str) -> bool:
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(patron, correo) is not None

    def resumen(self) -> str:
        return f"Cliente: {self.nombre}\nCorreo: {self.correo}\nTeléfono: {self.telefono or 'No especificado'}"

    def __str__(self):
        return f"{self.nombre} <{self.correo}>"

if __name__ == "__main__":
    cliente = Cliente("Ana Pérez", "ana@example.com")
    print(cliente.resumen())
    cliente.actualizar_datos(telefono="555-1234")
    print(cliente.resumen())
