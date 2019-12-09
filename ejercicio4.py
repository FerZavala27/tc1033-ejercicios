class VehiclesUI():
    def registrar_vehiculos():
        lista=[]
        mod=1
        while mod==1:
            mod==2
            matricula=int(input("Ingrese la matricula a registrar"))
            modelo=str(input("Ingrese el modelo"))
            fabricante=str(input("ingrese el nombre del fabricante"))
            opcion=int(input("Si desea continuar pulse 2, de otro modo para terminar pulse 1"))
            if opcion==1:
                resultado=VehiclesDP.__init__(matricula,modelo,fabricante)
                break
            if opcion==2:
                VehiclesUI.registrar_vehiculos()
    

class VehiclesDP():
    def __init__(resp1,resp2,resp3):
        print(resp1,resp2,resp3)


VehiclesUI.registrar_vehiculos()    
            
    


