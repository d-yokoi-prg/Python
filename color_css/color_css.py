import tkinter
import tkinter.ttk
import tkinter.font
import PIL
# カラー情報格納用の変数
R = "00"
G = "00"
B = "00"
rgb = "#" + R + G + B

# テキストカラー情報格納用の変数
TR = "00"
TG = "00"
TB = "ff"
textrgb = "#" + TR + TG + TB

fontList = []

# カラー情報を取得して変更
def updateColor():
    global R, G, B, TR, TG, TB, rgb, textrgb
    R = Rvar.get()
    G = Gvar.get()
    B = Bvar.get()

    TR = RTextvar.get()
    TG = GTextvar.get()
    TB = BTextvar.get()

    R = format(int(R), "02x")
    G = format(int(G), "02x")
    B = format(int(B), "02x")

    TR = format(int(TR), "02x")
    TG = format(int(TG), "02x")
    TB = format(int(TB), "02x")

# 背景色の更新
    rgb = "#" + R + G + B
    label["text"] = "背景色のカラーコード：" + rgb
    canvas.itemconfig(rect, fill=rgb)

# 文字色の更新
    textrgb = "#" + TR + TG + TB
    textlabel["text"] = "文字のカラーコード：" + textrgb
    canvas.itemconfig(canTex, fill=textrgb)
    getF = combo.get()
    canvas.itemconfigure(canTex, font=(getF, 64))


def getFontList():
    ffont = tkinter.font.families()

    for i in range(len(ffont)):
        fontList.append(ffont[i])

# ウィンドウのオブジェクトをつくる
root = tkinter.Tk()
root.title("16進数のカラー")
root.geometry("800x700")

# キャンバスを描画
canvas = tkinter.Canvas(root, width=800, height=400, background="white")
canvas.pack()

# カラー確認用の枠を描画
rect = canvas.create_rectangle(10, 10, 800, 400, fill="#000000")
canTex = canvas.create_text(320, 220, text="文字の色", font=("System", 64), fill="#0000ff")

# カラー調整用のバーを描画
# R
Rvar = tkinter.Scale(root, label="Rの強度", orient=tkinter.HORIZONTAL, from_=0, to=255)
Rvar.place(x=150, y=405)

# G
Gvar = tkinter.Scale(root, label="Gの強度", orient=tkinter.HORIZONTAL, from_=0, to=255)
Gvar.place(x=150, y=460)

# B
Bvar = tkinter.Scale(root, label="Bの強度", orient=tkinter.HORIZONTAL, from_=0, to=255)
Bvar.place(x=150, y=515)

# 文字のカラー調整用のバーを描画
RTextvar = tkinter.Scale(root, label="Rの強度(文字)", orient=tkinter.HORIZONTAL, from_=0, to=255)
RTextvar.place(x=450, y=405)

GTextvar = tkinter.Scale(root, label="Gの強度(文字)", orient=tkinter.HORIZONTAL, from_=0, to=255)
GTextvar.place(x=450, y=460)

BTextvar = tkinter.Scale(root, label="Bの強度(文字)", orient=tkinter.HORIZONTAL, from_=0, to=255)
BTextvar.set(255)
BTextvar.place(x=450, y=515)

# ラベルを描画
label = tkinter.Label(root, text="背景色のカラーコード：" + rgb, font=("MS ゴシック", 18))
label.place(x=225, y=590)

textlabel = tkinter.Label(root, text="文字のカラーコード：" + textrgb, font=("MS ゴシック", 18))
textlabel.place(x=225, y=625)

# フォントのプルダウンメニューを描画
getFontList()
combo = tkinter.ttk.Combobox(root, height=10, width=25, values=fontList)
combo.set("System")
combo.place(x=260, y=500)

# ボタンを描画
button = tkinter.Button(root, text="カラー変更", command=updateColor)
button.place(x=350, y=670)

root.mainloop()
