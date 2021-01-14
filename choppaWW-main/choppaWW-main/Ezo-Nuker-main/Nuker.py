import discord
import os
import ctypes
import colorama
import requests
import time
from colorama import Fore



def Clear():
    os.system('cls')
Clear()


while True:
    password = input("[+] Enter Password: ")
    if password =="VloneX":
        print("Correct password")
        input("[+] enter to continue to Selfbot")
        break
    else:
        print("Wrong Password Jit")
Clear()

while True:
    Text = input("[+] Enter Text you want to send : ")
    if Text =="TEXT_HERE":
        print("you forgot to add text")
        input("Wyd you didnt add text")
        exit(0)
    else:
        print("[+] Enter to continue to nuker")
        break
Clear()


token = input("Enter token jit : ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('[+] Valid token')
    input("Press any key")
else:
    print(f'[{Fore.ORANGE}-{Fore.RESET}] Wrong token tuff')
    input("Press any key")
    exit(0)
Clear()


print(f'''{Fore.ORANGE}
                                   __      ___      ____  _   _ ________   __  _   _ _    _ _  ________ _____  
                                   \ \    / / |    / __ \| \ | |  ____\ \ / / | \ | | |  | | |/ /  ____|  __ \ 
                                    \ \  / /| |   | |  | |  \| | |__   \ V /  |  \| | |  | | ' /| |__  | |__) |
                                     \ \/ / | |   | |  | | . ` |  __|   > <   | . ` | |  | |  < |  __| |  _  / 
                                      \  /  | |____ |__| | |\  | |____ / . \  | |\  | |__| | . \| |____| | \ \ 
                                       \/   |______\____/|_| \_|______/_/ \_\ |_| \_|\____/|_|\_\______|_|  \_\
                                                                             

                                                                                                       ''')

client = discord.Client()


@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      vlonex = discord.Embed(color= discord.Color(0x4146d1))
      vlonex.set_author(name="Nuker by VloneX")
      vlonex.add_field(name="VloneX nuker",value=Text)
      vlonex.set_image(url="")
      await user.send(embed=vlonex)
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")
       print(f"Directed messaged all users friends")


client.run(token, bot=False)
