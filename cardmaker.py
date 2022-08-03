import pygame
import time
import sys, os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from threading import Thread

def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		absolute_path = os.path.join(sys._MEIPASS, relative)
	else:
		absolute_path = os.path.join(relative)
	return absolute_path

card_cost_1 = 0
card_cost_2 = 0
card_level = 0
issave = 0
rare = 'N'
cardname = ''
classes = '場地'
istouming = 0
def datawindow():
    global card_cost_1,card_cost_2,card_level,cardname,classes,rare,cardrule,istouming
    root= Tk()
    root.iconbitmap(resource_path('icon/icon.ico'))
    root.title('Card Maker')
    root.geometry('252x352')

    com1 = ttk.Combobox(root, textvariable=StringVar() ,width=3)
    com1.pack()
    com1['value'] = ([str(i)for i in range(10)])
    com1.current(0)
    com2 = ttk.Combobox(root, textvariable=StringVar() ,width=3)
    com2.pack()
    com2['value'] = ([str(i)for i in range(10)])
    com2.current(0)
    com3 = ttk.Combobox(root, textvariable=StringVar() ,width=3)
    com3.pack()
    com3['value'] = ([str(i)for i in range(10)])
    com3.current(0)
    com4 = ttk.Combobox(root, textvariable=StringVar() ,width=10)
    com4.pack()
    com4['value'] = (['場地','结界','法術','瞬發','道具','陷阱','生物--種類'])
    com4.current(0)
    com5 = ttk.Combobox(root, textvariable=StringVar() ,width=4)
    com5.pack()
    com5['value'] = (['N','R','SR','SSR','UR','IE'])
    com5.current(0)
    def card_cost_1_func(eve):
        global card_cost_1
        card_cost_1 = com1.get()
    def card_cost_2_func(eve):
        global card_cost_2
        card_cost_2 = com2.get()
    def card_level_func(eve):
        global card_level
        card_level = com3.get()
    def rarity(eve):
        global rare
        rare = com5.get()
    CLASS=StringVar()
    classinput = Entry(root,width=10,textvariable=CLASS)
    classinput.pack()
    def cget():
        global classes
        while True:
            time.sleep(0.1)
            if '生物--' in classes:
                classes = '生物--' + classinput.get()
    def card_class(eve):
        global classes
        if com4.get() == '生物--種類':
            classes = '生物--'
        else:
            classes = com4.get()
    com1.bind('<<ComboboxSelected>>', card_cost_1_func)
    com2.bind('<<ComboboxSelected>>', card_cost_2_func)
    com3.bind('<<ComboboxSelected>>', card_level_func)
    com4.bind('<<ComboboxSelected>>', card_class)
    com5.bind('<<ComboboxSelected>>', rarity)
    def savecard():
        global issave
        issave = 1
    def istm():
        global istouming
        if istouming == 0:
            istouming = 1
        else:
            istouming = 0
    save_card = ttk.Button(root, text='Save card', command=savecard)
    save_card.pack()

    nametext = ttk.Label(root,text='Input card name')
    nametext.pack()
    ruletext = ttk.Label(root,text='Input card effect')
    ruletext.pack()
    cost2 = ttk.Label(root,text='cost2:')
    cost2.pack()
    cost1 = ttk.Label(root,text='cost1:')
    cost1.pack()
    level = ttk.Label(root,text='Level:')
    level.pack()
    NAME=StringVar()
    nameinput = Entry(root,width=16,textvariable=NAME)
    nameinput.pack()
    RULE=StringVar()
    ruleinput = Entry(root,width=30,textvariable=RULE)
    ruleinput.pack()
    def getname():
        global cardname
        while True:
            time.sleep(0.1)
            cardname = nameinput.get()
    def getrule():
        global cardrule
        while True:
            time.sleep(0.1)
            cardrule = ruleinput.get()
    save_card.place(x=80,y=200)
    cost2.place(x=150,y=20)
    cost1.place(x=150,y=60)
    level.place(x=150,y=100)
    com1.place(x=200,y=20)
    com2.place(x=200,y=60)
    com3.place(x=200,y=100)
    com4.place(x=0,y=100)
    com5.place(x=0,y=60)
    nametext.place(x=0,y=0)
    nameinput.place(x=0,y=20)
    ruletext.place(x=0,y=120)
    ruleinput.place(x=0,y=140)
    classinput.place(x=100,y=100)
    def sefi():
        global Filepath,isimg
        root2 = Tk()
        root2.withdraw()
        Filepath = filedialog.askopenfilename()
        isimg = 1

    def thsc():
        global card_cost_1,card_cost_2,card_level,cardname,classes,rare,cardrule
        root2 = Tk()
        root2.withdraw()
        thscpath = filedialog.askopenfilename()
        l=[]
        with open (thscpath,encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip('\n')
                l.append(line)

        cardname=l[0]
        card_cost_1=l[1]
        card_cost_2=l[2]
        card_level=l[3]
        classes=l[4]
        rare=l[5]
        cardrule=l[6]
        NAME.set(l[0])
        RULE.set(l[6])
        if '生物--' in classes:
            CLASS.set(l[4][4:])

    x = ttk.Button(root, text='Select image', command=sefi)
    x.pack()
    x.place(x=80,y=230)

    tm = ttk.Button(root, text='Transparent bg', command=istm)
    tm.pack()
    tm.place(x=80,y=260)

    tm = ttk.Button(root, text='import thsc', command=thsc)
    tm.pack()
    tm.place(x=80,y=290)

    thread3 = Thread(target=getname)
    thread3.setDaemon(True)
    thread3.start()
    thread4 = Thread(target=getrule)
    thread4.setDaemon(True)
    thread4.start()
    thread5 = Thread(target=cget)
    thread5.setDaemon(True)
    thread5.start()
    root.mainloop()

def cardwindow():
    global card_cost_1,card_cost_2,card_level,cardname,issave,classes,rare,cardrule,Filepath,isimg,istouming
    pygame.init()
    pygame.display.set_icon(pygame.image.load(resource_path('icon/icon.png')))
    x=504
    y=704
    screen = pygame.display.set_mode((x,y))
    pygame.display.set_caption('Card maker')
    card_cost1_img = pygame.image.load('assets/frame_sets/card_cost1.png').convert()
    card_cost1_img.set_colorkey((0,0,0))
    card_cost2_img = pygame.image.load('assets/frame_sets/card_cost2.png').convert()
    card_cost2_img.set_colorkey((0,0,0))
    card_level_img = pygame.image.load('assets/frame_sets/card_level.png').convert()
    card_level_img.set_colorkey((0,0,0))
    card_bg = pygame.image.load('assets/frame_sets/card_bg.png').convert()
    card_bg.set_colorkey((0,0,0))
    trans_crad_bg = pygame.image.load('assets/frame_sets/card_bg.png').convert()
    trans_crad_bg.set_colorkey((0,0,0))
    trans_crad_bg.set_alpha(100)
    pygame.font.init()
    card_font='assets/fonts/wenyue.ttf'
    clock = pygame.time.Clock()
    imgx = 0
    imgy = 0
    isimg = 0
    cardimg = 0
    cardrule = ''
    classes = ''
    k=1
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            imgx += 1
        if keys[pygame.K_LEFT]:
            imgx -= 1
        if keys[pygame.K_UP]:
            imgy -= 1
        if keys[pygame.K_DOWN]:
            imgy += 1

        screen.fill((0,0,0))
        i=rare
        if i=='UR':
            colo=(205,0,0)
        elif i=='SSR':
            colo=(255,127,0)
        elif i=='SR':
            colo=(148,0,211)
        elif i=='R':
            colo=(144,238,144)
        elif i=='N':
            colo=(0,0,0)
        else:
            colo=(255,255,255)

        if isimg == 1:
            isimg = 0
            k = 1
            cardimg = pygame.image.load(Filepath).convert()
        if cardimg != 0:
            cwidth = cardimg.get_rect()[2]
            cheight = cardimg.get_rect()[3]
            if keys[pygame.K_w]:
                if k <= 2.01:
                    k += 0.01
                    cardimgc = pygame.transform.smoothscale(cardimg,(int(cwidth*k),int(cheight*k)))
            if keys[pygame.K_s]:
                if k >= 0.11:
                    k -= 0.01
                    cardimgc = pygame.transform.smoothscale(cardimg,(int(cwidth*k),int(cheight*k)))
            if k != 1:
                screen.blit(cardimgc,(imgx,imgy))
            if k == 1:
                screen.blit(cardimg,(imgx,imgy))

        if istouming == 0:
            screen.blit(card_bg,(0,0))
            colorw = (255,255,255)
        else:
            screen.blit(trans_crad_bg,(0,0))
            colorw = (0,0,0)
        fo=pygame.font.Font(card_font,30)
        text=fo.render(cardname,True,colo)
        screen.blit(text,(40,40))
        fo=pygame.font.Font(card_font,24)

        if '//' not in cardrule:
            text=fo.render(cardrule,True,colorw)
            screen.blit(text,(50,400))
        else:
            cdr = cardrule
            lines = -1
            while True:
                lines += 1
                text=fo.render(cdr[:cdr.find('//')],True,colorw)
                screen.blit(text,(50,400+24*lines))
                cdr = cdr[cdr.find('//')+2:]
                if '//' not in cdr:
                    lines += 1
                    text=fo.render(cdr,True,colorw)
                    screen.blit(text,(50,400+24*lines))
                    break

        text=fo.render(classes,True,colo)
        screen.blit(text,(50,368))
        num = 0
        for i in range(int(card_cost_2)):
            screen.blit(card_cost1_img,(x-68-num*36,40))
            num += 1
        for i in range(int(card_cost_1)):
            screen.blit(card_cost2_img,(x-68-num*36,40))
            num += 1
        if int(card_level) == 0 and (int(card_cost_2) !=0 or int(card_cost_1) != 0):
            pass
        else:
            screen.blit(card_level_img,(x-68-num*36,40))
            fo=pygame.font.Font(card_font,30)
            text=fo.render(str(card_level),True,(0,0,0))
            screen.blit(text,(x-60-num*36,40))

        pygame.display.update()
        if issave == 1:
            issave = 0
            # img_cv2=cv2.cvtColor(numpy.asarray(screen),cv2.COLOR_RGB2BGR)
            # for save cards
            pygame.image.save(screen,'./output/images/'+cardname+'.png')
            with open('./output/thsc/'+cardname+'.thsc','w',encoding="utf-8") as f:
                f.write(str(cardname)+'\n')
                f.write(str(card_cost_1)+'\n')
                f.write(str(card_cost_2)+'\n')
                f.write(str(card_level)+'\n')
                f.write(str(classes)+'\n')
                f.write(str(rare)+'\n')
                f.write(str(cardrule))

if __name__ == '__main__':
    thread1 = Thread(target=datawindow)
    thread2 = Thread(target=cardwindow)
    threads =[thread1,thread2]
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
