Algoritmo Ejercicio_9
	escribir "Digite número: "
	leer numero 
	
	normal <- numero 
	reseverso <- 0
	
	Mientras numero > 0 hacer 
		digito <- numero mod 10
		reverso <- reverso * 10 + digito
		numero <- trunc(numero /10)
	FinMientras
    
	si normal = reverso Entonces
		escribir "es palindromo"
	sino 
		escribir "no es palindromo"
		
	FinSi
	
FinAlgoritmo