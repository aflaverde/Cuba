import numpy as np
from CIPW import *

############################################

#Normalizacion a condrito segun Thompson, 1982
ce_cond =  0.87
sr_cond = 11.80
nd_cond =  0.63
p_cond  = 46.00
sm_cond =  0.20
zr_cond =  6.84
hf_cond =  0.20
ti_cond =620.00
tb_cond =  0.05
y_cond  =  2.00
tm_cond =  0.03
yb_cond =  0.22

############################################

norm_varios = np.genfromtxt("Norm_MORB.txt")

############################################
norm_sunmcd = np.genfromtxt("Norm_Sun_McDonough-1989.txt", delimiter=",") #Normalización según Sun & McDonough, 1989

cond_sunmcd = norm_sunmcd[1:,1]
manto_sunmcd = norm_sunmcd[1:,2]
N_MORB_sunmcd = norm_sunmcd[1:,3]
E_MORB_sunmcd = norm_sunmcd[1:,4]
OIB_sunmcd = norm_sunmcd[1:,5]

############################################




print(cond_sunmcd)