def calcularGrade(score):
    if(score >= 0.9 and score <= 1.0):
        grade = "Sobresaliente"
    elif (score >= 0.8 and score < 0.9):
        grade = "Notable"
    elif (score >= 0.7 and score < 0.8):
        grade = "Bien"
    elif (score >= 0.6 and score < 0.7):
        grade = "Suficiente"
    elif (score >= 0 and score < 0.6):
        grade= "insuficiente"
    else:
        grade = "score no valido"
    return grade

try:
    score= float(input("ingrese la calificación(0.01 - 1.00):"))
    grade = calcularGrade(score)
    print ("El grado de de su calificacion es:", grade)
except:
    print ("error, debe ingresar un valor numerico")