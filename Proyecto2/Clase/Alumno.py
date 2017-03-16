from datetime import date
class Alumno(object)
    Nombre=" "
    Apellido=" "
    FechaN=None
    ListaNotas=[]
    def setNombre(self, n):
        self.Nombre=n
    def setApellido(self, n):
        self.Apellido=n
    def setFecha(self, a, m, d):
        self.FechaN=(int(a),int(m),int(d))
    def setAgregarNota(self, n):
        self.ListaNotas.append()=n
    def menorNota(self):
        menor=ListaNotas[0]
        for Valor in ListaNotas:
            if Valor < menor:
                menor = Valor
        return menor
    def mayorNota(self):

    def promedioNota(self):
