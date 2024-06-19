import csv

################
def eliminar(id_e,listita):
    for p in listita:
        if id_e==p[0]:
            listita.remove(p)
            print("Producto eliminado correctamente...")
            break
        
################
        ## precio < 1000 : barato
        ##precio 1000 y 10000 : comprable
        ##precio>10000 caro
#### funcion encontrar producto
def buscar(id_e,listita):
    encontrado=False
    for p in listita :
        if id_e==p[0]:
            print("producto encontrado : \n")
            print(f"ID : {p[0]} Nombre : {p[1]} Precio : {p[2]} Categoria : {p[3]}")
            encontrado=True
            break
    if encontrado==False:
        print("El producto no esta en la lista ")

lista=[]
while(True):
    print("")
    print(".-.-.- M E N U .-.-.-")
    print("")
    print("1.- Agregar producto")
    print("2.- Listar productos")
    print("3.- Eliminar por id")
    print("4.- Generar archivo CSV")
    print("5.- Cargar archivo CSV")
    print("6.- Estadísticas")
    print("7.- Buscar producto por id: ")
    print("0.- Salir")
    print("")
    op=int(input("Ingrese una opción : "))
    if op==1:
        print("")
        print(".-.A G R E G A R   P R O D U C T O .-.--.")
        print("")
        id=int(input("Ingrese id : "))
        nombre=input("Ingrese nombre : ")
        precio=int(input("Ingrese precio : "))
        if precio<1000:
            categoria="barato"
        elif precio>=1000 and precio<=10000:
            categoria="comprable"
        elif precio>10000:
            categoria="caro"
            
        producto=[id,nombre,precio,categoria]
        lista.append(producto)
        print("Producto agregado correctamente...")
    elif op==2:
        print("")
        print(".-.-L I S T A   P R O D U C T O S .-.-")
        print("")
        for p in lista:
            print(f"ID : {p[0]} Nombre : {p[1]} Precio : {p[2]} Categoria : {p[3]}")
            print(".-.-.-.-.-.")        
        
    elif op==3:
        encontrado=False
        print("")
        print(".-.- E L I M I N A R   P R O D U C T O .-.-")
        print("")
        id_eliminar=int(input("Ingrese id a eliminar : "))

        eliminar(id_eliminar,lista)

        '''
        for p in lista:
            if id_eliminar==p[0]:
                encontrado=True
                lista.remove(p)
                break
        '''
    
    elif op==4:
        print("")
        print(".-.- GENERANDO BASE DE DATOS .-.-.-")
        print("") 
        with open ('bbdd_producto.csv','w',newline='') as bbdd_producto:
            escritor_csv = csv.writer(bbdd_producto)
            escritor_csv.writerow(['id','nombre','precio','categoria'])
            escritor_csv.writerows(lista)
        print("")    
        print("Archivo generado correctamente...")
    elif op==5:
        print("")
        print(".-.- CARGANDO BASE DE DATOS.-.-")
        print("")
        lista.clear()
        cont=0
        with open ('bbdd_producto.csv','r',newline='') as bbdd_producto:
            lector_csv = csv.reader(bbdd_producto)
            for fila in lector_csv:
                if cont==0:
                    cont+=1 #--> cont=cont+1
                    continue
                i=int(fila[0])
                n=fila[1]
                p=int(fila[2])
                c=fila[3]
                listita_chica=[i,n,p,c]
                lista.append(listita_chica)
                
        #lista.pop(0)
    elif op==6:
        acum=0
        print("")
        print(".-.-.- E S T A D Í S T I C A S  .-.-.-")
        print("")
        cant=len(lista)
        if cant>0:
            for p in lista:
                acum = acum+p[2]
            prom = acum/cant
            print("Productos        : ",cant)
            print("Precio acumulado : ",acum)
            print("Precio promedio  : ",prom)
        else:
            print("No hay productos agregados...")
    elif op==7:
        print("")
        print(".-.- B U S C A N D O   P R O D U C T O .-.-")
        print("")
        id_buscar = int(input("Ingrese el id del producto a buscar : "))
        buscar(id_buscar,lista)
        
                
        
    elif op==0:
        print("")
        print("Adioooooooooooooooooos")
        break
    else:
        print("")
        print("Ingrese una opción válida..")
    
