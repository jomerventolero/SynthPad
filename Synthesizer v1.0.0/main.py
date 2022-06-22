'''
	Author: Jomer Augustin Ventolero
	Email: orekihoutaro1218@gmail.com / hiroventolero@gmail.com
'''
import pygame as pygame
from sys import exit
import sys
from settings import *
from graphics import *
import os


class SynthPad:
    def __init__(self, debug=False):
        pg.mixer.pre_init(44100, 16, 2, 2048)
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.main_volume = 0.5
        self.debug = debug
        self.play1 = True
        self.play2 = True
        self.play3 = True
        self.play4 = True
        self.play5 = True
        self.play6 = True
        self.play7 = True
        self.play8 = True
        self.play9 = True
        self.play10 = True
        self.play11 = True
        self.play12 = True
        self.vol = 0
        if sys.platform.startswith("win"):
        	self.pathsep = "\\"
        else:
        	self.pathsep = "/"  


    def load_graphics_data(self):
        if self.debug:
            print('...loading graphics data')
        self.cpad0 = pg.image.load(os.getcwd() + self.pathsep + "Images" + self.pathsep + "CPad0.png").convert()
        self.cpad1 = pg.image.load(os.getcwd() + self.pathsep + "Images" + self.pathsep + "CPad1.png").convert()
        self.cspad0 = pg.image.load(os.getcwd() + self.pathsep + "Images" + self.pathsep + "C#Pad0.png").convert()
        self.cspad1 = pg.image.load(os.getcwd() + self.pathsep + "Images" + self.pathsep + "C#Pad1.png").convert()
        self.dpad0 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "DPad0.png").convert()
        self.dpad1 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "DPad1.png").convert()
        self.dspad0 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "D#Pad0.png").convert()
        self.dspad1 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "D#Pad1.png").convert()
        self.epad0 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "EPad0.png").convert()
        self.epad1 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "EPad1.png").convert()
        self.fpad0 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "FPad0.png").convert()
        self.fpad1 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "FPad1.png").convert()
        self.fspad0 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "F#Pad0.png").convert()
        self.fspad1 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "F#Pad1.png").convert()
        self.gpad0 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "GPad0.png").convert()
        self.gpad1 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "GPad1.png").convert()
        self.gspad0 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "G#Pad0.png").convert()
        self.gspad1 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "G#Pad1.png").convert()
        self.apad0 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "APad0.png").convert()
        self.apad1 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "APad1.png").convert()
        self.aspad0 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "A#Pad0.png").convert()
        self.aspad1 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "A#Pad1.png").convert()
        self.bpad0 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "BPad0.png").convert()
        self.bpad1 = pg.image.load(os.getcwd() + self.pathsep+ "Images" + self.pathsep + "BPad1.png").convert()
        self.top1 = pg.image.load(os.getcwd() + self.pathsep + "Images" + self.pathsep +"SynthPad.png").convert()
        self.top2 = pg.image.load(os.getcwd() + self.pathsep + "Images" + self.pathsep +"panel_top_2.png").convert()
        self.volume = []
        for i in range(1,11):
            self.volume.append(pg.image.load(os.getcwd() + self.pathsep + "Images" + self.pathsep + "Volume{}.png".format(i)))
        if self.debug:
            print('Done!')
        


    def load_sound_data(self):
        if self.debug:
            print('...loading sound data')
        self.pad1 = pg.mixer.Sound(os.getcwd() + self.pathsep + "Audio" + self.pathsep + "CMajorDPad.ogg")
        self.pad2 = pg.mixer.Sound(os.getcwd() + self.pathsep + "Audio" + self.pathsep + "C#MajorDPad.ogg")
        self.pad3 = pg.mixer.Sound(os.getcwd() + self.pathsep + "Audio" + self.pathsep + "DMajorDPad.ogg")                
        self.pad4 = pg.mixer.Sound(os.getcwd() + self.pathsep + "Audio" + self.pathsep + "D#MajorDPad.ogg")
        self.pad5 = pg.mixer.Sound(os.getcwd() + self.pathsep + "Audio" + self.pathsep + "EMajorDPad.ogg")
        self.pad6 = pg.mixer.Sound(os.getcwd() + self.pathsep + "Audio" + self.pathsep + "FMajorDPad.ogg")
        self.pad7 = pg.mixer.Sound(os.getcwd() + self.pathsep + "Audio" + self.pathsep + "F#MajorDPad.ogg")
        self.pad8 = pg.mixer.Sound(os.getcwd() + self.pathsep + "Audio" + self.pathsep + "GMajorDPad.ogg")
        self.pad9 = pg.mixer.Sound(os.getcwd() + self.pathsep + "Audio" + self.pathsep + "G#MajorDPad.ogg")
        self.pad10 = pg.mixer.Sound(os.getcwd() + self.pathsep + "Audio" + self.pathsep + "AMajorDPad.ogg")
        self.pad11 = pg.mixer.Sound(os.getcwd() + self.pathsep + "Audio" + self.pathsep + "A#MajorDPad.ogg")
        self.pad12 = pg.mixer.Sound(os.getcwd() + self.pathsep + "Audio" + self.pathsep + "BMajorDPad.ogg")
        if self.debug:
            print('Done!')


    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.dt = self.clock.tick(FPS) / 1000
            

    def update(self):
        pg.display.flip()


    def update_volume(self):
        self.pad1.set_volume(self.main_volume)
        self.pad2.set_volume(self.main_volume)
        self.pad3.set_volume(self.main_volume)
        self.pad4.set_volume(self.main_volume)
        self.pad5.set_volume(self.main_volume)
        self.pad6.set_volume(self.main_volume)
        self.pad7.set_volume(self.main_volume)
        self.pad8.set_volume(self.main_volume)
        self.pad9.set_volume(self.main_volume)
        self.pad10.set_volume(self.main_volume)
        self.pad11.set_volume(self.main_volume)
        self.pad12.set_volume(self.main_volume)


    def init_screen(self):
        # UI Components
        Pad(self.screen, self.top1, 0, 0)
        SPad(self.screen, self.top2, 0, 1.0)
        SPad(self.screen, self.volume[4], 4.0, 0)
        # Pads
        Pad(self.screen, self.cpad0, 0, 1)
        Pad(self.screen, self.cspad0, 1, 1)
        Pad(self.screen, self.dpad0, 2, 1)
        Pad(self.screen, self.dspad0, 3, 1)
        Pad(self.screen, self.epad0, 0, 2)
        Pad(self.screen, self.fpad0, 1, 2)
        Pad(self.screen, self.fspad0, 2, 2)
        Pad(self.screen, self.gpad0, 3, 2)
        Pad(self.screen, self.gspad0, 0, 3)
        Pad(self.screen, self.apad0, 1, 3)
        Pad(self.screen, self.aspad0, 2, 3)
        Pad(self.screen, self.bpad0, 3, 3)


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                    self.quit()
                if event.key == pg.K_q:
                    if self.play1:
                        self.pad1.play(loops=-1)
                        self.play1 = not self.play1
                        Pad(self.screen, self.cpad1, 0, 1)
                    else:
                        self.pad1.stop()
                        self.play1 = not self.play1
                        Pad(self.screen, self.cpad0, 0, 1)
                if event.key == pg.K_w:
                    if self.play2:  
                        self.pad2.play(loops=-1)
                        self.play2 = not self.play2
                        Pad(self.screen, self.cspad1, 1, 1)
                    else:
                        self.pad2.stop()
                        self.play2 = not self.play2
                        Pad(self.screen, self.cspad0, 1, 1)
                if event.key == pg.K_e:
                    if self.play3:
                        self.pad3.play(loops=-1)
                        self.play3 = not self.play3
                        Pad(self.screen, self.dpad1, 2, 1)
                    else:
                        self.pad3.stop()
                        self.play3 = not self.play3
                        Pad(self.screen, self.dpad0, 2, 1)
                if event.key == pg.K_r:
                    if self.play4:
                        self.pad4.play(loops=-1)
                        self.play4 = not self.play4
                        Pad(self.screen, self.dspad1, 3, 1)
                    else:
                        self.pad4.stop()
                        self.play4 = not self.play4
                        Pad(self.screen, self.dspad0, 3, 1)
                if event.key == pg.K_a:
                    if self.play5:
                        self.pad5.play(loops=-1)
                        self.play5 = not self.play5
                        Pad(self.screen, self.epad1, 0, 2)
                    else:
                        self.pad5.stop()
                        self.play5 = not self.play5
                        Pad(self.screen, self.epad0, 0, 2)
                if event.key == pg.K_s:
                    if self.play6:
                        self.pad6.play(loops=-1)
                        self.play6 = not self.play6
                        Pad(self.screen, self.fpad1, 1, 2)
                    else:
                        self.pad6.stop()
                        self.play6 = not self.play6
                        Pad(self.screen, self.fpad0, 1, 2)
                if event.key == pg.K_d:
                    if self.play7:
                        self.pad7.play(loops=-1)
                        self.play7 = not self.play7
                        Pad(self.screen, self.fspad1, 2, 2)
                    else:
                        self.pad7.stop()
                        self.play7 = not self.play7
                        Pad(self.screen, self.fspad0, 2, 2)
                if event.key == pg.K_f:
                    if self.play8:
                        self.pad8.play(loops=-1)
                        self.play8 = not self.play8
                        Pad(self.screen, self.gpad1, 3, 2)
                    else:
                        self.pad8.stop()
                        self.play8 = not self.play8
                        Pad(self.screen, self.gpad0, 3, 2)
                if event.key == pg.K_z:
                    if self.play9:
                        self.pad9.play(loops=-1)
                        self.play9 = not self.play9
                        Pad(self.screen, self.gspad1, 0, 3)
                    else:
                        self.pad9.stop()
                        self.play9 = not self.play9
                        Pad(self.screen, self.gspad0, 0, 3)
                if event.key == pg.K_x:
                    if self.play10:
                        self.pad10.play(loops=-1)
                        self.play10 = not self.play10
                        Pad(self.screen, self.apad1, 1, 3)
                    else:
                        self.pad10.stop()
                        self.play10 = not self.play10
                        Pad(self.screen, self.apad0, 1, 3)
                if event.key == pg.K_c:
                    if self.play11:
                        self.pad11.play(loops=-1)
                        self.play11 = not self.play11
                        Pad(self.screen, self.aspad1, 2, 3)
                    else:
                        self.pad11.stop()
                        self.play11 = not self.play11
                        Pad(self.screen, self.aspad0, 2, 3)
                if event.key == pg.K_v:
                    if self.play12:
                        self.pad12.play(loops=-1)
                        self.play12 = not self.play12
                        Pad(self.screen, self.bpad1, 3, 3)
                    else:
                        self.pad12.stop()
                        self.play12 = not self.play12
                        Pad(self.screen, self.bpad0, 3, 3)
                if event.key == pg.K_KP_PLUS:
                    if self.main_volume > 1.0:
                        self.vol = self.main_volume * 10 - 1
                        self.main_volume = 1.0
                        self.update_volume()
                        if self.vol <= 0:
                            SPad(self.screen, self.volume[0], 4.0, 0)
                        else:
                            SPad(self.screen, self.volume[int(self.vol)], 4.0, 0)
                    else:
                        self.vol = self.main_volume * 10 - 1
                        self.main_volume += 0.1
                        self.update_volume()
                        if self.vol > 10:
                            SPad(self.screen, self.volume[9], 4.0, 0)
                        else:
                            if self.vol > 9:
                                self.vol = 9
                            SPad(self.screen, self.volume[int(self.vol)], 4.0, 0)
                    if self.debug:
                        #print(self.main_volume)
                        print(self.vol)
                if event.key == pg.K_KP_MINUS:
                    if self.vol < 0:
                            self.vol = 0
                    if self.main_volume <= 0.0:
                        self.main_volume = 0
                        self.vol = self.main_volume * 10 - 1
                        self.update_volume()
                        if self.vol <= 0:
                            SPad(self.screen, self.volume[0], 4.0, 0)
                        else:
                            SPad(self.screen, self.volume[int(self.vol)], 4.0, 0)
                    else:
                        self.main_volume -= 0.1
                        self.vol = self.main_volume * 10 - 1
                        self.update_volume()
                        if self.vol <= 0:
                            SPad(self.screen, self.volume[0], 4.0, 0)
                        else:
                            SPad(self.screen, self.volume[int(self.vol)], 4.0, 0)
                    if self.debug:
                        #print(self.main_volume)
                        print(self.vol)

            
    def quit(self):
        pg.mixer.quit()
        pg.quit()
        exit()
