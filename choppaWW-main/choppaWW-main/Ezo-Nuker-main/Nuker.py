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
    if password =="EzoW":
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


token = input("Enter token noob : ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('[+] Valid token')
    input("Press any key")
else:
    print(f'[{Fore.RED}-{Fore.RESET}] Wrong token tuff')
    input("Press any key")
    exit(0)
Clear()


print(f'''{Fore.RED}
                                     ______ __________   __          __
                                     |  ____|___  / __ \  \ \        / /
                                     | |__     / / |  | |  \ \  /\  / / 
                                     |  __|   / /| |  | |   \ \/  \/ /  
                                     | |____ / /__ |__| |    \  /\  /   
                                     |______/_____\____/      \/  \/    
                                    

                                                                                                       ''')

client = discord.Client()


@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      Ezo = discord.Embed(color= discord.Color(0xDBC415))
      Ezo.set_author(name="Nuker by Ezo")
      Ezo.add_field(name="Ezo nuker",value=Text)
      Ezo.set_image(url="https://media.discordapp.net/attachments/676163687869841418/799136057757138975/image0.gif?width=422&height=422")
      await user.send(embed=Ezo)
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")
       print(f"Directed messaged all users friends")


client.run(token, bot=False)
