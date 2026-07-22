import tkinter as tk
from tkinter import messagebox
import random
root = tk.Tk()
root.title("表白小窗口")
root.geometry("520x380")
root.resizable(False,False)
root.configure(bg="#fff0f5")
content = """
其实我一直有句话想和你说：
从我认识你的那天开始，我的生活多了很多喜欢。
是你让我再次看到了爱情的希望。
你的出现，让平凡的日子变得闪闪发光。
所以，你愿意做我女朋友么？
"""
text_label = tk.Label(
    root,
    text=content,
    font=("微软雅黑",12),
    bg="#fff0f5",
    fg="#c41e3a",
    justify="center"
)
text_label.pack(pady=30)
def agree():
    messagebox.showinfo("双向奔赴","很高兴认识你答应我，朝夕相伴！")
    root.destroy()
def move_no_btn(_):
    new_x = random.randint(30,420)
    new_y = random.randint(280,330)
    no_btn.place(x=new_x,y=new_y)
yes_btn = tk.Button(
    root,
    text="我愿意",
    width=10,
    height=2,
    font=("微软雅黑",11),
    bg="#ff6b81",
    fg="white",
    command=agree
)
yes_btn.place(x=150,y=300)
no_btn = tk.Button(
    root,
    text="再考虑一下",
    width=10,
    height=2,
    font=("微软雅黑",11),
    bg="#cccccc"
)
no_btn.place(x=280,y=300)
no_btn.bind("<Enter>",move_no_btn)
root.mainloop()