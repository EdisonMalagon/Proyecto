print("--------------------------------------------------------------------------")
print("                           Calculadora Quimica                            ")
print("--------------------------------------------------------------------------")
d1=int(input("Digite la funcion que desea utilizar 1. Convertir temperaturas  2. Convertir presiones 3. Numero de moles 4. reactivo limite y en execeso 5. Gases ideales 6. Rendimiento procentual: "))
while True:
  if(d1==1):
    d2=int(input("1. celsius a kelvin 2. kelvin a celsius 3. fahrenheit a rankie 4. rankie a fahrenheit: "))
    if(d2==1):
      ti=float(input("digite la temperatura °C: "))
      tf=ti+273.15
      print(tf,"°K")
    if(d2==2):
      ti=float(input("digite la temperatura °K: "))
      tf=ti-273.15
      print(tf,"°C")
    if(d2==3):
      ti=float(input("digite la temperatura °F: "))
      tf=ti+459.67
      print(tf,"°R")
    if(d2==4):
      ti=float(input("digite la temperatura °R: "))
      tf=ti-459.67
      print(tf,"°F")
  if(d1==2):
    d2=int(input("1. atm a bar 2. atm a pascal 3. bar a atm 4. bar a pascal 5. pascal a atm 6. pascal a bar: "))
    if(d2==1):
      pi=float(input("Digite la presion en atm: "))
      pf=pi*1.01325
      print(pf,"Bar")
    if(d2==2):
      pi=float(input("Digite la presion en atm: "))
      pf=pi*101325
      print(pf,"pascales")
    if(d2==3):
      pi=float(input("Digite la presion en Bar: "))
      pf=pi/1.013
      print(pf,"atm")
    if(d2==4):
      pi=float(input("Digite la presion en Bar: "))
      pf=pi*100000
      print(pf,"Pascales")
    if(d2==5):
      pi=float(input("Digite la presion en pascales: "))
      pf=pi/101300
      print(pf,"atm")
    if(d2==6):
      pi=float(input("Digite la presion en pascales: "))
      pf=pi/100000
      print(pf,"Bar")
  if(d1==3):
    print("Digite la masa total seguido por un espacio y la masa molecular del reactivo: ")
    datos=input()
    mt,mm=datos.split(" ")
    mt=float(mt)
    mm=float(mm)
    n=mt/mm
    print(n,"moles")
  if(d1==4):
    print("Digite el numero de moles del primer reactivo seguido de un espacio y el coeficiente estequiometrico, este se obtiene observando la ecuacion balanceada: ")
    datos=input()
    m,c=datos.split(" ")
    m=float(m)
    c=float(c)
    print("Digite el numero de moles del segundo reactivo seguido de un espacio y el coeficiente estequiometrico, este se obtiene observando la ecuacion balanceada: ")
    datos=input()
    m2,c2=datos.split(" ")
    m2=float(m2)
    c2=float(c2)
    r1=m/c
    r2=m2/c2
    if(r1>r2):
      print("El reactivo 1 es el reactivo en exceso, el reactivo 2 es el limitante")
    else:
      print("El reactivo 2 es el reactivo en exceso, el reactivo 1 es el limitante")
  if(d1==5):
    d2=int(input("Digite la variable a hallar 1. presion 2.Volumen 3. moles 4.temperatura: "))
    if(d2==1):
      print("Digite los datos en el siguiente orden separados por un espacio volumen, moles, R(esta es una constante rectifica que las unidades suplan la ecuacion), temperatura: ")
      datos=input()
      v,n,r,t=datos.split(" ")
      v=float(v)
      n=float(n)
      r=float(r)
      t=float(t)
      p=(n*r*t)/v
      print("presion es", p)
    if(d2==2):
      print("Digite los datos en el siguiente orden separados por un espacio presion, moles, R(esta es una constante rectifica que las unidades suplan la ecuacion), temperatura: ")
      datos=input()
      p,n,r,t=datos.split(" ")
      p=float(p)
      n=float(n)
      r=float(r)
      t=float(t)
      v=(n*r*t)/p
      print("volumen es", v)
    if(d2==3):
      print("Digite los datos en el siguiente orden separados por un espacio volumen, presion, R(esta es una constante rectifica que las unidades suplan la ecuacion), temperatura: ")
      datos=input()
      v,p,r,t=datos.split(" ")
      v=float(v)
      p=float(p)
      r=float(r)
      t=float(t)
      n=(p*v)/(r*t)
      print("moles es", n)
    if(d2==4):
      print("Digite los datos en el siguiente orden separados por un espacio volumen, moles, R(esta es una constante rectifica que las unidades suplan la ecuacion), presion: ")
      datos=input()
      v,n,r,p=datos.split(" ")
      v=float(v)
      n=float(n)
      r=float(r)
      p=float(p)
      t=(p*v)/(n*r)
      print("temperatura es", t)
  if(d1==6):
    print("Digite el rendimiento real seguido de un espacio y el rendimiento teorico: ")
    datos=input()
    r,t=datos.split(" ")
    r=float(r)
    t=float(t)
    rp=(r/t)*100
    print(rp,"%")
  i=int(input("Digite 1 para hacer otro calculo o 0 para finalizar: "))
  if(i==0):
    break