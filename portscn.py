#!/bin/python3
import nmap
from pyfiglet import Figlet
from termcolor import colored
print("                                                                ")
custom_fig = Figlet(font='smslant')
print(colored(custom_fig.renderText('         Port' '   SCANNER'), 'magenta'))
print(colored(custom_fig.renderText('         CyBeR  BuLL'), "red"))
print(colored("----------------------------- By :- Aadi OP---------------------", 'green'))

# take the range of ports to 
# be scanned
begin = 1
end = 80
  
# assign the target ip to be scanned to
# a variable
target = input(colored("Enter IP address :- ", 'yellow'))
port = input(colored("Enter Port number:- ", 'cyan'))
   
# instantiate a PortScanner object
scanner = nmap.PortScanner()
   
for i in range(begin,end+1):
   
    # scan the target port
    res = scanner.scan(target,str(i))
   
    # the result is a dictionary containing 
    # several information we only need to
    # check if the port is opened or closed
    # so we will access only that information 
    # in the dictionary
    res = res['scan'][target]['tcp'][i]['state']
   
    print(colored(f'This port {i} is {res}.', 'green'))
