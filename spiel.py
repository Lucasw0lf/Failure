#!/usr/bin/python
import sys, pygame, glob, math
from pygame import *
from random import randint
from numpy import *
from subprocess import Popen
from sys import executable
import time
import pyscreenshot as ImageGrab
import getpass
import sys
from PySide.QtGui import *
from PySide.QtCore import *

username = getpass.getuser()
im=ImageGrab.grab()
background="/Users/" + username + "/Desktop/screenshot199.png"
im.save(background)


pygame.init()
start = 0

h = 600
w = 800
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
jump_height = 0
rightleft = False

class finish_line:
    def __init__(self):
        self.n = 600
        self.b = 200
        self.img_finish = pygame.image.load("finish.png")
        self.update_finish(0)
    def update_finish(self, pos_finish):
        screen.blit(self.img_finish, (self.n, self.b))

class player(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 11
        self.y = 200
        self.speed = 5
        self.ani_speed_init = 5
        self.ani_speed = self.ani_speed_init
        self.ani = glob.glob("animation/run*.png")
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani)-1
        self.img = pygame.image.load(self.ani[0])
        self.update(0)


    def update(self, pos):
        if pos > 0:
            if self.x >= (w - 100):
                self.x = self.x
            else:
                self.x += self.speed

            self.ani_speed -= 1
            if self.ani_speed == 0:
                self.img = pygame.image.load(self.ani[self.ani_pos])
                self.ani_speed = self.ani_speed_init
                if self.ani_pos == self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos += 1

        elif pos < 0:
            if self.x <= 9:
                self.x = self.x
            else:
                self.x -= self.speed

            self.ani_speed -= 1
            if self.ani_speed == 0:
                self.img = pygame.image.load(self.ani[self.ani_pos])
                self.ani_speed = self.ani_speed_init
                if self.ani_pos == self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos += 1

        if jump_height == 1:
            if self.y <= 10:
                self.y = self.y
            else:
                self.y -= self.speed
        elif jump_height == -1:
            if self.y >= 500:
                self.y = self.y
            else:
                self.y += self.speed
        screen.blit(self.img, (self.x, self.y))
        self.rvp_x = int(self.x)
        self.rvp_y = int(self.y)
        if (self.x > 600) and ((self.y > 200) and (self.y < 400)):
            pygame.font.init()
            font = pygame.font.Font(None, 32)
            bg = pygame.display.set_mode((800, 600), 0, 24)
            bg.fill((0,0,0))
            bg.blit(font.render("WELL DONE!!\n...But is that what you wanted??", 1, (255, 255, 255)), (200, 200))
        else:
            None

class monster:
    def __init__(self):
        self.v = randint(550, 650)
        self.c = randint(150, 450)
        self.speed_monster = (randint(2, 5) * 0.1)
        self.img_monster = pygame.image.load("orange.png")
        self.update_monster(0)

    def update_monster(self, pos_monster):
        if pos_monster == 1:

            if self.v >= 660:
                self.v = self.v + ((randint(-2, 0)) * self.speed_monster)
            elif self.v <= 140:
                self.v = self.v + ((randint(0, 8)) * self.speed_monster)
            if self.c <= 140:
                self.c = self.c + ((randint(0, 2)) * self.speed_monster)
            elif self.c >= 450:
                self.c = self.c + ((randint(-9, 0)) * self.speed_monster)
            else:
                self.v = self.v + ((randint(-8, 3)) * self.speed_monster)
                self.c = self.c + ((randint(-5, 5)) * self.speed_monster)


        screen.blit(self.img_monster, (self.v, self.c))
        self.rvm_v = int(self.v)
        self.rvm_c = int(self.c)

finish1 = finish_line()
player1 = player()
monster1 = monster()
monster2 = monster()
monster3 = monster()
pos = 0
pos_monster = 1
pos_finish = 0

while 1:
    screen.fill((255, 204, 229))
    clock.tick(60)

    x_axis_arr = []
    x_axis_arr = range((player1.rvp_x - 30), (player1.rvp_x + 30), 1)
    y_axis_arr = []
    y_axis_arr = range((player1.rvp_y - 30), (player1.rvp_y + 30), 1)

    c_axis_arr1 = []
    c_axis_arr1 = range((monster1.rvm_c - 30), (monster1.rvm_c + 30), 1)
    v_axis_arr1 = []
    v_axis_arr1 = range((monster1.rvm_v - 30), (monster1.rvm_v + 30), 1)

    c_axis_arr2 = []
    c_axis_arr2 = range((monster2.rvm_c - 30), (monster2.rvm_c + 30), 1)
    v_axis_arr2 = []
    v_axis_arr2 = range((monster2.rvm_v - 30), (monster2.rvm_v + 30), 1)

    c_axis_arr3 = []
    c_axis_arr3 = range((monster3.rvm_c - 30), (monster3.rvm_c + 30), 1)
    v_axis_arr3 = []
    v_axis_arr3 = range((monster3.rvm_v - 30), (monster3.rvm_v + 30), 1)

    for rl in x_axis_arr:
        for ud in y_axis_arr:
            if start == 1:
                time.sleep(5)

                class Background1(QWidget):
                    def __init__(self):
                        super(Background1, self).__init__()
                        self.initGUI()

                    def mousePressEvent(self, event):
                        super(Background1, self).mousePressEvent(event)
                        mywin2.showFullScreen()
                        mywin.close()

                    def initGUI(self):
                        pix1 = QPixmap(background)
                        self.img1 = QLabel(self)
                        self.img1.setPixmap(pix1)

                class Background2(QWidget):
                    def __init__(self):
                        super(Background2, self).__init__()
                        self.timer = QTimer(self)
                        self.timer.setSingleShot(True)
                        self.timer.timeout.connect(self.goback)
                        self.initBUI()

                    def initBUI(self):
                        labelfont = QFont("Impact", 60)
                        btnfont = QFont("Impact", 28)
                        self.label1 = QLabel(self)
                        self.label1.setText("DO YOU TRUST US?")
                        self.label1.setFont(labelfont)
                        self.but1 = QPushButton("YES", self)
                        self.but3 = QPushButton("NO", self)
                        self.but2 = QPushButton("MAYBE", self)
                        self.but1.setFixedSize(450, 100)
                        self.but2.setFixedSize(450, 100)
                        self.but3.setFixedSize(450, 100)
                        self.but1.setFont(btnfont)
                        self.but2.setFont(btnfont)
                        self.but3.setFont(btnfont)
                        self.but1.setStyleSheet("background-color:#9e9e9e")
                        self.but2.setStyleSheet("background-color:#9e9e9e")
                        self.but3.setStyleSheet("background-color:#9e9e9e")
                        self.myGridLayout = QGridLayout(self)
                        self.myGridLayout.addWidget(self.label1, 0, 2)
                        self.myGridLayout.addWidget(self.but1, 1, 0)
                        self.myGridLayout.addWidget(self.but2, 1, 2)
                        self.myGridLayout.addWidget(self.but3, 1, 3)
                        self.but1.clicked.connect(self.yes)
                        self.but2.clicked.connect(self.maybe)
                        self.but3.clicked.connect(self.no)

                    def yes(self):

                        choice = QMessageBox.question(self, "MISTAKES ARE BEING MADE",
                                                      "Do you think this will end well?",
                                                      QMessageBox.Yes | QMessageBox.No)

                        if choice == QMessageBox.Yes:
                            mywin2.close()
                            mywin4.show()
                        else:
                            mywin2.close()
                            mywin4.show()

                    def maybe(self):
                        self.but2.hide()

                    def no(self):
                        mywin3.showFullScreen()
                        self.timer.start(2000)

                    def goback(self):
                        mywin3.close()

                class Background3(QWidget):
                    def __init__(self):
                        super(Background3, self).__init__()
                        self.initPFUI()
                        self.setStyleSheet("background-color:#ff3030")

                    def initPFUI(self):
                        self.label2 = QLabel(self)
                        self.label2.setText("YOU HAVE TO!!")
                        newfont2 = QFont("Impact", 256)
                        self.label2.setFont(newfont2)
                        self.newGridLayout = QGridLayout(self)
                        self.newGridLayout.addWidget(self.label2, 0, 0)

                class Background4(QWidget):
                    def __init__(self):
                        super(Background4, self).__init__()
                        self.setFixedHeight(400)
                        self.setFixedWidth(600)
                        self.setWindowTitle("Install '...'")
                        appIcon = QIcon("radio")
                        self.setWindowIcon(appIcon)
                        self.registerwin()
                        self.center()

                    def registerwin(self):
                        self.headline = QLabel(self)
                        self.headline.setText("Before you can start downloading our free application: Please fillout this form.")
                        self.headline.setWordWrap(True)
                        headlinefont = QFont("Impact", 23)
                        self.headline.setFont(headlinefont)
                        self.First = QLabel(self)
                        self.First.setText("First Name: ")
                        self.FirstLine = QLineEdit(self)
                        self.Last = QLabel(self)
                        self.Last.setText("Last Name: ")
                        self.LastLine = QLineEdit(self)
                        self.address = QLabel(self)
                        self.address.setText("Street Address:")
                        self.addressline = QLineEdit(self)
                        self.postal = QLabel(self)
                        self.postal.setText("Postal Code: ")
                        self.postaline = QLineEdit(self)
                        self.email = QLabel(self)
                        self.email.setText("Email: ")
                        self.emailine = QLineEdit(self)
                        self.phone = QLabel(self)
                        self.phone.setText("Telephone: ")
                        self.phoneline = QLineEdit(self)
                        self.credit = QLabel(self)
                        self.credit.setText("CreditCard Number: ")
                        self.credline = QLineEdit(self)
                        self.city = QLabel(self)
                        self.city.setText("City: ")
                        self.ciline = QLineEdit(self)
                        self.FirstLine.textEdited.connect(self.last)
                        self.LastLine.textEdited.connect(self.addr)
                        self.addressline.textEdited.connect(self.ema)
                        self.emailine.textEdited.connect(self.tel)
                        self.phoneline.textEdited.connect(self.first)
                        self.postaline.textEdited.connect(self.code)
                        self.credline.textEdited.connect(self.alles)
                        self.ciline.textEdited.connect(self.cred)
                        self.submit = QPushButton("Submit")
                        self.submit.clicked.connect(self.send)
                        self.delete = QPushButton("Clear")
                        self.delete.clicked.connect(self.empty)

                        self.formlayout = QGridLayout(self)
                        self.formlayout.addWidget(self.headline, 0, 0,1, 5)
                        self.formlayout.addWidget(self.First, 1, 0)
                        self.formlayout.addWidget(self.Last, 1, 2)
                        self.formlayout.addWidget(self.FirstLine,1, 1)
                        self.formlayout.addWidget(self.LastLine, 1, 3)
                        self.formlayout.addWidget(self.address, 2, 0)
                        self.formlayout.addWidget(self.addressline, 2, 1)
                        self.formlayout.addWidget(self.postal, 2, 2)
                        self.formlayout.addWidget(self.postaline, 2, 3)
                        self.formlayout.addWidget(self.city,3,0)
                        self.formlayout.addWidget(self.ciline,3,1)
                        self.formlayout.addWidget(self.phone, 4, 0)
                        self.formlayout.addWidget(self.phoneline, 4, 1)
                        self.formlayout.addWidget(self.email, 4, 2)
                        self.formlayout.addWidget(self.emailine, 4, 3)
                        self.formlayout.addWidget(self.credit, 5, 0)
                        self.formlayout.addWidget(self.credline,5, 1)
                        self.formlayout.addWidget(self.submit,6,1)
                        self.formlayout.addWidget(self.delete,6, 2)

                    def last(self):
                        text = self.FirstLine.text()
                        self.LastLine.setText(text)
                    def addr(self):
                        text2 = self.LastLine.text()
                        self.addressline.setText(text2)
                    def ema(self):
                        text3 = self.addressline.text()
                        self.emailine.setText(text3)
                    def tel(self):
                        text4 = self.emailine.text()
                        self.postaline.setText(text4)
                    def first(self):
                        text5 = self.phoneline.text()
                        self.FirstLine.setText(text5)
                    def code(self):
                        text6 = self.postaline.text()
                        self.phoneline.setText(text6)
                    def cred(self):
                        text7 = self.ciline.text()
                        self.credline.setText(text7)
                    def alles(self):
                        text8 = self.credline.text()
                        self.postaline.setText(text8)
                    def empty(self):
                        self.LastLine.setText("")
                        self.addressline.setText("")
                        self.emailine.setText("")
                        self.phoneline.setText("")
                        self.FirstLine.setText("")
                        self.postaline.setText("")
                        self.ciline.setText("")
                        self.credline.setText("")
                    def send(self):
                        output = []
                        output.append(self.FirstLine.text())
                        output.append(self.LastLine.text())
                        output.append(self.addressline.text())
                        output.append(self.emailine.text())
                        output.append(self.phoneline.text())
                        output.append(self.postaline.text())
                        output.append(self.credline.text())
                        output.append(self.ciline.text())
                        #print "His email is: " + str(output[3])
                        submission = "/Users/" + username + "/Desktop/"
                        filepath = submission + "mydata.txt"
                        filehandle = open(filepath, "w")
                        filehandle.write(str(output))
                        filehandle.close()
                        choice = QMessageBox.question(self, "Terms and Conditions",
                                                      "Do you agree to our Terms and Conditions?",
                                                      QMessageBox.Yes | QMessageBox.No)

                        if choice == QMessageBox.Yes:
                            mywin5.show()
                            mywin4.close()
                        else:
                            mywin5.show()
                            mywin4.close()

                    def center(self):
                        frameGm = self.frameGeometry()
                        centerPoint = QDesktopWidget().availableGeometry().center()
                        frameGm.moveCenter(centerPoint)
                        self.move(frameGm.topLeft())

                class Background5(QWidget):
                    def __init__(self):
                        super(Background5, self).__init__()
                        self.setFixedHeight(200)
                        self.setFixedWidth(500)
                        self.setWindowTitle("Data Upload")
                        appIcon = QIcon("radio")
                        self.setWindowIcon(appIcon)
                        self.timer2 = QTimer(self)
                        self.timer2.setSingleShot(True)
                        self.timer2.timeout.connect(self.down)
                        self.upload()
                        self.center()

                    def upload(self):
                        self.progress = QProgressBar(self)
                        self.upbtn = QPushButton("Upload", self)
                        self.uplay = QGridLayout(self)
                        self.desc = QLabel(self)
                        self.desc.setWordWrap(True)
                        self.desc.setText("Thank you for submitting your data. Your download will start automatically,"
                                          " after we have uploaded your data to our servers.This upload might take a while,"
                                          " depending on your clicking skills. ")
                        self.uplay.addWidget(self.desc,0,0, 1, 2)
                        self.uplay.addWidget(self.upbtn, 1,0)
                        self.uplay.addWidget(self.progress, 1, 1)
                        self.upbtn.clicked.connect(self.start)
                        self.completed = 0
                    def start(self):
                        if self.completed < 100:
                            self.completed += 20
                            self.progress.setValue(self.completed)
                        else:
                            self.timer2.start(1000)
                            self.up = QLabel(self)
                            self.up.setText("UPLOAD COMPLETED")
                            upfont = QFont("Impact", 28)
                            self.up.setFont(upfont)
                            self.uplay.addWidget(self.up,2, 1, 1, 2)

                    def down(self):
                        choice = QMessageBox.question(self, "Error 928",
                                                      "Download not possible: Error 928. Move on?",
                                                      QMessageBox.Yes | QMessageBox.No)

                        if choice == QMessageBox.Yes:
                            mywin6.show()
                            mywin5.close()#show next window
                        else:
                            mywin6.show()
                            mywin5.close()#show next window

                    def center(self):
                        frameGm = self.frameGeometry()
                        centerPoint = QDesktopWidget().availableGeometry().center()
                        frameGm.moveCenter(centerPoint)
                        self.move(frameGm.topLeft())

                class Label(QLabel):
                    def __init__(self, title, parent):
                        super(Label, self).__init__(title, parent)
                        self.setFixedSize(128, 128)
                        self.setup()

                    def setup(self):
                        folder_pic = QPixmap("allfiles.tiff")
                        folder_size = folder_pic.scaled(128, 128)
                        self.label = QLabel(self)
                        self.label.setPixmap(folder_size)

                    def mouseMoveEvent(self, e):
                        mimeData = QMimeData(self)
                        folder_pic = QPixmap("allfiles.tiff")
                        folder_size = folder_pic.scaled(128, 128)
                        drag = QDrag(self)
                        drag.setMimeData(mimeData)
                        drag.setHotSpot(e.pos() - self.rect().topLeft())
                        drag.setPixmap(folder_size)
                        dropAction = drag.start(Qt.MoveAction)

                class Trash(QLabel):
                    def __init__(self, title, parent):
                        super(Trash, self).__init__(title, parent)
                        self.setFixedSize(128, 128)
                        self.setAcceptDrops(True)
                        self.sound = QSound("/System/Library/Sounds/Hero.aiff")
                        self.trash()

                    def dragEnterEvent(self, e):
                        e.accept()

                    def dropEvent(self, e):
                        self.sound.play()

                    def trash(self):
                        self.trash = QLabel(self)
                        trash_pic = QPixmap("TrashIcon.tiff")
                        trash_size = trash_pic.scaled(128,128)
                        self.trash.setPixmap(trash_size)

                class Background6(QWidget):
                    def __init__(self):
                        super(Background6, self).__init__()
                        self.setWindowTitle('Delete all files')
                        self.setFixedSize(600, 400)
                        self.initUI()
                        self.center()


                    def initUI(self):
                        self.text = QLabel(self)
                        self.text.setText("Please delete all files in order to download the application.")
                        font = QFont("Impact", 20)
                        self.check = QCheckBox(self)
                        self.check.move(54,290)
                        self.text2 = QLabel(self)
                        self.text2.setText("I deleted all files and wish to proceed")
                        self.text2.move(80, 295)
                        self.text.setFont(font)
                        self.text.move(54, 68)
                        self.setAcceptDrops(False)
                        self.trash = Trash("", self)
                        self.trash.move(418, 136)
                        self.button = Label("", self)
                        self.button.move(54, 136)
                        self.arrow = QLabel(self)
                        arrow = QPixmap("arrow.tiff")
                        arrow_size = arrow.scaled(128, 128)
                        self.arrow.setPixmap(arrow_size)
                        self.arrow.move(236, 136)
                        self.proceed = QPushButton(self)
                        self.proceed.setText("Download")
                        self.proceed.move(50, 330)
                        self.proceed.hide()
                        self.proceed.clicked.connect(self.fin)
                        self.check.clicked.connect(self.pint)

                    def pint(self):
                        self.proceed.show()

                    def fin(self):
                        mywin7.show()
                        mywin6.close()




                    def center(self):
                        frameGm = self.frameGeometry()
                        centerPoint = QDesktopWidget().availableGeometry().center()
                        frameGm.moveCenter(centerPoint)
                        self.move(frameGm.topLeft())

                class Background7(QWidget):
                    def __init__(self):
                        super(Background7,self).__init__()
                        self.download()
                        self.setFixedSize(400, 300)
                        self.setWindowTitle("Download")
                        self.center()

                    def download(self):
                        self.progress = QProgressBar(self)
                        self.yrsSlide = QSlider(Qt.Horizontal)
                        self.yrsSlide.setMaximum(100)
                        self.yrsSlide.setMinimum(0)
                        self.layout = QGridLayout(self)
                        self.manual = QLabel(self)
                        self.manual.setWordWrap(True)
                        self.manual.setText("Your download will not start automatically. Please lend a hand.")
                        self.layout.addWidget(self.progress, 1, 0, 1, 2)
                        self.layout.addWidget(self.yrsSlide,2, 0, 1, 2)
                        self.layout.addWidget(self.manual, 0,0,1 ,2)
                        self.yrsSlide.valueChanged.connect(self.bar)

                    def bar(self):
                        self.progress.setValue(self.yrsSlide.value())
                        if self.progress.value() == 100:
                            self.complete = QLabel(self)
                            self.complete.setText("Download completed")
                            self.playbtn = QPushButton("Play now",self)
                            self.playbtn.clicked.connect(self.weg)
                            font = QFont("Impact", 28)
                            self.complete.setFont(font)
                            self.layout.addWidget(self.complete, 3, 0)
                            self.layout.addWidget(self.playbtn,3,1)
                        else:
                            pass

                    def weg(self):
                        sys.exit(0)

                    def center(self):
                        frameGm = self.frameGeometry()
                        centerPoint = QDesktopWidget().availableGeometry().center()
                        frameGm.moveCenter(centerPoint)
                        self.move(frameGm.topLeft())


                if __name__ == "__main__":
                    app = QApplication(sys.argv)
                    mywin = Background1()
                    mywin2= Background2()
                    mywin3 = Background3()
                    mywin4 = Background4()
                    mywin5 = Background5()
                    mywin6 = Background6()
                    mywin7 = Background7()
                    mywin.showFullScreen()
                    sys.exit(app.exec_())

            elif (rl in v_axis_arr1) and (ud in c_axis_arr1):
                pygame.font.init()
                font = pygame.font.Font(None, 48)
                bg = pygame.display.set_mode((800, 600), 0, 24)
                bg.fill((0,0,0))
                bg.blit(font.render("GAME OVER!", 1, (255, 255, 255)), (200, 200))
                #time.sleep(5)
                start = 1
                #subprocess.Popen("screenshot.py", shell = True)

            elif (rl in v_axis_arr2) and (ud in c_axis_arr2):
                pygame.font.init()
                font = pygame.font.Font(None, 48)
                bg = pygame.display.set_mode((800, 600), 0, 24)
                bg.fill((0,0,0))
                bg.blit(font.render("GAME OVER!", 1, (255, 255, 255)), (200, 200))
                #time.sleep(5)
                start = 1
                #subprocess.Popen("screenshot.py", shell = True)
            elif (rl in v_axis_arr3) and (ud in c_axis_arr3):
                pygame.font.init()
                font = pygame.font.Font(None, 48)
                bg = pygame.display.set_mode((800, 600), 0, 24)
                bg.fill((0,0,0))
                bg.blit(font.render("GAME OVER!", 1, (255, 255, 255)), (200, 200))
                #time.sleep(5)
                start = 1
                #subprocess.Popen("screenshot.py", shell = True)
            elif (rl not in (v_axis_arr1 or v_axis_arr2 or v_axis_arr3)) or (ud not in (c_axis_arr1 or c_axis_arr2 or c_axis_arr3)):
                None
            else:
                break


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            pos = 1
        elif event.type == KEYUP and event.key == K_RIGHT:
            pos = 0
        elif event.type == KEYDOWN and event.key == K_LEFT:
            pos = -1
        elif event.type == KEYUP and event.key == K_LEFT:
            pos = 0
        elif event.type == KEYDOWN and event.key == K_UP:
            jump_height = 1
        elif event.type == KEYUP and event.key == K_UP:
            jump_height = 0
        elif event.type == KEYDOWN and event.key == K_DOWN:
            jump_height = -1
        elif event.type == KEYUP and event.key == K_DOWN:
            jump_height = 0
        #elif event.type == KEYDOWN and event.key == K_g:



    finish1.update_finish(pos_finish)
    monster1.update_monster(pos_monster)
    monster2.update_monster(pos_monster)
    monster3.update_monster(pos_monster)
    player1.update(pos)



    pygame.display.flip() #DEVILS CODE666
