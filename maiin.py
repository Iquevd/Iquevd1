tabla_periodica={
    'Tl':{
        'Nombre':'Talio',
        'Número Atómico':81,
        'Peso Atómico':204.3833,
        'Estado de Oxidación':1-3,
        'Densidad':11.85
    },
    'Pb':{
        'Nombre':'Plomo',
        'Número Atómico':82,
        'Peso Atómico':207.2,
        'Estado de Oxidación':2-4,
        'Densidad':11.34
    },
       'Bi':{
        'Nombre':'Bismuto',
        'Número Atómico':83,
        'Peso Atómico':208.9803,
        'Estado de Oxidación':3-5,
        'Densidad':9.78
    },
    'Po':{
        'Nombre':'Polonio',
        'Número Atómico':84,
        'Peso Atómico':208.9824,
        'Estado de Oxidación':2-4,
        'Densidad':9.19
    },
}
print("Bienvenido a la Tabla Periódica de los Elementos!")
print("Ingrese por favor la opcion que desee buscar el elemento: 1(Símbolo)")
opcion=int(input())
if opcion==1:
    simbolo=input("Ingrese el símbolo del elemento químico: ")
    print("La información del elemento químico",simbolo,"es",tabla_periodica[simbolo])

"""
tabla_periodicax={'H':1.00794,'He':4.002602,'Li':6.941,'Be':9.012182,'B':10.811,'C':12.0107,'N':14.0067,'O':15.9994,'F':18.998403,'Ne':20.1797,'Na':22.98976,'Mg':24.3050,'Al':26.98153,'Si':28.0855,'P':30.97696,'S':32.065,'Cl':35.453,'Ar':39.948,'K':39.0983,'Ca':40.078,'Sc':44.95591,'Ti':47.867,'V':50.9415,'Cr':51.9962,'Mn':54.93804,'Fe':55.845,'Co':58.93319,'Ni':58.6934,'Cu':63.546,'ZN':65.38,'Ga':69.723,'Ge':72.64,'As':74.92160,'Se':78.96,'Br':79.904,'Kr':83.798,'Rb':85.4678,'Sr':87.62,'Y':88.90585,'Zr':91.224,'Nb':92.90638,'Mo':95.96,'Tc':98,'Ru':101.07,'Rh':102.9055,'Pd':106.42,'Ag':107.8682,'Cd':112.441,'In':114.818,'Sn':118.710,'Sb':121.760,'Te':127.60,'I':126.9044,'Xe':131.293,'Cs':132.9054,'Ba':137.327,'Lu':174.9668,'Hf':178.49,'Ta':180.9478,'W':183.84,'Re':186.207,'Os':190.23,'Ir':192.217,'Pt':195.084,'Au':196.9665,'Hg':200.59,'Ti':204.3833,'Pb':207.2,'Bi':208.9804,'Po':208.9824,'At':209.9871,'Rn':220.0175,'Fr':223.0197,'Ra':226.0254,'Ac':227.0278,'Lr':262,'Rf':261.11,'Db':262.114,'Sg':263.12,'Bh':262.12,'Hs':264,'Mt':266.1378,'Ds':269,'Rg':272,'Cn':277,'Ra':140.115,'Pr':140.90765,'Nd':144.24,'Pm':114.9127,'Sm':150.36,'Eu':151.965}
print("Desea abrir la opción Calculadora de Compuestos: 1(Si) o 2(No)")
opcion1=int(input())
otravez=input()
contador=0
sumatorio=0
if opcion1==1:
    compuesto=int(input("Ingrese los elementos que tiene su compuesto: "))
    while(contador<compuesto):
        print("Ingrese el",contador+1,"elemento químico: ")
        elemento=input()
        multiplicacion=float(input("Ingrese la cantidad por la cual lo va a multitplicar: "))
        key=tabla_periodicax.get(elemento)
        resultado=multiplicacion*key
        print(f"El resultado de la multiplicacion es: {resultado}")
        sumatoria=sumatoria+resultado
        contador+=1
        print(f"El peso atomico del compuesto es de: {sumatoria}")
        print("Desea calcular otro compuesto: 1(Si) o 2(No)")
elif otravez==1:
    compuesto=int(input("Ingrese los elementos que tiene su compuesto: "))
elif otravez==2:
    print("Gracias por usar el programa, hasta pronto!")
"""
