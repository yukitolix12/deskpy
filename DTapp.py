import tkinter as tk
import openpyxl as excel

from tkinter import messagebox as mbox

window=tk.Tk()
window.geometry("300x100")
window.title("Excelをいじる")

label=tk.Label(window,text="入力するのだ")
label.pack()

text_box=tk.Entry(window,width=40)
text_box.pack()

wb=excel.Workbook()
ws=wb.worksheets[0]

def close_window():
    window.destroy()

def ok_button():
    textA=text_box.get()
    ws["A1"].value=textA
    mbox.showinfo("結果","反映完了")
    wb.save("デスクトップアプリ.xlsx")

okbutton=tk.Button(window,text="反映",command=ok_button,width=14)
desbutton=tk.Button(window,text="終了",command=close_window,width=14)

okbutton.pack(fill = 'x', padx=20, side='left')
desbutton.pack(fill = 'x', padx=20, side='left')

window.mainloop()

