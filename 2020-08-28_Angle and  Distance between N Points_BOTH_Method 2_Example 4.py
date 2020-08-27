import math
#Comentario:
##N_p, N_a,Nb, E_p,E_a,E_b) Coordenadas en metros
##pow = power = elevado a la potencia, ejemplo:  x^0.5 = pow(x,0.5)
## 1 pi = 180 degrees = 57.2956  : Conversion Factor

def CalculateBoth(N_p, N_a,N_b, E_p,E_a,E_b):

    distance = round(math.pow(((N_p - N_a)**2 + ( E_p -E_a)**2),0.5),3)


    angle = "%.3f"%(90 - (180/math.pi)* (math.atan((N_p - N_a)/(E_p - E_a)) + math.atan((E_b - E_a)/(N_b - N_a))))

    return distance,angle


distance,angle = CalculateBoth(2055.55,2000,2077.869,1160.245,1000, 1078.331)
print(distance,angle )
