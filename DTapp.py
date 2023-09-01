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

window.mainloop()
