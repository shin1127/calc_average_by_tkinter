import tkinter as tk
import numpy as np

root = tk.Tk()
root.title(u"平均算出アプリ")
root.geometry("400x300")


# ボタンを押したときの処理

def buttoneffect(event):
    value = EditBox.get()
    split_value = value.split(",")
    int_values = list(map(int, split_value))
    average = sum(int_values) / len(int_values)

    variance = 0  # 分散についての変数を初期化する
    for i in range(len(int_values)):

        variance += (int_values[i] - average) ** 2 / len(int_values)

    sd = np.sqrt(variance)

    EditBox.delete(0, tk.END)  # テキストボックスの中身を初期化する
    Static4["text"] = "平均値は%sです。" % average  # ラベルの中身を書き換える
    Static5["text"] = "標準偏差は%sです。" % sd


# ボタンやテキストボックスの配置

Static1 = tk.Label(text=u"入力された値の平均値を算出します。", font=("", 12))
Static1.pack()

Static2 = tk.Label(text=u"カンマ区切りで数値を入力してください。", font=("", 12))
Static2.pack()


#  テキストボックス

EditBox = tk.Entry()
EditBox.insert(tk.END, "Input this box.")
EditBox.place(x=140, y=70)


button = tk.Button(text=u"計算する")
button.bind("<Button-1>", buttoneffect)
button.place(x=150, y=100)

Static3 = tk.Label(text=u"統計データ", font=("", 12))
Static3.place(x=50, y=140)

Static4 = tk.Label(text=u"　", font=("", 12))  # 平均値の出力に利用する空のラベル
Static4.place(x=140, y=160)

Static5 = tk.Label(text=u"　", font=("", 12))  # 標準偏差の出力に利用する空のラベル
Static5.place(x=140, y=180)


root.mainloop()
