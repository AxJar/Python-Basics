print("Este programa a partir de segundos , despliega la equivalencia en horas, minutos y segundos lo que tarda en realizar un participante el triatlon")
seg = int(input("Ingrese el tiempo que tarda en realizar el participante el triatlon , en segundos "))
horas = seg//3600
sob_horas = seg%3600
minutos = sob_horas//60
sob_minutos = sob_horas%60
segundos = sob_minutos
print("El tiempo que tarda en realizar el participante es de ", horas, " hora(s), ", minutos, " minuto(s), ", segundos, " segundos(s)")
