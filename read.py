#Class zone, used to save the data from all the zones
class Zone:
    number=0
    busy=0
    total=0
    def __init__(self,number,busy):
        self.number=number
        self.total=1
        if busy=="Ocupado\n":
            self.busy=1
            
    def getNumber(self):
        return self.number
    
    def getBusy(self):
        return self.busy

    def setBusy(self,busy):
        self.busy=busy

    def increaseBusy(self):
        self.busy+=1

    def getTotal(self):
        return self.total

    def setTotal(self,total):
        self.total=total

    def increaseTotal(self):
        self.total+=1

    def printZone(self):
        print ("Zone: ",self.number,"\nTotal: ",self.total,"\nBusy: ",self.busy)
        

#this function is used to obtain data from the txt file
def obtainData():

    #opening the text file
    file=open("prueba.txt","r")



    line=[] #includes all the lines in the file
    
    i=0
    text=file.readline()


    #reading the text file
    while text!="":
        line.append(text)
        line[i]=line[i].split(",")
        i+=1
        text=file.readline()

    file.close() #closing the file
    return line



#this function initializes the list of zone objects based on the line list
def initializeZones(line):
    zones=[] #includes the object of class zone
    
    #initializing the zone list objects to None
    for x in range (len(line)):
        zones.append(None)


    #Introducing the zones according to the list
    for x in line:
        if(zones[int(x[0])]==None):
            zones[int(x[0])]=Zone(int(x[0]),x[2])
        else:
            zones[int(x[0])].increaseTotal()

            if x[2]=="Ocupado\n":
                       zones[int(x[0])].increaseBusy()

    noneCount=0 #variable to count the number of nones
    for x in zones: #counting the None objects in the list
        if x==None:
            noneCount+=1

    for x in range(noneCount): #removing the nones in the list
        zones.remove(None)      

    return zones

#Updates the data of the zone to the database
def update(zone):
    url="ITESM/Zone"+str(zone.getNumber())
    #update busy and update total with zone.getBusy and zone.getTotal     
    print (url)

    
line=obtainData()
zones=initializeZones(line)


for x in zones:
        update(x)
        x.printZone()

print (line[0][0])

'''
print (line[0].count("Libre\n"))
print (line[7][0])
print (len(line))
print (len(zones))
'''
