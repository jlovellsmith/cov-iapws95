#import iapws.iapws95_parameters_150908b as iapws 
#import iapws.iapws95_parameters_151023_rho_data_0_9corr as iapws
#import iapws95_parameters_151023_rho_data_99corr as iapws
from GTC import *
from iapws.iapws95_fluid_1_161020 import *
"""iapws95_fluid_1_151216.py
Dens_ex_Tp_151216.py
Attempt to calculate desity for T and p in order to compare T-rho-p input 
data and fitted uncertainties in density, 
"""
#==========================================================================
Version = "Dens_ex_Tp_151216.py using dens data" 
#==========================================================================
import math as mm
from itertools import izip 

#==========================================================================
# Critical Point
#Tc = 647.096  ##CP_temperature_si, K
#rhoc = 322    ## CP_density_si,  kg/m3
print "Tc  1.", Tc.x, Tc.u, Tc.u/Tc.x*100,"%"

Tc1 = ureal(647.096,0,inf,"Tc")  ##CP_temperature_si, K
rhoc1 = ureal(322,0,inf,"rhoc")    ## CP_density_si,  kg/m3
R = 461.51805 ## Specific gas constant, J/kg/K    
ErrorReturn = 9.99999999E+98  



pcm="F12347_ALL_ideal_uy160921r0a.py"
fname= 'Data_Trho_for_w_160426.txt'
with open(fname, 'r') as f:
    header1 = f.readline()
#    header2 = f.readline()
#    header3 = f.readline()
    print header1,"using",pcm#,header2, header3
    ## #print header2
    ## #print header3,flu_f_si
    for line in f:
        columns = line.split()
        t_si = ureal(float(columns[0]),0,inf)
        print t_si.x,
        for col_ind in (1,2,3,4,5,6):
            d_si=ureal(float(columns[col_ind]),0,inf)
            cp=Cp(d_si/rhoc1,Tc1/t_si)
            print cp.u/cp.x, #cp.u/cp.x,
        print


## t_si =ureal(300,2,inf)
## d_si=ureal(1000,0,inf)
## cp=Cp(d_si/rhoc,Tc/t_si)
## print cp.x, cp.u, cp.u/cp.x
## print "---------------------"
## print "u(cp:t_si)", reporting.u_component(cp, t_si) 
## #print "u(cp:n33)", reporting.u_component(cp, ni33) 

## print "---------------------"

## for l,u in reporting.budget(cp,trim=0):
    ## print "%s: %G" % (l,u)

