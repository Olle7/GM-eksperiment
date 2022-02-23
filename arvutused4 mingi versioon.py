from sympy import *
from sympy import symbols
sigma,sigma_t,sigma_r,tühi_osa_raadiusest_1,dl2,omega,ro,mu,r2,r1,nu_g,m_2,m_1=symbols("sigma,sigma_t,sigma_r,tühi_osa_raadiusest_1,dl2,omega,ro,mu,r2,r1,nu_g,m_2,m_1",positive=True)
def my_latex(vorrand):
    v=latex(vorrand).replace(".0","")
    for i in range(10):
        v=v.replace("_{"+str(i)+"}","_"+str(i)).replace("^{"+str(i)+"}","^"+str(i))
    return v
def küsi_väärtus(küsitav,vaike):
    v=input(küsitav+":")
    if v:
        return float(v)
    return vaike
from math import pi
c=299792458
k_G=6.67384*10**-11
#nu_g=4*pi*k_G/c**2

max_omega=simplify(solve((( (ro*omega*(3+mu)*(r2-r1)**2)/8 )**2+( ro*omega*((1-mu)*r1**2+(3+mu)*r2**2)/4 )**2)**(1/2)-sigma,omega)[1])
#print("omega=",my_latex(max_omega))

B_G=simplify(max_omega*(r2**2-r1**2)*ro*nu_g/2)
#print("B_G=",my_latex(B_G))

B_G_p=simplify(B_G.subs(r1, r2 * tühi_osa_raadiusest_1))
#print("B_G(p)=",my_latex(B_G_p))

max_omega=simplify(max_omega.subs(r1, r2 * tühi_osa_raadiusest_1))

mu_v=küsi_väärtus("poissoni tegur",-2)
#plot(B_G_p,(mu,-0.1,5))
B_G_p=simplify(B_G_p.subs(mu,mu_v))


#tuletis=str(simplify(diff(B_G_p,p)))
#print(tuletis)
#exec("tuletis=simplify("+tuletis[tuletis.find("(")+1:tuletis.find(")")+1])
#print(tuletis)

tuletis=simplify(diff(B_G_p, tühi_osa_raadiusest_1)).subs(nu_g, 1).subs(sigma, 1)
#print(tuletis)
parim_p=nsolve(tuletis,0.15)
print("parim täidetus=",parim_p)
print("B_G_p/nu/sigma=", simplify(B_G_p.subs(nu_g,1).subs(sigma,1).subs(tühi_osa_raadiusest_1, parim_p)))
sigma_v=küsi_väärtus("maksimaalne tõbetugevus",3.3*10**10)

B_G_p=simplify(B_G_p.subs(sigma,sigma_v).subs(tühi_osa_raadiusest_1, parim_p).subs(nu_g, 4 * pi * k_G / c ** 2))
print("B_G=",B_G_p)
r2_v=küsi_väärtus("silindri raadius",5)
ro_v=küsi_väärtus("tihedus",22570)
print("nurkkiirus=", simplify(max_omega.subs(sigma,sigma_v).subs(mu,mu_v).subs(tühi_osa_raadiusest_1, parim_p).subs(ro, ro_v).subs(r2, r2_v)))


mõõtva_ketta_oomega=simplify(B_G_p*(m_2**4-m_1**4)/(m_2**2-m_1**2)**2/2)
print("mõõtvaketta omega on:",mõõtva_ketta_oomega)
mõõtva_ketta_oomega=simplify(mõõtva_ketta_oomega.subs(m_1,m_2-dl2))
#mõõtva_ketta_oomega=mõõtva_ketta_oomega.subs(m_2,1)
print("mõõtvaketta omega on:",mõõtva_ketta_oomega)
m_2_v=küsi_väärtus("silindri, mille pöörlema hakkamise abil GM välja mõõdetakse välimine raadius(et antud lähendus kehtiks peab see olema palju väikse, kui pöörleva välja tekitava silindri raadius)",0.1)
mõõtva_ketta_oomega=mõõtva_ketta_oomega.subs(m_2,m_2_v)
print("mõõtvaketta nurkkiirus peale esmase ketta peatamist on:",mõõtva_ketta_oomega.subs(dl2,küsi_väärtus("mõõtva silindri seina paksus",0.0001)))#0,1*mm
plot(mõõtva_ketta_oomega.subs(m_2,m_2_v),(dl2,-m_2_v*0.01,m_2_v),nb_of_points=2000,xlabel="mõõtva silindri seina paksus")
#from sympy.plotting import plot3d

dt=m_2_v=küsi_väärtus("silindri peatamiseks kuluv aeg",0.1)#et katki ei läheks. Tegelikult kindlasti rohkem kui 1 sekund.
h=küsi_väärtus("teisese silindri kõrgus",0.5)#teisese silindri kõrgus. Tehtud lährenduste tkehtimiseks peab esmase silindri kõrgusest üpalju väiksem olema.
ro_2=küsi_väärtus("teisese silindri tihedus",22570)

teisele_silindrile_tekitatav_jõumoment=simplify(pi*h*ro_2*B_G_p*h*m_2**4).subs(m_2,m_2_v)
print("teisele_silindrile_tekitatav_jõumoment on:",teisele_silindrile_tekitatav_jõumoment)