import os
from colorama import Fore, Back, Style
from anonfile import AnonFile
from pystyle import Colors, Colorate, Center
from pathlib import Path
anon = AnonFile()

banner = (f"""
| Anonfile-Uploader Very Fast | v.1
|══════════════════════════════════════════════
| By DEUS-WEB#9999
| Discord : .gg/696
|══════════════════════════════════════════════
| Welcome to Anonfile-Uploader.
""")

def menu():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(Colorate.Horizontal(Colors.yellow_to_red, banner, 1))
	print(Fore.RED + "\n \n[" + Fore.YELLOW + "!" + Fore.RED + "] " + Fore.YELLOW + "Welcome to Anonfile-Uploader")
	path = input(Fore.RED + "[" + Fore.YELLOW + "!" + Fore.RED + "] " + Fore.YELLOW + "Drag your file: " + Fore.RESET)
	upload = anon.upload(path, progressbar=False)
	print(Fore.RED + "[" + Fore.YELLOW + "!" + Fore.RED + "] " + Fore.YELLOW + "Succes ! -> " + upload.url.geturl())
menu()