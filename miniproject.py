from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def __init__(self, model):
        pass


# creating types of vehicle class

class PassengerVehicle(Vehicle):
    vehicleType = 'PassengerVehicle'

    def vehicleType(self):
        return self.vehicleType


class CargoVehicle(Vehicle):
    vehicleType = 'CargoVehicle'

    def vehicleType(self):
        return self.vehicleType


# creating the real vehicle classes now

class Car(PassengerVehicle):
    count = 0

    def __init__(self, model, vNumber, maxNoOfPassengers, acOrNonac, isHired):
        self._model = model
        self._vNumber = vNumber
        self._maxNoOfPassengers = maxNoOfPassengers
        self._acOrNonac = acOrNonac
        self._isHired = isHired

        Car.count += 1

    # getting and setting hired property of Car
    def getHiredStatus(self):
        return self._isHired

    def setHiredStatus(self, hiredInput):
        self._isHired = False
        self._isHired = hiredInput

    def getModel(self):
        return self._model

    def getvNumber(self):
        return self._vNumber

    def getMaxNoOfPassengers(self):
        return self._maxNoOfPassengers

    def getAcOrNonac(self):
        return self._acOrNonac

    # returns total number of cars we have
    def getNoOfCars(self):
        return self.count


# creating van class
class Van(PassengerVehicle):
    count = 0

    def __init__(self, model, vNumber, maxNoOfPassengers, acOrNonac, isHired):
        self._model = model
        self._vNumber = vNumber
        self._maxNoOfPassengers = maxNoOfPassengers
        self._acOrNonac = acOrNonac
        self._isHired = isHired

        Van.count += 1

    # getting and setting hired property of Van
    def getHiredStatus(self):
        return self._isHired

    def setHiredStatus(self, hiredInput):
        self._isHired = False
        self._isHired = hiredInput

    def getModel(self):
        return self._model

    def getvNumber(self):
        return self._vNumber

    def getMaxNoOfPassengers(self):
        return self._maxNoOfPassengers

    def getAcOrNonac(self):
        return self._acOrNonac

    # returns total number of vans we have
    def getNoOfVans(self):
        return self.count


# creating ThreeWheeler class
class ThreeWheeler(PassengerVehicle):
    count = 0
    maxNoOfPassengers = 3

    def __init__(self, model, vNumber, isHired):
        self._model = model
        self._vNumber = vNumber
        self._maxNoOfPassengers = 3
        self._isHired = isHired

        ThreeWheeler.count += 1

    # getting and setting hired property of ThreeWheeler
    def getHiredStatus(self):
        return self._isHired

    def setHiredStatus(self, hiredInput):
        self._isHired = False
        self._isHired = hiredInput

    def getModel(self):
        return self._model

    def getvNumber(self):
        return self._vNumber

    def getMaxNoOfPassengers(self):
        return self._maxNoOfPassengers

    # returns total number of ThreeWheelers we have
    def getNoOfThreeWheelers(self):
        return self.count


# creating cargo vehicles now

class Truck(CargoVehicle):
    _count = 0

    def __init__(self, model, vNumber, length, isHired):

        self._model = model
        self._vNumber = vNumber
        self._length = length
        self._isHired = isHired

        Truck._count += 1

    # getting and setting hired property of Truck
    def getHiredStatus(self):

        return self._isHired

    def setHiredStatus(self, hiredInput):

        self._isHired = False
        self._isHired = hiredInput

    def getModel(self):

        return self._model

    def getvNumber(self):

        return self._vNumber

    def getLength(self):
        if (self._length == '7ft' or self._length == '12ft'):
            return self._length
        else:
            while self._length != '7ft' and self._length != '12ft':
                print("unidentfied length")
                print("Enter either 7ft or 12 ft ")
                self._length = input("Enter length : ")
            return self._length

    # returns total number of vans we have
    def getNoOfTrucks(self):

        return self._count


# creating lorry class now

class Lorry(CargoVehicle):
    _count = 0

    def __init__(self, model, vNumber, load, isHired):

        self._model = model
        self._vNumber = vNumber
        self._load = load
        self._isHired = isHired

        Lorry._count += 1

    # getting and setting hired property of Lorry
    def getHiredStatus(self):

        return self._isHired

    def setHiredStatus(self, hiredInput):

        self._isHired = False
        self._isHired = hiredInput

    def getModel(self):

        return self._model

    def getvNumber(self):

        return self._vNumber

    def getLoad(self):

        if self._load >= 2500 and self._load <= 3500:

            return self._load
        else:
            while self._load < 2500 or self._load > 3500:
                print("Unidentified Load ")
                print("Only load weight between 2500kg and 3500kg are allowed")
                self._load = int(input("Enter load value : "))
            return self._load

    # returns total number of vans we have
    def getNoOfLorries(self):

        return self._count


# adding new vehicles to the system
# adding cars

car1 = Car("Nissan", "RT3020", 4, "AC", False)
car2 = Car("Toyota", "EX1478", 3, "AC", False)
car3 = Car("Nano", "YG6541", 3, "NON-AC", False)
car4 = Car("Prado", "WE1234", 4, "AC", False)
car5 = Car("Alto", "PO1020", 3, "AC", False)
car6 = Car("Nero", "LP5210", 4, "NON-AC", False)
car7 = Car("Kia", "PO1673", 4, "AC", False)

# adding Vans

van1 = Van("Hiace", "AS5236", 8, "AC", False)
van2 = Van("Dolphin", "KJ2356", 8, "NON-AC", False)
van3 = Van("Sorento", "TR7896", 6, "NON-AC", False)
van4 = Van("Noah", "CV2310", 7, "AC", False)
van5 = Van("Nissan long", "KJ5236", 6, "AC", False)

# adding threewheelers

twheel1 = ThreeWheeler("Bajaj", "OKJ2356", False)
twheel2 = ThreeWheeler("TVS", "AKJ9564", False)
twheel3 = ThreeWheeler("Bajaj", "OLI5214", False)
twheel4 = ThreeWheeler("Bajaj", "MN2310", False)
twheel5 = ThreeWheeler("Piagio", "UY1025", False)
twheel6 = ThreeWheeler("TVS", "LA8961", False)
twheel7 = ThreeWheeler("Bajaj", "AJK1202", False)
twheel8 = ThreeWheeler("Bajaj", "LO5263", False)

# adding trucks

truck1 = Truck("Renault", "EE3210", "7ft", False)
truck2 = Truck("Leyland", "QQ2597", "12ft", False)
truck3 = Truck("Tata", "EL0210", "7ft", False)
truck4 = Truck("Mahindra", "IKN8965", "12ft", False)
truck5 = Truck("Eicher", "KII3265", "7ft", False)

# adding lorries

lorry1 = Lorry("Ram", "CC6666", 2700, False)
lorry2 = Lorry("Ashok", "OO3693", 3500, False)
lorry3 = Lorry("Ashok", "WS8520", 3300, False)
lorry4 = Lorry("Isuzu", "ML9494", 2500, False)

# creating lists of vehicles  - passenger Vehicles
passengerVehicles = []

carVehicles = []
vanVehicles = []
threeWheelVehicles = []

carVehicles.append(car1)
carVehicles.append(car2)
carVehicles.append(car3)
carVehicles.append(car4)
carVehicles.append(car5)
carVehicles.append(car6)
carVehicles.append(car7)

vanVehicles.append(van1)
vanVehicles.append(van2)
vanVehicles.append(van3)
vanVehicles.append(van4)
vanVehicles.append(van5)

threeWheelVehicles.append(twheel1)
threeWheelVehicles.append(twheel2)
threeWheelVehicles.append(twheel3)
threeWheelVehicles.append(twheel4)
threeWheelVehicles.append(twheel5)
threeWheelVehicles.append(twheel6)
threeWheelVehicles.append(twheel7)
threeWheelVehicles.append(twheel8)

passengerVehicles = carVehicles + vanVehicles + threeWheelVehicles

# adding list of cargo vehicles

cargoVehicles = []

truckVehicles = []
lorryVehicles = []

truckVehicles.append(truck1)
truckVehicles.append(truck2)
truckVehicles.append(truck3)
truckVehicles.append(truck4)
truckVehicles.append(truck5)

lorryVehicles.append(lorry1)
lorryVehicles.append(lorry2)
lorryVehicles.append(lorry3)
lorryVehicles.append(lorry4)

cargoVehicles = truckVehicles + lorryVehicles

# hiredvehicles array and not hired vehicles array - passenger vehicles

notHiredCarVehicles = []
hiredCarVehicles = []

notHiredVanVehicles = []
hiredVanVehicles = []

notHiredThreeWheelerVehicles = []
hiredThreeWheelerVehicles = []

# hiredvehicles array and not hired vehicles array - passenger vehicles

notHiredTruckVehicles = []
hiredTruckVehicles = []

notHiredLorryVehicles = []
hiredLorryVehicles = []

# loops to set not hired vehicles and hired vehicles as a queue in seperate arrays - passenger vehicles
for x in range(len(carVehicles)):

    status = str(carVehicles[x].getHiredStatus())
    if status == 'False':
        notHiredCarVehicles.append(carVehicles[x])
    elif status == 'True':
        hiredCarVehicles.append(carVehicles[x])

for x in range(len(vanVehicles)):

    status = str(vanVehicles[x].getHiredStatus())
    if status == 'False':
        notHiredVanVehicles.append(vanVehicles[x])
    elif status == 'True':
        hiredVanVehicles.append(vanVehicles[x])

for x in range(len(threeWheelVehicles)):

    status = str(threeWheelVehicles[x].getHiredStatus())
    if status == 'False':
        notHiredThreeWheelerVehicles.append((threeWheelVehicles[x]))
    elif status == 'True':
        hiredThreeWheelerVehicles.append(threeWheelVehicles[x])

# loops to set not hired vehicles and hired vehicles as a queue in seperate arrays - cargo vehicles
for x in range(len(truckVehicles)):

    status = str(truckVehicles[x].getHiredStatus())
    if status == 'False':
        notHiredTruckVehicles.append(truckVehicles[x])
    elif status == 'True':
        hiredTruckVehicles.append(truckVehicles[x])

for x in range(len(lorryVehicles)):

    status = str(lorryVehicles[x].getHiredStatus())
    if status == 'False':
        notHiredLorryVehicles.append(lorryVehicles[x])
    elif status == 'True':
        hiredLorryVehicles.append(lorryVehicles[x])

#function created on top to access in both passenger and cargo classes
def createObject():

    print("You can create vehicles here...")
    inputVehicleType = input("What type of vehicles do you want to create (car or van or threewheeler or truck or lorry)? :  ").lower()

    if inputVehicleType == 'car':

        inputVehicleName = input("Name your vehicle : ")
        inputVnumber = input("Enter vehicle number : ")
        inputNoOfPassengers = int(input("Enter max passengers (3-4): "))
        inputAcOrNonac = input("Enter whether vehicle is AC or NON-AC : ").upper()

        inputVehicleName = Car(inputVehicleName, inputVnumber, inputNoOfPassengers, inputAcOrNonac, False)

        carVehicles.append(inputVehicleName)
        notHiredCarVehicles.append(inputVehicleName)

    elif inputVehicleType == 'van':

        inputVehicleName = input("Name your vehicle : ")
        inputVnumber = input("Enter vehicle number : ")
        inputNoOfPassengers = int(input("Enter max passengers (3-4): "))
        inputAcOrNonac = input("Enter whether vehicle is AC or NON-AC : ").upper()

        inputVehicleName = Van(inputVehicleName, inputVnumber, inputNoOfPassengers, inputAcOrNonac, False)

        vanVehicles.append(inputVehicleName)
        notHiredVanVehicles.append(inputVehicleName)

    elif inputVehicleType == 'threewheeler':

        inputVehicleName = input("Name your vehicle : ")
        inputVnumber = input("Enter vehicle number : ")

        inputVehicleName = ThreeWheeler(inputVehicleName, inputVnumber, False)

        threeWheelVehicles.append(inputVehicleName)
        notHiredThreeWheelerVehicles.append(inputVehicleName)

    elif inputVehicleType == 'truck':

        inputVehicleName = input("Name your vehicle : ")
        inputVnumber = input("Enter vehicle number : ")
        inputLength = input("Enter length of truck (7ft or 12ft) : ")

        inputVehicleName = Truck(inputVehicleName, inputVnumber, inputLength, False)

        truckVehicles.append(inputVehicleName)
        notHiredTruckVehicles.append(inputVehicleName)

    elif inputVehicleType == 'lorry':

        inputVehicleName = input("Name your vehicle : ")
        inputVnumber = input("Enter vehicle number : ")
        inputLoad = input("Enter Load (2500 - 3500) kg : ")

        inputVehicleName = Lorry(inputVehicleName, inputVnumber, inputLoad, False)

        lorryVehicles.append(inputVehicleName)
        notHiredLorryVehicles.append(inputVehicleName)

    else:
        print("Unidentified vehicle type ...")

#delete vehicles functionality

def removeVehicle():

    print("You can remove vehicles ")
    vehicleType = input("Input vehicle type (car or van or threewheeler or truck or lorry) : ").lower()
    vehicleNum = input("Enter vehicle number (eg : AS2653) : ").upper()

    if vehicleType == 'car':

        for w in range(len(carVehicles)):
            if vehicleNum == str(carVehicles[w].getvNumber()):
                carVehicles.pop(w)
                print("Successfully removed ")
                break

    elif vehicleType == 'van':

        for w in range(len(vanVehicles)):
            if vehicleNum == str(vanVehicles[w].getvNumber()):
                vanVehicles.pop(w)
                print("Successfully removed ")
                break


    elif vehicleType == 'threewheeler':

        for w in range(len(threeWheelVehicles)):
            if vehicleNum == str(threeWheelVehicles[w].getvNumber()):
                threeWheelVehicles.pop(w)
                print("Successfully removed ")
                break

    elif vehicleType == 'truck':

        for w in range(len(truckVehicles)):
            if vehicleNum == str(truckVehicles[w].getvNumber()):
                truckVehicles.pop(w)
                print("Successfully removed ")
                break



    elif vehicleType == 'lorry':

        for w in range(len(lorryVehicles)):
            if vehicleNum == str(lorryVehicles[w].getvNumber()):
                lorryVehicles.pop(w)
                print("Successfully removed ")
                break

    else:
        print("Invalid input ")



# customer interaction setup

print("Welcome to Cab Service")
print("\nIf you are looking to travel as a passenger enter 'p'")
print("If you need to transport goods enter 'c'")

userSelection = input("Enter here : ").upper()
print(userSelection)

if userSelection == 'P':



    def choosePassengerVehicle():
        print("We have Cars, Vans and Three Wheelers..\n")
        print("To select Car , enter 1 ")
        print("To select Van , enter 2 ")
        print("To select ThreeWheeler , enter 3\n")

        vehicleSelection = int(input("Enter : "))

        return vehicleSelection


    def assignCar():

        if len(notHiredCarVehicles) != 0:

            reqInputNoOfPassenger = int(input("Enter No of passengers (3-4): "))
            reqInputAcOrNonac = input("Enter AC or NON-AC : ").upper()

            reqList = []
            for car in range(len(notHiredCarVehicles)):

                if reqInputAcOrNonac == notHiredCarVehicles[car].getAcOrNonac() and reqInputNoOfPassenger <= notHiredCarVehicles[car].getMaxNoOfPassengers():
                    if str(notHiredCarVehicles[car].getHiredStatus()) == 'False':
                        reqList.append(notHiredCarVehicles[car].getvNumber())

            if reqList == []:
                print("Sorry.. the vehicles which meets your requirements aren't available at the moment..")

            else:
                firstVehicle = reqList[0]


                for a in range(len(notHiredCarVehicles)):

                    if notHiredCarVehicles[a].getvNumber() == firstVehicle:
                        latestHired = notHiredCarVehicles[a]
                        hiredCarVehicles.append(latestHired)
                        notHiredCarVehicles.pop(a)
                        hiredCarVehicles[-1].setHiredStatus(True)
                        newHired = hiredCarVehicles[-1].getvNumber()


                        for y in range(len(carVehicles)):
                            if newHired not in carVehicles[y].getvNumber():
                                continue
                            carVehicles[y].setHiredStatus(True)
                        break


                print("you have hired " + latestHired.getModel() + ". The vehicle no is " + latestHired.getvNumber())
                print("Enjoy your ride !")

            print("\nDo you wanna choose a another ride ? ")
            userAnotherRide = input("Enter 'y' for y=Yes and 'n' for No : ").upper()

            while userAnotherRide == 'Y':
                vehicleSelection(choosePassengerVehicle())
                break

            if userAnotherRide == 'N':
                print("Thank you .. ")
                print("Do you want to release from an assigned job (hire) ? : ")
                userRelease = input("Enter 'y' for Yes and 'n' for No : ").upper()
                if userRelease == 'Y':
                    releaseHire()
                    print("Thank you")
                elif userRelease == 'N':
                    print("Thank you ")

                else:
                    print("invalid input given ")



        else:
            print("Sorry currently there aren't any available Cars...\n")
            print("You can check for other passenger vehicles if you wish\n")
            vehicleSelection(choosePassengerVehicle())


    def assignVan():

        if len(notHiredVanVehicles) != 0:

            reqInputNoOfPassenger = int(input("Enter No of passengers (6-8): "))
            reqInputAcOrNonac = input("Enter AC or NON-AC : ").upper()

            reqList = []
            for car in range(len(notHiredVanVehicles)):

                if reqInputAcOrNonac == notHiredVanVehicles[car].getAcOrNonac() and reqInputNoOfPassenger <= notHiredVanVehicles[car].getMaxNoOfPassengers():
                    if str(notHiredVanVehicles[car].getHiredStatus()) == 'False':
                        reqList.append(notHiredVanVehicles[car].getvNumber())

            if reqList == []:
                print("Sorry.. the vehicles which meets your requirements aren't available at the moment..")

            else:
                firstVehicle = reqList[0]


                for a in range(len(notHiredVanVehicles)):

                    if notHiredVanVehicles[a].getvNumber() == firstVehicle:
                        latestHired = notHiredVanVehicles[a]
                        hiredVanVehicles.append(latestHired)
                        notHiredVanVehicles.pop(a)
                        hiredVanVehicles[-1].setHiredStatus(True)
                        newHired = hiredVanVehicles[-1].getvNumber()


                        for y in range(len(vanVehicles)):
                            if newHired not in vanVehicles[y].getvNumber():
                                continue
                            vanVehicles[y].setHiredStatus(True)
                        break


                print("you have hired " + latestHired.getModel() + ". The vehicle no is " + latestHired.getvNumber())
                print("Enjoy your ride !")

            print("\nDo you wanna choose a another ride ? ")
            userAnotherRide = input("Enter 'y' for y=Yes and 'n' for No : ").upper()

            while userAnotherRide == 'Y':
                vehicleSelection(choosePassengerVehicle())
                break

            if userAnotherRide == 'N':
                print("Thank you .. ")
                print("Do you want to release from an assigned job (hire) ? : ")
                userRelease = input("Enter 'y' for Yes and 'n' for No : ").upper()
                if userRelease == 'Y':
                    releaseHire()
                    print("Thank you")
                elif userRelease == 'N':
                    print("Thank you ")
                else:
                    print("invalid input given ")



        else:
            print("Sorry currently there aren't any available Vans...\n")
            print("You can check for other passenger vehicles if you wish\n")
            vehicleSelection(choosePassengerVehicle())


    def assignThreeWheeler():

        if len(notHiredThreeWheelerVehicles) != 0:

            reqInputNoOfPassenger = int(input("Enter No of passengers (max - 3): "))

            reqList = []
            for car in range(len(notHiredThreeWheelerVehicles)):

                if reqInputNoOfPassenger <= notHiredThreeWheelerVehicles[car].getMaxNoOfPassengers():
                    if str(notHiredThreeWheelerVehicles[car].getHiredStatus()) == 'False':
                        reqList.append(notHiredThreeWheelerVehicles[car].getvNumber())

            if reqList == []:
                print("Sorry.. the vehicles which meets your requirements aren't available at the moment..")

            else:
                firstVehicle = reqList[0]


                for a in range(len(notHiredThreeWheelerVehicles)):

                    if notHiredThreeWheelerVehicles[a].getvNumber() == firstVehicle:
                        latestHired = notHiredThreeWheelerVehicles[a]
                        hiredThreeWheelerVehicles.append(latestHired)
                        notHiredThreeWheelerVehicles.pop(a)
                        hiredThreeWheelerVehicles[-1].setHiredStatus(True)
                        newHired = hiredThreeWheelerVehicles[-1].getvNumber()

                        for y in range(len(threeWheelVehicles)):
                            if newHired not in threeWheelVehicles[y].getvNumber():
                                continue
                            threeWheelVehicles[y].setHiredStatus(True)
                        break


                print("you have hired " + latestHired.getModel() + ". The vehicle no is " + latestHired.getvNumber())
                print("Enjoy your ride !")

            print("\nDo you wanna choose a another ride ? ")
            userAnotherRide = input("Enter 'y' for y=Yes and 'n' for No : ").upper()

            while userAnotherRide == 'Y':
                vehicleSelection(choosePassengerVehicle())
                break

            if userAnotherRide == 'N':
                print("Thank you .. ")
                print("Do you want to release from an assigned job (hire) ? : ")
                userRelease = input("Enter 'y' for Yes and 'n' for No : ").upper()
                if userRelease == 'Y':
                    releaseHire()
                    print("Thank you")
                elif userRelease == 'N':
                    print("Thank you ")
                else:
                    print("invalid input given ")

        else:
            print("Sorry currently there aren't any available Three Wheelers ...\n")
            print("You can check for other passenger vehicles if you wish\n")
            vehicleSelection(choosePassengerVehicle())

    #input array name and vehicle number to release hired status
    def releaseHire():
        vehicle = input("\nEnter which vehicle type (car or van or threewheeler): ").lower()
        vNumber = input("Input vNumber : ")

        if vehicle == 'car':

            for d in range(len(hiredCarVehicles)):
                if vNumber == hiredCarVehicles[d].getvNumber():
                    notHiredCarVehicles.append(hiredCarVehicles[d])
                    del hiredCarVehicles[d]
                break

        if vehicle == 'van':

            for d in range(len(hiredVanVehicles)):
                if vNumber == hiredVanVehicles[d].getvNumber():
                    notHiredVanVehicles.append(hiredVanVehicles[d])
                    del hiredVanVehicles[d]
                break

        if vehicle == 'threewheeler':

            for d in range(len(hiredThreeWheelerVehicles)):
                if vNumber == hiredThreeWheelerVehicles[d].getvNumber():
                    notHiredThreeWheelerVehicles.append(hiredThreeWheelerVehicles[d])
                    del hiredThreeWheelerVehicles[d]
                break
    # to find all the vehicles the cab service has
    def seeVehicles():

        print("\nYou can find vehicles we have ")
        vehicle = input("Enter which vehicle type (car or van or threewheeler or all): ").lower()

        if vehicle == 'car':
            for x in carVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

        if vehicle == 'van':
            for x in vanVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

        if vehicle == 'threewheeler':
            for x in threeWheelVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

        if vehicle == 'all':
            for x in passengerVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

    #see hired vehicles

    def seeHiredVehicles():

        print("\nYou can find the currently hired vehicles here")
        vehicle = input("Enter which vehicle type (car or van or threewheeler): ").lower()

        if vehicle == 'car':
            for x in hiredCarVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

        if vehicle == 'van':
            for x in hiredVanVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

        if vehicle == 'threewheeler':
            for x in hiredThreeWheelerVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

    #to see umhired / available vehicles

    def seeAvailableVehicles():

        print("\nYou can find the currently Available (free) vehicles here")
        vehicle = input("Enter which vehicle type (car or van or threewheeler): ").lower()

        if vehicle == 'car':
            for x in notHiredCarVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

        if vehicle == 'van':
            for x in notHiredVanVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

        if vehicle == 'threewheeler':
            for x in notHiredThreeWheelerVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

    def vehicleSelection(vehicleSelection):

        if vehicleSelection == 1:
            assignCar()
        elif vehicleSelection == 2:
            assignVan()
        elif vehicleSelection == 3:
            assignThreeWheeler()
        else:
            print("incorrect value " + str(vehicleSelection))

    #
    vehicleSelection(choosePassengerVehicle())
    createObject()
    seeHiredVehicles()
    seeAvailableVehicles()
    seeVehicles()
    removeVehicle()

elif userSelection == 'C':

    def chooseCargoVehicle():
        print("We have Trucks and Lorries..\n")
        print("To select Truck , enter 1 ")
        print("To select Lorry , enter 2 \n")


        vehicleSelection = int(input("Enter : "))

        return vehicleSelection

    #vehicle selection
    def vehicleSelection(vehicleSelection):

        if vehicleSelection == 1:
            assignTruck()
        elif vehicleSelection == 2:
            assignLorry()

        else:
            print("incorrect value " + str(vehicleSelection))

    #assigning suitable vehicles
    def assignTruck():

        if len(notHiredTruckVehicles) != 0:

            reqInputSize = input("Enter Length size (7ft or 12ft) : ")

            reqList = []
            for truck in range(len(notHiredTruckVehicles)):

                if reqInputSize == notHiredTruckVehicles[truck].getLength():
                    if str(notHiredTruckVehicles[truck].getHiredStatus()) == 'False':
                        reqList.append(notHiredTruckVehicles[truck].getvNumber())

            if reqList == []:
                print("Sorry.. the vehicles which meets your requirements aren't available at the moment..")

            else:
                firstVehicle = reqList[0]


                for a in range(len(notHiredTruckVehicles)):

                    if notHiredTruckVehicles[a].getvNumber() == firstVehicle:
                        latestHired = notHiredTruckVehicles[a]
                        hiredTruckVehicles.append(latestHired)
                        notHiredTruckVehicles.pop(a)
                        hiredTruckVehicles[-1].setHiredStatus(True)
                        newHired = hiredTruckVehicles[-1].getvNumber()


                        for y in range(len(truckVehicles)):
                            if newHired not in truckVehicles[y].getvNumber():
                                continue
                            truckVehicles[y].setHiredStatus(True)
                        break


                print("you have hired " + latestHired.getModel() + ". The vehicle no is " + latestHired.getvNumber())
                print("Enjoy your ride !")

            print("\nDo you wanna choose a another ride ? ")
            userAnotherRide = input("Enter 'y' for y=Yes and 'n' for No : ").upper()

            while userAnotherRide == 'Y':
                vehicleSelection(chooseCargoVehicle())
                break

            if userAnotherRide == 'N':
                print("Thank you .. ")
                print("Do you want to release from an assigned job (hire) ? : ")
                userRelease = input("Enter 'y' for Yes and 'n' for No : ").upper()
                if userRelease == 'Y':
                    releaseHire()
                    print("Thank you")
                elif userRelease == 'N':
                    print("Thank you ")

                else:
                    print("invalid input given ")



        else:
            print("Sorry currently there aren't any available Trucks...\n")
            print("You can check for other Cargo vehicles if you wish\n")
            vehicleSelection(chooseCargoVehicle())

    def assignLorry():

        if len(notHiredLorryVehicles) != 0:

            reqInputWeight = int(input("Enter Load weight ( 2500 - 3500 ) kg : "))

            reqList = []
            for lorry in range(len(notHiredLorryVehicles)):

                if reqInputWeight >= 2500 and reqInputWeight <= 3500:

                    if reqInputWeight <= notHiredLorryVehicles[lorry].getLoad():
                        if str(notHiredLorryVehicles[lorry].getHiredStatus()) == 'False':
                            reqList.append(notHiredLorryVehicles[lorry].getvNumber())
                else:
                    print("Incorrect weight !")

            if reqList == []:
                print("Sorry.. the vehicles which meets your requirements aren't available at the moment..")

            else:
                firstVehicle = reqList[0]


                for a in range(len(notHiredLorryVehicles)):

                    if notHiredLorryVehicles[a].getvNumber() == firstVehicle:
                        latestHired = notHiredLorryVehicles[a]
                        hiredLorryVehicles.append(latestHired)
                        notHiredLorryVehicles.pop(a)
                        hiredLorryVehicles[-1].setHiredStatus(True)
                        newHired = hiredLorryVehicles[-1].getvNumber()


                        for y in range(len(lorryVehicles)):
                            if newHired not in lorryVehicles[y].getvNumber():
                                continue
                            truckVehicles[y].setHiredStatus(True)
                        break


                print("you have hired " + latestHired.getModel() + ". The vehicle no is " + latestHired.getvNumber())
                print("Enjoy your ride !")

            print("\nDo you wanna choose a another ride ? ")
            userAnotherRide = input("Enter 'y' for y=Yes and 'n' for No : ").upper()

            while userAnotherRide == 'Y':
                vehicleSelection(chooseCargoVehicle())
                break

            if userAnotherRide == 'N':
                print("Thank you .. ")
                print("Do you want to release from an assigned job (hire) ? : ")
                userRelease = input("Enter 'y' for Yes and 'n' for No : ").upper()
                if userRelease == 'Y':
                    releaseHire()
                    print("Thank you")
                elif userRelease == 'N':
                    print("Thank you ")

                else:
                    print("invalid input given ")



        else:
            print("Sorry currently there aren't any available Lorries...\n")
            print("You can check for other Cargo vehicles if you wish\n")
            vehicleSelection(chooseCargoVehicle())

    # input array name and vehicle number to release hired status
    def releaseHire():
        vehicle = input("\nEnter which vehicle type (truck or lorry): ").lower()
        vNumber = input("Input vNumber : ")

        if vehicle == 'truck':

            for d in range(len(hiredTruckVehicles)):
                if vNumber == hiredTruckVehicles[d].getvNumber():
                    hiredTruckVehicles.append(hiredTruckVehicles[d])
                    del hiredTruckVehicles[d]
                break

        if vehicle == 'lorry':

            for d in range(len(hiredLorryVehicles)):
                if vNumber == hiredLorryVehicles[d].getvNumber():
                    notHiredLorryVehicles.append(hiredLorryVehicles[d])
                    del hiredLorryVehicles[d]
                break

    # to find all the vehicles the cab service has
    def seeVehicles():

        print("\nYou can find vehicles we have ")
        vehicle = input("Enter which vehicle type (truck or lorry or all): ").lower()

        if vehicle == 'truck':
            for x in truckVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

        if vehicle == 'lorry':
            for x in lorryVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

        if vehicle == 'all':
            for x in cargoVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

    # see hired vehicles

    def seeHiredVehicles():

        print("\nYou can find the currently hired vehicles here")
        vehicle = input("Enter which vehicle type (truck or lorry): ").lower()

        if vehicle == 'truck':
            for x in hiredTruckVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

        if vehicle == 'lorry':
            for x in hiredLorryVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

    # to see unhired / available vehicles

    def seeAvailableVehicles():

        print("\nYou can find the currently Available (free) vehicles here")
        vehicle = input("Enter which vehicle type (truck or lorry): ").lower()

        if vehicle == 'truck':
            for x in notHiredTruckVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())

        if vehicle == 'lorry':
            for x in notHiredLorryVehicles:
                print("The Model is " + x.getModel() + " and the vehicle number is " + x.getvNumber())



    vehicleSelection(chooseCargoVehicle())
    createObject()
    seeHiredVehicles()
    seeAvailableVehicles()
    seeVehicles()
    removeVehicle()

else:
    print('Invalid Input !')
