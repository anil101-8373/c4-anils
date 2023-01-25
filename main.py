from keyauth import api
import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime
from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
from time import sleep
from datetime import datetime

# import json as jsond
# ^^ only for auto login/json writing/reading

# watch setup video if you need help https://www.youtube.com/watch?v=L2eAQOmuUiA

if sys.version_info.minor < 10:  # Python version check (Bypass Patch)
    print("[Security] - Python 3.10 or higher is recommended. The bypass will not work on 3.10+")
    print("You are using Python {}.{}".format(sys.version_info.major, sys.version_info.minor))

if platform.system() == 'Windows':
    os.system('cls & title Python Example')  # clear console, change title
elif platform.system() == 'Linux':
    os.system('clear')  # clear console
    sys.stdout.write("\x1b]0;Python Example\x07")  # change title
elif platform.system() == 'Darwin':
    os.system("clear && printf '\e[3J'")  # clear console
    os.system('''echo - n - e "\033]0;Python Example\007"''')  # change title

print("LEAREX DEV")


def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "devanil", #App name (Manage Applications --> Application name)
    ownerid = "S5mq4yf7Os", #Owner ID (Account-Settings --> OwnerID)
    secret = "fab5b174201cae9c7d80d753bb5a967bd397ad4c365f758f333aa14f807daaa8", #App secret(Manage Applications --> App credentials code)
    version = "1.0",
    hash_to_check = getchecksum()
)

def answer():
    try:
        print("""
1.Giriş
2.Kayıt
        """)
        ans = input("Seçim: ")
        if ans == "1":
            user = input('Kullanıcı: ')
            password = input('Şifre: ')
            keyauthapp.login(user, password)
        elif ans == "2":
            user = input('Kullanıcı: ')
            password = input('Şifre: ')
            license = input('Lisans: ')
            keyauthapp.register(user, password, license)
        elif ans == "3":
            user = input('Kullanıcı: ')
            license = input('Lisans: ')
            keyauthapp.upgrade(user, license)
        elif ans == "4":
            key = input('Senin Lisansın Enterla: ')
            keyauthapp.license(key)
        else:
            print("\nSeçim Bulunamadi")
            time.sleep(1)
            os.system('cls')
            answer()
    except KeyboardInterrupt:
        os._exit(1)


answer()

# region Extra Functions

# * Download Files form the server to your computer using the download function in the api class
# bytes = keyauthapp.file("FILEID")
# f = open("example.exe", "wb")
# f.write(bytes)
# f.close()


# * Set up user variable
# keyauthapp.setvar("varName", "varValue")

# * Get user variable and print it
# data = keyauthapp.getvar("varName")
# print(data)

# * Get normal variable and print it
# data = keyauthapp.var("varName")
# print(data)

# * Log message to the server and then to your webhook what is set on app settings
# keyauthapp.log("Message")

# * Get if the user pc have been blacklisted
# print(f"Blacklisted? : {keyauthapp.checkblacklist()}")

# * See if the current session is validated
# print(f"Session Validated?: {keyauthapp.check()}")


# * example to send normal request with no POST data
# data = keyauthapp.webhook("WebhookID", "?type=resetuser&user=username")

# * example to send form data
# data = keyauthapp.webhook("WebhookID", "", "type=init&name=test&ownerid=j9Gj0FTemM", "application/x-www-form-urlencoded")

# * example to send JSON
# data = keyauthapp.webhook("WebhookID", "", "{\"content\": \"webhook message here\",\"embeds\": null}", "application/json")

# * Get chat messages
# messages = keyauthapp.chatGet("CHANNEL")

# Messages = ""
# for i in range(len(messages)):
# Messages += datetime.utcfromtimestamp(int(messages[i]["timestamp"])).strftime('%Y-%m-%d %H:%M:%S') + " - " + messages[i]["author"] + ": " + messages[i]["message"] + "\n"

# print("\n\n" + Messages)

# * Send chat message
# keyauthapp.chatSend("MESSAGE", "CHANNEL")

# * Add Application Information to Title
# os.system(f"cls & title KeyAuth Python Example - Total Users: {keyauthapp.app_data.numUsers} - Online Users: {keyauthapp.app_data.onlineUsers} - Total Keys: {keyauthapp.app_data.numKeys}")

# * Auto-Login Example (THIS IS JUST AN EXAMPLE --> YOU WILL HAVE TO EDIT THE CODE PROBABLY)
# 1. Checking and Reading JSON

#### Note: Remove the ''' on line 151 and 226

'''try:
    if os.path.isfile('auth.json'): #Checking if the auth file exist
        if jsond.load(open("auth.json"))["authusername"] == "": #Checks if the authusername is empty or not
            print("""
1. Login
2. Register
            """)
            ans=input("Select Option: ")  #Skipping auto-login bc auth file is empty
            if ans=="1": 
                user = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(user,password)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            elif ans=="2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user,password,license) 
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            else:
                print("\nNot Valid Option") 
                os._exit(1) 
        else:
            try: #2. Auto login
                with open('auth.json', 'r') as f:
                    authfile = jsond.load(f)
                    authuser = authfile.get('authusername')
                    authpass = authfile.get('authpassword')
                    keyauthapp.login(authuser,authpass)
            except Exception as e: #Error stuff
                print(e)
    else: #Creating auth file bc its missing
        try:
            f = open("auth.json", "a") #Writing content
            f.write("""{
    "authusername": "",
    "authpassword": ""
}""")
            f.close()
            print ("""
1. Login
2. Register
            """)#Again skipping auto-login bc the file is empty/missing
            ans=input("Select Option: ") 
            if ans=="1": 
                user = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(user,password)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            elif ans=="2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user,password,license)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            else:
                print("\nNot Valid Option") 
                os._exit(1) 
        except Exception as e: #Error stuff
            print(e)
            os._exit(1) 
except Exception as e: #Error stuff
    print(e)
    os._exit(1)'''

# endregion


print("\nKullanıcı data: ")
print("Kullanıcı adı: " + keyauthapp.user_data.username)
print("IP address: " + keyauthapp.user_data.ip)
print("Hardware-Id: " + keyauthapp.user_data.hwid)
# print("Subcription: " + keyauthapp.user_data.subscription) ## Print Subscription "ONE" name

subs = keyauthapp.user_data.subscriptions  # Get all Subscription names, expiry, and timeleft
for i in range(len(subs)):
    sub = subs[i]["subscription"]  # Subscription from every Sub
    expiry = datetime.utcfromtimestamp(int(subs[i]["expiry"])).strftime(
        '%Y-%m-%d %H:%M:%S')  # Expiry date from every Sub
    timeleft = subs[i]["timeleft"]  # Timeleft from every Sub

    print(f"[{i + 1} / {len(subs)}] | Subscription: {sub} - Expiry: {expiry} - Timeleft: {timeleft}")

onlineUsers = keyauthapp.fetchOnline()
OU = ""  # KEEP THIS EMPTY FOR NOW, THIS WILL BE USED TO CREATE ONLINE USER STRING.
if onlineUsers is None:
    OU = "No online users"
else:
    for i in range(len(onlineUsers)):
        OU += onlineUsers[i]["credential"] + " "

print("\n" + OU + "\n")

print("Oluşturma Tarihi: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S'))
print("Önceki Giriş: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S'))
print("Kalan Zaman: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'))
print(f"Oturum Aktifligi Dogrulandı: {keyauthapp.check()}")
system("cls||clear")
r = get("https://raw.githubusercontent.com/anil101-8373/c4-anils/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms
r = get("https://raw.githubusercontent.com/anil101-8373/c4-anils/main/call.py").text
with open("call.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "Güncelleme yapılıyor...")
    with open("call.py", "w", encoding="utf-8") as f:
        f.write(r)
from call import SendCall

servisler_call = []
for attribute in dir(SendCall):
    attribute_value = getattr(SendCall, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_call.append(attribute)
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)    

while 1:
    system("cls||clear")
    print("""{}
    
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&##BGGP55555Y555PGGB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#BGGPPP5G5JG#J?Y5#JJGYYY55Y55PB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BGPPPP5?GYB:JG P@7^?.B.?@7~#@@GJ?J5YYPG&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BPYYG575Y&5^7@J:#~?GJ~?JB^PY~G@@@B:?B?JBJ5Y5G&@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@#PY5BG!7PB?^B@P7BB5GGGG#GGGGPGPGB&&&?7@Y!BJ:Y?Y5JYB@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@BYYP#@@@PY?Y#5G#BGBGP5GGG#BBBGGPPBGPGBBBBYBP57^Y&@&GJJG&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@BYJP&@@@@@@P#BBPGGPGB##&&&@@B?J#@@&&&##BBP5GBB#YG@@@@@&GJJG@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&5?5#@@@@@@&#BP5PGB#&&&&&&@&P!...:J#@@&&&&&&#BGPBB#&@@@@@@&P?J#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@BJJB@@@@@@&#GPGGB&@@@@@@@@&5~ :JBG! .?B@@@@@@@@@&BGP5B#@@@@@@#J7G@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@G?Y&@@@@@&#BP5GB5JYJJJJJJYJ^.^Y#@&&&G7.:?555555PPPP#BPGGB&@@@@@@5!5@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@G7Y&&YJB@&BPPGB&@! .!!~~!!~^.~??7!!!!7?!..^~^^^^^:..G@&B5YG#@@#BB@P!Y@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@B7Y&@&JJB#GPGP#&&&! ~&&&&BJ!~!?Y5PGGGGPYJ!^^?P#&&&5..G@&&BPPPB&5^Y@@5!5@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#?J&&??#@#GGPP#&&&&~ ~&&G!:!5B#&#######&&&&#P?:^5&@5..G&&&&#PJ5B&&BGB@J!G@@@@@@@@@@@@
@@@@@@@@@@@@@@@Y7G@&5Y#&G5YP#&&&&&~ ~#7.7G&&##B?J?!7J?775##&&#J.~B5..B&&&&&BPPPB@Y^5@#7?&@@@@@@@@@@@
@@@@@@@@@@@@@@#7J&G7Y&@GGPPG&&&@#5:.~~.5&#####BGBGGGGGGGB####&&G^:!..5&@&&&&GPPP&@BGB@5!G@@@@@@@@@@@
@@@@@@@@@@@@@@P7P@BJP&&PY5P&&&#Y^.~Y~.P&####BBBBBBBBBBBBB######&B^:?^.~5&@&&#P5PB@P~J&B7J@@@@@@@@@@@
@@@@@@@@@@@@@@Y7B&55B@BPPGP&BJ^.!P&G.7&####BBBBGGGGGGGBBBB######&5.J#Y^.~5&@&PP5P&&#B&&??&@@@@@@@@@@
@@@@@@@@@@@@@&?7#&J7G@BP5PGY:.^G&&&J.5&####BBBBGGGGPGGGBBB######&B:!&@&5^.^5&P55P&B!!B&J7#@@@@@@@@@@
@@@@@@@@@@@@@&J7B@#B#&BP5PP#Y~:!5#@Y.Y&####BBBBGGGGPGGBBBB######&G:7&&BJ::!P&PGPP&&#B&&?7#@@@@@@@@@@
@@@@@@@@@@@@&@Y!G&P^J&#PGBP&@#5~.~5G^!#####BBBBBBBBGBBBBBBB####&&J:PB?::?G&@#PY5P&Y!P@#??&@@@@@@@@@@
@@@@@@@@@@@@&@P!Y@&B##&PPPPB&&&#5~:~7:J&##BGB#BBBBBBBBB###BG#&&&P^~7:^JB&&&&GPYPB&BYB@G7Y@&@@@@@@@@@
@@@@@@@@@@@@&@#?7#&P~?&BP5PP&&&&@#^:J5^?B#GG###############GG#&Y^J7:~B@&&&&#PP5P#YJ#@&J!B@&&@@@@@@@@
@@@@@@@@@@&&@&@5!5@&G#&&G55BP&&&&#^:J@G7~JPG&&###########&&BPY!!P&?:!&&&&&#P5YP#&5J#@G!J&&&&@@@@@@@@
@@@@@@@@@@@BB@&&J7G@&Y!5&GGGGP#&&#^:Y@@&G?!75BYJJYJJJY5JYBP?7?P&@&?:!&&&&#PGP5BP5#&@#?7#@&GB@@@@@@@@
@@@@@@@@@@@&55&@B77B&JYB&&GPPGPB&B^^?GPGGG5J!!??JJYYYYJJ?!7JPBBBBB7:!&&&BPYYP##J!J&&Y7G@#YP&@@@@@@@@
@@@@@@@@@&&@&5JB&B?J#PYG7J#BP5YPGG!!!!!!!!!!~^?PGGPPPGG57^!!!!~~!!~~?&#GPG5GPYP#JG#Y?G&PJP@@#&@@@@@@
@@@@@@@@@@BG&@BY5#GJPBYJYB&&#GPY5PGB#&&&####BJ~~JB@@&G?^!YB########BGGGGPPB&G7JJ5B5?GBY5#@#G#@@@@@@@
@@@@@@@@@@&B5P##YY555PPP5G&&&BBBPPPPGB#&&&&&&&BJ~^J57^!5#&&&&&&&&#BGPPGGPG@&&G5PPP555Y5#BPP#@@@@@@@@
@@@@@@@@@@&##BPPPPP555PPPP5B#?~JBBGPPPPGGB##&&@@#Y!~?G&@@&&&##BGP5P5PGG?~?#B5PGGP555P5PPGB#&&@@@@@@@
@@@@@@@@@@@&#GPP55PPP55PPP555J~~JP&#BGPGPPGPPY?JYPPPGPY?J5PP55Y5PPG##5?~~J555P5PP5PPP55PPB&&@@@@@@@@
@@@@@@@@@@@&&@#5J5PGGGGGGP5GB5J?7!?G&@&#BBG5P5Y!^^JY!::?JY5PPGB#&&&G?!7?JPBG55PGGGGGPYJP#@&&@@@@@@@@
@@@@@@@@@@@@&&&&P55PPGGGGPPPBG5YJ7!!?J5B&&&&GJ##G!?5!?G#P?#&#&&B5J77!7JJYGGGPPGBGGGP55G&&&&@@@@@@@@@
@@@@@@@@@@@@&&&&@#5PGGPPGGBGP5PP5?7?7~~!7?777?5PY?5B?JYP57?777!!!!7?7JPPP5PBBGBGGPPPY#@&&&@@@@@@@@@@
@@@@@@@@@@@@@&&&&&B5PGGGGGGBBPPBP5JJ???77!!J7~JG5JGBB5PGJ~7J!~!7?JJJY5PBGPBGGPGGGGP5G&&&&&@@@@@@@@@@
@@@@@@@@@@@@@@&&&&&GPPGGGBGGGBBGPP55YJJY?JJ55J5YYYPG5JJ55JY5JJ?YJJJ55PGGBGPGGGGGGPPB&&&&&@@@@@@@@@@@
@@@@@@@@@@@@@@@&&&&@#GPPGPGGPPGGBGPPP55Y?JJJ5P&5!!J5?!!Y#P5YJJJY55PPPGBGPPPGGPPPPG#@&&&&@@@@@@@@@@@@
@@@@@@@@@@@@@@@@&&&&&&#BPGGGPPPPGBGGGGP5YY5P#&@#Y7!7!7YB@&&G5Y5PPGGGPGGPPPPGGGGB#&&&&&@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&&&&&&&#BPPPPP55GGGGGPGGBG#@#JGBP55GG?B@&BBGBPGGGGG55PPP5PG#&&&&&&&@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&&&&&&&&BPP55555PGGGGGGG&&J~B&&#&&#~?&&BGGGGGGP55555PPB&&&&&&&&@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&#BGGP5PP5PGPP#&#57GG&@&GG7J#&#GPPP5PPY5GGB#&&&&&&&&@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&@&&&##BGP5P##BJP5JPB@#GJ5PYB##P5GGB##&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&@#YPBGB@@@BPBGP&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&#BPY5#G5##&PG#PYPG#&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&#G5PYYPG#BG5PB#P5YY5PG#&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@&##BPPPGGGB5BGGGPPPG##&@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###GGGGGPGGGGG###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&###GB##&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

 
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), len(servisler_call), Style.RESET_ALL, Fore.LIGHTRED_EX))
    sleep(1)
    system("cls||clear")
    print(Fore.LIGHTRED_EX + "LEAREX DEV")
    system("cls||clear") 
    print(Fore.LIGHTRED_EX + "iade yasaktır.")
    print(Fore.LIGHTWHITE_EX + "key paylaşmak yasaktır.")
    sleep(1)
    system("cls||clear")
    try:
        menu = int(input(Fore.LIGHTWHITE_EX + "1- SMS Boomber\n2- Call Boomber(Kapalı)\n\n" + Fore.LIGHTGREEN_EX + ": "))
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı Giriş.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Lutfen +90 Olmadan Telefon Numarası Yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = int(input())
            if len(str(tel_no)) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Lutfen Kac Adet Gondermek Istedıgınızı Yazınız.: "+ Fore.LIGHTGREEN_EX, end="")
            kere = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        sms = SendSms(tel_no, mail)
        while sms.adet < kere:
            for attribute in dir(SendSms):
                attribute_value = getattr(SendSms, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if sms.adet == kere:
                            break
                        exec("sms."+attribute+"()")
                        sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
    elif menu == 2:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Lutfen +90 Olmadan Telefon Numarası Yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = int(input())
            if len(str(tel_no)) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç kere aransın (max: {len(servisler_call)}): "+ Fore.LIGHTGREEN_EX, end="")
            kere = int(input())
            if kere > len(servisler_call):
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız.") 
            sleep(3)
            continue
        system("cls||clear")
        call = SendCall(tel_no, mail)
        while call.adet < kere:
            for attribute in dir(SendCall):
                attribute_value = getattr(SendCall, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if call.adet == kere:
                            break
                        exec("call."+attribute+"()")
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
