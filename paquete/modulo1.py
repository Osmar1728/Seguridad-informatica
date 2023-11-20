def info():
    
    nombre =str(input("Cual es tu nombre? "))
    ap_paterno =str(input("Tu apellido paterno "))
    ap_materno =str(input("Tu apellido materno "))
    edad =str(input("Tu edad"))
    altura =float(input("Cuanto mides "))
    nombre_completo = f"{nombre} {ap_paterno} {ap_materno}"

    print("Hola, mi nombre es:", nombre_completo, "tengo", edad, "años de edad, yo mido", altura)
    
    
    return