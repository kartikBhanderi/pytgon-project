from tkinter import *  
from PIL import ImageTk,Image
import pickle
import Game_1 as g1
import Game_2 as g2
main_window = Tk()  
main_window.geometry("400x600")
main_window.title("Game Zone")

photo = ImageTk.PhotoImage(file="GameImage.gif")
lab=Label(main_window,image=photo)
lab.pack(fill=X,padx=(100,100),pady=(10,30))


def get_list():
    lst=list()
    with open("Scores.pickle","rb") as l:
        lst=pickle.load(l)
    return lst

def load_score(name,score):
    lst=list()
    with open("Scores.pickle","rb") as l:
        lst=pickle.load(l)
    lst.append(tuple([score,name]))
    with open("Scores.pickle","wb") as fw:
        pickle.dump(lst,fw)
name=""
def get_usr():
    user_window=Tk()
    user_window.geometry("700x400")
    user_window.title("Congratulations")
    lab1=Label(user_window,text="Enter your Name : ",font=("Arial Bold",30))
    lab1.grid(column=0,row=0)
    usrname=Entry(user_window)
    usrname.grid(column=1,row=0)
    def sub(username):
        global name
        name=username.get()
        user_window.destroy()
    but=Button(user_window,text="Submit",command=lambda : sub(usrname))
    but.grid(column=1,row=1)
    
    user_window.mainloop()
        
def game1(window):
    window.destroy()
    score=g1.play()
    load_score(name,score)

def game2(window):
    window.destroy()
    score=g2.play()
    load_score(name,score)



def start_new_game():
    main_window.destroy()
    usrname=get_usr()
    game_window=Tk()
    game_window.title("Start New Game")
    photo2 = ImageTk.PhotoImage(file=str('GameWindow1.png'))
    lab2=Label(game_window,image=photo2)
    lab2.pack(fill=X,padx=(100,100),pady=(30,30))
    photo3 = ImageTk.PhotoImage(file="SpaceInvader.jpg")
    Game1_button = Button(game_window,image=photo3,command=lambda : game1(game_window))
    Game1_button.pack(side=LEFT,fill=Y)
    photo4 = ImageTk.PhotoImage(file="RacingCar.jpg")
    Game2_button=Button(game_window,image=photo4,command=lambda : game2(game_window))
    Game2_button.pack(side=LEFT,fill=Y)
    game_window.mainloop()
    

def show_highscore():
    main_window.destroy()
    highscore_window=Tk()
    highscore_window.geometry("500x650")
    highscore_window.title("High Scores")
    lst=get_list()
    lst.sort(reverse=True)
    Label(highscore_window,text="Position",font=("Araial Bold",35)).grid(column=0,row=0,padx=(20,20),pady=(10,10))
    Label(highscore_window,text="Name",font=("Araial Bold",35)).grid(column=1,row=0,padx=(20,20),pady=(10,10))
    Label(highscore_window,text="Score",font=("Araial Bold",35)).grid(column=2,row=0,padx=(20,20),pady=(10,10))
    for i in range(min(10,len(lst))):
        Label(highscore_window,text=str(str(i+1)+"."),font=("Araial",25)).grid(column=0,row=i+1,padx=(20,20),pady=(10,10))
        Label(highscore_window,text=str(lst[i][1]),font=("Araial",25)).grid(column=1,row=i+1,padx=(20,20),pady=(10,10))
        Label(highscore_window,text=str(lst[i][0]),font=("Araial",25)).grid(column=2,row=i+1,padx=(20,20),pady=(10,10))
    
    
start_Button = Button(main_window,text="Start Game",font=("Arial Bold",25),command=start_new_game)
start_Button.pack(fill=X,padx=(100,100),pady=(10,30))

highscore_Button = Button(main_window,text="High Scores",font=("Arial Bold",25),command=show_highscore)
highscore_Button.pack(fill=X,padx=(100,100),pady=(10,30))

quit_Button = Button(main_window,text="End Game",font=("Arial Bold",25),command=main_window.destroy)
quit_Button.pack(fill=X,padx=(100,100),pady=(10,30))


main_window.mainloop()