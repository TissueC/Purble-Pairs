from graphics import*
from button import*
from time import sleep
from random import shuffle
from animation import*
from images import*
from threading import*
from record import*
import winsound,sys

class game:
    def __init__(self):
        self.win=GraphWin("Memory Challenge",600,600)
        self.win.setCoords(0,0,120,120)

    def startmusic(self):
        mp3 = 'bgm\\startbgm.wav'
        if len(sys.argv) < 2:
            times = 1
        else:
            times = int(sys.argv[1])
        if times == 0:
            while 1:
                winsound.PlaySound(mp3, winsound.SND_NODEFAULT)
        else:  
            for i in range(times):
                winsound.PlaySound(mp3, winsound.SND_NODEFAULT)
    def gamemusic(self):
        while (not self.musicLOCK) and self.win.isOpen():
            mp3 = 'bgm\\gamebgm.wav'
            if len(sys.argv) < 2:
                times = 1
            else:
                times = int(sys.argv[1])
            if times == 0:
                while 1:
                    winsound.PlaySound(mp3, winsound.SND_NODEFAULT)
            else:  
                for i in range(times):
                    winsound.PlaySound(mp3, winsound.SND_NODEFAULT)
    def stars1(self):
        self.animation1.pengpeng(self.win,"star",Point(20,70),20,"red",1,0,300)       
    def stars2(self):
        self.animation1.pengpeng(self.win,"star",Point(100,40),10,"brown",-1,0,300)
    def stars3(self):
        self.animation1.pengpeng(self.win,"star",Point(20,40),10,"yellow",1,0,300)       
    def stars4(self):
        self.animation1.pengpeng(self.win,"star",Point(100,70),20,"blue",-1,0,300)
    def stars5(self):
        self.animation1.pengpeng(self.win,"star",Point(20,20),5,"pink",1,0,300)       
    def stars6(self):
        self.animation1.pengpeng(self.win,"star",Point(100,20),5,"orange",-1,0,300)

    def stars(self):
        self.animation1=animation()
        t1=Thread(target=self.stars1,args=())
        t2=Thread(target=self.stars2,args=())
        t3=Thread(target=self.stars3,args=())
        t4=Thread(target=self.stars4,args=())
        t5=Thread(target=self.stars5,args=())
        t6=Thread(target=self.stars6,args=())
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        
    def init_interface(self):
        startmusic=Thread(target=self.startmusic,args=())
        startmusic.start()
        self.stars()
        self.win.setBackground("lightblue")
        self.welcomeText=Text(Point(60,110),"Welcome To Memory Challenge")
        self.welcomeText.setSize(30)
        self.welcomeText.draw(self.win)

        self.nameText=Text(Point(60,100),"By Sun Hao")
        self.nameText.setSize(25)
        self.nameText.draw(self.win)
        for i in range(21):
            sleep(0.04)
            self.win.setBackground("yellow")
            self.welcomeText.setFill("blue")
            self.nameText.setFill("red")
            sleep(0.04)
            self.win.setBackground("purple")
            self.welcomeText.setFill("yellow")
            self.nameText.setFill("green")
            sleep(0.04)
            self.win.setBackground("red")
            self.welcomeText.setFill("yellow")
            self.nameText.setFill("blue")
            sleep(0.04)
            self.win.setBackground("lightblue")
            self.welcomeText.setFill("red")
            self.nameText.setFill("yellow")
        
        self.startButton=Button(self.win,Point(60,80),30,20,"Start")
        self.helpButton=Button(self.win,Point(60,50),30,20,"Help")
        self.quitButton=Button(self.win,Point(60,20),30,20,"Quit")
        self.startButton.activate()
        self.helpButton.activate()
        self.quitButton.activate()

    def start_interface(self):
        pt=self.win.getMouse()
        while not self.quitButton.clicked(pt):
            if self.helpButton.clicked(pt):
                self.help_interface(self.win)
                pm=self.win.getMouse()
                while not self.startButton1.clicked(pm):
                    pm=self.win.getMouse()
                self.cleanAll()
                return self.difficulty_chioce_interface()
                
            elif self.startButton.clicked(pt):
                return self.difficulty_chioce_interface()
                
            pt=self.win.getMouse()
        self.win.close()


    def help_interface(self,window):
        self.startButton.undraw()
        self.helpButton.undraw()
        self.quitButton.undraw()
        self.welcomeText.setText("H e l p")
        self.welcomeText.setSize(45)
        self.text0=Text(Point(44,88),"Fisrt you have 5 seconds to memerize the colors")
        self.text1=Text(Point(58,80),"When you click any white poker site,The poker will be uncovered")
        self.text2=Text(Point(40,72),"then you'll see the color of it for a little time.")
        self.text3=Text(Point(56,64),"You should remember the color of as more pokers as possible")
        self.text4=Text(Point(55,56),"When you click two pokers with the same color in succession,")
        self.text5=Text(Point(42,48),"the two pokers will be uncovered permanently.")
        self.text6=Text(Point(36,40),"When all pokers are uncovered,you win!")
        self.text7=Text(Point(60,30),"After reading help,click start to have a try!")
        
        self.text0.setSize(15)
        self.text1.setSize(15)
        self.text2.setSize(15)
        self.text3.setSize(15)
        self.text4.setSize(15)
        self.text5.setSize(15)
        self.text6.setSize(15)
        self.text7.setSize(20)

        self.text0.draw(window)
        self.text1.draw(window)
        self.text2.draw(window)
        self.text3.draw(window)
        self.text4.draw(window)
        self.text5.draw(window)
        self.text6.draw(window)
        self.text7.draw(window)

        self.startButton1=Button(window,Point(90,10),20,10,"start")
        self.startButton1.activate()

    def cleanAll(self):   #clear the help text
        self.text0.undraw()
        self.text1.undraw()
        self.text2.undraw()
        self.text3.undraw()
        self.text4.undraw()
        self.text5.undraw()
        self.text6.undraw()
        self.text7.undraw()
        self.startButton1.undraw()

    def difficulty_chioce_interface(self):
        #when a round of game has been finished
        try:
            self.playagainButton.undraw()
            self.exitButton.undraw()
            self.score_Text.undraw()
            self.clickNum_Text.undraw()
            self.congraText.undraw()
            self.ranktitle.undraw()
            self.rank_1st.undraw()
            self.rank_2nd.undraw()
            self.rank_3rd.undraw()
            
            self.welcomeText.draw(self.win)  #In fact the Text is 'difficuties'
            self.welcomeText.move(0,+10)
        finally:
            self.nameText.undraw()
            self.win.setBackground("orange")

            self.welcomeText.setSize(45)
            self.welcomeText.setText("D i f f i c u l t i e s")
            self.welcomeText.move(0,-10)
            self.easyButton=Button(self.win,Point(60,80),30,20,"Easy")
            self.mediumButton=Button(self.win,Point(60,50),30,20,"Medium")
            self.hardButton=Button(self.win,Point(60,20),30,20,"Hard")

            self.easyButton.activate()
            self.mediumButton.activate()
            self.hardButton.activate()

            pt=self.win.getMouse()
            while 1:
                if self.easyButton.clicked(pt):
                    self.game_interface(self.win,4)
                    self.Poker_click(self.win,4)
                    return self.finish_interface(4)
                elif self.mediumButton.clicked(pt):
                    self.game_interface(self.win,6)
                    self.Poker_click(self.win,6)
                    return self.finish_interface(6)
                elif self.hardButton.clicked(pt):
                    self.game_interface(self.win,8)
                    self.Poker_click(self.win,8)
                    return self.finish_interface(8)
                pt=self.win.getMouse()
                

    def game_interface(self,window,n):
        x=120/n  #n is the amount of poker of every line
                 #x is the width and length of every poker
        self.welcomeText.undraw()
        self.startButton.undraw()
        self.helpButton.undraw()
        self.quitButton.undraw()

        self.easyButton.deactivate()
        self.mediumButton.deactivate()
        self.hardButton.deactivate()

        self.easyButton.undraw()
        self.mediumButton.undraw()
        self.hardButton.undraw()

        
        #self.matrix:to record whether a poker is covered or not
        #0--covered 1--uncovered

        #self.card:to record the color of every poker
        if n==4:
            self.matrix=[[0,0,0,0],[0,0,0,0],
                   [0,0,0,0],[0,0,0,0]]
            self.card=[[0,0,0,0],[0,0,0,0],
                   [0,0,0,0],[0,0,0,0]]
            self.colorList=["blue","green","red",
                        "black"]*2+["purple","yellow"]*4
                     
        elif n==6:
            self.matrix=[[0,0,0,0,0,0],[0,0,0,0,0,0],
                   [0,0,0,0,0,0],[0,0,0,0,0,0],
                   [0,0,0,0,0,0],[0,0,0,0,0,0]]
            self.card=[[0,0,0,0,0,0],[0,0,0,0,0,0],
                   [0,0,0,0,0,0],[0,0,0,0,0,0],
                   [0,0,0,0,0,0],[0,0,0,0,0,0]]

            self.colorList=["blue","green","red",
                            "black","orange","purple",
                            "gray","brown","yellow"]*4

        else:
            self.matrix=[[0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],    
                       [0,0,0,0,0,0,0,0,0,0],    
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0]]
            
            self.card=[[0,0,0,0,0,0,0,0,0,0],   
                       [0,0,0,0,0,0,0,0,0,0],  
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0]]

            self.colorList=["blue","green","red",
                            "orange","purple",
                            "gray","brown","yellow",]*6+["pink","beige"]*8
                   
        for i in range(n):
            for j in range(n):
                self.card[i][j]=Rectangle(Point(j*x,i*x),Point(j*x+x,i*x+x))
                self.card[i][j].setFill("white")
                self.card[i][j].draw(window)

        shuffle(self.colorList)  #make the colors disorder
        self.count_down(n)

    def count_down(self,n):
        self.Pokercolor(n)

        self.timeText=Text(Point(60,70),"Remember")
        self.timeText2=Text(Point(60,50),"The colors!")
        self.timeText.setFill("white")
        self.timeText2.setFill("white")
        self.timeText.setSize(70)
        self.timeText2.setSize(70)
        self.timeText.draw(self.win)
        self.timeText2.draw(self.win)
        sleep(2)
        self.timeText2.undraw()
        self.timeText.move(0,-10)
        self.timeText.setText("3")
        self.timeText.setSize(200)
        
        sleep(1)
        self.timeText.setText("2")
        sleep(1)
        self.timeText.setText("1")
        sleep(1)
        self.timeText.setText("Go!")
        sleep(0.5)
        self.timeText.undraw()
        self.musicLOCK=False
        gamemusic=Thread(target=self.gamemusic,args=())
        gamemusic.start()
        
        self.Pokerundraw(n)

    def Pokercolor(self,n):
        for cardrow in range(n):
            for cardcolumn in range(n):
                coloritem=cardrow*n+cardcolumn
                color=self.colorList[coloritem]
                self.card[cardrow][cardcolumn].setFill(color)

    def Pokerundraw(self,n):
        for cardrow in range(n):
            for cardcolumn in range(n):
                coloritem=cardrow*n+cardcolumn
                self.card[cardrow][cardcolumn].setFill("white")
        

    def Poker_click(self,window,n):
        cardcolumn1,cardrow1=0,0
        cardcolumn2,cardrow2=0,0
        self.clickNum=0
        color1,color2=0,0
        x=120/n  #n is the amount of poker of every line
                 #x is the width and length of every poker
        pt=window.getMouse()
        self.clickNum+=1
        while not self.isFinished(n):
            extra_cardcolumn1,extra_cardrow1=cardcolumn1,cardrow1
            # make cardcolumn1 and cradrow1 remain
            for p in range(n):   #find the site of poker clicked
                if x*p<= pt.getX() <x*p+x:
                    cardcolumn1=p
                if x*p<= pt.getY() <x*p+x:
                    cardrow1=p
                    
            if self.isCovered(cardrow1,cardcolumn1):
                coloritem1=cardrow1*n+cardcolumn1
                color1=self.colorList[coloritem1]
                self.card[cardrow1][cardcolumn1].setFill(color1)
                sleep(0.2)
                if not self.isSame(color1,color2):
                    self.card[cardrow1][cardcolumn1].setFill("white")
                else:
                    if (cardrow1==cardrow2) and (cardcolumn1==cardcolumn2):
                    #if the player click one site twice in succession
                        self.card[cardrow1][cardcolumn1].setFill("white")
                    else:
                        if self.isCovered(cardrow1,cardcolumn1) and self.isCovered(cardrow2,cardcolumn2):

                            self.card[cardrow2][cardcolumn2].setFill(color2)
                            self.matrix[cardrow1][cardcolumn1]=1
                            self.matrix[cardrow2][cardcolumn2]=1
                            color1,color2=0,0
            else:
                cardcolumn1,cardrow1=extra_cardcolumn1,extra_cardrow1
                # make cardcolumn1 and cradrow1 not change
                
        
            if self.isFinished(n):break
                            
            pt=window.getMouse()
            self.clickNum+=1

            extra_cardcolumn2,extra_cardrow2=cardcolumn2,cardrow2
            # make cardcolumn2 and cradrow2 remain
            
            for p in range(n):      #find the site of poker clicked
                if x*p<= pt.getX() <x*p+x:
                    cardcolumn2=p
                if x*p<= pt.getY() <x*p+x:
                    cardrow2=p
        
            if self.isCovered(cardrow2,cardcolumn2):
                coloritem2=cardrow2*n+cardcolumn2
                color2=self.colorList[coloritem2]
                self.card[cardrow2][cardcolumn2].setFill(color2)
                sleep(0.2)
                if not self.isSame(color1,color2):
                    self.card[cardrow2][cardcolumn2].setFill("white")
                else:
                    if (cardrow1==cardrow2) and (cardcolumn1==cardcolumn2):
                    #if the player click one site twice in succession
                        self.card[cardrow2][cardcolumn2].setFill("white")
                    else:
                        if self.isCovered(cardrow1,cardcolumn1) and self.isCovered(cardrow2,cardcolumn2):
                            color2=0
                            self.card[cardrow1][cardcolumn1].setFill(color1)
                            self.matrix[cardrow1][cardcolumn1]=1
                            self.matrix[cardrow2][cardcolumn2]=1
                            color1,color2=0,0

            else:
                cardcolumn2,cardrow2=extra_cardcolumn2,extra_cardrow2
                # make cardcolumn2 and cradrow2 not change
                            
            if self.isFinished(n):break
            
            pt=window.getMouse()
            self.clickNum+=1

    def isSame(self,x,y): 
        return (x==y)

    def isCovered(self,cardrow,cardcolumn):
        return (self.matrix[cardrow][cardcolumn]==0)
    
    def isFinished(self,n):
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j]==0:
                    return False
        else:
            return True

    def circle1(self):
        self.circle.pengpeng(self.win,"circle",Point(20,20),15,"red",0.5,0.3,500)
    def circle2(self):
        self.circle.pengpeng(self.win,"circle",Point(90,100),15,"brown",0.25,0.5,500)
    def circle3(self):
        self.circle.pengpeng(self.win,"circle",Point(60,40),15,"yellow",0.7,0.5,500)
    def circle4(self):
        self.circle.pengpeng(self.win,"circle",Point(80,70),15,"blue",0.5,0.8,500)
    def circle5(self):
        self.circle.pengpeng(self.win,"circle",Point(45,30),15,"red",0.5,1.2,500)
    def circle6(self):
        self.circle.pengpeng(self.win,"circle",Point(30,80),15,"purple",0.5,1,500)
    def circle7(self):
        self.circle.pengpeng(self.win,"circle",Point(75,50),15,"orange",1,0.5,500)
    def circle8(self):
        self.circle.pengpeng(self.win,"circle",Point(70,60),15,"yellow",0.5,1.8,500)
    def circle9(self):
        self.circle.pengpeng(self.win,"circle",Point(100,20),15,"red",0.5,0.3,500)
    def circle10(self):
        self.circle.pengpeng(self.win,"circle",Point(50,100),15,"brown",0.5,1,500)
    def circle11(self):
        self.circle.pengpeng(self.win,"circle",Point(25,40),15,"yellow",0.7,1,500)
    def circle12(self):
        self.circle.pengpeng(self.win,"circle",Point(60,70),15,"blue",1,0.8,500)
    def circle13(self):
        self.circle.pengpeng(self.win,"circle",Point(90,30),15,"purple",1,1.2,500)
    def circle14(self):
        self.circle.pengpeng(self.win,"circle",Point(30,30),15,"pink",0.5,1,500)
    def circle15(self):
        self.circle.pengpeng(self.win,"circle",Point(75,75),15,"green",1,2,500)
    def circle16(self):
        self.circle.pengpeng(self.win,"circle",Point(70,100),15,"yellow",1,1.8,500)
    def circles(self):
        self.circle=animation()
        t1=Thread(target=self.circle1,args=())
        t2=Thread(target=self.circle2,args=())
        t3=Thread(target=self.circle3,args=())
        t4=Thread(target=self.circle4,args=())
        t5=Thread(target=self.circle5,args=())
        t6=Thread(target=self.circle6,args=())
        t7=Thread(target=self.circle7,args=())
        t8=Thread(target=self.circle8,args=())
        t9=Thread(target=self.circle9,args=())
        t10=Thread(target=self.circle10,args=())
        t11=Thread(target=self.circle11,args=())
        t12=Thread(target=self.circle12,args=())
        t13=Thread(target=self.circle13,args=())
        t14=Thread(target=self.circle14,args=())
        t15=Thread(target=self.circle15,args=())
        t16=Thread(target=self.circle16,args=())
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        t12.start()
        t13.start()
        t14.start()
        t15.start()
        t16.start()

    def recordText(self):
        self.ranktitle=Text(Point(78,80),"Score Ranks")
        self.ranktitle.setSize(30)
        self.ranktitle.setFill("orange")
        
        self.rank_1st=Text(Point(80,70),self.Record.readfile_1st())
        self.rank_1st.setSize(20)
        self.rank_2nd=Text(Point(80,55),self.Record.readfile_2nd())
        self.rank_2nd.setSize(20)
        self.rank_3rd=Text(Point(80,40),self.Record.readfile_3rd())
        self.rank_3rd.setSize(20)

        self.ranktitle.draw(self.win)
        self.rank_1st.draw(self.win)
        self.rank_2nd.draw(self.win)
        self.rank_3rd.draw(self.win)

    def finish_interface(self,n):
        self.musicLOCK=True
        
        self.clean_cards(n)
        
        self.win.setBackground("lightyellow")        
        self.congraText=Text(Point(60,100),"You Win!")
        #Congratulations to the player
        self.congraText.setSize(60)
        self.congraText.setFill("red")
        self.congraText.draw(self.win)

        if n==4:
            score=(41-self.clickNum)*4
            difficulty="easy"
        elif n==6:
            score=150-self.clickNum
            difficulty="medium"
        else:
            score=eval("%d" % ((480-self.clickNum)/4))
            difficulty="hard"

        self.clickNum_Text=Text(Point(30,70),"Clicks: "+str(0))
        self.clickNum_Text.setSize(25)
        self.clickNum_Text.setFill("green")
        self.clickNum_Text.draw(self.win)

        self.score_Text=Text(Point(30,50),"Scores: "+str(0))
        self.score_Text.setSize(25)
        self.score_Text.setFill("green")
        self.score_Text.draw(self.win)

        self.Record=record(difficulty)
        self.Record.remain_first3(score)
        self.Record.writefile()

        self.recordText()

        
        for i in range(self.clickNum+1) :   
            self.clickNum_Text.setText("Clicks: "+str(i))
            sleep(0.02)
        for j in range(score+1):    
            self.score_Text.setText("Scores: "+str(j))
            sleep(0.03)

        self.circles()
        sleep(9)

        self.playagainButton=Button(self.win,Point(30,15),30,10,"Play again")
        self.exitButton=Button(self.win,Point(90,15),30,10,"Exit")
        
        self.playagainButton.activate()
        self.exitButton.activate()
        
        pt=self.win.getMouse()
        while not self.exitButton.clicked(pt):
            if self.playagainButton.clicked(pt):
                return self.difficulty_chioce_interface()
            pt=self.win.getMouse()
        self.win.close()
                
    def clean_cards(self,n):
        for i in range(n):
            for j in range(n):
                self.card[i][j].undraw()
        # make all cards disappear
Game=game()
Game.init_interface()
Game.start_interface()

    
        
        
