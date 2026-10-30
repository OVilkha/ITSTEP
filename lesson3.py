import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Візуальний асистент")

face_label = tk.Label(root)
face_label.pack(pady = 20)

happy_face = tk.PhotoImage(file = "happy.png")
sad_face = tk.PhotoImage(file = "sad.png")


def blink(original_color):
    root.configure(bg = original_color)
    root.after(200, lambda: root.configure(bg = "white"))
    root.after(3000, blink)

blink("blue")



