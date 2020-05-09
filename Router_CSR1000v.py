#!/usr/bin/env python3

import json, requests, urllib3
from pprint import pprint
from netmiko import ConnectHandler
from ncclient import manager
import xml.dom.minidom
from tabulate import *


def menu():
    print("ROUTER CSR1000v")
    print()
    print("1. Listado de las interfaces en el router")
    print("2. Creación de dos interfaces Loopback")
    print("3. Borrado de las dos interfaces Loopback")
    print("4. Tabla de enrutamiento")
    print("5. Petición a módulos yang.")

    opcion = input("Elige una opción: ")
    return opcion
    


while True:
    try:
        
        funcion= menu()
        

        if funcion == "1":
            sshovercli = ConnectHandler(device_type='cisco_ios', host='192.168.56.101', port=22,
            username='cisco', password='cisco123!')

            

            output= sshovercli.send_command("show ip interface brief")
            print("show ip interface brief:\n{}".format(output))

        elif funcion=="2":
            
            sshovercli = ConnectHandler(device_type='cisco_ios', host='192.168.56.101', port=22,
            username='cisco', password='cisco123!')



            interfaz1= ['interface loopback1','ip address 192.168.1.67 255.255.255.0','description loopback over ssh']
            outputInterfaz1= sshovercli.send_config_set(interfaz1)
            interfaz2= ['interface loopback2','ip address 10.10.10.10 255.255.255.0','description loopback over ssh']
            outputInterfaz2= sshovercli.send_config_set(interfaz2)

            output= sshovercli.send_command("show ip interface brief")
            print("show ip interface brief:\n{}".format(output))
            print()
            
        elif funcion =="3":

            sshovercli = ConnectHandler(device_type='cisco_ios', host='192.168.56.101', port=22,
            username='cisco', password='cisco123!')

            interfaz1= ['no int loopback1']
            outputInterfaz= sshovercli.send_config_set(interfaz1)
            interfaz2=['no int loopback2']
            outputInterfaz2= sshovercli.send_config_set(interfaz2)

            output= sshovercli.send_command("show ip interface brief")
            print("show ip interface brief:\n{}".format(output))
            print()

        elif funcion == "4":

            requests.packages.urllib3.disable_warnings()

            api_url = "https://192.168.56.101/restconf/data/ief-interfaces:interfaces"

            headers= {"Accept": "application/yang-data+json",
            "Content-Type": "application/yang-data+json"
            }

            basic_auth=("cisco", "cisco123!")

            response = requests.get(api_url, auth=basic_auth, headers=headers, verify=False)

            response_json = response.json()

            routeList=[]
            counter=0
            for el in response_json['response']:
                counter+=1
                route = [
                    counter,
                    el['name'],
                    el['enabled'],
                    el['ip'],
                    el['netmask']
                ]
                routeList.append(route)
            tableHeader = ["Número", "Nombre Interfaz", "Encendido", "IP", "Máscara"]

            print(tabulate(routeList, tableHeader))


            #A través del comando show ip route, también sacaríamos la tabla de enrutamiento.
            """sshovercli = ConnectHandler(device_type='cisco_ios', host='192.168.56.101', port=22,
            username='cisco', password='cisco123!')

            

            output= sshovercli.send_command("show ip interface brief")
            print("show ip interface brief:\n{}".format(output))"""

        elif funcion == "5":

            conexión= manager.connect(host="192.168.56.101",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

            netconf_filter="""
            <filter>
                <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces" />
            </filter>
            """
            netconf_reply= conexión.get(filter=netconf_filter)
            
            print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


        
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