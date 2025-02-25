from tkinter import *
from tkinter import messagebox
import time

window = Tk()
window.geometry("300x250")
window.title("Auto Clicker")
window.config(bg="#def6fa")
running=False
delay=0

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
        print("Клац!") # тут потім додамо клацання миші замість print
        time.sleep(delay) # затримка між кліками
        schedule_click() # функція знову викликає сама себе

def show_info(event):
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

Label(window, font=("",24),text="Auto Clicker", bg="#def6fa", pady=10, fg="#027870").place(relx=0.5, rely=0.1, anchor="center")
Label(window, font=("",14),text="Кліків на секунду:", bg="#def6fa", pady=10, fg="#027870").place(relx=0.5, rely=0.25, anchor="center")
entry=Entry(window, font=("",16))
entry.place(relx=0.5, rely=0.3125, anchor="n")
Button(window, bg="#4dae4f",activebackground="#4dae4f", text="Почати", fg="white", command=start_clicker).place(relx=0.4, rely=0.5, anchor="center")
Button(window, bg="#f44132",activebackground="#f44132", text="Вийти", fg="white", command=lambda: window.destroy()).place(relx=0.6, rely=0.5, anchor="center")
window.bind("i",show_info)
window.mainloop()
