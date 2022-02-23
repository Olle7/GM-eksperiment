from sympy import *
from sympy.plotting import plot3d

var("sigma,sigma_t,sigma_r,p,omega,ro,mu,r2,r1,nu_g",positive=True)

#((ro*omega*(3+mu)*(r2-r1)**2)/8 )**2+( ro*omega*((1-mu)*r1**2+(3+mu)*r2**2)/4 )**2

#sigma_t=simplify((ro*omega*(3+mu)*(r2-r1)**2)/8)
#sigma_r=ro*omega*((1-mu)*r1**2+(3+mu)*r2**2)/4
#sigma=simplify((sigma_t**2+sigma_r**2)**(1/2))
#sigma=simplify((( (ro*omega*(3+mu)*(r2-r1)**2)/8 )**2+( ro*omega*((1-mu)*r1**2+(3+mu)*r2**2)/4 )**2)**(1/2))
#print(simplify(sigma)==simplify((sigma_t**2+sigma_r**2)**(1/2)))

def my_latex(vorrand):
    v=latex(vorrand).replace(".0","")
    for i in range(10):
        v=v.replace("_{"+str(i)+"}","_"+str(i)).replace("^{"+str(i)+"}","^"+str(i))
    return v


max_omega=simplify(solve((( (ro*omega*(3+mu)*(r2-r1)**2)/8 )**2+( ro*omega*((1-mu)*r1**2+(3+mu)*r2**2)/4 )**2)**(1/2)-sigma,omega)[1])
print("omega=",my_latex(max_omega))

B_G=simplify(max_omega*(r2**2-r1**2)*ro*nu_g/2)
print("B_G=",my_latex(B_G))

B_G_p=simplify(B_G.subs(r1,r2*p))
print("B_G(p)=",my_latex(B_G_p))

plot3d(B_G_p.subs(nu_g,1).subs(sigma,1), (p, 0, 1),(mu,-5,1))

tuletis=simplify(diff(B_G_p,p))
print("dB_G/dp=",my_latex(tuletis))

#U 0.15 on parim p


#LIHTSUSTAN KÄSITSI:
tuletis=8*mu**2*p**4-32*mu**2*p**3+48*mu**2*p**2-32*mu**2*p+8*mu**2+48*mu*p**4-64*mu*p**3+288*mu*p**2-320*mu*p+48*mu+72*p**4-416*p**3+432*p**2-672*p+72
plot3d(tuletis.subs(nu_g,1).subs(sigma,1),0, (p, 0, 1),(mu,-1,5))
#murru_alune=10*dl**4*mu**2 - 4*dl**4*mu + 26*dl**4 - 32*dl**3*mu**2*r2 + 64*dl**3*mu*r2 - 32*dl**3*r2 + 32*dl**2*mu**2*r2**2 - 128*dl**2*mu*r2**2 + 96*dl**2*r2**2 + 128*dl*mu*r2**3 - 128*dl*r2**3 + 128*r2**4
#juure_alune=

#latex(diff(diff(vordeline_BGga,dl),dl))

parim_p=simplify(solve([tuletis.subs(nu_g,1).subs(sigma,1),mu>0,mu<10,p>=0,p<=1],p))#4 erinevat piecewise'i.
print("pp=",my_latex(parim_p))
print(len(parim_p))
for l in parim_p:
    print(l)
print(dir(parim_p[1]))
print(parim_p[1].removeO())
print("lihtsustus",end="")
print(parim_p[1].simplify())

#käsitsi:
#-1/(-5*mu^2*p^4 + 4*mu^2*p^3 + 2*mu^2*p^2 + 4*mu^2*p - 5*mu^2 + 2*mu*p^4 + 24*mu*p^3 - 20*mu*p^2 + 24*mu*p - 30*mu - 13*p^4 + 36*p^3 - 78*p^2 + 36*p - 45)^(1/2)*(1-p^2)