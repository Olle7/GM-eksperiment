from sympy import *
var("sigma,sigma_t,sigma_r,dl,omega,ro,mu,r2,r1,nu_g",positive=True)
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


omega_lahend=solve((( (ro*omega*(3+mu)*(r2-r1)**2)/8 )**2+( ro*omega*((1-mu)*r1**2+(3+mu)*r2**2)/4 )**2)**(1/2)-sigma,omega)
#omega_lahend=solve()
#>>> str(omega_lahend).replace("**", "^")
#assert(latex(omega_lahend)=='\\left [ - \\frac{8.0 \\sigma}{ro} \\sqrt{- \\frac{1}{- 5.0 \\mu^{2} r_{1}^{4} + 4.0 \\mu^{2} r_{1}^{3} r_{2} + 2.0 \\mu^{2} r_{1}^{2} r_{2}^{2} + 4.0 \\mu^{2} r_{1} r_{2}^{3} - 5.0 \\mu^{2} r_{2}^{4} + 2.0 \\mu r_{1}^{4} + 24.0 \\mu r_{1}^{3} r_{2} - 20.0 \\mu r_{1}^{2} r_{2}^{2} + 24.0 \\mu r_{1} r_{2}^{3} - 30.0 \\mu r_{2}^{4} - 13.0 r_{1}^{4} + 36.0 r_{1}^{3} r_{2} - 78.0 r_{1}^{2} r_{2}^{2} + 36.0 r_{1} r_{2}^{3} - 45.0 r_{2}^{4}}}, \\quad \\frac{8.0 \\sigma}{ro} \\sqrt{- \\frac{1}{- 5.0 \\mu^{2} r_{1}^{4} + 4.0 \\mu^{2} r_{1}^{3} r_{2} + 2.0 \\mu^{2} r_{1}^{2} r_{2}^{2} + 4.0 \\mu^{2} r_{1} r_{2}^{3} - 5.0 \\mu^{2} r_{2}^{4} + 2.0 \\mu r_{1}^{4} + 24.0 \\mu r_{1}^{3} r_{2} - 20.0 \\mu r_{1}^{2} r_{2}^{2} + 24.0 \\mu r_{1} r_{2}^{3} - 30.0 \\mu r_{2}^{4} - 13.0 r_{1}^{4} + 36.0 r_{1}^{3} r_{2} - 78.0 r_{1}^{2} r_{2}^{2} + 36.0 r_{1} r_{2}^{3} - 45.0 r_{2}^{4}}}\\right ]')
#assert(omega_lahend[0]==-omega_lahend[1])

max_omega=simplify(omega_lahend[1].subs(r1, r2 - dl))
#assert(max_omega==8.0*sigma*sqrt(1/(5.0*dl**4*mu**2 - 2.0*dl**4*mu + 13.0*dl**4 - 16.0*dl**3*mu**2*r2 + 32.0*dl**3*mu*r2 - 16.0*dl**3*r2 + 16.0*dl**2*mu**2*r2**2 - 64.0*dl**2*mu*r2**2 + 48.0*dl**2*r2**2 + 64.0*dl*mu*r2**3 - 64.0*dl*r2**3 + 64.0*r2**4))/ro)
#assert(latex(max_omega)=='\\frac{8.0 \\sigma}{ro} \\sqrt{\\frac{1}{5.0 dl^{4} \\mu^{2} - 2.0 dl^{4} \\mu + 13.0 dl^{4} - 16.0 dl^{3} \\mu^{2} r_{2} + 32.0 dl^{3} \\mu r_{2} - 16.0 dl^{3} r_{2} + 16.0 dl^{2} \\mu^{2} r_{2}^{2} - 64.0 dl^{2} \\mu r_{2}^{2} + 48.0 dl^{2} r_{2}^{2} + 64.0 dl \\mu r_{2}^{3} - 64.0 dl r_{2}^{3} + 64.0 r_{2}^{4}}}')

#latex(max_omega_dl).replace(r"\\",r"\")
B_G=simplify(max_omega*dl*(2*r2-dl)*ro*nu_g/2)

tuletis=simplify(diff(B_G,dl))
print("t:",tuletis)
#LIHTSUSTAN KÄSITSI:
#tuletis=-16*dl**4*mu**2-96*dl**4*mu-144*dl**4+256*dl**3*mu*r2-256*dl**3*r2-768*dl**2*mu*r2**2+768*dl**2*r2**2+512*dl*mu*r2**3-1536*dl*r2**3+1024*r2**4
#murru_alune=10.0*dl**4*mu**2 - 4.0*dl**4*mu + 26.0*dl**4 - 32.0*dl**3*mu**2*r2 + 64.0*dl**3*mu*r2 - 32.0*dl**3*r2 + 32.0*dl**2*mu**2*r2**2 - 128.0*dl**2*mu*r2**2 + 96.0*dl**2*r2**2 + 128.0*dl*mu*r2**3 - 128.0*dl*r2**3 + 128.0*r2**4
#juure_alune=

#latex(diff(diff(vordeline_BGga,dl),dl))

parim_dl=simplify(solve(tuletis,dl))#4 erinevat piecewise'i.
print(type(parim_dl[0]),dir(parim_dl[0]))
print(my_latex(parim_dl))
print("---")
print(parim_dl)
print(parim_dl[0]==simplify(parim_dl[0]))
#print(parim_dl[1])
#print(parim_dl[2])
#print(parim_dl[3])
tx_dl_a=(str(parim_dl[0]),str(parim_dl[1]),str(parim_dl[2]),str(parim_dl[3]))
for i in range(len(str(parim_dl[0]))):
    if not tx_dl_a[0][i]==tx_dl_a[1][i]==tx_dl_a[2][i]==tx_dl_a[3][i]:
        print(i,str(parim_dl[0])[i],str(parim_dl[1])[i],str(parim_dl[2])[i],str(parim_dl[3])[i])
print(str(parim_dl[0])==str(parim_dl[1])==str(parim_dl[2])==str(parim_dl[3]))
#>>> latex(simplify(diff(vordeline_BGga,dl)))
#>>> latex(simplify(diff(vordeline_BGga,dl)))==latex(diff(vordeline_BGga,dl))

#tuletis=r2*sigma*(-16*dl**4*mu**2 - 96*dl**4*mu - 144*dl**4 + 256*dl**3*mu*r2 - 256*dl**3*r2 - 768*dl**2*mu*r2**2 + 768*dl**2*r2**2 + 512*dl*mu*r2**3 - 1536*dl*r2**3 + 1024*r2**4)
#parim_dl=solve(tuletis,dl)"""