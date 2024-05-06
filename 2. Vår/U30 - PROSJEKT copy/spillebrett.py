import pygame
import random

from figur import Figur
from ball import Ball
from hinder import Hinder
from spiller import Spiller
from booster import Booster

# Starter med spillbrett da den er relevant for spillobjekt.
class Spillebrett:
    def __init__(self, hoyde, bredde):
            

        self.hoyde: int = hoyde
        self.bredde: int = bredde
        self.objekter: list[Figur] = []

        # Må opprette et surface for å så tegne brettet. 
        # Alle ting i pygame må ha surface og rect.
        self.surface = pygame.Surface( (self.bredde, self.hoyde) )
        self.rect = self.surface.get_rect()

        # Plasserer rektangelet til brettet i (x,y) av vinduet.
        self.rect.topleft = (0,0)

        # definerer en font
        self.font = pygame.font.SysFont("Arial", 50)

        # Oppretter spillere
        self.spiller1 = Spiller(25, hoyde / 2)
        self.spiller2 = Spiller(bredde - 25, hoyde / 2)
        # Oppretter tre sauer og putter dem alle i listen sauer.
        self.baller = [Ball(bredde / 2, 200)]

        self.hindere: list[Hinder] = []
        for i in range(5):
            self.hindere.append(Hinder(bredde / 2, 100 + i * 100))

        self.tid_siden_forrige_nye_ball = 0
        self.tid_mellom_booster = 0


        self.boostere: list[Booster] = []




## Oppdaterer her

    # Funksjon for å flytte spillere
    def spiller_input(self, taster):
        # For spiller 2. -> sjekker om toppen er i toppen av vindu
        # Om ja, stopper den å bevege seg utenfor.
        if taster[pygame.K_UP]:
            if self.spiller2.rect.top > 0:
                self.spiller2.flytt_opp()
        if taster[pygame.K_DOWN]:
            if self.spiller2.rect.bottom < self.hoyde:
                self.spiller2.flytt_ned()

        # For spiller 1. 
        if taster[pygame.K_w]:
            if self.spiller1.rect.top > 0:
                self.spiller1.flytt_opp()
        if taster[pygame.K_s]:
            if self.spiller1.rect.bottom < self.hoyde:
                self.spiller1.flytt_ned()
        
    # Funksjon for å flytte hindere
    def flytt_hinder(self, hoyde: int):
        for hinder in self.hindere:
            hinder.flytt()

            if hinder.rect.left > 550 or hinder.rect.right < 250:
                hinder.snu_x()
            
            if hinder.rect.top > hoyde - 50 or hinder.rect.bottom < 0 + 50:
                hinder.snu_y()


    # Funksjon for å bruke ballen med alle sine egenskaper
    def aktiver_ball(self, hoyde: int, bredde: int):

        for ball in self.baller:
            ball.flytt()

            if ball.rect.y < 0 or ball.rect.y > hoyde:
                ball.snu_y()

            if ball.rect.colliderect(self.spiller1.rect) or ball.rect.colliderect(self.spiller2.rect):
                if self.tid_siden_forrige_nye_ball > 60:
                    # Fikk en bug her, hvor nye baller kunne bli sittende fast i spilleren.
                    # Løsningen ble å sette x-posisjonen til nye baller litt til siden for 
                    # spilleren, x-posisjonen er derfor satt til ball.rect.x - (ball.x_fart * 2),
                    # som gjør at spilleren ikke treffer ballen igjen med en gang. 
                    self.baller.append(Ball(ball.rect.x - (ball.x_fart * 2), ball.rect.y, -ball.x_fart, -ball.y_fart))
                    self.tid_siden_forrige_nye_ball = 0
                ball.snu_x()

            if ball.rect.x < 0 or ball.rect.x > bredde:
                self.baller.remove(ball)
                if len(self.baller) == 0:
                    self.baller.append(Ball(bredde / 2, 200))
                if ball.rect.x < 0:
                    self.spiller2.poeng += 1
                else:
                    self.spiller1.poeng += 1

            for hinder in self.hindere:
                if ball.rect.colliderect(hinder.rect):
                    ball.snu_x()
                    ball.snu_y()



    def aktiver_boosters(self):
        ## NB! Jeg har gjort sånn at bare en ball får boost om gangen. Dette har jeg valgt for å gjøre det mer gøy
        ##     For å få alle til å booste må du bare legge til en for løkke, slik at alle ballene blir tatt i boosten.
        ##     Jeg har satt tiden til hver 300 frame, altså hvert 6 sekund. da dukker en ny booster opp.
        if self.tid_mellom_booster > 300:
            self.boostere.append(Booster(random.randint(130,630),random.randint(20, 580), 20, 20))
            self.tid_mellom_booster = 0

        for booster in self.boostere:
            for ball in self.baller:
                if ball.rect.colliderect(booster.rect):
                    # Sjekker hva tilfeldig boost returnerer, og endrer ballens egenskaper basert på det. 
                    # Boost er permanent for den ballen og de som splittes fra den.'
                    if booster.tilfedlig_boost() == "ØK_FART":
                        if ball.x_fart < 4:
                            ball.oek_fart()

                    if booster.tilfedlig_boost() == "MINK_FART":
                        if ball.x_fart > 1:
                            ball.mink_fart()

                    self.boostere.remove(booster)



## Tegner under her
    
    def tegn(self, vindu: pygame.Surface):
        self.surface.fill("black")
        # Tegner spillobjekter før vi tegner vinduet for hele brettet. Tegner spilleren på overflaten til spillbrettet.
        self.spiller1.tegn(self.surface)
        self.spiller2.tegn(self.surface)

        for ball in self.baller:
            ball.tegn(self.surface)

        # Tegner hinder og booster som er satt i en liste. Vi bruker midlertidige variabler i for løkker.
        for booster in self.boostere:
            booster.tegn(self.surface)

        for hinder in self.hindere:
            hinder.tegn(self.surface)



        poeng_spiller_2 = self.font.render(str(self.spiller1.poeng), True, "white")
        self.surface.blit(poeng_spiller_2, (25, 25))
        poeng_spiller_1 = self.font.render(str(self.spiller2.poeng), True, "white")
        self.surface.blit(poeng_spiller_1, (self.bredde - 50, 25))        
    
        # Tegner spillbrettets surface i posisjonen til spillbrettets rect på vinduet.
        vindu.blit(self.surface, self.rect)