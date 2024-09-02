class Persona:
    def __init__(self, nombre, apellido, direccion, telefono, edad, email):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.edad = edad
        self.email = email

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email


class Empleado(Persona):
    def __init__(self, nombre, apellido, direccion, telefono, edad, email, nombre_cargo, salario, jefe_inmediato, años_experiencia):
        super().__init__(nombre, apellido, direccion, telefono, edad, email)
        self.nombre_cargo = nombre_cargo
        self.salario = salario
        self.jefe_inmediato = jefe_inmediato
        self.años_experiencia = años_experiencia

    def get_nombre_cargo(self):
        return self.nombre_cargo

    def set_nombre_cargo(self, nombre_cargo):
        self.nombre_cargo = nombre_cargo

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

    def get_jefe_inmediato(self):
        return self.jefe_inmediato

    def set_jefe_inmediato(self, jefe_inmediato):
        self.jefe_inmediato = jefe_inmediato

    def get_años_experiencia(self):
        return self.años_experiencia

    def set_años_experiencia(self, años_experiencia):
        self.años_experiencia = años_experiencia

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
direccion = input("Ingrese la direccion: ")
telefono = input("Ingrese el telefono: ")
edad = int(input("Ingrese la edad: "))
email = input("Ingrese el email: ")
salario = float(input("Ingrese el salario: "))
jefe_inmediato = input("Ingrese el jefe inmediato: ")
años_experiencia = int(input("Ingrese los años de experiencia: "))

cargo = "Empleado"
if salario >= 5000000 and años_experiencia >= 5 and 25 <= edad <= 45:
    cargo = "Senior"
elif 900000 <= salario <= 1200000 and 1 <= años_experiencia <= 2 and 18 <= edad <= 22:
    cargo = "Junior"

empleado = Empleado(nombre, apellido, direccion, telefono, edad, email, cargo, salario, jefe_inmediato, años_experiencia)

print("\nEmpleado:")
print(f"Nombre: {empleado.get_nombre()} {empleado.get_apellido()}")
print(f"Direccion: {empleado.get_direccion()}")
print(f"Telefono: {empleado.get_telefono()}")
print(f"Edad: {empleado.get_edad()}")
print(f"Email: {empleado.get_email()}")
print(f"Salario: {empleado.get_salario()}")
print(f"Jefe Inmediato: {empleado.get_jefe_inmediato()}")
print(f"Años de Experiencia: {empleado.get_años_experiencia()}")
print(f"Cargo: {empleado.get_nombre_cargo()}")
