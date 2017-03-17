from Proyecto2.Clase.Alumno import Alumno
from datetime import date
from Proyecto2.Clase.Materia import Materia

UnAlumno=Alumno()
UnAlumno.setNombre("Allahu")
UnAlumno.setApellido("Akbar")
UnAlumno.setFecha(2017, 3, 17)
UnAlumno.setAgregarNota(9)
UnAlumno.setAgregarNota(8)
UnAlumno.setAgregarNota(7)
UnAlumno.setAgregarNota(10)
UnAlumno.setAgregarNota(6)
print(UnAlumno.mayorNota())

M=Materia()
M.Nombre="Matematica"
M.ListaNotas=[1, 2]
UnAlumno.setMaterias(M)
UnAlumno.setAgregarNota(3)

