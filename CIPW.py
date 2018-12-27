import numpy as np
import matplotlib as plt

oxidos=np.genfromtxt("oxidos1.txt", usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14))
#1:SiO2, 2:TiO2, 3:Al2O3, 4:Fe2O3, 5:FeO, 6:FeO_T, 7:MnO, 8:MgO, 9:CaO, 10:Na2O, 11:K2O, 12:P2O5, 13:LOI, 14:Suma
muestras=np.genfromtxt("oxidos1.txt", dtype="|U5", usecols=(0)) #Numero de muestra

