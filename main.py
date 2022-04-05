import pygame
import random

# Initialiseer pygame
pygame.init()
pygame.font.init()

# Maak scherm aan op grootte 1280 x 720
screen = pygame.display.set_mode((1280, 720))

# Standaard kleuren in variabelen
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Titel & icoon aanwijzen
pygame.display.set_caption("Monopoly")
pygame.display.set_icon(pygame.image.load('monopoly.png'))

# Afbeelding bord inladen juiste grootte maken en coordinaten meegeven
bordImg = pygame.image.load('bord.png')
bordImg = pygame.transform.scale(bordImg, (600, 600))
bordX = 1
bordY = 120

# Kaartjes inladen, in variables zetten en op het juiste formaat zetten
alkmaarImg = pygame.image.load('Alkmaar.png')
alkmaarImg = pygame.transform.scale(alkmaarImg, (80, 100))
amersfoortImg = pygame.image.load('Amersfoort.png')
amersfoortImg = pygame.transform.scale(amersfoortImg, (80, 100))
amsterdamImg = pygame.image.load('Amsterdam.png')
amsterdamImg = pygame.transform.scale(amsterdamImg, (80, 100))
apeldoornImg = pygame.image.load('Apeldoorn.png')
apeldoornImg = pygame.transform.scale(apeldoornImg, (80, 100))
arnhemImg = pygame.image.load('Arnhem.png')
arnhemImg = pygame.transform.scale(arnhemImg, (80, 100))
bredaImg = pygame.image.load('Breda.png')
bredaImg = pygame.transform.scale(bredaImg, (80, 100))
delftImg = pygame.image.load('Delft.png')
delftImg = pygame.transform.scale(delftImg, (80, 100))
denhaagImg = pygame.image.load('DenHaag.png')
denhaagImg = pygame.transform.scale(denhaagImg, (80, 100))
dordrechtImg = pygame.image.load('Dordrecht.png')
dordrechtImg = pygame.transform.scale(dordrechtImg, (80, 100))
enschedeImg = pygame.image.load('Enschede.png')
enschedeImg = pygame.transform.scale(enschedeImg, (80, 100))
goudaImg = pygame.image.load('Gouda.png')
goudaImg = pygame.transform.scale(goudaImg, (80, 100))
groningenImg = pygame.image.load('Groningen.png')
groningenImg = pygame.transform.scale(groningenImg, (80, 100))
leeuwardenImg = pygame.image.load('Leeuwarden.png')
leeuwardenImg = pygame.transform.scale(leeuwardenImg, (80, 100))
lelystadImg = pygame.image.load('Lelystad.png')
lelystadImg = pygame.transform.scale(lelystadImg, (80, 100))
maastrichtImg = pygame.image.load('Maastricht.png')
maastrichtImg = pygame.transform.scale(maastrichtImg, (80, 100))
middelburgImg = pygame.image.load('Middelburg.png')
middelburgImg = pygame.transform.scale(middelburgImg, (80, 100))
nijmegenImg = pygame.image.load('Nijmegen.png')
nijmegenImg = pygame.transform.scale(nijmegenImg, (80, 100))
rotterdamImg = pygame.image.load('Rotterdam.png')
rotterdamImg = pygame.transform.scale(rotterdamImg, (80, 100))
utrechtImg = pygame.image.load('Utrecht.png')
utrechtImg = pygame.transform.scale(utrechtImg, (80, 100))
zaanstadImg = pygame.image.load('Zaanstad.png')
zaanstadImg = pygame.transform.scale(zaanstadImg, (80, 100))
zoetermeerImg = pygame.image.load('Zoetermeer.png')
zoetermeerImg = pygame.transform.scale(zoetermeerImg, (80, 100))
zwolleImg = pygame.image.load('Zwolle.png')
zwolleImg = pygame.transform.scale(zwolleImg, (80, 100))

# Kaartjes eigenaar op niemand zetten

alkmaarEigenaar = 0
amersfoortEigenaar = 0
amsterdamEigenaar = 0
apeldoornEigenaar = 0
arnhemEigenaar = 0
bredaEigenaar = 0
delftEigenaar = 0
denhaagEigenaar = 0
dordrechtEigenaar = 0
enschedeEigenaar = 0
goudaEigenaar = 0
groningenEigenaar = 0
leeuwardenEigenaar = 0
lelystadEigenaar = 0
maastrichtEigenaar = 0
middelburgEigenaar = 0
nijmegenEigenaar = 0
rotterdamEigenaar = 0
utrechtEigenaar = 0
zaanstadEigenaar = 0
zoetermeerEigenaar = 0
zwolleEigenaar = 0

# Kaartjes tekst variable aanmaken en invullen

myFont = pygame.font.SysFont("Arial", 18)
myFontGroot = pygame.font.SysFont("Arial", 28)

alkmaarTekst = myFontGroot.render("Alkmaar", 1, black)
amersfoortTekst = myFontGroot.render("Alkmaar", 1, black)
amsterdamTekst = myFontGroot.render("Amsterdam", 1, black)
apeldoornTekst = myFontGroot.render("Apeldoorn", 1, black)
arnhemTekst = myFontGroot.render("Arnhem", 1, black)
bredaTekst = myFontGroot.render("Breda", 1, black)
delftTekst = myFontGroot.render("Delft", 1, black)
denhaagTekst = myFontGroot.render("Den Haag", 1, black)
dordrechtTekst = myFontGroot.render("Dordrecht", 1, black)
enschedeTekst = myFontGroot.render("Enschede", 1, black)
goudaTekst = myFontGroot.render("Gouda", 1, black)
groningenTekst = myFontGroot.render("Groningen", 1, black)
leeuwardenTekst = myFontGroot.render("Leeuwarden", 1, black)
lelystadTekst = myFontGroot.render("Lelystad", 1, black)
maastrichtTekst = myFontGroot.render("Maastricht", 1, black)
middelburgTekst = myFontGroot.render("Middelburg", 1, black)
nijmegenTekst = myFontGroot.render("Nijmegen", 1, black)
rotterdamTekst = myFontGroot.render("Rotterdam", 1, black)
utrechtTekst = myFontGroot.render("Utrecht", 1, black)
zaanstadTekst = myFontGroot.render("Zaanstad", 1, black)
zoetermeerTekst = myFontGroot.render("Zoetermeer", 1, black)
zwolleTekst = myFontGroot.render("Zwolle", 1, black)

# "Wil je dit eigendom kopen tekst" in variable zetten

kopenTekst = myFont.render("U heeft dit eigendom gekocht", 1, black)

# Speler pion aanwijzen
speler1Img = pygame.image.load('speler1.png')
# player functie gebruikt om de coordinaten makkelijker vast te stellen, nu niet meer nodig
# speler1X = 530
# speler1Y = 600
speler2Img = pygame.image.load('speler2.png')
# player functie gebruikt om de coordinaten makkelijker vast te stellen, nu niet meer nodig
# speler2X = 600
# speler2Y = 440
# speler stappen op 0 zetten (0 is start)
speler1stappen = 0
speler2stappen = 0
# beurtteller op 0 zetten, speler 1 is dus eerst
beurtteller = 0
# Start geld aan beide spelers geven
speler1geld = 1500
speler2geld = 1500
# Kaarten stapel naar begin zetten
kaartNummer = 0
vrijParkeren = 0

# Functies aanmaken

# player functie gebruikt om de coordinaten makkelijker vast te stellen, nu niet meer nodig
# def player():
    # projecteer speler pion op het scherm
    # screen.blit(speler1Img, (speler1X, speler1Y))
    # screen.blit(speler2Img, (speler2X, speler2Y))

def kans():
    global speler1stappen
    global speler2stappen
    global beurtteller
    global kaartNummer
    global speler1geld, speler2geld
    myFont = pygame.font.SysFont("Arial", 18)
    myFontGroot = pygame.font.SysFont("Arial", 28)
    kansTextBoven = myFontGroot.render("KANS", 1, black)
    algemeenFondsTextBoven = myFontGroot.render("ALGEMEEN FONDS", 1, black)

    if kaartNummer == 0:
        kansText = myFont.render("Ga 3 plaatsen terug", 1, black)
        algemeenFondsText = myFont.render("Betaal uw doktersrekening van 50 euro", 1, black)
    elif kaartNummer == 1:
        kansText = myFont.render("U heeft een kruiswoordpuzzel gewonnen en ontvangt 100 euro", 1, black)
        algemeenFondsText = myFont.render("U erft 100 euro", 1, black)
    elif kaartNummer == 2:
        kansText = myFont.render("Betaal schoolgeld, 150 euro", 1, black)
        algemeenFondsText = myFont.render("Door verkoop van effecten ontvangt u 50 euro", 1, black)
    elif kaartNummer == 3:
        kansText = myFont.render("Ga door naar vrij parkeren", 1, black)
        algemeenFondsText = myFont.render("Een vergissin van de bank, u ontvangt 200 euro", 1, black)
    elif kaartNummer == 4:
        kansText = myFont.render("Aangehouden wegens dronkenschap, 20 euro boette", 1, black)
        algemeenFondsText = myFont.render("U hebt de 2de prijs gewonnen, u ontvangt 10 euro", 1, black)

    # kansKaart = screen.blit(kansText, (300, 220))
    # algemeenFondsKaart = screen.blit(algemeenFondsText,(300, 220))

    # als speler aan de beurt is eind van beurt code uitvoeren
    if beurtteller == 1:
        # als speler op een kans vakje staat code uitvoeren
        if speler1stappen == 5 or speler1stappen == 15 or speler1stappen == 22 or speler1stappen == 38:
            # Rode rechthoek projecteren
            pygame.draw.rect(screen, red, pygame.Rect(300, 200, 600, 300))
            # zwarte dunne rechthoek in rode rechthoek projecteren
            pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
            # KANS tekst projecteren
            screen.blit(kansTextBoven, (570, 197))
            # Volgende kaart van de stapel de beurt geven
            kaartNummer = kaartNummer + 1
            if kaartNummer == 0:
                speler1stappen = speler1stappen - 3
                # screen.blit(kansKaart, (570, 225))
            elif kaartNummer == 1:
                speler1geld = speler1geld + 100
                # screen.blit(kansKaart, (570, 225))
            elif kaartNummer == 2:
                speler1geld = speler1geld - 150
                # screen.blit(kansKaart, (570, 225))
            elif kaartNummer == 3:
                speler1stappen = 20
                # screen.blit(kansKaart, (570, 225))
            elif kaartNummer == 4:
                speler1geld = speler1geld - 20
                # screen.blit(kansKaart, (570, 225))
    # Code van hierboven maar dan voor algemeen fonds
    if beurtteller == 1:
        if speler1stappen == 3 or speler1stappen == 12 or speler1stappen == 25 or speler1stappen == 32:
            pygame.draw.rect(screen, red, pygame.Rect(300, 200, 600, 300))
            pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
            screen.blit(algemeenFondsTextBoven, (500, 197))
            # screen.blit(algemeenFondsText, (500, 197))
            kaartNummer = kaartNummer + 1
            if kaartNummer == 0:
                speler1geld = speler1geld - 50
            elif kaartNummer == 1:
                speler1geld = speler1geld + 100
            elif kaartNummer == 2:
                speler1geld = speler1geld + 50
            elif kaartNummer == 3:
                speler1geld = speler1geld + 200
            elif kaartNummer == 4:
                speler1geld = speler1geld + 10
    # Code van hierboven maar dan voor andere speler
    if beurtteller == 0:
        if speler2stappen == 5 or speler2stappen == 15 or speler2stappen == 22 or speler2stappen == 38:
            pygame.draw.rect(screen, red, pygame.Rect(300, 200, 600, 300))
            pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
            screen.blit(kansTextBoven, (570, 197))
            # screen.blit(kansKaart, (570, 225))
            kaartNummer = kaartNummer + 1
            if kaartNummer == 0:
                speler2stappen = speler2stappen - 3
            elif kaartNummer == 1:
                speler2geld = speler2geld + 100
            elif kaartNummer == 2:
                speler2geld = speler2geld - 150
            elif kaartNummer == 3:
                speler2stappen = 20
            elif kaartNummer == 4:
                speler2geld = speler2geld - 20
    # Code van hierboven maar dan voor algemeen fonds
    if beurtteller == 0:
        if speler2stappen == 3 or speler2stappen == 12 or speler2stappen == 25 or speler2stappen == 32:
            pygame.draw.rect(screen, red, pygame.Rect(300, 200, 600, 300))
            pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
            screen.blit(algemeenFondsTextBoven, (500, 197))
            # screen.blit(algemeenFondsText, (500, 197))
            kaartNummer = kaartNummer + 1
            if kaartNummer == 0:
                speler2geld = speler2geld - 50
            elif kaartNummer == 1:
                speler2geld = speler2geld + 100
            elif kaartNummer == 2:
                speler2geld = speler2geld + 50
            elif kaartNummer == 3:
                speler2geld = speler2geld + 200
            elif kaartNummer == 4:
                speler2geld = speler2geld + 10

def stappen():
    global speler1stappen, speler2stappen
    global speler1geld, speler2geld
    global rotterdamEigenaar, denhaagEigenaar, maastrichtEigenaar, amsterdamEigenaar, utrechtEigenaar, arnhemEigenaar, amersfoortEigenaar, delftEigenaar, zwolleEigenaar, bredaEigenaar, groningenEigenaar, leeuwardenEigenaar, enschedeEigenaar, alkmaarEigenaar, dordrechtEigenaar, apeldoornEigenaar, goudaEigenaar, nijmegenEigenaar, middelburgEigenaar, zoetermeerEigenaar, zaanstadEigenaar, lelystadEigenaar
    # stappen aan locatie definieren
    if speler1stappen == 0:
        speler1X = 525
        speler1Y = 650
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 1:
        speler1X = 485
        speler1Y = 650
        screen.blit(speler1Img, (speler1X, speler1Y))
        # Kijken of kaart al een eigenaar heeft, voer deze code uit als ie geen eigenaar heeft
        if rotterdamEigenaar == 0:
            # voer code uit als speler aan de beurt is
            if beurtteller == 1:
                # Als speler genoeg geld heeft het landgoed kopen
                if speler1geld >= 50:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(rotterdamTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 50
                    rotterdamEigenaar = rotterdamEigenaar + 1
                # Als speler niet genoeg geld heeft het land niet kopen (tijdelijk = 5 is zodat python nog wel kan runnen, word verder niet gebruikt)
                elif speler1geld < 50:
                    tijdelijk = 5
        # Als landgoed al een eigenaar heeft, de eigenaar huur betalen
        elif rotterdamEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 20
    # Zelfde code die je nog heel vaak gaat zien
    elif speler1stappen == 2:
        speler1X = 440
        speler1Y = 650
        screen.blit(speler1Img, (speler1X, speler1Y))
        if denhaagEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 50:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(denhaagTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 50
                    denhaagEigenaar = denhaagEigenaar + 1
                elif speler1geld < 50:
                    tijdelijk = 5
        elif denhaagEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 20
    elif speler1stappen == 3:
        speler1X = 390
        speler1Y = 650
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 4:
        speler1X = 340
        speler1Y = 650
        screen.blit(speler1Img, (speler1X, speler1Y))
        if maastrichtEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 50:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(maastrichtTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 50
                    maastrichtEigenaar = maastrichtEigenaar + 1
                elif speler1geld < 50:
                    tijdelijk = 5
        elif maastrichtEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 20
    elif speler1stappen == 5:
        speler1X = 295
        speler1Y = 650
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 6:
        speler1X = 245
        speler1Y = 650
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 7:
        speler1X = 190
        speler1Y = 650
        screen.blit(speler1Img, (speler1X, speler1Y))
        if amsterdamEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 100:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(amsterdamTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 100
                    amsterdamEigenaar = amsterdamEigenaar + 1
                elif speler1geld < 100:
                    tijdelijk = 5
        elif amsterdamEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 50
    elif speler1stappen == 8:
        speler1X = 140
        speler1Y = 650
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 9:
        speler1X = 90
        speler1Y = 650
        screen.blit(speler1Img, (speler1X, speler1Y))
        if utrechtEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 100:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(utrechtTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 100
                    utrechtEigenaar = utrechtEigenaar + 1
                elif speler1geld < 100:
                    tijdelijk = 5
        elif utrechtEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 50
    elif speler1stappen == 10:
        speler1X = 0
        speler1Y = 650
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 11:
        speler1X = 0
        speler1Y = 600
        screen.blit(speler1Img, (speler1X, speler1Y))
        if arnhemEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 100:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(arnhemTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 100
                    arnhemEigenaar = arnhemEigenaar + 1
                elif speler1geld < 100:
                    tijdelijk = 5
        elif arnhemEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 50
    elif speler1stappen == 12:
        speler1X = 0
        speler1Y = 550
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 13:
        speler1X = 0
        speler1Y = 500
        screen.blit(speler1Img, (speler1X, speler1Y))
        if amersfoortEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 100:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(amersfoortTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 100
                    amersfoortEigenaar = amersfoortEigenaar + 1
                elif speler1geld < 100:
                    tijdelijk = 5
        elif amersfoortEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 50
    elif speler1stappen == 14:
        speler1X = 0
        speler1Y = 450
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 15:
        speler1X = 0
        speler1Y = 400
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 16:
        speler1X = 0
        speler1Y = 350
        screen.blit(speler1Img, (speler1X, speler1Y))
        if delftEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 150:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(delftTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 150
                    delftEigenaar = delftEigenaar + 1
                elif speler1geld < 150:
                    tijdelijk = 5
        elif delftEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 70
    elif speler1stappen == 17:
        speler1X = 0
        speler1Y = 300
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 18:
        speler1X = 0
        speler1Y = 260
        screen.blit(speler1Img, (speler1X, speler1Y))
        if zwolleEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 150:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(zwolleTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 150
                    zwolleEigenaar = zwolleEigenaar + 1
                elif speler1geld < 150:
                    tijdelijk = 5
        elif zwolleEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 70
    elif speler1stappen == 19:
        speler1X = 0
        speler1Y = 210
        screen.blit(speler1Img, (speler1X, speler1Y))
        if bredaEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 150:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(bredaTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 150
                    bredaEigenaar = bredaEigenaar + 1
                elif speler1geld < 150:
                    tijdelijk = 5
        elif bredaEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 70
    elif speler1stappen == 20:
        speler1X = 0
        speler1Y = 160
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 21:
        speler1X = 90
        speler1Y = 160
        screen.blit(speler1Img, (speler1X, speler1Y))
        if groningenEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 200:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(groningenTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 200
                    groningenEigenaar = groningenEigenaar + 1
                elif speler1geld < 200:
                    tijdelijk = 5
        elif groningenEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 100
    elif speler1stappen == 22:
        speler1X = 140
        speler1Y = 160
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 23:
        speler1X = 190
        speler1Y = 160
        screen.blit(speler1Img, (speler1X, speler1Y))
        if leeuwardenEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 200:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(leeuwardenTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 200
                    leeuwardenEigenaar = leeuwardenEigenaar + 1
                elif speler1geld < 200:
                    tijdelijk = 5
        elif leeuwardenEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 100
    elif speler1stappen == 24:
        speler1X = 240
        speler1Y = 160
        screen.blit(speler1Img, (speler1X, speler1Y))
        if enschedeEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 200:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(enschedeTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 200
                    enschedeEigenaar = enschedeEigenaar + 1
                elif speler1geld < 200:
                    tijdelijk = 5
        elif enschedeEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 100
    elif speler1stappen == 25:
        speler1X = 290
        speler1Y = 160
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 26:
        speler1X = 340
        speler1Y = 160
        screen.blit(speler1Img, (speler1X, speler1Y))
        if alkmaarEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 250:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(alkmaarTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 250
                    alkmaarEigenaar = alkmaarEigenaar + 1
                elif speler1geld < 250:
                    tijdelijk = 5
        elif alkmaarEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 120
    elif speler1stappen == 27:
        speler1X = 390
        speler1Y = 160
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 28:
        speler1X = 440
        speler1Y = 160
        screen.blit(speler1Img, (speler1X, speler1Y))
        if dordrechtEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 250:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(dordrechtTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 250
                    dordrechtEigenaar = dordrechtEigenaar + 1
                elif speler1geld < 250:
                    tijdelijk = 5
        elif dordrechtEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 120
    elif speler1stappen == 29:
        speler1X = 480
        speler1Y = 160
        screen.blit(speler1Img, (speler1X, speler1Y))
        if apeldoornEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 250:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(apeldoornTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 250
                    apeldoornEigenaar = apeldoornEigenaar + 1
                elif speler1geld < 250:
                    tijdelijk = 5
        elif apeldoornEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 120
    elif speler1stappen == 30:
        speler1X = 10
        speler1Y = 650
        screen.blit(speler1Img, (speler1X, speler1Y))
        # zet speler in gevangenis en laat hem zijn schuld afkopen
        speler1geld = speler1geld - 200
        speler1stappen = 10
    elif speler1stappen == 31:
        speler1X = 530
        speler1Y = 210
        screen.blit(speler1Img, (speler1X, speler1Y))
        if goudaEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 300:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(goudaTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 300
                    goudaEigenaar = goudaEigenaar + 1
                elif speler1geld < 300:
                    tijdelijk = 5
        elif goudaEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 150
    elif speler1stappen == 32:
        speler1X = 530
        speler1Y = 260
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 33:
        speler1X = 530
        speler1Y = 310
        screen.blit(speler1Img, (speler1X, speler1Y))
        if nijmegenEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 300:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(nijmegenTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 300
                    nijmegenEigenaar = nijmegenEigenaar + 1
                elif speler1geld < 300:
                    tijdelijk = 5
        elif nijmegenEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 150
    elif speler1stappen == 34:
        speler1X = 530
        speler1Y = 360
        screen.blit(speler1Img, (speler1X, speler1Y))
        if middelburgEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 300:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(middelburgTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 300
                    middelburgEigenaar = middelburgEigenaar + 1
                elif speler1geld < 300:
                    tijdelijk = 5
        elif middelburgEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 150
    elif speler1stappen == 35:
        speler1X = 530
        speler1Y = 400
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 36:
        speler1X = 530
        speler1Y = 450
        screen.blit(speler1Img, (speler1X, speler1Y))
        if zoetermeerEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 350:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(zoetermeerTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 350
                    zoetermeerEigenaar = zoetermeerEigenaar + 1
                elif speler1geld < 350:
                    tijdelijk = 5
        elif zoetermeerEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 170
    elif speler1stappen == 37:
        speler1X = 530
        speler1Y = 500
        screen.blit(speler1Img, (speler1X, speler1Y))
        if zaanstadEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 350:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(zaanstadTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 350
                    zaanstadEigenaar = zaanstadEigenaar + 1
                elif speler1geld < 350:
                    tijdelijk = 5
        elif zaanstadEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 200
    elif speler1stappen == 38:
        speler1X = 530
        speler1Y = 550
        screen.blit(speler1Img, (speler1X, speler1Y))
    elif speler1stappen == 39:
        speler1X = 530
        speler1Y = 600
        screen.blit(speler1Img, (speler1X, speler1Y))
        if lelystadEigenaar == 0:
            if beurtteller == 1:
                if speler1geld >= 350:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(lelystadTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler1geld = speler1geld - 350
                    lelystadEigenaar = lelystadEigenaar + 1
                elif speler1geld < 350:
                    tijdelijk = 5
        elif lelystadEigenaar == 2:
            if beurtteller == 1:
                speler1geld = speler1geld - 200

    if speler2stappen == 0:
        speler2X = 525
        speler2Y = 650
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 1:
        speler2X = 485
        speler2Y = 650
        screen.blit(speler2Img, (speler2X, speler2Y))
        if rotterdamEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 50:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(rotterdamTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 50
                    rotterdamEigenaar = rotterdamEigenaar + 2
                elif speler2geld < 50:
                    tijdelijk = 5
        elif rotterdamEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 20
    elif speler2stappen == 2:
        speler2X = 440
        speler2Y = 650
        screen.blit(speler2Img, (speler2X, speler2Y))
        if denhaagEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 50:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(denhaagTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 50
                    denhaagEigenaar = denhaagEigenaar + 2
                elif speler2geld < 50:
                    tijdelijk = 5
        elif denhaagEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 20
    elif speler2stappen == 3:
        speler2X = 390
        speler2Y = 650
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 4:
        speler2X = 340
        speler2Y = 650
        screen.blit(speler2Img, (speler2X, speler2Y))
        if maastrichtEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 50:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(maastrichtTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 50
                    maastrichtEigenaar = maastrichtEigenaar + 2
                elif speler2geld < 50:
                    tijdelijk = 5
        elif maastrichtEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 20
    elif speler2stappen == 5:
        speler2X = 295
        speler2Y = 650
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 6:
        speler2X = 245
        speler2Y = 650
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 7:
        speler2X = 190
        speler2Y = 650
        screen.blit(speler2Img, (speler2X, speler2Y))
        if amsterdamEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 100:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(amsterdamTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 100
                    amsterdamEigenaar = amsterdamEigenaar + 2
                elif speler2geld < 100:
                    tijdelijk = 5
        elif amsterdamEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 50
    elif speler2stappen == 8:
        speler2X = 140
        speler2Y = 650
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 9:
        speler2X = 90
        speler2Y = 650
        screen.blit(speler2Img, (speler2X, speler2Y))
        if utrechtEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 100:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(utrechtTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 100
                    utrechtEigenaar = utrechtEigenaar + 2
                elif speler2geld < 100:
                    tijdelijk = 5
        elif utrechtEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 50
    elif speler2stappen == 10:
        speler2X = 0
        speler2Y = 650
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 11:
        speler2X = 0
        speler2Y = 600
        screen.blit(speler2Img, (speler2X, speler2Y))
        if arnhemEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 100:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(arnhemTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 100
                    arnhemEigenaar = arnhemEigenaar + 2
                elif speler2geld < 100:
                    tijdelijk = 5
        elif arnhemEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 50
    elif speler2stappen == 12:
        speler2X = 0
        speler2Y = 550
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 13:
        speler2X = 0
        speler2Y = 500
        screen.blit(speler2Img, (speler2X, speler2Y))
        if amersfoortEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 100:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(amersfoortTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 100
                    amersfoortEigenaar = amersfoortEigenaar + 2
                elif speler2geld < 100:
                    tijdelijk = 5
        elif amersfoortEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 50
    elif speler2stappen == 14:
        speler2X = 0
        speler2Y = 450
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 15:
        speler2X = 0
        speler2Y = 400
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 16:
        speler2X = 0
        speler2Y = 350
        screen.blit(speler2Img, (speler2X, speler2Y))
        if delftEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 150:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(delftTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 150
                    delftEigenaar = delftEigenaar + 2
                elif speler2geld < 150:
                    tijdelijk = 5
        elif delftEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 70
    elif speler2stappen == 17:
        speler2X = 0
        speler2Y = 300
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 18:
        speler2X = 0
        speler2Y = 260
        screen.blit(speler2Img, (speler2X, speler2Y))
        if zwolleEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 150:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(zwolleTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 150
                    zwolleEigenaar = zwolleEigenaar + 2
                elif speler2geld < 150:
                    tijdelijk = 5
        elif zwolleEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 70
    elif speler2stappen == 19:
        speler2X = 0
        speler2Y = 210
        screen.blit(speler2Img, (speler2X, speler2Y))
        if bredaEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 150:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(bredaTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 150
                    bredaEigenaar = bredaEigenaar + 2
                elif speler2geld < 150:
                    tijdelijk = 5
        elif bredaEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 70
    elif speler2stappen == 20:
        speler2X = 0
        speler2Y = 160
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 21:
        speler2X = 90
        speler2Y = 160
        screen.blit(speler2Img, (speler2X, speler2Y))
        if groningenEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 200:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(groningenTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 200
                    groningenEigenaar = groningenEigenaar + 2
                elif speler2geld < 200:
                    tijdelijk = 5
        elif groningenEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 100
    elif speler2stappen == 22:
        speler2X = 140
        speler2Y = 160
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 23:
        speler2X = 190
        speler2Y = 160
        screen.blit(speler2Img, (speler2X, speler2Y))
        if leeuwardenEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 200:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(leeuwardenTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 200
                    leeuwardenEigenaar = leeuwardenEigenaar + 2
                elif speler2geld < 200:
                    tijdelijk = 5
        elif leeuwardenEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 100
    elif speler2stappen == 24:
        speler2X = 240
        speler2Y = 160
        screen.blit(speler2Img, (speler2X, speler2Y))
        if enschedeEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 200:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(enschedeTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 200
                    enschedeEigenaar = enschedeEigenaar + 2
                elif speler2geld < 200:
                    tijdelijk = 5
        elif enschedeEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 100
    elif speler2stappen == 25:
        speler2X = 290
        speler2Y = 160
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 26:
        speler2X = 340
        speler2Y = 160
        screen.blit(speler2Img, (speler2X, speler2Y))
        if alkmaarEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 250:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(alkmaarTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 250
                    alkmaarEigenaar = alkmaarEigenaar + 2
                elif speler2geld < 250:
                    tijdelijk = 5
        elif alkmaarEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 120
    elif speler2stappen == 27:
        speler2X = 390
        speler2Y = 160
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 28:
        speler2X = 440
        speler2Y = 160
        screen.blit(speler2Img, (speler2X, speler2Y))
        if dordrechtEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 250:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(dordrechtTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 250
                    dordrechtEigenaar = dordrechtEigenaar + 2
                elif speler2geld < 250:
                    tijdelijk = 5
        elif dordrechtEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 120
    elif speler2stappen == 29:
        speler2X = 480
        speler2Y = 160
        screen.blit(speler2Img, (speler2X, speler2Y))
        if apeldoornEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 250:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(apeldoornTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 250
                    apeldoornEigenaar = apeldoornEigenaar + 2
                elif speler2geld < 250:
                    tijdelijk = 5
        elif apeldoornEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 120
    elif speler2stappen == 30:
        speler2X = 10
        speler2Y = 650
        screen.blit(speler2Img, (speler2X, speler2Y))
        speler2geld = speler2geld - 200
        speler2stappen = 10
    elif speler2stappen == 31:
        speler2X = 530
        speler2Y = 210
        screen.blit(speler2Img, (speler2X, speler2Y))
        if goudaEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 300:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(goudaTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 300
                    goudaEigenaar = goudaEigenaar + 2
                elif speler2geld < 300:
                    tijdelijk = 5
        elif goudaEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 150
    elif speler2stappen == 32:
        speler2X = 530
        speler2Y = 260
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 33:
        speler2X = 530
        speler2Y = 310
        screen.blit(speler2Img, (speler2X, speler2Y))
        if nijmegenEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 300:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(nijmegenTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 300
                    nijmegenEigenaar = nijmegenEigenaar + 2
                elif speler2geld < 300:
                    tijdelijk = 5
        elif nijmegenEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 150
    elif speler2stappen == 34:
        speler2X = 530
        speler2Y = 360
        screen.blit(speler2Img, (speler2X, speler2Y))
        if middelburgEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 300:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(middelburgTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 300
                    middelburgEigenaar = middelburgEigenaar + 2
                elif speler2geld < 300:
                    tijdelijk = 5
        elif middelburgEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 150
    elif speler2stappen == 35:
        speler2X = 530
        speler2Y = 400
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 36:
        speler2X = 530
        speler2Y = 450
        screen.blit(speler2Img, (speler2X, speler2Y))
        if zoetermeerEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 350:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(zoetermeerTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 350
                    zoetermeerEigenaar = zoetermeerEigenaar + 2
                elif speler2geld < 350:
                    tijdelijk = 5
        elif zoetermeerEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 170
    elif speler2stappen == 37:
        speler2X = 530
        speler2Y = 500
        screen.blit(speler2Img, (speler2X, speler2Y))
        if zaanstadEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 350:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(zaanstadTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 350
                    zaanstadEigenaar = zaanstadEigenaar + 2
                elif speler2geld < 350:
                    tijdelijk = 5
        elif zaanstadEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 170
    elif speler2stappen == 38:
        speler2X = 530
        speler2Y = 550
        screen.blit(speler2Img, (speler2X, speler2Y))
    elif speler2stappen == 39:
        speler2X = 530
        speler2Y = 600
        screen.blit(speler2Img, (speler2X, speler2Y))
        if lelystadEigenaar == 0:
            if beurtteller == 0:
                if speler2geld >= 350:
                    pygame.draw.rect(screen, green, pygame.Rect(300, 200, 600, 300))
                    pygame.draw.rect(screen, black, pygame.Rect(325, 225, 550, 250), 2)
                    screen.blit(lelystadTekst, (550, 197))
                    screen.blit(kopenTekst, (450, 250))
                    speler2geld = speler2geld - 350
                    lelystadEigenaar = lelystadEigenaar + 2
                elif speler2geld < 350:
                    tijdelijk = 5
        elif lelystadEigenaar == 1:
            if beurtteller == 0:
                speler2geld = speler2geld - 170

def bord():
    # Afbeelding en coordinaten spelbord aanwijzen
    screen.blit(bordImg, (bordX, bordY))
    # linkermuisknop om dobbelstenen te gooien tekst toevoegen
    myFont = pygame.font.SysFont("Arial", 18)
    # Tekst linksboven in het scherm aan variabelen toevoegen
    dobbelUitlegText = myFont.render("klik linkermuisknop om de dobbelstenen te gooien", 1, black)
    dobbelLabelVoor = myFont.render("Je hebt ", 1, black)
    dobbelLabelAchter = myFont.render("gegooit", 1, black)
    # Tekst linksboven in het scherm afbeelden
    screen.blit(dobbelUitlegText, (10, 10))
    screen.blit(dobbelLabelVoor, (10, 30))
    screen.blit(dobbelLabelAchter, (100, 30))

def dobbelsteen():
    # de benodigde global variables importeren
    global speler1stappen
    global speler2stappen
    global beurtteller
    global speler1geld
    global speler2geld
    # Twee dobbelstenen aanmaken en gooien
    dobbel1 = random.randrange(1, 7)
    dobbel2 = random.randrange(1, 7)
    # Dobbelstenen bij elkaar optellen
    worp = dobbel1 + dobbel2
    # Tekst voor de dobbelstenen configureren
    myFont = pygame.font.SysFont("Arial", 18)
    myFontGroot = pygame.font.SysFont("Arial", 28)
    dobbelTekst = myFont.render(str(worp), True, black)
    screen.blit(dobbelTekst, (75, 30))
    # begin van stappentellen
    # speler 1 aan de beurt
    if beurtteller == 0:
        # stappen en nieuwe worp bij elkaar optellen
        speler1stappen = speler1stappen + worp
        # beurt naar speler 2
        beurtteller = beurtteller + 1
        # tekst voor beurt teller omkeren
        spelerBeurt = beurtteller + 1
        # als speler1 langs start komt plek 0 aanwijzen
        if speler1stappen >= 40:
            # speler stappen -40 zodra hij over start loopt, zodat hij gewoon verder kan lopen zonder dat de rest van zn worp verloren gaat
            speler1stappen = speler1stappen - 40
            # 200 euro startgeld
            speler1geld = speler1geld + 200
        # Als je dubbel gooit opnieuw de beurt krijgen
        if dobbel1 == dobbel2:
            # Tekst als je dubbel gooit
            dubbelTekst = myFontGroot.render("Dubbel!", 1, black)
            screen.blit(dubbelTekst, (400, 50))
            # Gooi dobbelsteen opnieuw
            dobbel1 = random.randrange(1, 7)
            dobbel2 = random.randrange(1, 7)
            # Dobbelstenen bij elkaar optellen
            worp = dobbel1 + dobbel2
            # Tekst voor de dobbelstenen configureren
            myFont = pygame.font.SysFont("Arial", 18)
            dobbelTekst = myFont.render(str(worp), True, black)
            screen.blit(dobbelTekst, (75, 30))
            # stappen en nieuwe worp bij elkaar optellen
            speler1stappen = speler1stappen + worp
            if dobbel1 == dobbel2:
                # naar gevangenis
                speler1stappen = 10
                speler1geld = speler1geld - 200

    # speler 2 aan de beurt
    elif beurtteller == 1:
        # stappen en nieuwe worp bij elkaar optellen
        speler2stappen = speler2stappen + worp
        # beurt naar speler 1
        beurtteller = beurtteller - 1
        # tekst voor beurt teller omkeren
        spelerBeurt = beurtteller + 1
        # als speler2 langs start komt plek 0 aanwijzen
        if speler2stappen >= 40:
            # speler stappen -40 zodra hij over start loopt, zodat hij gewoon verder kan lopen zonder dat de rest van zn worp verloren gaat
            speler2stappen = speler2stappen - 40
            # 200 euro startgeld
            speler2geld = speler2geld + 200
        # Als je dubbel gooit opnieuw de beurt krijgen
        if dobbel1 == dobbel2:
            # Tekst als je dubbel gooit
            dubbelTekst = myFontGroot.render("Dubbel!", 1, black)
            screen.blit(dubbelTekst, (400, 50))
            # Gooi dobbelsteen opnieuw
            dobbel1 = random.randrange(1, 7)
            dobbel2 = random.randrange(1, 7)
            # Dobbelstenen bij elkaar optellen
            worp = dobbel1 + dobbel2
            # Tekst voor de dobbelstenen configureren
            myFont = pygame.font.SysFont("Arial", 18)
            dobbelTekst = myFont.render(str(worp), True, black)
            screen.blit(dobbelTekst, (75, 30))
            # stappen en nieuwe worp bij elkaar optellen
            speler2stappen = speler2stappen + worp
            if dobbel1 == dobbel2:
                # naar gevangenis
                speler2stappen = 10
                speler2geld = speler2geld - 200

    # Tekst voor speler beurt aanmaken
    beurtTextVoor = myFont.render("Speler ", 1, black)
    beurtTextAchter = myFont.render("is nu aan de beurt ", 1, black)
    beurtTekst = myFont.render(str(spelerBeurt), True, black)
    # Tekst voor speler beurt afbeelden
    screen.blit(beurtTextVoor, (10, 50))
    screen.blit(beurtTekst, (60, 50))
    screen.blit(beurtTextAchter, (80, 50))

def rekening():
    global speler1geld
    global speler2geld
    global speler1stappen
    global speler2stappen
    myFont = pygame.font.SysFont("Arial", 18)
    # Tekst van rekening in het scherm aan variabelen toevoegen
    speler1RekeningTextVoor = myFont.render("Bankrekening :", 1, black)
    speler2RekeningTextVoor = myFont.render("Bankrekening :", 1, black)
    speler1RekeningText = myFont.render(str(speler1geld), True, black)
    speler2RekeningText = myFont.render(str(speler2geld), True, black)
    # Tekst van rekening in het scherm afbeelden
    screen.blit(speler1RekeningTextVoor, (650, 50))
    screen.blit(speler1RekeningText, (750, 50))
    screen.blit(speler2RekeningTextVoor, (650, 400))
    screen.blit(speler2RekeningText, (750, 400))


def belasting():
    global speler1stappen, speler2stappen
    global speler1geld, speler2geld
    global vrijParkeren
    # als speler aan de beurt is en op een belasting vakje staat code uitvoeren
    if beurtteller == 0:
        if speler1stappen == 6:
            # geld van speler zijn rekening afhalen
            speler1geld = speler1geld - 200
            # geld in de vrijparkeren 'pot' doen
            vrijParkeren = vrijParkeren + 200
        if speler1stappen == 35:
            # opnieuw code van hierboven
            speler1geld = speler1geld - 100
            vrijParkeren = vrijParkeren + 100
        if speler1stappen == 20:
            speler1geld + vrijParkeren
            vrijParkeren = 0
    if beurtteller == 1:
        if speler2stappen == 6:
            speler2geld = speler2geld - 200
            vrijParkeren = vrijParkeren + 200
        if speler2stappen == 35:
            speler2geld = speler2geld - 100
            vrijParkeren = vrijParkeren + 100
        if speler2stappen == 20:
            speler2geld + vrijParkeren
            vrijParkeren = 0

def spelerScherm():
    myFont = pygame.font.SysFont("Arial", 18)
    # Tekst van rekening in het scherm aan variabelen toevoegen
    speler1Text = myFont.render("Speler 1", 1, black)
    speler2Text = myFont.render("Speler 2", 1, black)
    # Tekst van rekening in het scherm afbeelden
    screen.blit(speler1Text, (650, 30))
    screen.blit(speler2Text, (650, 380))
    # Als het landgoed in eigendom is van speler 1 dit kaartje bij zijn portfolio projecteren
    if rotterdamEigenaar == 1:
        screen.blit(rotterdamImg, (650, 75))
    if denhaagEigenaar == 1:
        screen.blit(denhaagImg, (700, 75))
    if maastrichtEigenaar == 1:
        screen.blit(maastrichtImg, (750, 75))
    if amsterdamEigenaar == 1:
        screen.blit(amsterdamImg, (800, 75))
    if utrechtEigenaar == 1:
        screen.blit(utrechtImg, (850, 75))
    if arnhemEigenaar == 1:
        screen.blit(arnhemImg, (900, 75))
    if amersfoortEigenaar == 1:
        screen.blit(amersfoortImg, (950, 75))
    if delftEigenaar == 1:
        screen.blit(delftImg, (1000, 75))
    if zwolleEigenaar == 1:
        screen.blit(zwolleImg, (1050, 75))
    if bredaEigenaar == 1:
        screen.blit(bredaImg, (1100, 75))
    if groningenEigenaar == 1:
        screen.blit(groningenImg, (1150, 75))
    if leeuwardenEigenaar == 1:
        screen.blit(leeuwardenImg, (650, 185))
    if enschedeEigenaar == 1:
        screen.blit(enschedeImg, (700, 185))
    if alkmaarEigenaar == 1:
        screen.blit(alkmaarImg, (750, 185))
    if dordrechtEigenaar == 1:
        screen.blit(dordrechtImg, (800, 185))
    if apeldoornEigenaar == 1:
        screen.blit(apeldoornImg, (850, 185))
    if goudaEigenaar == 1:
        screen.blit(goudaImg, (900, 185))
    if nijmegenEigenaar == 1:
        screen.blit(nijmegenImg, (950, 185))
    if middelburgEigenaar == 1:
        screen.blit(middelburgImg, (1000, 185))
    if zoetermeerEigenaar == 1:
        screen.blit(zoetermeerImg, (1050, 185))
    if zaanstadEigenaar == 1:
        screen.blit(zaanstadImg, (1100, 185))
    if lelystadEigenaar == 1:
        screen.blit(lelystadImg, (1150, 185))

    # Als het landgoed in eigendom is van speler 2 dit kaartje bij zijn portfolio projecteren
    if rotterdamEigenaar == 2:
        screen.blit(alkmaarImg, (650, 425))
    if denhaagEigenaar == 2:
        screen.blit(denhaagImg, (700, 425))
    if maastrichtEigenaar == 2:
        screen.blit(maastrichtImg, (750, 425))
    if amsterdamEigenaar == 2:
        screen.blit(amsterdamImg, (800, 425))
    if utrechtEigenaar == 2:
        screen.blit(utrechtImg, (850, 425))
    if arnhemEigenaar == 2:
        screen.blit(arnhemImg, (900, 425))
    if amersfoortEigenaar == 2:
        screen.blit(amersfoortImg, (950, 425))
    if delftEigenaar == 2:
        screen.blit(delftImg, (1000, 425))
    if zwolleEigenaar == 2:
        screen.blit(zwolleImg, (1050, 425))
    if bredaEigenaar == 2:
        screen.blit(bredaImg, (1100, 425))
    if groningenEigenaar == 2:
        screen.blit(groningenImg, (1150, 425))
    if leeuwardenEigenaar == 2:
        screen.blit(leeuwardenImg, (650, 535))
    if enschedeEigenaar == 2:
        screen.blit(enschedeImg, (700, 535))
    if alkmaarEigenaar == 2:
        screen.blit(alkmaarImg, (750, 535))
    if dordrechtEigenaar == 2:
        screen.blit(dordrechtImg, (800, 535))
    if apeldoornEigenaar == 2:
        screen.blit(apeldoornImg, (850, 535))
    if goudaEigenaar == 2:
        screen.blit(goudaImg, (900, 535))
    if nijmegenEigenaar == 2:
        screen.blit(nijmegenImg, (950, 535))
    if middelburgEigenaar == 2:
        screen.blit(middelburgImg, (1000, 535))
    if zoetermeerEigenaar == 2:
        screen.blit(zoetermeerImg, (1050, 535))
    if zaanstadEigenaar == 2:
        screen.blit(zaanstadImg, (1100, 535))
    if lelystadEigenaar == 2:
        screen.blit(lelystadImg, (1150, 535))


# Game loop
running = True
# Scherm updaten als programma initialiseerd
laatMaarDraaien = 0
# Achtergrond kleur en bord weergeven
screen.fill((27, 196, 123))
bord()
pygame.display.update()
while running:
    for event in pygame.event.get():
        # Kruisje functioneel maken
        if event.type == pygame.QUIT:
            running = False
        # Als er een muisknop word ingedrukt voor dan functie uit
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Reset het vorige scherm en update het met de nieuwe waardes
            screen.fill((27, 196, 123))
            bord()
            dobbelsteen()
            # player()
            rekening()
            belasting()
            spelerScherm()
            stappen()
            kans()
            print(rotterdamEigenaar, denhaagEigenaar, maastrichtEigenaar, amsterdamEigenaar, utrechtEigenaar, arnhemEigenaar, amersfoortEigenaar, delftEigenaar, zwolleEigenaar, bredaEigenaar, groningenEigenaar, leeuwardenEigenaar, enschedeEigenaar, alkmaarEigenaar, dordrechtEigenaar, apeldoornEigenaar, goudaEigenaar, nijmegenEigenaar, middelburgEigenaar, zoetermeerEigenaar, zaanstadEigenaar, lelystadEigenaar)
            pygame.display.update()
    # Scherm updaten als programma initialiseerd
    if laatMaarDraaien == 0:
        stappen()
        spelerScherm()
        rekening()
        pygame.display.update()
        laatMaarDraaien = laatMaarDraaien + 1
