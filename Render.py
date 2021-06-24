import tkinter as tk
from Object import OBJ


if __name__ == '__main__':
    print("Start Running...")
    obj = OBJ()
    obj.parse_from_file("D:\\ML\\cube.obj")
    
    window = tk.Tk()
    window.geometry("800x600")
    window.title("Simple Render")
    lbl = tk.Label(window, text=f"Now open: {obj.name}")
    lbl.grid(column=0, row=0)
    window.mainloop()