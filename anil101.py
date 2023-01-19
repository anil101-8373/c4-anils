from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
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
r = get("https://raw.githubusercontent.com/anil101-8373/c4-anils/main/anil101.py").text
with open("anil101.py", "r", encoding="utf-8") as f:
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
    
PPPPPPPPPPPPPPPPPPPPPPG?!!~^^^^^^^^^^^^^^^^^^^^^^^~~7JPB&@@#PPP5!~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
PPPPPPPPPPPPPPPPPPPPPPP7!~^^^^^^^^^^^^^^^^^^^^^^^^^^::^^~7JGPPP##GY?!^::::^^^^^^^^^^^^^^^^^^^^^^^^^^
PPPPPPPPPPPGGPPPPPPPPPP!!^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:JGPP55B#&&#G5?!^^:::^^^^^^^^^^^^^^^^^^^^^
PPPPPPPPPPPGPPPPPPPPPPY!~^^^^^^^^^^^^^^^^^^^^^^^^^^~~~!!!!!YGPG?~~!7?YPB&&#B5J7~^::::^^^^^^^^^^^^^^^
PPPPPPPPPPBGPPPPPPPPPGJ!^::^::::::::^^^^^~~~^^^^^^:::::^^^~?GPP?!!!!!~~~!7?YGB##BG5?!~^::::::^^^!^^^
PPPPPPPPPG#GPPPPPPPPPP?!7JJYP5JJY55PPPGGPPPPGB#BBGGP5Y?7!^:!GPP!!777!!!!!!~~^^~!?YPB##BGPYJ?7~~!~^^^
PPPPPPPPG##PPPPPPPPPPG&&#&&BGP5YJJ??777!!?5GB#####&&#&&&##G5PPP^:^~!77!!!!!!!!~~^::^~!7J5PGJ~~!^^^^^
PPPPPPPG###PPPPPPPPPPB&Y?7!!!~~~~~~~^^^7G##BGGGPPG@@#PPGB#&#GPG5?~::^~!!!!!!!!!!!~~^^:::::::^^^^^^^^
PPPPPPP###BPPPPPPPPPP##!~!!!~^^:..... ?##BPPPPP555GBG5PPPPG#BPPJ5GP?^:^~!!!!!!!!!!!!~^^^^^^^^^^^^^^^
PPPPPPB###BPPPPPPPPPP5&?!!^......... ?&PYJPPP555PPP5555PGP5GBPP^:~?PBY~^:~!!!!!!!!!!!!~^^^^^^^^^^^^^
PPPPPB####BPPPPPPPPPG?YG!: .........:B#Y7?PP55PB#&&#G5555PP5BGP^ ..:!YPJ~^^~!!!!!!!!!!!!~^^^^^^^^^^^
PPPPG#####BPPPPPPPPPG?^5Y.......... ^##PPPP555G&@@@@#P555GP5BGP^ .....~YY!~^^~!!!!!!!!!!77^^^^^^^^^^
PPPPB#####BPPPPPPPPPP7^^P~ ..........G#G5G##P5PG###BP55PGG55B#G~ ......:!J!^^^^!!!!!!!!!!!7~^^^^^^^^
PPPG######BPPPPPPPPPP7^:^P~ ........ ~##P##BPP55555555P#@&GG&BG7 ........^7!^^^^!!!!!!!!!!!7!^^^^^^^
PPP#######BPPPPPPPPPP7^^:~P7 ........ ~G#G55PPPPPPPPGPPPPG#&5:YY..........^!!^^^~!!!!!!!!!!!7!^^^^^^
PPG########PPPPPPPPPP7^^^:^YJ: ....... .?G#BGPPP5P5PPPPGB#P!  ~P:........ :!?~^^!!!!!!!!!!!!7!^^^^^^
PPB########PPPPPPPPPP!^^^^^:7J!:.        .~JPBBBBBBBBBG5?^     Y~ ......:~!7!^^!!!!!!!!!!!!77~^^^^^^
PG#########GPPPPPPPPP!^^^^^^^?BBG5?7!~~^^^:::^!7?JJ?7~^:::^^^~^7Y~!!777!!!~^:^~!!!!!!!!!!!77~^^^^^^^
PB#########GPPPPPPPPP!^^^^^7J?~!!~~~~~~!!!!!!!!!~~~~~~~!!!!~!~~^J7^^~^^^^^^^^~!!!!!!!!!!!7!^^^^^^^^^
P##########GPPPPPPPPP!^^^^^^::^^:^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^?^^^^^^^^^^~!!!!!!!!!!77!^^^^^^^^^^
G##########GPPPPPPPPP!^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!^^^^^^^^!!!!!!!!!!!7!~^^^^^^^^^^^
B##########BPPPPPPPPP!^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~^^^^^^!!!!!!!!!!77~^^^^^^^^^^^^^
B##########BPPPPPPPPP!^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!!!!!!!!!77!^^^^^^^^^^^^^^^
###########BPPPPPPPPP!^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!!!!!!!77!^^^^^^^^^^^^^^^^^

 
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), len(servisler_call), Style.RESET_ALL, Fore.LIGHTRED_EX))
    sleep(1)
    system("cls||clear")
    print(Fore.LIGHTRED_EX + "baba#8373")
    print(Fore.LIGHTWHITE_EX + "anil101#8373")
    print(Fore.LIGHTBLUE_EX + "anil101#8373")
    print(Fore.LIGHTYELLOW_EX + "anil101#8373")
    sleep(1)
    sleep(1)
    system("cls||clear")
    print(Fore.LIGHTRED_EX + "Dosyalar Kontrol Ediliyor")
    print(Fore.LIGHTWHITE_EX + "Dosyalar Kontrol Ediliyor")
    print(Fore.LIGHTBLUE_EX + "Dosyalar Kontrol Ediliyor")
    print(Fore.LIGHTYELLOW_EX + "Dosyalar Kontrol Ediliyor")
    sleep(1)
    system("cls||clear")
    print(Fore.LIGHTRED_EX + "Dogrulandı")
    print(Fore.LIGHTWHITE_EX + "Dogrulandı")
    print(Fore.LIGHTBLUE_EX + "Dogrulandı")
    print(Fore.LIGHTGREEN_EX + "Dogrulandı")
    sleep(1)
    system("cls||clear") 
    print(Fore.LIGHTRED_EX + "developer 'anil101#8373'")
    print(Fore.LIGHTWHITE_EX + "developer 'anil101#8373'")
    print(Fore.LIGHTBLUE_EX + "developer 'anil101#8373'")
    print(Fore.LIGHTYELLOW_EX + "developer 'anil101#8373'")
    sleep(1)
    system("cls||clear")
    print(Fore.LIGHTRED_EX + "by anil101#8373 https://discord.gg/BM7vjzURDc")
    print(Fore.LIGHTWHITE_EX + "by anil101#8373 https://discord.gg/BM7vjzURDc")
    print(Fore.LIGHTBLUE_EX + "by anil101#8373 https://discord.gg/BM7vjzURDc")
    print(Fore.LIGHTYELLOW_EX + "by anil101#8373 https://discord.gg/BM7vjzURDc")
    sleep(1)
    system("cls||clear")
    try:
        menu = int(input(Fore.LIGHTWHITE_EX + "1- SMS Boomber\n2- Call Boomber\n\n" + Fore.LIGHTGREEN_EX + ": "))
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
