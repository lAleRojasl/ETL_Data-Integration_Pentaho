import csv
import string
import random
from random import randint
from datetime import date, timedelta

#Estrategia de produccion ATO - Assemble To Order
#products ordered by customers are produced quickly and are customizable to a certain extent.
#The assemble-to-order (ATO) strategy requires that the basic parts for the product are already
#manufactured but not yet assembled. Once an order is received, the parts are assembled quickly and sent to the customer.

distribuidores = ["Allied Electronics","Neward","Toyo Communication Equipment CO.",
                  "NIC Components Corporations","RCD Components","Megaphase LLC","RARA Electronics Corp.",
                  "Avnet Inc.", "Future Electronics", "Digi-Key Corp.", "Bisco Industries Inc."]

mats_comunes = [("Battery","B"), ("Capacitor","C"), ("Microprocessor","MP"), ("Cathode Ray Tube","CTR"),
              ("Fuse","F"), ("Gas Discharge Tube","GDT"), ("Wire Link", "WL"), ("Motor","M"),
              ("Junction Gate Field-effect transistor","JFET"), ("Circuit Breaker","MCB"),("Resistor","R"),
              ("Operational Amplifier","OP"),("Silicon controlled rectifier","SCR"),("Switch","SW"),
              ("Transformer","T"),("Thin film transistor","TFT"),("Digital signal processor","DSP"),
              ("Integrated Circuit","IC"),("Variable capacitor","VC"),("Plastic Casing","PCS"),("Digital Signal Processor","DSP"),
              ("Relay","RLA"),("Field effect Transistor","FET"),("Very Large Scale Integration","VLSI"),
              ("Valve Tube","V"),("Crystal resonator","X"),("Test Point","TP"),("Zener Diode","Z")]

#productos IoT Nombre - Descripcion - link
productos = [("Ankuoo NEO Smart Switch","http://www.ankuoo.com/products/?sort=2","SS","1"),
             ("BayitHome Switch","http://www.bayithomeautomation.com/products/bayit-switch/","SS","1"),
             ("BlueSpray Irrigation","https://www.bluespray.net/","IRS","2"),
             ("Blossom Sprinkler System","https://www.myblossom.com/","IRS","2"),("GreenIQ Smart Garden","http://greeniq.co/","IRS","2"),
             ("Neurio Energy Monitor","https://www.neur.io/","EM","3"),
             ("Eyedro Electricity Monitor","http://eyedro.com/home-electricity-monitors/","EM","3"),
             ("Smappee Electicity Monitor","http://www.smappee.com/eu_es/monitor-de-energia/","EM","3"),
             ("Smappee Gas&Water Monitor","http://www.smappee.com/eu_es/monitor-de-agua-y-gas/","GWM","4"),
             ("AcuRite Sensors","https://www.acurite.com/indoor-outdoor-thermometer-humidity-sensor-hd-display-my-acurite.html","THM","5"),
             ("Keen Temp&Air Control","https://keenhome.io/","THM","5"),
             ("ConnectSense Temperature Sensor","https://www.connectsense.com/wireless-temperature-sensor","THM","5"),
             ("SensorPush Monitors","http://www.sensorpush.com/","THM","5"),("LIFX SmartBulbs","https://www.lifx.com/","SLB","6"),
             ("Phillips Hue Bulbs","http://www2.meethue.com/en-us/productdetail/philips-hue-white-and-color-ambiance-br30-e26","SLB","6"),
             ("FluxSmart Bulbs","https://www.fluxsmartlighting.com/products/flux-bluetooth","SLB","6"),
             ("August Smart Lock","http://august.com/products/august-smart-lock/","SLK","7"),
             ("August Doorbell Cam","http://august.com/products/doorbell-camera/","SLK","7"),
             ("Lockitron Bolt","https://lockitron.com/","SLK","7"),
             ("Chipolo Tracker","https://chipolo.net/products","TKR","8"),("Lapa KeyTracker","https://findlapa.com/","TKR","8"),
             ("Neposmart Outdoor Camera","https://neposmart.com/outdoor-camera/","CAM","9"),
             ("Neposmart Indoor Camera","https://neposmart.com/indoor-camera/","CAM","9")]

max_mats = 6000

generated_mats = 0

base_mats = []
base_prods = []

#Debemos simular los events ocurridos en un lapso de los ultimos 5 años
#Para esto usamos la libreria datetime para iterar sobre estas fechas de manera precisa.
startDate = date(2012, 10, 1)  # start date
endDate = date(2017, 5, 31)  # end date

#Funcion para devolver la fecha X dias despues de la fecha actual
def getNextDate(currentDate, moveDays=1):
    delta = endDate - currentDate         # timedelta
    return currentDate + timedelta(days=moveDays)

#dato = getNextDate(startDate, 20)
#print(dato)
#print(getNextDate(dato,20))

#Funcion para generar numeros seriales random de materiales o productos
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

with open('simData.csv', 'w', newline='') as matsCSV:
    #Primero vamos a generar una lista de materiales iniciales
    #En base a estos se van a generar las "entradas" y "salidas" para que sea mas realista
    #Luego de realizar las entradas y salida nos va a quedar un 
    while(generated_mats < 6000):
        #Material random basado en la lista de posibilidades
        random_mat = random.choice(mats_comunes)
        random_mat_name = random_mat[0]
        random_mat_letter = random_mat[1]
         
        #Modelo generado basado en el material seleccionado.
        #Formato: Letra + '-' + numero. Ej: C-592 para un Capacitor
        mat_modelNum = randint(0,1000)
        mat_model = random_mat_letter + '-' + str(mat_modelNum)

        #Cantidad disponible (Stock).
        #Deben haber suficientes materiales para 100 dispositivos
        #Vamos a usar stocks entre 45 y 75 hasta llegar a un total de 6000
        random_stock = randint(45,75)
            
        #Total de materiales que hemos generado
        generated_mats += random_stock

        #Generamos un costo del material
        random_cost = round(random.uniform(0.01,0.9),5)

        #Lista con la base de materiales iniciales
        base_mats.append([random_mat_name,mat_model,id_generator(),random_stock])

        spamwriter = csv.writer(matsCSV, delimiter=',',
                           quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([random_mat_name,mat_model,id_generator(),random_stock])

with open('prodsData.csv', 'w', newline='') as prodCSV:
    for i in range(0,len(productos)):
        prod = productos[i]
        prod_models = randint(3,6)
        for x in range(0,prod_models):
            #Formato: Letra + '-' + numero. Ej: TKR-52 para productos de Smart Tracking
            prod_modelNum = randint(0,100)
            prod_model = prod[2] + '-' + str(prod_modelNum)
            base_prods.append([prod[0],prod[1],prod_model,prod[3]])
            spamwriter = csv.writer(prodCSV, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([prod[0],prod[1],prod_model,prod[3]])


#Teniendo los productos y los materiales base
#Podemos simular cuales materiales se necesitan para ensamblar cada producto
#   - Vamos a asumir que un dispositivo necesita en promedio ~60 materiales
#     divididos entre 12 a 20 tipos. Esto es, un dispositivo puede necesitar
#     por ejemplo, 6 transistores, 4 resistores, 2 baterias, 1 motor, etc.
with open('matXProdData.csv', 'w', newline='') as mXpCSV:
    matNum = 0
    cant_prods = len(base_prods)
    for i in range(0, cant_prods):
        matNum += 1
        #cantidad de materiales necesarios para un producto
        distribucion_mats = randint(14,20)
        #escogemos los 12 a 20 materiales aleatorios (sin repetir) 
        selected_mats = random.sample(range(1,len(base_mats)),distribucion_mats)
        for matXprod in selected_mats:
            mat_cant = randint(3,6)
            spamwriter = csv.writer(mXpCSV, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([matNum, matXprod, mat_cant])
                

#Debemos simular las entradas y salidas de materiales durante 5 años
#Aspectos a considerar:
#   - Deben ser 80000 movimientos, esto es aproximadamente 43.8 movimientos por dia
#     O 333 movimientos por semana.
#   SALIDAS:
#   - Las salidas van a ser la cantidad de componentes que necesita un producto(entre 50 y 70), multiplicado por otro
#     random entre 3 y 6 que representen los dispositivos que se vendieron
#     esa semana y que deben ser ensamblados con dichos componentes.
#     R(50,70)*R(3,6). Esto nos da un minimo de 300 y un maximo de 420 movimientos semanales.
#   - Para tratar de hacerlo mas distribuido vamos a usar un random entre 1 y 7
#     que determine el dia a la semana que se hicieron las salidas
#   ENTRADAS:
#   - Vamos a asumir que las entradas (re-supply) son en base a los componentes que se
#     van gastando, por lo que a principio de cada semana (lunes) se hacen ordenes de compra con los componentes que estan
#     por debajo de cierta cantidad. Esta orden llega a la bodega entre 2 a 5 dias despues.

with open('simMovements','w',newline='') as movsCSV:
    currentDate = startDate
    
    spamwriter = csv.writer(movsCSV, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([])

print(len(base_mats))
print(len(base_prods))

