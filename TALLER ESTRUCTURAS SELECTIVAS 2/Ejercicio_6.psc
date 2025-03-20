Algoritmo Ejercicio_6
	Escribir ("Digite el año: ")
	Leer año
	Si (año mod 4==0) Y (año mod 100<>0) O (año mod 400=0) Entonces
		Escribir "El Año es bisiesto"
	SiNo
		Escribir "El Año no es bisiesto"
	Fin Si
FinAlgoritmo
