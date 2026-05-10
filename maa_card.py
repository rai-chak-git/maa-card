import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence

# Create main window
root = tk.Tk()
root.title("Mother's Day Surprise")
root.geometry("600x400")

pages = []
current_page = 0

def show_page(index):
    global current_page
    current_page = index
    for widget in root.winfo_children():
        widget.destroy()
    pages[index]()

def next_page():
    global current_page
    if current_page + 1 < len(pages):
        show_page(current_page + 1)

# Page 1
def page1():
    label = tk.Label(root, text="Happy Mother's Day to my beautiful Maa", font=("Helvetica", 20), wraplength=500)
    label.pack(expand=True)
    tk.Button(root, text="Next ➡️", command=next_page).pack()

# Page 2
def page2():
    label = tk.Label(root, text="I have a surprise for you...", font=("Helvetica", 20))
    label.pack(expand=True)
    tk.Button(root, text="Next ➡️", command=next_page).pack()

# Page 3 (Question)
def page3():
    label = tk.Label(root, text="Are you ready to receive the surprise?", font=("Helvetica", 18))
    label.pack(pady=20)
    tk.Button(root, text="Yes ✅", command=next_page).pack(pady=10)
    tk.Button(root, text="Option One ❓", command=next_page).pack(pady=10)

# Page 4 (Card + Letter)
def page4():
    title = tk.Label(root, text="♥️ The love that never fails ♥️", font=("Helvetica", 22, "bold"))
    title.pack(pady=10)
    text = """My Dearest Maa,

Happy Mother's Day! Today is all about celebrating you.
As I was thinking about everything you mean to me, a few special things came to mind:
One of my absolute favorite memories of us is the winter afternoons we spent together among the marigold garden when I was younger.
You are most powerful and truly most beautiful.
Thank you for teaching me to see the good in any situation.
Your Aalu posto tastes like home!
Above all, I appreciate your patience and belief.
I love you more than words can say.

All my love,
Babin
May 08, 2026"""
    msg = tk.Label(root, text=text, font=("Helvetica", 14), wraplength=550, justify="left")
    msg.pack(pady=10)
    tk.Button(root, text="Next ➡️", command=next_page).pack()

# Page 5 (Hug GIF)
def page5():
    label = tk.Label(root, text="A Big Hug for You 🤗", font=("Helvetica", 20))
    label.pack()
    
    # Load GIF
    gif = Image.open("hug.gif")  # <-- Place your hug.gif in same folder
    frames = [ImageTk.PhotoImage(frame.copy().resize((300,300))) for frame in ImageSequence.Iterator(gif)]
    
    gif_label = tk.Label(root)
    gif_label.pack()

    def animate(counter=0):
        gif_label.config(image=frames[counter])
        root.after(100, animate, (counter+1) % len(frames))
    animate()

# Add pages
pages = [page1, page2, page3, page4, page5]

# Start
show_page(0)
root.mainloop()
