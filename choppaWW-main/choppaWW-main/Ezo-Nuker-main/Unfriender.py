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
        print("Wrong passoword jit")
Clear()


token = input("Put The Token Jit : ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('[+] Valid token')
    input("Press any key")
else:
    print(f'[{Fore.RED}-{Fore.RESET}] Wrong token jit')
    input("Press any key")
    exit(0)
Clear()


print(f''' 
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
    print('Unfriending friends')
    for user in client.user.friends:
	        try:
	            await user.remove_friend()
	            print(f'unfriended {user}')
	        except:
	            print(f"can't unfriend {user}")


client.run(token, bot=False)
