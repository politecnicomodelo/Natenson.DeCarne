from datetime import date
from .Materia import Materia

class Alumno(object):

    def __init__(self):
        self.ListaMaterias=[]

    Nombre=" "

    Apellido=" "

    FechaN=None

    def setMaterias(self, n):
        self.ListaMaterias.append(n)

    def setNombre(self, n):
        self.Nombre=n

    def setApellido(self, n):
        self.Apellido=n

    def setFecha(self, a, m, d):
        self.FechaN=date(int(a),int(m),int(d))

    def setAgregarNota(self, n, nota):
        for Variable in self.ListaMaterias:
            if Variable==n:
                self.ListaMaterias[n].ListaNotas.append(nota)

    def menorNota(self, n):
        for Variable in self.ListaMaterias:
            if Variable==n:
                return min(self.ListaMaterias[Variable].ListaNotas)

    def mayorNota(self, n):
        for Variable in self.ListaMaterias:
            if Variable==n:
                return max(self.ListaMaterias[Variable].ListaNotas)

    def promedioNotaMateria(self, n):
        for Variable in self.ListaMaterias:
            if Variable==n:
                return sum(self.ListaMaterias[Variable].ListaNotas)/\
                       len(self.ListaMaterias[Variable].ListaNotas)

    def promedioNotasAlumno(self):
        Suma=0
        for Variable in self.ListaMaterias:
            Suma+=sum(self.ListaMaterias[Variable].ListaNotas)/\
                   len(self.ListaMaterias[Variable].ListaNotas)
        return Suma/len(self.ListaMaterias)

    def promedioMinimo(self):
        ListaPromedios=[]
        for Variable in self.ListaMaterias:
            ListaPromedios[Variable] = sum(
                self.ListaMaterias[Variable].ListaNotas) / \
                                       len(self.ListaMaterias[Variable].ListaNotas)
        return min(self.ListaPromedios)

    def promedioMaximo(self):
        ListaPromedios = []
        for Variable in self.ListaMaterias:
            ListaPromedios[Variable] = sum(
                self.ListaMaterias[Variable].ListaNotas) / \
                                       len(self.ListaMaterias[Variable].ListaNotas)
        return max(self.ListaPromedios)