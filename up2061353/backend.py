
class SmartPlug():
    def __init__(self):
        '''The initialisation of the class that has two variables which will be used throughout'''
        self.switchedOn = False
        self.consumptionRate=0


    def toggleSwitch(self):
        ''' Allows the Switch to be Toggled'''
        self.switchedOn = not self.switchedOn


    def showswitchState(self):
        '''  returns the switch state allowing it to be showed '''

        if self.switchedOn == True:
            return "On"
        else:
            return "Off"

    def showConsumprionRate(self):
        ''' Shows the Consumption Rate'''
        return self.consumptionRate

    def changeConsumption(self,newRate):
        ''' ALlows us to change the consumption Rate using NewRate as a required variable'''
        self.consumptionRate = newRate

    def __str__(self):
        output=(" Your Smart Plug is = {}, ConsumptionRate is {}").format(self.showswitchState(),self.consumptionRate)
        return output



def TestSmartPlug():
    plug=SmartPlug()
    plug.toggleSwitch()
    print(plug.showswitchState())
    print(plug.showConsumprionRate())
    plug.changeConsumption(100)
    print(plug.showConsumprionRate())
    print(plug)


#Task2

class  SmartTv():
    def __init__(self):
        self.switchedOn=False
        self.channel=1
        self.Name= SmartTv

    def toggleSwitch(self):
        '''Allows Switch to be Toggled'''
        self.switchedOn = not self.switchedOn

    def showswitchState(self):
        '''Shows the Switch State'''
        if self.switchedOn == True:
            return "On"
        else:
            return "Off"


    def ShowChannel(self):
        '''Shows Current Channel'''
        return self.channel

    def NewChannel(self,newChannel):
        '''Allows the new channel  to be made up to the number 734'''
        if newChannel < 0 or newChannel > 734:
            print("Invalid Channel")

        else:
            self.channel = newChannel


    def __str__(self):
        output="Your Smart TV is {}, and you are on channel {}".format(self.showswitchState(),self.channel)
        return output

def TestTV():
    TV=SmartTv()
    TV.toggleSwitch()
    print(TV.showswitchState())
    print(TV.ShowChannel())
    TV.NewChannel(int(input("What channel number?")))
    print(TV.ShowChannel())
    print(TV)
TestTV()


class SmartHome:
    def __init__(self):
        self.devices = []


    def getDevices(self):
        '''Allows us to get Devices from the list'''
        for device in self.devices:
           return device


    def getDevicesAt(self,index):
        '''Gives us an index allowing us to use the devices in the list and where we got them'''
        return (self.devices[index])

    def getDeviceLength(self):
        '''How many Devices are in the list '''
        return len(self.devices)

    def addDevice(self,newDevice):
        '''Adding a new device'''
        self.devices.append(newDevice)


    def toggleSwitch(self,index):
        'Toggling Switches'
        DevicesChange = self.devices[index]
        DevicesChange.toggleSwitch()

    def turnAllon(self):
        '''Allows us to turn all the devices on'''
        for device in self.devices:
            if device.showswitchState() == "Off":
                device.toggleSwitch()

    def turnAlloff(self):
        '''Allows us to turn all devices off'''
        for device in self.devices:
            if device.showswitchState() == "On":
                device.toggleSwitch()


    def __str__(self):
        output = " Devices in list:\n"
        for device in self.devices:
            string= str(device)
            output=output + "   " +  string
        return output



def TestSmartHome():
    Home=SmartHome()
    plug1=SmartPlug()
    plug2=SmartPlug()
    TV=SmartTv()
    plug2.toggleSwitch()
    plug2.changeConsumption(45)
    TV.NewChannel(75)
    Home.addDevice(plug1)
    Home.addDevice(plug2)
    Home.addDevice(TV)
    print(Home)
    Home.turnAllon()
    print(Home)
TestSmartHome()









