from tkinter import *
from tkinter import messagebox
import time
import keyboard
import mouse

window = Tk()
window.geometry("300x250")
window.title("Auto Clicker")
window.config(bg="#def6fa")
running=False
delay=0

def exit_app():
    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")
    window.destroy() # Закриття вікна Tkinter

def start_clicker():
    global running, delay # "знаходимо" змінні, що існують поза функцією
    clicks_per_second = int(entry.get())
    delay = 1 / clicks_per_second # рахуємо затримку між кліками
    messagebox.showinfo("Auto Clicker", "Auto Clicker розпочинає роботу.")
    running = True
    # Запуск процесу кліків
    schedule_click()

def schedule_click():
    if running:
        mouse.click() # тут потім додамо клацання миші замість print
        time.sleep(delay) # затримка між кліками
        #schedule_click()

def show_info(event):
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

def addbind():
    global bind
    messagebox.showinfo("Інформація", 'Нажміть "Окей" та кнопку яку назначити на активацію автоклікера')
    bind=keyboard.read_key()
    if bind!="esc" and bind!="i":
        keyboard.add_hotkey(bind, start_clicker)
        messagebox.showinfo("Інформація","кнопку назначено")
        a.config(state="disabled")
    else:
        messagebox.showinfo("Інформація", "Назначити не вдалось: Кнопка зайнята")

Label(window, font=("",24),text="Auto Clicker", bg="#def6fa", pady=10, fg="#027870").place(relx=0.5, rely=0.1, anchor="center")
Label(window, font=("",14),text="Кліків на секунду:", bg="#def6fa", pady=10, fg="#027870").place(relx=0.5, rely=0.25, anchor="center")
entry=Entry(window, font=("",16))
entry.place(relx=0.5, rely=0.3125, anchor="n")
Button(window,bg="white", text="T",command=lambda: print("Натиснуто")).place(x=0,y=0)
Button(window, bg="#4dae4f",activebackground="#4dae4f", text="Почати", fg="white", command=start_clicker).place(relx=0.4, rely=0.5, anchor="center")
Button(window, bg="#f44132",activebackground="#f44132", text="Вийти", fg="white", command=lambda: window.destroy()).place(relx=0.6, rely=0.5, anchor="center")
a = Button(window, bg="yellow",activebackground="yellow", text="Призначити кнопку активації", command=addbind)
a.place(relx=0.5, rely=0.65, anchor="center")
window.bind("i",show_info)
keyboard.add_hotkey('esc', exit_app)
window.mainloop()
