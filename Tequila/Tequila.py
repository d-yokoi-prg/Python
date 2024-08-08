import tkinter
from PIL import ImageTk
import tkinter.ttk

#お酒
cap = [[150,100, 300, 150],
       [150,150,300,200],
       [150, 200, 300, 250],
       [150, 250, 300, 300]]
capText =[]         #お酒のテキストを格納する
Tequila = 0

botol = [[400, 100, 550, 150],
         [400, 150, 550, 200],
         [400, 200, 550, 250],
         [400, 250, 550, 300]]
water = 0

tequilaMassage = ""
waterMassage = ""
#お酒のポイントを追加
def getTequila(event):
    global tequilaMassage, Tequila
    count = 0
    if event.widget.cget("text") == "最下位":
        count = 4
    elif event.widget.cget("text") == "11位":
        count = 2
    else:
        count = 1
    for i in range(len(capText)):
        if canvas.itemcget(capText[(len(capText)-1) - i], "fill") != "#ffffff":
            pass

        else:
            canvas.itemconfig(capText[(len(capText)-1) - i], fill="#ff0000")
            count = count - 1
            Tequila = Tequila + 1
            if Tequila == 4:
                tequilaMassage = tkinter.Canvas(root, width=200, height=50)
                tequilaMassage.place(x=120, y=310)
                tequilaMassage.create_text(100, 30, text="テキーラ1杯", tag="messageT",
                                           font=("MS ゴシック", 24), fill="#000000")
        if count == 0:
            break

def getWater(event):
    global water, waterMassage
    if event.widget.cget("text") == "1位":
        count = 4
    elif event.widget.cget("text") == "2位":
        count = 2
    else:
        count = 1
    for i in range(len(botol)):
        if canvas.itemcget(botol[(len(botol)-1) - i], "fill") != "#ffffff":
            pass

        else:
            canvas.itemconfig(botol[(len(botol)-1) - i], fill="#00ffff")
            water = water + 1
            count = count - 1
            if water == 4:
                waterMassage = tkinter.Canvas(root, width=200, height=50)
                waterMassage.place(x=380, y=310)
                waterMassage.create_text(100, 30, tag="messageW", text="お水獲得",
                                         font=("MS ゴシック", 24), fill="#000000")

        if count == 0:
            break


def resetDrink(event):
    global Tequila, water
    if event.widget.cget("text") == "テキーラリセット":
        Tequila = 0
        print(tequilaMassage)
        for i in range(len(capText)):
            if canvas.itemcget(capText[i], "fill") != "#ffffff":
                canvas.itemconfig(capText[i], fill="#ffffff")
            else:
                pass
        tequilaMassage.destroy()

    else:
        water = 0
        print(waterMassage)
        for i in range(len(botol)):
            if canvas.itemcget(botol[i], "fill") != "#ffffff":
                canvas.itemconfig(botol[i], fill="#ffffff")
            else:
                pass
        waterMassage.destroy()

    canvas.update()

root = tkinter.Tk()
root.title("テキーラカウント")
canvas = tkinter.Canvas(root,width=864, height=486)
bgimage = ImageTk.PhotoImage(file="../image/bar.png")
canvas.pack()
canvas.create_image(432, 260, image=bgimage)

#カップを描画
for i in range(len(cap)):
    capText.append(canvas.create_rectangle(cap[i][0], cap[i][1], cap[i][2], cap[i][3], fill="#ffffff"))


canvas.create_line(150, 100, 150, 300, width=5)
canvas.create_line(300, 100, 300, 300, width=5)
canvas.create_line(150, 300, 300, 300, width=5)

#水入りのボトルを描画
for i in range(len(botol)):
    botol.append(canvas.create_rectangle(botol[i][0], botol[i][1], botol[i][2], botol[i][3], fill="#ffffff"))

canvas.create_line(400, 100, 400, 300, width=5)
canvas.create_line(550, 100, 550, 300, width=5)
canvas.create_line(400, 300, 550, 300, width=5)

#ボタンを設置
buttonTop = []
for i in range(3):
    num = i+1
    buttonTop.append(tkinter.Button(root, height=2, width=20, text=str(num)+"位"))
    buttonTop[i].bind("<ButtonPress>", getWater)
    buttonTop[i].place(x=650, y=50*num)

buttonLow = []
for i in range(10, 13, 1):
    num = 200 + 50 *(i - 10 + 1)
    if i == 12:
        buttonLow.append(tkinter.Button(root, height=2, width=20, text="最下位"))
        buttonLow[i-10].bind("<ButtonPress>", getTequila)

    else:
        buttonLow.append(tkinter.Button(root, height=2, width=20, text=str(i) +"位"))
        buttonLow[i-10].bind("<ButtonPress>", getTequila)

    buttonLow[i-10].place(x=650, y=num)

resetButton = []
word = ["テキーラ", "お水"]

for i in range(2):
    resetButton.append(tkinter.Button(root, height=2, width=20, text=word[i] + "リセット"))
    resetButton[i].bind("<ButtonPress>", resetDrink)
    if i == 0:
        resetButton[i].place(x=150, y=380)

    else:
        resetButton[i].place(x=400, y=380)

root.mainloop()
