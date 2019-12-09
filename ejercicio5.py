class excel():
    po=[]
    def grabar(resp):
        arch=open("vehicles.csv","w")
        resp=resp+"\n"
        arch.write(resp)
        arch.close()
    
   
