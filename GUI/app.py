import ttkbootstrap as ttk;
import tkinter as tk;

window = tk.Tk();
width = window.winfo_screenwidth();
height = window.winfo_screenheight();
window.geometry(f"{width}x{height}");

############################
if __name__ == '__main__':
    window.mainloop();