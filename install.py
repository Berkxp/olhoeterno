import os
import platform

def instalar_pacotes():
    sis = platform.system()

    if sis == "Windows":
        # Comandos para Windows usando winget
        os.system("winget install Python.Python")
        os.system("winget install git")
    elif sis == "Linux":
        # Verifica a distribuição do Linux
        try:
            with open('/etc/os-release') as f:
                for line in f:
                    if line.startswith('ID='):
                        distro = line.split('=')[1].strip().replace('"', '')
                        break

            # Comandos para diferentes distribuições Linux
            if distro in ["ubuntu", "debian", "linuxmint"]:
                os.system("sudo apt update")
                os.system("sudo apt install python3 python3-pip git -y")
            elif distro in ["fedora"]:
                os.system("sudo dnf install python3 python3-pip git -y")
            elif distro in ["arch"]:
                os.system("sudo pacman -Syu python python-pip git --noconfirm")
            else:
                print(f"Distribuição Linux não reconhecida: {distro}")
                return  # Retorna se a distribuição não for reconhecida

        except Exception as e:
            print(f"Ocorreu um erro ao verificar a distribuição: {e}")
            return  # Retorna se houver um erro ao ler o arquivo

    else:
        print(f"Sistema operacional não suportado: {sis}")
        return  # Retorna se o sistema não for suportado

    # Instala pacotes Python
    os.system("pip install sockets")
    os.system("pip install faker")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install whois")
    
    print("Instalação completa!")
    os.system("python olhoeterno.py")

# Chama a função

instalar_pacotes()
