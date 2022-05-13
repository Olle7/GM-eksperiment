from math import pi
k_G=6.67384*10**-11
c=299792458
müü_G=4*pi*k_G/c**2#ühik on 1/sekund

#print(müü_G)
#nüü on poissooni tegur
#roo on tihedus
#sigma on maksimaalne mehhaaniline pinge
#pl on rõnga paksus



roo=22570#osmium
sigma=7000*10**6
pl=6*10**-2#1*cm
nüü=0
R=1


oomega_radiaal_piir=(sigma*8/roo/(3+nüü))**(1/2)/pl**2#https://www.engineersedge.com/mechanics_machines/solid_disk_flywheel_design_14642.html
oomega_tangentsiaal_piir=(sigma*8/roo)**(1/2)#https://www.engineersedge.com/mechanics_machines/solid_disk_flywheel_design_14642.html
print(oomega_radiaal_piir,oomega_tangentsiaal_piir)
oomega=max(oomega_tangentsiaal_piir,oomega_radiaal_piir)#makx väärtus. Kui ei tea eeldan, et andmed on sellised, et B oleks kergelt mõõdetav.
#oomega=#https://physics.stackexchange.com/questions/161948/the-storage-of-kinetic-energy-in-a-flywhell/161956#161956


#dmdt=(roo*2*sigma/(3+nüü))*(2*R-pl)
dm2_dmdl=roo*oomega*pl*(2*R-pl)
B_max=müü_G*dm2_dmdl



#F_max=4*v*B_max
print("B_max=",B_max)
print("oomega=",oomega)