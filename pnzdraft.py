import tkinter as tk

class MoveCanvas(tk.Canvas):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        self.dx = 0
        self.dy = 0
  
        self.my_canvas = self.create_rectangle(200, 220, 210, 230, fill="blue")  # Create blue canvas

        self.dt = 25
        self.tick()
      
    def tick(self):
        self.move(self.my_canvas, self.dx, self.dy)  # Move the blue canvas
        self.after(self.dt, self.tick)
 
    def change_heading(self, dx, dy):
        self.dx = dx
        self.dy = dy
  
# Function to create new window
def create_window():
    # Create new window
    pnz = tk.Tk()
    main_window.destroy()  # Close main window
    pnz.geometry("400x240")
    
    # Create MoveCanvas widget
    cvs = MoveCanvas(pnz)
    cvs.pack(fill="both", expand=True)
 
    ds = 3

    # Bind key events to the MoveCanvas widget
    pnz.bind("<KeyPress-Left>", lambda event: cvs.change_heading(-ds, 0))
    pnz.bind("<KeyPress-Right>", lambda event: cvs.change_heading(ds, 0))
    pnz.bind("<KeyPress-Up>", lambda event: cvs.change_heading(0, -ds))
    pnz.bind("<KeyPress-Down>", lambda event: cvs.change_heading(0, ds))
    
    pnz.mainloop()
    
# Creating StartMenu
main_window = tk.Tk()
main_window.geometry("400x240")
main_window.title("start")

tk.Button(main_window, text="START", command=create_window).pack()

main_window.mainloop()

