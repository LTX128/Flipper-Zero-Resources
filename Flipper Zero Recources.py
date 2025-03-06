import os
import time
import webbrowser
import sys

BY_LTX74 = """\033[38;5;141m
 ██████   ██████   █████████   ██████████   ██████████      
░░██████ ██████   ███░░░░░███ ░░███░░░░███ ░░███░░░░░█      
 ░███░█████░███  ░███    ░███  ░███   ░░███ ░███  █ ░       
 ░███░░███ ░███  ░███████████  ░███    ░███ ░██████         
 ░███ ░░░  ░███  ░███░░░░░███  ░███    ░███ ░███░░█         
 ░███      ░███  ░███    ░███  ░███    ███  ░███ ░   █      
 █████     █████ █████   █████ ██████████   ██████████      
░░░░░     ░░░░░ ░░░░░   ░░░░░ ░░░░░░░░░░   ░░░░░░░░░░       
                                                            
                                                            
                                                            
 ███████████  █████ █████                                   
░░███░░░░░███░░███ ░░███                                    
 ░███    ░███ ░░███ ███                                     
 ░██████████   ░░█████                                      
 ░███░░░░░███   ░░███                                       
 ░███    ░███    ░███                                       
 ███████████     █████                                      
░░░░░░░░░░░     ░░░░░                                       
                                                            
                                                            
                                                            
 █████       ███████████ █████ █████ ██████████ █████ █████ 
░░███       ░█░░░███░░░█░░███ ░░███ ░███░░░░███░░███ ░░███  
 ░███       ░   ░███  ░  ░░███ ███  ░░░    ███  ░███  ░███ █
 ░███           ░███      ░░█████         ███   ░███████████
 ░███           ░███       ███░███       ███    ░░░░░░░███░█
 ░███      █    ░███      ███ ░░███     ███           ░███░ 
 ███████████    █████    █████ █████   ███            █████ 
░░░░░░░░░░░    ░░░░░    ░░░░░ ░░░░░   ░░░            ░░░░░
"""

clear_console = "cls" if os.name == "nt" else "clear"

logo_first = """\033[34m
    dMMMMMP dMP     dMP dMMMMb  dMMMMb  dMMMMMP dMMMMb         dMMMMMP dMMMMMP dMMMMb  .aMMMb 
   dMP     dMP     amr dMP.dMP dMP.dMP dMP     dMP.dMP          .dMP" dMP     dMP.dMP dMP"dMP 
  dMMMP   dMP     dMP dMMMMP" dMMMMP" dMMMP   dMMMMK"         .dMP"  dMMMP   dMMMMK" dMP dMP  
 dMP     dMP     dMP dMP     dMP     dMP     dMP"AMF        .dMP"   dMP     dMP"AMF dMP.aMP   
dMP     dMMMMMP dMP dMP     dMP     dMMMMMP dMP dMP        dMMMMMP dMMMMMP dMP dMP  VMMMP" 

"""   
                                                                                              
                                                                                              
                                                                                              
logo_midlle ="""                           \033[38;5;141mFlipper Zero Resources | By: LTX74

                    For any questions or tool problems, contact me on

                                  \033[38;5;141mDiscord: ltx___7401
                                    \033[38;5;141mGitHub: LTX128

                    https://github.com/LTX128/Flipper-Zero-Resources\033[34m
"""                                                                     
                                                                                              
                                                                                              
logo_second = """                                                                                              
    dMMMMb  dMMMMMP .dMMMb  .aMMMb  dMP dMP dMMMMb  .aMMMb  dMMMMMP .dMMMb                    
   dMP.dMP dMP     dMP" VP dMP"dMP dMP dMP dMP.dMP dMP"VMP dMP     dMP" VP                    
  dMMMMK" dMMMP    VMMMb  dMP dMP dMP dMP dMMMMK" dMP     dMMMP    VMMMb                      
 dMP"AMF dMP     dP .dMP dMP.aMP dMP.aMP dMP"AMF dMP.aMP dMP     dP .dMP                      
dMP dMP dMMMMMP  VMMMP"  VMMMP"  VMMMP" dMP dMP  VMMMP" dMMMMMP  VMMMP"              
"""

def afficher_texte_anime(texte, vitesse=0.02):
    for lettre in texte:
        sys.stdout.write(lettre)
        sys.stdout.flush()
        time.sleep(vitesse)
    print()

while True:
    os.system(clear_console)
    print(logo_first)
    afficher_texte_anime(logo_midlle)
    print(logo_second)
    print()
    afficher_texte_anime("\033[38;5;141mFlipper Zero Resources: \033[34m")
    print()
    afficher_texte_anime("-----------------------------------------")
    afficher_texte_anime("")
    afficher_texte_anime("\033[38;5;141m[1]\033[34m - Install Flipper Zero Firmware")
    afficher_texte_anime("\033[38;5;141m[2]\033[34m - Install Flipper Zero Tools")
    afficher_texte_anime("\033[38;5;141m[3]\033[34m - Install QFlipper")
    afficher_texte_anime("\033[38;5;141m[4]\033[34m - Discord Server about Flipper Zero and more")
    afficher_texte_anime("\033[38;5;141m[5]\033[34m - Modules (GPIO)")
    afficher_texte_anime("\033[38;5;141m[6]\033[34m - Aesthetic Products")
    afficher_texte_anime("\033[38;5;141m[7]\033[34m - Wifi Devboard Flasher by \033[38;5;141mUberGuidoZ\033[34m")
    afficher_texte_anime("\033[38;5;141m[8]\033[34m - Useful .fap applications")
    afficher_texte_anime("\033[38;5;141m[9]\033[34m - Diagrams for module connections")
    afficher_texte_anime("\033[38;5;141m[10]\033[34m - Buy a Flipper Zero")
    afficher_texte_anime("\033[38;5;196m[11] - Exit\033[34m")
    afficher_texte_anime("")
    afficher_texte_anime("-----------------------------")
    
    x = input("Select an option: ")

    if x == "1":
        os.system(clear_console)
        afficher_texte_anime("Flipper Zero Firmware Options")
        afficher_texte_anime("-------------------------------")
        afficher_texte_anime("")
        afficher_texte_anime("[A] - Momentum Firmware (Recommended)")
        afficher_texte_anime("[B] - Xtreme Firmware")
        afficher_texte_anime("[C] - Unleashed Firmware")
        afficher_texte_anime("[D] - Default Firmware")
        afficher_texte_anime("[E] - Rogumaster Firmware")
        afficher_texte_anime("\033[38;5;196m[F] - Return to Main Menu\033[34m")
        afficher_texte_anime("")
        afficher_texte_anime("----------------------------")

        y = input("Select a firmware: ")

        if y == "A":
            os.system(clear_console)
            afficher_texte_anime("MOMUNTUM FIRMWARE")
            time.sleep(1)
            webbrowser.open("https://momentum-fw.dev/")
            continue
        elif y == "B":
            os.system(clear_console)
            afficher_texte_anime("XTREME FIRMWARE")
            time.sleep(1)
            webbrowser.open("https://flipper-xtre.me/")
            continue
        elif y == "C":
            os.system(clear_console)
            afficher_texte_anime("UNLEASHED FIRMWARE")
            time.sleep(1)
            webbrowser.open("https://flipperunleashed.com/")
            continue
        elif y == "D":
            os.system(clear_console)
            afficher_texte_anime("DEFAULT FIRMWARE")
            time.sleep(1)
            webbrowser.open("https://flipperzero.one/")
            continue
        elif y == "E":
            os.system(clear_console)
            afficher_texte_anime("ROGUMASTER FIRMWARE")
            time.sleep(1)
            webbrowser.open("https://rogue-master.net/")
            continue
        elif y == "F":
            os.system(clear_console)
            continue
        else:
            os.system(clear_console)
            afficher_texte_anime("\033[38;5;196mInvalid option\033[34m")
            time.sleep(1)
            continue

    elif x == "2":
        os.system(clear_console)
        afficher_texte_anime("Flipper Zero Tools Options")
        afficher_texte_anime("----------------------------")
        afficher_texte_anime("")
        afficher_texte_anime("[A] - Sub-GHz Collection")
        afficher_texte_anime("[B] - NFC Collection")
        afficher_texte_anime("[C] - Infrared Collection")
        afficher_texte_anime("[D] - USB - BLE script Collection")
        afficher_texte_anime("[E] - RFID Collection")
        afficher_texte_anime("[F] - All in one + other (Recommended)")
        afficher_texte_anime("\033[38;5;196m[G] - Return to Main Menu\033[34m")
        afficher_texte_anime("")
        afficher_texte_anime("----------------------------")

        z = input("Select a collection: ")

        if z == "A":
            os.system(clear_console)
            afficher_texte_anime("Sub-GHz Collection")
            time.sleep(1)
            webbrowser.open("https://www.mediafire.com/file/l7cs01x5gho6nti/Sub-GHz_Collection.zip/file")
            continue
        elif z == "B":
            os.system(clear_console)
            afficher_texte_anime("NFC Collection")
            time.sleep(1)
            webbrowser.open("https://www.mediafire.com/file/lnetzsflnme479w/NFC_Collection.zip/file")
            continue
        elif z == "C":
            os.system(clear_console)
            afficher_texte_anime("Infrared Collection")
            time.sleep(1)
            webbrowser.open("https://www.mediafire.com/file/reyblgkcw6jff72/Infrared_Collection.zip/file")
            continue
        elif z == "D":
            os.system(clear_console)
            afficher_texte_anime("USB - BLE script Collection")
            time.sleep(1)
            webbrowser.open("https://www.mediafire.com/file/dewd32r9q4pl0q6/BadUSB_-_BLE_Collection.zip/file")
            continue
        elif z == "E":
            os.system(clear_console)
            afficher_texte_anime("RFID Collection")
            time.sleep(1)
            webbrowser.open("https://www.mediafire.com/file/3g1exm8isstg7q0/RFID_Collection.zip/file")
            continue
        elif z == "F":
            os.system(clear_console)
            afficher_texte_anime("All in one + other")
            time.sleep(1)
            webbrowser.open("https://github.com/UberGuidoZ/Flipper")
            continue
        elif z == "G":
            os.system(clear_console)
            continue
        else:
            os.system(clear_console)
            afficher_texte_anime("\033[38;5;196mInvalid option\033[34m")
            time.sleep(1)
            continue

    elif x == "3":
        os.system(clear_console)
        afficher_texte_anime("QFlipper Options")
        afficher_texte_anime("----------------------------")
        afficher_texte_anime("")
        afficher_texte_anime("[A] - QFlipper for Windows")
        afficher_texte_anime("[B] - QFlipper for Linux")
        afficher_texte_anime("[C] - QFlipper for MacOS")
        afficher_texte_anime("[D] - QFlipper for Android")
        afficher_texte_anime("[E] - QFlipper for iOS")
        afficher_texte_anime("[F] - \033[38;5;196mReturn to Main Menu\033[34m")
        afficher_texte_anime("")
        afficher_texte_anime("----------------------------")

        w = input("Select an option: ")

        if w == "A":
            os.system(clear_console)
            afficher_texte_anime("QFlipper for Windows")
            time.sleep(1)
            webbrowser.open("https://update.flipperzero.one/builds/qFlipper/1.3.3/qFlipperSetup-64bit-1.3.3.exe?_gl=1*1mcus1w*_ga_GM78S6JK0K*MTc0MTIxMDIxMC4xLjAuMTc0MTIxMDIxOC41Mi4wLjA.")
            continue
        elif w == "B":
            os.system(clear_console)
            afficher_texte_anime("QFlipper for Linux")
            time.sleep(1)
            webbrowser.open("https://update.flipperzero.one/builds/qFlipper/1.3.3/qFlipper-x86_64-1.3.3.AppImage?_gl=1*pt4app*_ga_GM78S6JK0K*MTc0MTIxMDIxMC4xLjAuMTc0MTIxMDIxOC41Mi4wLjA.")
            continue
        elif w == "C":
            os.system(clear_console)
            afficher_texte_anime("QFlipper for MacOS")
            time.sleep(1)
            webbrowser.open("https://update.flipperzero.one/builds/qFlipper/1.3.3/qFlipper-1.3.3.dmg?_gl=1*93hi4i*_ga_GM78S6JK0K*MTc0MTIxMDIxMC4xLjAuMTc0MTIxMDIxOC41Mi4wLjA.")
            continue
        elif w == "D":
            os.system(clear_console)
            afficher_texte_anime("QFlipper for Android")
            time.sleep(1)
            webbrowser.open("https://play.google.com/store/apps/details?id=com.flipperdevices.app")
            continue
        elif w == "E":
            os.system(clear_console)
            afficher_texte_anime("QFlipper for iOS")
            time.sleep(1)
            webbrowser.open("https://apps.apple.com/app/flipper-mobile-app/id1534655259")
            continue
        elif w == "F":
            os.system(clear_console)
            continue
        else:
            os.system(clear_console)
            afficher_texte_anime("\033[38;5;196mInvalid option\033[34m")
            time.sleep(1)
            continue

    elif x == "4":
        os.system(clear_console)
        afficher_texte_anime("Discord Server Options")
        afficher_texte_anime("----------------------------")
        afficher_texte_anime("[A] - Official Flipper Zero Discord Server")
        afficher_texte_anime("[B] - Momentum Firmware Discord Server")
        afficher_texte_anime("[C] - Xtreme Firmware Discord Server")
        afficher_texte_anime("[D] - Unleashed Firmware Discord Server")
        afficher_texte_anime("[E] - Rogumaster Firmware Discord Server")
        afficher_texte_anime("\033[38;5;196m[F] - Return to Main Menu\033[34m")
        afficher_texte_anime("----------------------------")
        afficher_texte_anime("Other Discord Servers for Flipper Zero... (Very useful)")
        afficher_texte_anime("[G] - Kanjian")
        afficher_texte_anime("[H] - HackLab")
        afficher_texte_anime("[I] - Emensta's community")
        afficher_texte_anime("[J] - POPP.N")
        afficher_texte_anime("\033[38;5;196m[F] - Return to Main Menu\033[34m")
        afficher_texte_anime("------------------------------------------")

        a = input("Select a Discord Server: ")

        if a == "A":
            os.system(clear_console)
            afficher_texte_anime("Official Flipper Zero Discord Server")
            time.sleep(1)
            webbrowser.open("https://discord.gg/RpEk2NQ3pQ")
            continue
        elif a == "B":
            os.system(clear_console)
            afficher_texte_anime("Momentum Firmware Discord Server")
            time.sleep(1)
            webbrowser.open("https://discord.gg/mdEQjg33DG")
            continue
        elif a == "C":
            os.system(clear_console)
            afficher_texte_anime("Xtreme Firmware Discord Server")
            time.sleep(1)
            webbrowser.open("https://discord.gg/crazyco")
            continue
        elif a == "D":
            os.system(clear_console)
            afficher_texte_anime("Unleashed Firmware Discord Server")
            time.sleep(1)
            webbrowser.open("https://discord.unleashedflip.com/")
            continue
        elif a == "E":
            os.system(clear_console)
            afficher_texte_anime("Rogumaster Firmware Discord Server")
            time.sleep(1)
            webbrowser.open("https://discord.gg/gF2bBUzAFe")
            continue
        elif a == "G":
            os.system(clear_console)
            afficher_texte_anime("Kanjian")
            time.sleep(1)
            webbrowser.open("https://discord.gg/EGQJurMUwh")
            continue
        elif a == "H":
            os.system(clear_console)
            afficher_texte_anime("HackLab")
            time.sleep(1)
            webbrowser.open("https://discord.gg/CqqPS5Tc3T")
            continue
        elif a == "I":
            os.system(clear_console)
            afficher_texte_anime("Emensta's community")
            time.sleep(1)
            webbrowser.open("https://discord.gg/emensta-s-community-1229027335534153791")
            continue
        elif a == "J":
            os.system(clear_console)
            afficher_texte_anime("POPP.N")
            time.sleep(1)
            webbrowser.open("https://discord.gg/rkJDEgY6qP")
            continue
        elif a == "F":
            os.system(clear_console)
            continue
        else:
            os.system(clear_console)
            afficher_texte_anime("\033[38;5;196mInvalid option\033[34m")
            time.sleep(1)
            continue
    
    elif x == "5":
        os.system(clear_console)
        afficher_texte_anime("Modules (GPIO)")
        afficher_texte_anime("----------------------------")
        afficher_texte_anime("")
        afficher_texte_anime("[A] - Wifi Module v1 (Devboard)")
        afficher_texte_anime("[B] - CC1101 Module + Protective cover + Full black silicone case (Aesthetic)")
        afficher_texte_anime("[C] - CC1101 Module")
        afficher_texte_anime("[D] - Dupont Cables")
        afficher_texte_anime("[E] - NRF24L01 Module (Aesthetic)")
        afficher_texte_anime("[F] - NRF24L01 Module")
        afficher_texte_anime("[G] - CC1101 + WiFi + ESP32/NRF24 (Multiboard)")
        afficher_texte_anime("[H] - IR module")
        afficher_texte_anime("[I] - Deauther Module")
        afficher_texte_anime("[J] - NFC cards")
        afficher_texte_anime("\033[38;5;196m[K] - Return to Main Menu\033[34m")
        afficher_texte_anime("")
        afficher_texte_anime("----------------------------")

        b = input("Select an option: ")

        if b == "A":
            os.system(clear_console)
            afficher_texte_anime("Wifi Module v1 (Devboard)")
            time.sleep(1)
            webbrowser.open("https://www.amazon.fr/-/en/dp/B0BBWHS5R1/ref=sr_1_5?crid=234ICU4KP907S&dib=eyJ2IjoiMSJ9.vcWyGk7zLsCqgTDDsdeyyDnjgZw1NbgHhKUZCQ5wZ1hvFDM6LT6hhjaP71v-k4vvd0hAGZx4m9snX3Nsge-eeegSaMviDsFU2j380w_VYRjG_D7KZdTQ4olGugEN48eHB3GHHK-H3YfkidPD9HKOmWN_xCIhXGo1QGGxVJenqFphpML-TIjPoZbFw8cqMKEvzWVXWULq-QkXKBaUgJ0aqbslqe2llOtFihlB49abFwYxsXJeR4CKBGdLarfOwgDLNeKJwrejvY0OJHbWSMFBTJoJi_MSxnXuEXOOqPxNWHWNFGevQPkOElJwzIG9paRKB7PUZUSdL6-zMf3vo3PiSCK3CkAZ2UOBaJVtDaLgVuv7hJYxHlwI2FvlBkkgriOtcM0a3U1_H2CyqJIVESanRj5BX-yQlwqESLvwqWbCQs7FcfFi-63deCmHA2tGD_zU.-E6aOTR2Q2k0XVcJ5MltW2bnpRSutfNPNCQNSSZlDNQ&dib_tag=se&keywords=flipper+zero+wifi+devboard&qid=1741214420&sprefix=flipper+zero+w%2Caps%2C108&sr=8-5")
            continue
        elif b == "B":
            os.system(clear_console)
            afficher_texte_anime("CC1101 Module + Protective cover + Full black silicone case (Aesthetic)")
            time.sleep(1)
            webbrowser.open("https://www.amazon.fr/-/en/dp/B0CSVRTZD9/ref=sr_1_6?crid=105VUG1E2N65J&dib=eyJ2IjoiMSJ9.78yRPA6vQjt42H7YvzlL-q0G7BC1okfQaYREPQJbOqcL1sMkZEmx0bh9_nYShO8bj8aMi1VfSJB7PJiP73pVUh8ouQ2Q9nVamuEqvi3936OV4lZg2osgiDvOo-HsjF9ksvALX3Jbt8Em1QmDEN6ZH6SFGtnxY2Fs0wFfrHa-VlqDFbi6xQyBUmqYoggvmaILBzhIEfHcYSpGZwGrXs6ehyp5gUXHYYbVoUgKOIZLYWWgb0zC7ufg2ssQGWEdNru_q0z2x662TA6pK8zbEox04bvy3lYh80WpAgCcViWAuI_pRJ_zJCIoZkyleo6WdSp78i68PhrLfvva2VwAudZlRjCclcQJPfd4hckRnf3OsqZ-GTlycwQgxtFNwONzlGJIUlWo4uk7t-rIKHyUqgy8anJAWKzrG97q2rZFkP8RS3Zr6db5PFKDSxa_-wosfDKI.CIPYQSLlltIloDITki_9U9TgsqzrMUQUX6YY_qUyeu8&dib_tag=se&keywords=flipper%2Bzero%2Bmodule&qid=1741214469&sprefix=flipper%2Bzero%2Bmodu%2Caps%2C113&sr=8-6&th=1")
            continue
        elif b == "C":
            os.system(clear_console)
            afficher_texte_anime("CC1101 Module")
            time.sleep(1)
            webbrowser.open("https://fr.aliexpress.com/item/1005007894499552.html")
            continue
        elif b == "D":
            os.system(clear_console)
            afficher_texte_anime("Dupont Cables")
            time.sleep(1)
            webbrowser.open("https://fr.aliexpress.com/item/1005007072081464.html")
            continue
        elif b == "E":
            os.system(clear_console)
            afficher_texte_anime("NRF24L01 Module (Aesthetic)")
            time.sleep(1)
            webbrowser.open("https://fr.aliexpress.com/item/1005007530439808.html")
            continue
        elif b == "F":
            os.system(clear_console)
            afficher_texte_anime("NRF24L01 Module")
            time.sleep(1)
            webbrowser.open("https://fr.aliexpress.com/item/1005007279570381.html")
            continue
        elif b == "G":
            os.system(clear_console)
            afficher_texte_anime("CC1101 + WiFi + ESP32/NRF24 (Multiboard)")
            time.sleep(1)
            webbrowser.open("https://fr.aliexpress.com/item/1005008555214261.html")
            continue
        elif b == "H":
            os.system(clear_console)
            afficher_texte_anime("IR module")
            time.sleep(1)
            webbrowser.open("https://fr.aliexpress.com/item/1005008555214261.html")
            continue
        elif b == "I":
            os.system(clear_console)
            afficher_texte_anime("Deauther Module")
            time.sleep(1)
            webbrowser.open("https://fr.aliexpress.com/item/1005008555071982.html")
            continue
        elif b == "J":
            os.system(clear_console)
            afficher_texte_anime("NFC cards")
            time.sleep(1)
            webbrowser.open("https://www.etsy.com/fr/listing/1626018148/carte-magique-nfc-1k-uid-modifiable-pour?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=flipper+zero&ref=sr_gallery-1-1&pro=1&sts=1&content_source=6e1ad03d1bfeb3625a05973c3cad390f21f52f5c%253A1626018148&organic_search_click=1&logging_key=6e1ad03d1bfeb3625a05973c3cad390f21f52f5c%3A1626018148")
            continue
        elif b == "K":
            os.system(clear_console)
            continue
        else:
            os.system(clear_console)
            afficher_texte_anime("\033[38;5;196mInvalid option\033[34m")
            time.sleep(1)
            continue

    elif x == "6":
        os.system(clear_console)
        afficher_texte_anime("Aesthetic Products")
        afficher_texte_anime("----------------------------")
        afficher_texte_anime("")
        afficher_texte_anime("[A] - Protection for devboard")
        afficher_texte_anime("[B] - Full black silicone case")
        afficher_texte_anime("[C] - Protective cover")
        afficher_texte_anime("[D] - Transparent case")
        afficher_texte_anime("[E] - Silicone Protective Case")
        afficher_texte_anime("[F] - Screen Protector")
        afficher_texte_anime("[G] - Others")
        afficher_texte_anime("\033[38;5;196m[H] - Return to Main Menu\033[34m")
        afficher_texte_anime("")
        afficher_texte_anime("----------------------------")

        c = input("Select an option: ")

        if c == "A":
            os.system(clear_console)
            afficher_texte_anime("Protection for devboard")
            time.sleep(1)
            webbrowser.open("https://www.etsy.com/fr/listing/1665924660/estuche-flipper-zero-wifi-devboard?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=flipper+zero&ref=sr_gallery-1-6&pro=1&sts=1&content_source=abeebb4dccb54a6e8a7e0c3d727ee00137b2cd00%253A1665924660&organic_search_click=1&logging_key=abeebb4dccb54a6e8a7e0c3d727ee00137b2cd00%3A1665924660")
            continue
        elif c == "B":
            os.system(clear_console)
            afficher_texte_anime("Full black silicone case")
            time.sleep(1)
            webbrowser.open("https://fr.aliexpress.com/item/1005007732068498.html")
            continue
        elif c == "C":
            os.system(clear_console)
            afficher_texte_anime("Protective cover")
            time.sleep(1)
            webbrowser.open("https://fr.aliexpress.com/item/1005006391639410.html")
            continue
        elif c == "D":
            os.system(clear_console)
            afficher_texte_anime("Transparent case")
            time.sleep(1)
            webbrowser.open("https://fr.aliexpress.com/item/1005006174311166.html")
            continue
        elif c == "E":
            os.system(clear_console)
            afficher_texte_anime("Silicone Protective Case")
            time.sleep(1)
            webbrowser.open("https://www.amazon.fr/-/en/dp/B0CK4V8M4M/ref=sr_1_7?crid=SBGDNCAT8ETH&dib=eyJ2IjoiMSJ9.U-3lRF_uQROAVfastNmqPRoSSjmH4gflHyZSlTjk5bUE4d1DfuALcMa0GO4jlzJaBr_B5KTQTpmSz5576QVWjRfy21UsymZBAenHFxfxmHknSycGFIQUq_BxCWdVFUF8SXOntcnDbIzgUJf1DBb3Cte92N43mTmPzzgIoaoy4MCOrfl2hBxVfhv62_oUnNy_wDqjuLwt-PKalyPWK5i6QpcrJSvaGc6TEVDuwoNGD8x2JiX8DvVuySvtDMJ_ZtBzL2lbIw9J9F9mMxTt72fHA8eUXIemN-s764o7w2fYvu-wBjNQ5-Gosuw4cNdZK-n5w72_F7A4OmoQW6kjwt8IKEQ9rOeR471YGwfMXr-k_to2YzT-oaa7O5ktqtmNHf4hCVA44pui7FzHeXJdcMjqwd7YsGPw-X0VRrJ9wshNmQlrRiu5tl0CmhTSPfC1ov1m.Ar-q3JIdBajJfG5oYvQMvSVBag64eLNIu6_pDuF4z48&dib_tag=se&keywords=etui%2Bcoque%2Bde%2Bprotection%2Ben%2Bsilicone%2Bpour%2Bflipper%2Bzero&qid=1741217077&sprefix=flipper%2Bzero%2Betui%2B%2Caps%2C104&sr=8-7&th=1")
            continue
        elif c == "F":
            os.system(clear_console)
            afficher_texte_anime("Screen Protector")
            time.sleep(1)
            webbrowser.open("https://shop.flipperzero.one/collections/flipper-zero-accessories/products/screen-protector-for-flipper-zero")
            continue
        elif c == "G":
            os.system(clear_console)
            afficher_texte_anime("Others")
            time.sleep(1)
            webbrowser.open("https://www.etsy.com/fr/search?q=flipper%20zero&ref=search_bar")
            continue
        elif c == "H":
            os.system(clear_console)
            continue
        else:
            os.system(clear_console)
            afficher_texte_anime("\033[38;5;196mInvalid option\033[34m")
            time.sleep(1)
            continue
    
    elif x == "7":
        os.system(clear_console)
        afficher_texte_anime("Wifi Devboard Flasher")
        time.sleep(1)
        afficher_texte_anime("-----------------------------------------------------------------------")
        afficher_texte_anime("")
        afficher_texte_anime("This tool is used to flash the Wifi Devboard of the Flipper Zero.")
        afficher_texte_anime("This tool is make by \033[38;5;141mUberGuidoZ\033[34m.")
        afficher_texte_anime("")
        afficher_texte_anime("------------------------------------------------------------------------------------------------------")
        time.sleep(3)
        afficher_texte_anime("")
        afficher_texte_anime("\033[38;5;196mIf you have any problems, watch this tutorial:\033[34m https://www.youtube.com/watch?v=CabgV-ljjRM&t=312s")
        afficher_texte_anime("")
        afficher_texte_anime("-----------------------------------------------------------------------------------------------------")
        afficher_texte_anime("")
        input("Press Enter when you are ready to download the tool...")
        webbrowser.open("https://www.mediafire.com/file/unj92220mo0g02j/FZ_Marauder_v2.8.zip/file")
        continue

    elif x == "8":
        os.system(clear_console)
        afficher_texte_anime("Useful .fap applications")
        afficher_texte_anime("----------------------------")
        afficher_texte_anime("")
        afficher_texte_anime("[A] - BLE Spam")
        afficher_texte_anime("[B] - NRF24 Tools")
        afficher_texte_anime("[C] - ESP Tools")
        afficher_texte_anime("[D] - Sub-GHz Bruteforcer + Jammer \033[38;5;196m(May at your own risk)\033[34m")
        afficher_texte_anime("\033[38;5;196m[E] - Return to Main Menu\033[34m")
        afficher_texte_anime("")
        afficher_texte_anime("----------------------------")

        d = input("Select an option: ")

        if d == "A":
            os.system(clear_console)
            afficher_texte_anime("BLE Spam")
            time.sleep(1)
            webbrowser.open("https://www.mediafire.com/file/vcjzs0mm29gu8uf/ble_spam.zip/file")
            continue
        elif d == "B":
            os.system(clear_console)
            afficher_texte_anime("NRF24 Tools")
            time.sleep(1)
            webbrowser.open("https://www.mediafire.com/file/zkoh37yeh83apy7/NRF24_Tools.zip/file")
            continue
        elif d == "C":
            os.system(clear_console)
            afficher_texte_anime("ESP Tools")
            time.sleep(1)
            webbrowser.open("https://www.mediafire.com/file/hoxtoxdmuuxdpow/ESP_Tools.zip/file")
            continue
        elif d == "D":
            os.system(clear_console)
            afficher_texte_anime("Sub-GHz Bruteforcer + Jammer")
            time.sleep(1)
            webbrowser.open("https://www.mediafire.com/file/af42wyy5odumevv/subghz_bruteforcer_%252B_jammer.zip/file")
            continue
        elif d == "E":
            os.system(clear_console)
            continue
        else:
            os.system(clear_console)
            afficher_texte_anime("\033[38;5;196mInvalid option\033[34m")
            time.sleep(1)
            continue

    elif x == "9":
        os.system(clear_console)
        afficher_texte_anime("Diagrams for module connections")
        afficher_texte_anime("----------------------------")
        afficher_texte_anime("")
        afficher_texte_anime("[A] - CC1101 Module + NRF24 Module (Same)")
        afficher_texte_anime("[B] - Deauther Module image 1")
        afficher_texte_anime("[C] - Deauther Module image 2")
        afficher_texte_anime("\033[38;5;196m[D] - Return to Main Menu\033[34m")
        afficher_texte_anime("")
        afficher_texte_anime("----------------------------")

        e = input("Select an option: ")

        if e == "A":
            os.system(clear_console)
            afficher_texte_anime("CC1101 Module + NRF24 Module")
            time.sleep(1)
            webbrowser.open("https://user-images.githubusercontent.com/10090793/216795803-31a787c6-a19b-4368-8fcb-68438207683b.png")
            continue
        elif e == "B":
            os.system(clear_console)
            afficher_texte_anime("Deauther Module image 1")
            time.sleep(1)
            webbrowser.open("https://github.com/SequoiaSan/FlipperZero-Wifi-ESP8266-Deauther-Module/blob/FlipperZero-Module-v2/FlipperZeroModule/rep_images/Schematics_1.jpg?raw=true")
            continue
        elif e == "C":
            os.system(clear_console)
            afficher_texte_anime("Deauther Module image 2")
            time.sleep(1)
            webbrowser.open("https://github.com/SequoiaSan/FlipperZero-Wifi-ESP8266-Deauther-Module/blob/FlipperZero-Module-v2/FlipperZeroModule/rep_images/Schematics_2.jpg?raw=true")
            continue
        elif e == "D":
            os.system(clear_console)
            continue
        else:
            os.system(clear_console)
            afficher_texte_anime("\033[38;5;196mInvalid option\033[34m")
            time.sleep(1)
            continue

    elif x == "10":
        os.system(clear_console)
        afficher_texte_anime("Buy a Flipper Zero")
        time.sleep(1)
        afficher_texte_anime("--------------------------------------------------------------------")
        afficher_texte_anime("")
        afficher_texte_anime("[A] - Buy a Flipper Zero on the official website (Recommended)")
        afficher_texte_anime("[B] - Buy a Flipper Zero on Amazon")
        afficher_texte_anime("\033[38;5;196m[C] - Return to Main Menu\033[34m")
        afficher_texte_anime("")
        afficher_texte_anime("-------------------------------------------------------------------")

        f = input("Select an option: ")

        if f == "A":
            os.system(clear_console)
            afficher_texte_anime("Official website")
            time.sleep(1)
            webbrowser.open("https://shop.flipperzero.one/")
            continue
        elif f == "B":
            os.system(clear_console)
            afficher_texte_anime("Amazon")
            time.sleep(1)
            webbrowser.open("https://www.amazon.fr/-/en/dp/B0D5ZBSBDL/ref=sr_1_11?__mk_fr_FR=ÅMÅŽÕÑ&dib=eyJ2IjoiMSJ9.HpidoBezbGqhtZzRFxpGMAlIk_jYt4wMgbMHcfkHkSHu8p7tfetyXPAHvBgWcFyIc0am-7S0XhqB_oBMfahAI6T690utyuZNnf_1zvsaGmTt0xaquPisbaCLlKXaYNI-OBTfwlihijOP5OCv6KXT6_lE9T4XpfkDiCLJyT0IscWXpMNycntDHHJAa4R83y2xZi9vtgWhY6tYxV7CBiRajQEX7N4a4G4IqcNdOqP00lE6PrAgUq8wVH6R2-tiNh3n42AVB3McfHbPJl_imD41Pr9N1gfNF2_IPgsXAC_3AUvfQFnO5gZgK73MEP_Ka0gvUjJxDFHwgLkPZCNXvDo8O556JTnoMJErQqdNpgtWBrX4ZiaIuU6laRbG1r9ie9Fsm2mRDkH0-9vltELD6eLlGK0wal9RUgCqmk9STB1xNQes0ROEwRzaaXpIcPBafnAf.bO3cwnOm6NL2Ehc_uqpKmRqlx1rL8wNCpi-1QZx6RDA&dib_tag=se&keywords=flipper%2Bzero&qid=1741276839&sr=8-11&th=1")
            continue
        elif f == "C":
            os.system(clear_console)
            continue
        else:
            os.system(clear_console)
            afficher_texte_anime("\033[38;5;196mInvalid option\033[34m")
            time.sleep(1)
            continue
    
    elif x == "11":
        os.system(clear_console)
        afficher_texte_anime("Thank you very much for using this tool.")
        time.sleep(1)
        afficher_texte_anime("See you soon! 👋")
        time.sleep(1)
        os.system(clear_console)
        print(BY_LTX74)
        time.sleep(1)
        break

    else:
        os.system(clear_console)
        print("\033[38;5;196mInvalid option\033[34m")
        time.sleep(1)
        continue