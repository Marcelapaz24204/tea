def computepay(hours, rate):
    MAX_HOURS = 40
    if ( hours >MAX_HOURS):
        extra_hours = hours - MAX_HOURS
    else:
        extra_hours= 0
    payment = (hours * rate) + (extra_hours * (rate/2))
    return payment

try: 
    hours = float(input("Ingrese el numero de horas:"))
    rate = float(input("Ingrese tarfia por hora:"))
    payment = computepay (hours,rate)
    print("El pago es:", payment)
except:
    print ("Error, favor ingresar un valor numerico")