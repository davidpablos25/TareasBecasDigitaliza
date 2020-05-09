#!/usr/bin/env python3

import requests
import json
import urllib3
from pprint import pprint
from tabulate import *

requests.packages.urllib3.disable_warnings()
url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
headers = {
    'Content-Type': 'application/json'
}

body_json={
    
  "password": "Xj3BDqbU",
  "username": "devnetuser"
}

resp= requests.post(url,json.dumps(body_json), headers= headers, verify= False)

print("La petición tiene el estado:", resp.status_code)
ticket_json=resp.json()
print("El ticket de servicio asignado es: ", ticket_json['response']['serviceTicket'])



def menu():
    print("FUNCIONALIDADES")
    print()
    print("1. Ver los Hosts conexionados")
    print("2. Ver los tipos de dispositivo de red")
    print("3. Ver interfaces de los dispositivos de red (necesario saber la ID de los dispositivos del apartado 2)")
    print("4. Ver listas de localización")
    print("5. Obtención de tag")

    funcionalidad = input("Elige una funcionalidad: ")
    return funcionalidad
    

while True:
    try:
        
        funcionalidad= menu()
        
        requests.packages.urllib3.disable_warnings()

        if funcionalidad == "1":
            url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"

            headers={
    
            'Content-Type': 'application/json',
            'X-Auth-Token': ticket_json['response']['serviceTicket']
            }

            resp= requests.get(url, headers=headers, verify=False)

            hostList=[]

            print("La petición del estado:", resp.status_code)
            response_json = resp.json()
            #pprint(response_json)
            counter=0
            for el in response_json['response']:
                counter+=1
                host = [
                    counter,
                    el['hostType'],
                    el['hostIp'],
                    el['hostMac']
                ]
                hostList.append(host)
            tableHeader = ["Número", "Tipo", "IP", "MAC"]

            print(tabulate(hostList, tableHeader))

        
        elif funcionalidad=="2":
            
            url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"

            headers={
    
            'Content-Type': 'application/json',
            'X-Auth-Token': ticket_json['response']['serviceTicket']
            }

            resp= requests.get(url, headers=headers, verify=False)

            deviceList= []
        
            print("La petición del estado:", resp.status_code)
            response_json = resp.json()
            #pprint(response_json)

            counter=0
            for equipo in response_json['response']:
                counter+=1
                device =[
                    counter,
                    equipo['hostname'],
                    equipo['family'],
                    equipo['macAddress'],
                    equipo['id']
                
                ]
                deviceList.append(device)
            tableHeader = ["Número", "Nombre de host", "Familia", "MAC", "ID del dispositivo"]
            print(tabulate(deviceList, tableHeader))
             
        elif funcionalidad =="3":

            deviceId=input("Introduzca el ID del dispositivo que desee según el apartado 2: ")
    
            url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/interface/network-device/"+deviceId
            

            headers={
    
            'Content-Type': 'application/json',
            'X-Auth-Token': ticket_json['response']['serviceTicket']

            }

            resp= requests.get(url, headers=headers, verify=False)

            interfaceList= []
        
            print("La petición del estado:", resp.status_code)
            response_json = resp.json()
            #pprint(response_json)

            counter=0
            for equipo in response_json['response']:
                counter+=1
                interface =[
                    counter,
                    equipo['interfaceType'],
                    equipo['portName'],
                    equipo['portMode'],
                    equipo['portType'],
                    equipo['ipv4Address']
                
                ]
                interfaceList.append(interface)
            tableHeader=["Número", "Física/virtual", "Nombre interfaz", "Modo interfaz", "Tipo interfaz", "IP interfaz"]
            print(tabulate(interfaceList, tableHeader))
        
        elif funcionalidad =="4":
            
            url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location"

            headers={
    
            'Content-Type': 'application/json',
            'X-Auth-Token': ticket_json['response']['serviceTicket']
            }

            resp= requests.get(url, headers=headers, verify=False)

            locList= []
        
            print("La petición del estado:", resp.status_code)
            response_json = resp.json()
            #pprint(response_json)

            counter=0
            for loc in response_json['response']:
                counter+=1
                localización =[
                    counter,
                    loc['id'],
                   
                    loc['locationName'],
                    loc['geographicalAddress'],
                   
                ]
                locList.append(localización)
            tableHeader=["Número", "ID", "Nombre", "Dirección geográfica"]
            print(tabulate(locList, tableHeader))

        elif funcionalidad=="5":
            url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/tag"

            headers={
    
            'Content-Type': 'application/json',
            'X-Auth-Token': ticket_json['response']['serviceTicket']
            }

            resp= requests.get(url, headers=headers, verify=False)

            etiquetaList=[]

            print("La petición del estado:", resp.status_code)
            response_json = resp.json()
            #pprint(response_json)

            counter=0
            for tagg in response_json['response']:
                counter+=1
                etiqueta =[
                    counter,
                    tagg['id'],
                   
                    tagg['tag'],
                    
                   
                ]
                etiquetaList.append(etiqueta)
            tableHeader=["Número", "ID", "Etiquetado"]
            print(tabulate(etiquetaList, tableHeader))
        
        else:
            print("Opción incorrecta, reinicie el programa")
            break


        continuar = input("Introduzca (n) si no quiere continuar, y cualquier tecla para sí: ")
        

        if continuar == "n":
            print("Has parado el programa")
            break
        
        print()
         
        
        

    except KeyboardInterrupt:
        print("Has cerrado el programa")
        break