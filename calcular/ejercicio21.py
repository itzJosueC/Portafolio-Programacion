antiguedad = int(input('Ingresa el valor de antiguedad: '))
salario = int(input('Ingresa el valor de salario: '))
utilidades = 0

if antiguedad < 1:
    utilidades = 0.05*salario
if antiguedad >=1 and antiguedad <2:
    utilidades = 0.07*salario
if antiguedad >=2 and antiguedad <5:
    utilidades = 0.10*salario
if antiguedad >=5 and antiguedad <10:
    utilidades = 0.015*salario
if antiguedad >=10:
    utilidades = 0.20*salario

print('Valor de utilidades: ' + repr (utilidades))