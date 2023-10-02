from tkinter import *
global SmartHome
from backend import *
global mainwin
global InitalLoad
InitalLoad = False
global OnLabel
mainwin=Tk()
Plug=SmartPlug()
Tv=SmartTv()



Home=SmartHome()
def SetupHome():
  ''' Allows us to set up our SmartHome GUI by using it a list it compiles the code and allows more devices
   to be added more fluently'''
  Devices = [SmartPlug(), SmartTv(),SmartPlug(),SmartTv(),SmartTv()]
  for i in range(len(Devices)):
      Home.addDevice(Devices[i])


def SetUpmainwin():
    '''Setting up the main GUI using tkinter as well as the set ups for the turn all OFF/ON Button
    which uses the Function set in the backend and creation of the buttons'''
    mainwin.title("SmartHome")
    mainwin.geometry("250x100")
    mainwin.resizable(True,True)
    listDevices()



    mainwin.columnconfigure(index=0,weight=4)
    def TurnallOn():
        Home.turnAllon()
        listDevices()

    def TurnallOff():
        Home.turnAlloff()
        listDevices()







    onBtn= Button(mainwin,text="Turn All On",command = TurnallOn)
    onBtn.grid(row=0,column=0, padx=15,pady=15, sticky="w")

    OffBtn = Button(mainwin, text= "Turn All Off", command =TurnallOff)
    OffBtn.grid(row=1,column=0, padx=15,pady=15, sticky="w")



    quitBtn= Button(mainwin,text="Quit", command=mainwin.destroy)
    quitBtn.grid(row=1,column=2, padx=15, pady=10, sticky="e")

    mainwin.mainloop()

def listDevices():
    '''Listing of the devices and pasting them into the GUI by use of the Device Index and setting how
    much space we'd want to give them.'''
    numberofDevices = Home.getDeviceLength()
    height = 60 * (numberofDevices + 1)
    mainwin.geometry("550x{}".format(height))

    for DeviceIndex in range(numberofDevices):
        device = Home.getDevicesAt(DeviceIndex)

        deviceTxt = Text(mainwin, height=2,width=50)
        deviceTxt.insert("1.0",str(device))
        deviceTxt.grid(row=DeviceIndex + 2 , column=0, padx=1)

        def ToggleWindow(i=DeviceIndex):
            ''' Allows us to individualy switch each device via the Toggle Button '''
            Home.toggleSwitch(i)
            listDevices()

        Addbtn=Button(mainwin,text="Add",command= addDeviceMenu)
        Addbtn.grid(row = DeviceIndex + 3 , column=1, padx=10)

        toggleBtn=Button(mainwin, text="Toggle",command=ToggleWindow)
        toggleBtn.grid(row=DeviceIndex + 2 ,column=1 , padx=10)

    

    
    


def addDeviceMenu():
    Possiblelist=["SmartPlug", "SmartTv"]
    DeviceMenu=Tk()
    DeviceMenu.geometry("400x100")
    DeviceMenu.title("add a device")
    dropdownmenu(DeviceMenu)


def dropdownmenu(DeviceMenu,):
    click = StringVar(DeviceMenu)
    click.set("Add Device...")
    dropdownmenu = OptionMenu(DeviceMenu,click, "SmartPlug","SmartTv")
    dropdownmenu.grid(row=2,column=1, padx=100,)

    def submitcmd():
    
        if click.get() == "SmartPlug":
            Home.addDevice(SmartPlug())
            listDevices()
            DeviceMenu.destroy()
        elif click.get() == "SmartTv":
            Home.addDevice(SmartTv())
            listDevices()
            DeviceMenu.destroy()
        else:
            pass
    submitButton=Button(DeviceMenu,text="Submit", command=submitcmd)
    submitButton.grid(row=4,column=3)
    




def main():
    SetupHome()
    print(Home)
    SetUpmainwin()
main()


