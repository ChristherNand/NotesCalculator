def calcularPromedioDeNotas():
	examenes = int(input("Introduzca el numero de notas a evaluar: "))
	notas = []
	acumulador = 0
	porcentaje_eva = 0.55
	while(examenes > 0):
		numNota = 0
		nota = int(input("Introduzca la nota: "))
		notas.append(float(nota))
		examenes= examenes - 1
			
	for i in notas:
		sum = i
		acumulador+=sum
	promedioGeneral = (acumulador/len(notas))
	promedio = (acumulador/len(notas))*porcentaje_eva
	

	print("El promedio general es de",promedioGeneral)	
	print("El promedio de las evaluaciones finales total es de",promedio)	

calcularPromedioDeNotas()

	




	





