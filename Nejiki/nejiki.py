import tkinter
from PIL import ImageTk


def battleCount():
    global loop, count
    if loop == 7 and count==7:
        message["text"] = "Congratulations!"

    else:
        count = count + 1
        if count >= 8 and loop != 8:
            loop = loop + 1
            count = 1
            canvas01.delete("p1")
            canvas01.create_image(125, 125, image=pkmn[loop-1], tag="p1")
            canvas01.place(x=290, y=20)

        message["text"] = "現在" + str(loop) + "周目、" + str(count) + "戦中"

def battleReset():
    global loop, count
    count = 1
    loop = 1
    message["text"] = "現在" + str(loop) + "周目、" + str(count) + "戦中"
    canvas01.delete("p1")
    canvas01.create_image(125, 125, image=pkmn[loop - 1], tag="p1")
    canvas01.place(x=290, y=20)


loop = 1
count = 1
root = tkinter.Tk()
root.title("ネ○キ")
root.resizable(False, False)
root.geometry("500x250")

pkmn = [ImageTk.PhotoImage(file="./img/pikachu.png"),
        ImageTk.PhotoImage(file="./img/dodaitosu.png"),
        ImageTk.PhotoImage(file="./img/gokazaru.png"),
        ImageTk.PhotoImage(file="./img/enperuto.png"),
        ImageTk.PhotoImage(file="./img/rucario.png"),
        ImageTk.PhotoImage(file="./img/gaburiasu.png"),
        ImageTk.PhotoImage(file="./img/arceus.png")]

canvas = tkinter.Canvas(root,width=340, height=221)
fukidashi = ImageTk.PhotoImage(file="./img/fukidashi.png")
canvas.create_image(170, 110, image=fukidashi)
canvas.place(x=-30, y=-40)

canvas01 = tkinter.Canvas(root,width=250, height=400)
canvas01.create_image(125, 125, image=pkmn[loop - 1], tag="p1")
canvas01.place(x=300, y=20)


message = tkinter.Label(root,text="現在" + str(loop) + "周目、" + str(count) + "戦中", font=("MS ゴシック", 18))
message.place(x=50, y=50)

winBtm = tkinter.Button(root, text="勝ち", command=battleCount, font=("MS ゴシック", 18))
winBtm.place(x=40, y=180)

loseBtm = tkinter.Button(root, text="負け", command=battleReset, font=("MS ゴシック", 18))
loseBtm.place(x=150, y=180)

root.mainloop()
