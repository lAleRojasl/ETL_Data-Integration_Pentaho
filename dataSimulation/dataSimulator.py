import csv
import string
import random
from random import randint
from datetime import date, timedelta
import operator

#Estrategia de produccion ATO - Assemble To Order
#products ordered by customers are produced quickly and are customizable to a certain extent.
#The assemble-to-order (ATO) strategy requires that the basic parts for the product are already
#manufactured but not yet assembled. Once an order is received, the parts are assembled quickly and sent to the customer.

distribuidores = ["Allied Electronics","Neward","Toyo Communication Equipment CO.",
                  "NIC Components Corporations","RCD Components","Megaphase LLC","RARA Electronics Corp.",
                  "Avnet Inc.", "Future Electronics", "Digi-Key Corp.", "Bisco Industries Inc."]

mats_comunes = [("Battery","B"), ("Capacitor","C"), ("Microprocessor","MP"), ("Cathode Ray Tube","CTR"),
              ("Fuse","F"), ("Gas Discharge Tube","GDT"), ("Wire Link", "WL"), ("Motor","M"),
              ("Junction Gate Field-effect transistor","JFET"),("Glass Lense","GL"), ("Circuit Breaker","CBK"),("Resistor","R"),
              ("Operational Amplifier","OP"),("Silicon controlled rectifier","SCR"),("Switch","SW"), ("Peltier Cooler","PCL"),
              ("Tunnel Diode", "TDE"),("Metal Oxide Semiconductor FET","MOSFET"),("Static Induction transistor","SIT"),
              ("Filament lamp","FLP"),("LCD Screen","LCD"),("Light Emitting Diode","LED"), ("Phototube","PTT"),("Nixie Tube","NXT"),
              ("Transformer","T"),("Thin film transistor","TFT"),("Digital signal processor","DSP"),
              ("Integrated Circuit","IC"),("Variable capacitor","VC"),("Plastic Casing","PCS"),("Digital Signal Processor","DSP"),
              ("Relay","RLA"),("Field effect Transistor","FET"),("Very Large Scale Integration","VLSI"),
              ("Valve Tube","V"),("Crystal resonator","CRS"),("Test Point","TP"),("Zener Diode","ZDE"), ("Motherboard","MB")]

#productos IoT Nombre - Descripcion - link
productos = [("Ankuoo NEO Smart Switch","http://www.ankuoo.com/products/?sort=2","SS","1","25.99"),
             ("BayitHome Switch","http://www.bayithomeautomation.com/products/bayit-switch/","SS","1","39.99"),
             ("BlueSpray Irrigation","https://www.bluespray.net/","IRS","2","89.99"),
             ("Blossom Sprinkler System","https://www.myblossom.com/","IRS","2","99.99"),
             ("GreenIQ Smart Garden","http://greeniq.co/","IRS","2","185.99"),
             ("Neurio Energy Monitor","https://www.neur.io/","EM","3","219.99"),
             ("Eyedro Electricity Monitor","http://eyedro.com/home-electricity-monitors/","EM","3","250.99"),
             ("Smappee Electicity Monitor","http://www.smappee.com/eu_es/monitor-de-energia/","EM","3","229.99"),
             ("Smappee Gas&Water Monitor","http://www.smappee.com/eu_es/monitor-de-agua-y-gas/","GWM","4","315.99"),
             ("AcuRite Sensors","https://www.acurite.com/indoor-outdoor-thermometer-humidity-sensor-hd-display-my-acurite.html","THM","5","80.99"),
             ("Keen Temp&Air Control","https://keenhome.io/","THM","5","99.99"),
             ("ConnectSense Temperature Sensor","https://www.connectsense.com/wireless-temperature-sensor","THM","5","75.99"),
             ("SensorPush Monitors","http://www.sensorpush.com/","THM","5","88.85"),("LIFX SmartBulbs","https://www.lifx.com/","SLB","6","45.95"),
             ("Phillips Hue Bulbs","http://www2.meethue.com/en-us/productdetail/philips-hue-white-and-color-ambiance-br30-e26","SLB","6","60.99"),
             ("FluxSmart Bulbs","https://www.fluxsmartlighting.com/products/flux-bluetooth","SLB","6","75.99"),
             ("August Smart Lock","http://august.com/products/august-smart-lock/","SLK","7","140.95"),
             ("August Doorbell Cam","http://august.com/products/doorbell-camera/","SLK","7","99.95"),
             ("Lockitron Bolt","https://lockitron.com/","SLK","7","120.99"),
             ("Chipolo Tracker","https://chipolo.net/products","TKR","8","59.99"),("Lapa KeyTracker","https://findlapa.com/","TKR","8","39.99"),
             ("Neposmart Outdoor Camera","https://neposmart.com/outdoor-camera/","CAM","9","399.99"),
             ("Neposmart Indoor Camera","https://neposmart.com/indoor-camera/","CAM","9","420.95")]

max_mats = 6000

generated_mats = 0

base_mats = []
base_prods = []
matsXProds = []

#Debemos simular los events ocurridos en un lapso de los ultimos 5 años
#Para esto usamos la libreria datetime para iterar sobre estas fechas de manera precisa.
startDate = date(2012, 5, 7)  # start date (lunes)
endDate = date(2017, 5, 31)  # end date

#Funcion para devolver la fecha X dias despues de la fecha actual
def getNextDate(currentDate, moveDays=1):
    return currentDate + timedelta(days=moveDays)

#dato = getNextDate(startDate, 20)
#print(dato)
#print(getNextDate(dato,20))

#Funcion para generar numeros seriales random de materiales o productos
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

with open('matsData.csv', 'w', newline='') as matsCSV:
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
        #Vamos a usar stocks entre 40 y 60 hasta llegar a un total de 6000
        random_stock = randint(40,60)
            
        #Total de materiales que hemos generado
        generated_mats += random_stock

        #Generamos un costo del material
        random_cost = round(random.uniform(0.01,0.9),5)

        #Lista con la base de materiales iniciales
        base_mats.append([random_mat_name,mat_model,random_stock,random_cost])
        
    sortedlist = sorted(base_mats)
    for mat in sortedlist:
        spamwriter = csv.writer(matsCSV, delimiter=',',
                          quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([mat[0],mat[1],mat[2]])

with open('prodsData.csv', 'w', newline='') as prodCSV:
    for i in range(0,len(productos)):
        prod = productos[i]
        prod_models = randint(3,6)
        for x in range(0,prod_models):
            #Formato: Letra + '-' + numero. Ej: TKR-52 para productos de Smart Tracking
            prod_modelNum = randint(0,100)
            prod_model = prod[2] + '-' + str(prod_modelNum)
            base_prods.append([prod[0],prod[1],prod_model,prod[3],prod[4]])
            spamwriter = csv.writer(prodCSV, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([prod[0],prod[1],prod_model,prod[3],prod[4]])


#Teniendo los productos y los materiales base
#Podemos simular cuales materiales se necesitan para ensamblar cada producto
#   - Vamos a asumir que un dispositivo necesita en promedio ~60 materiales
#     divididos entre 10 a 25 tipos. Esto es, un dispositivo puede necesitar
#     por ejemplo, 6 transistores, 4 resistores, 2 baterias, 1 motor, etc.
with open('matXProdData.csv', 'w', newline='') as mXpCSV:
    matNum = 0
    cant_prods = len(base_prods)
    for i in range(0, cant_prods):
        matNum += 1
        #cantidad de materiales necesarios para un producto
        distribucion_mats = randint(10,25)
        #escogemos los 10 a 25 materiales aleatorios (sin repetir) 
        selected_mats = random.sample(range(1,len(base_mats)),distribucion_mats)
        for matXprod in selected_mats:
            mat_cant = randint(1,6)
            matsXProds.append([matNum, matXprod, mat_cant])
            spamwriter = csv.writer(mXpCSV, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([matNum, matXprod, mat_cant])
                

#Debemos simular las entradas y salidas de materiales durante 5 años
#Aspectos a considerar:
#   - Deben ser 80000 movimientos, esto es aproximadamente 43.8 movimientos por dia
#     O 333 movimientos por semana.
#   VENTAS:
#   - Las ventas deben sumar 9000 en los ultimos 5 años, lo que son 1800 al año, 150 por mes o 37 por semana.
#   SALIDAS:
#   - Para tratar de hacerlo mas distribuido vamos a usar un random entre 1 y 7
#     que determine el dia a la semana que se hicieron las salidas
#   ENTRADAS:
#   - Vamos a asumir que las entradas (re-supply) son en base a los componentes que se
#     van gastando, por lo que a principio de cada semana (lunes) se hacen ordenes de compra con los componentes que estan
#     por debajo de cierta cantidad minima (30). Esta orden llega a la bodega entre 2 a 5 dias despues.


with open('simSalidas','w',newline='') as salidasCSV:
    with open('simOrdenesCompra','w',newline='') as ordenesCSV:
        with open('simLineasXOrden','w',newline='') as lineasCSV:
            with open('simVentasXCliente','w',newline='') as ventasCSV:
                with open('simVariacionPrecios','w',newline='') as variacionesCSV:
                    #Iteramos sobre todas las fechas desde 1-5-2012 hasta 31-5-2017 (~5 años)
                    delta = endDate - startDate
                    currentDate = startDate
                    currentMonth = currentDate.month
                    min_prods_changed = int(len(base_prods)/3)
                    max_prods_changed = int(len(base_prods) - min_prods_changed)
                    while currentDate < endDate:
                        currentDate = getNextDate(currentDate)

                        #A principio de cada semana (cada lunes)
                        #Vamos a simular las ordenes de compra en base a lo que se gasto la semana anterior
                        if(currentDate.weekday() == 1):
                            #Cada mes se ajustan los precios de ciertos productos para controlar la demanda y ganancias
                            if(currentMonth != currentDate.month):
                                #print("New month. Prices changes for some products")
                                #Cantidad de precios de productos a modificar
                                cant_mod_prods = randint(min_prods_changed,max_prods_changed)
                                #escogemos aleatoriamente cuales se modifican (sin repetir)
                                selected_prods = random.sample(range(len(base_prods)),cant_mod_prods)
                                #moficamos cada precio con +- %10 uniform(-10,10)
                                for prodIndex in selected_prods:
                                    mod_prct = random.uniform(-0.05,0.06)
                                    temp_price = float(base_prods[prodIndex][4])
                                    new_price = str(round((temp_price + temp_price*mod_prct), 2))
                                    base_prods[prodIndex][4] = new_price
                                    spamwriter = csv.writer(variacionesCSV, delimiter=',',
                                                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                    spamwriter.writerow([prodIndex+1,new_price,str(currentDate)])
                                currentMonth = currentDate.month
                            
                                
                        
                        
                        #Cada dia se hacen entre 4 y 8 ventas a clientes (tenemos un listado de 1000 clientes generados)
                        week_sales = randint(4,8)
                        #Determinamos cuales clientes compraron esos productos y lo guardamos
                        # for x in range(week_sales):
                            
                        #spamwriter = csv.writer(ventasCSV, delimiter=',',
                         #                       quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        #spamwriter.writerow([])

            

print(len(base_mats))
print(len(base_prods))

