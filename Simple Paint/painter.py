import os
from sys import platform
from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter.colorchooser import *
from tkinter import simpledialog
from PIL import Image, ImageDraw, ImageTk

root = Tk()

class Painter:
    lmb = "up"
    x_pos, y_pos = None, None
    line_x1, line_y1, line_x2, line_y2 = None, None, None, None
    my_image = Image.new("RGB",(800,600),(255,255,255))
    draw = ImageDraw.Draw(my_image)
    canvas = Canvas(root,width=800,height=600,highlightthickness=0)
    logger = ""
    
    @staticmethod
    def quit_app(event=None):
        self.logger += "Application quit.\n"
        root.destroy()
        
    def save_file(self,event=None):
        file = filedialog.asksaveasfile(mode="w",defaultextension=".png")
        if file:
            file_path = os.path.abspath(file.name)
            self.my_image.save(file_path)
            self.logger += f"File saved.\t{file_path}\n"
            
    def open_file(self,event=None):
        file_path = filedialog.askopenfilename(parent=root)
        if (file_path):
            my_pic = Image.open(file_path)
            self.canvas.image = ImageTk.PhotoImage(my_pic)
            self.canvas.create_image(0,0,image=self.canvas.image,anchor='nw')
            self.logger += f"File opened.\t{file_path}\n"

    def pick_fill(self,event=None):
        (rgb,hex) = askcolor(title="Colors")    #askcolor returns tuple ((R,G,B),hex)
        if hex:
            self.fill_color.set(hex)
            self.logger += f"Fill color set to {hex}.\n"
            
    def pick_stroke(self,event=None):
        (rgb,hex) = askcolor(title="Colors")    #askcolor returns tuple ((R,G,B),hex)
        if hex:
            self.stroke_color.set(hex)
            self.logger += f"Stroke color set to {hex}.\n"
            
    def increment_size(self,event=None):
        self.text_size.set(self.text_size.get()+1)
        self.logger += f"Text size increased.\n"
        
    def decrease_size(self,event=None):
        self.text_size.set(self.text_size.get()-1)
        self.logger += f"Text size decreased.\n"
        
    def setup_menu_bar(self):
        the_menu = Menu(root)
    
        #FILE MENU
        file_menu = Menu(the_menu,tearoff=0)
        file_menu.add_command(label="Open File...",command=self.open_file,accelerator="Command+O")
        file_menu.add_command(label="Save As...",command=self.save_file,accelerator="Command+S")
        file_menu.add_separator()
        file_menu.add_command(label="Quit",command=self.quit_app)
        the_menu.add_cascade(label="File",menu=file_menu)
        
        #TEXT MENU
        text_menu = Menu(the_menu,tearoff=0)
        the_menu.add_cascade(label="Text",menu=text_menu)
        
        #TEXT STYLE
        text_menu.add_checkbutton(label="Bold",variable=self.text_weight,onvalue='bold',offvalue='normal',accelerator="Command+B")
        text_menu.add_checkbutton(label="Italic",variable=self.text_slant,onvalue='italic',offvalue='roman',accelerator="Command+I")
        text_menu.add_checkbutton(label="Underline",variable=self.text_underline,onvalue=1,offvalue=0,accelerator="Command+U")
        text_menu.add_separator()
        text_menu.add_command(label="Bigger",command=self.increment_size,accelerator="Command++")
        text_menu.add_command(label="Smaller",command=self.decrease_size,accelerator="Command+-")
        text_menu.add_separator()
        
        #FONT SUBMENU
        font_submenu = Menu(text_menu,tearoff=0)
        font_submenu.add_radiobutton(label="Times",variable=self.text_font,value="Times")
        font_submenu.add_radiobutton(label="Courier",variable=self.text_font,value="Courier")
        font_submenu.add_radiobutton(label="Ariel",variable=self.text_font,value="Ariel")
        text_menu.add_cascade(menu=font_submenu,label="Font")
        
        #FONT_SIZE SUBMENU
        font_size_submenu = Menu(text_menu)
        font_size_submenu.add_radiobutton(label="12",variable=self.text_size,value=12)
        font_size_submenu.add_radiobutton(label="16",variable=self.text_size,value=16)
        font_size_submenu.add_radiobutton(label="20",variable=self.text_size,value=20)
        text_menu.add_cascade(menu=font_size_submenu,label="Font Size")
        
        #TOOL MENU
        tool_menu = Menu(the_menu,tearoff=0)
        the_menu.add_cascade(label="Tool",menu=tool_menu)
        tool_menu.add_radiobutton(label="Pencil",variable=self.drawing_tool,value="Pencil",accelerator="Command+1")
        tool_menu.add_radiobutton(label="Line",variable=self.drawing_tool,value="Line",accelerator="Command+2")
        tool_menu.add_radiobutton(label="Arc",variable=self.drawing_tool,value="Arc",accelerator="Command+3")
        tool_menu.add_radiobutton(label="Rectangle",variable=self.drawing_tool,value="Rectangle",accelerator="Command+4")
        tool_menu.add_radiobutton(label="Oval",variable=self.drawing_tool,value="Oval",accelerator="Command+5")
        tool_menu.add_radiobutton(label="Text",variable=self.drawing_tool,value="Text",accelerator="Command+6")
        
        #COLOR MENU
        color_menu = Menu(the_menu,tearoff=0)
        the_menu.add_cascade(label="Color",menu=color_menu)
        color_menu.add_command(label="Fill Color",command=self.pick_fill)
        color_menu.add_command(label="Stroke Color",command=self.pick_stroke)
        color_menu.add_separator()
        
        #STROKE SIZE SUBMENU
        stroke_size_menu = Menu(color_menu)
        stroke_size_menu.add_radiobutton(label="1",variable=self.stroke_size,value=1)
        stroke_size_menu.add_radiobutton(label="2",variable=self.stroke_size,value=2)
        stroke_size_menu.add_radiobutton(label="3",variable=self.stroke_size,value=3)
        stroke_size_menu.add_radiobutton(label="4",variable=self.stroke_size,value=4)
        stroke_size_menu.add_radiobutton(label="5",variable=self.stroke_size,value=5)
        color_menu.add_cascade(menu=stroke_size_menu,label="Stroke Size")
        
        root.config(menu=the_menu)
    
    def lmb_down(self,event=None):
        self.lmb = "down"
        self.line_x1 = event.x
        self.line_y1 = event.y
    
    def lmb_up(self,event=None):
        self.lmb = "up"
        self.x_pos = None
        self.y_pos = None
        self.line_x2 = event.x
        self.line_y2 = event.y
        
        if self.drawing_tool.get() == "Line":
            self.line_draw(event)
        elif self.drawing_tool.get() == "Arc":
            self.arc_draw(event)
        elif self.drawing_tool.get() == "Oval":
            self.oval_draw(event)
        elif self.drawing_tool.get() == "Rectangle":
            self.rec_draw(event)
        elif self.drawing_tool.get() == "Text":
            self.text_draw(event)
            
        print(self.drawing_tool.get(), self.stroke_color.get())
        
    def motion(self,event=None):
        if self.drawing_tool.get() == "Pencil":
            self.pencil_draw(event)
    
    def pencil_draw(self,event=None):
        if self.lmb == "down":
            if self.x_pos and self.y_pos:
                event.widget.create_line(self.x_pos,self.y_pos,event.x,event.y,smooth=True,fill=self.stroke_color.get(),width=self.stroke_size.get())
                self.draw.line([(self.x_pos,self.y_pos),(event.x,event.y)],fill=self.stroke_color.get(),width=self.stroke_size.get())
            self.x_pos,self.y_pos = event.x,event.y
    
    def line_draw(self,event=None):
        if None not in (self.line_x1,self.line_y1,self.line_x2,self.line_y2):
            event.widget.create_line(self.line_x1,self.line_y1,self.line_x2,self.line_y2,smooth=True,fill=self.stroke_color.get(),width=self.stroke_size.get())
            self.draw.line([(self.line_x1,self.line_y1),(self.line_x2,self.line_y2)],fill=self.stroke_color.get(),width=self.stroke_size.get())
        self.line_x1, self.line_y1, self.line_x2, self.line_y2 = None, None, None, None
    
    def rec_draw(self,event=None):
        if None not in (self.line_x1,self.line_y1,self.line_x2,self.line_y2):
            event.widget.create_rectangle(self.line_x1,self.line_y1,self.line_x2,self.line_y2,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
            self.draw.rectangle([(self.line_x1,self.line_y1),(self.line_x2,self.line_y2)],fill=self.stroke_color.get(),outline=self.stroke_color.get())
    
    def text_draw(self,event=None):
        text_font = font.Font(family=self.text_font.get(),
                                        size=self.text_size.get(),
                                        weight=self.text_weight.get(),
                                        slant=self.text_slant.get(),underline=self.text_underline.get())
        text = simpledialog.askstring("Input","Enter Text",parent=root)
        if text:
            event.widget.create_text(event.x,event.y,fill=self.stroke_color.get(),font=text_font,text=text)
            
            
    def oval_draw(self,event=None):
        if None not in (self.line_x1,self.line_y1,self.line_x2,self.line_y2):
            event.widget.create_oval(self.line_x1,self.line_y1,self.line_x2,self.line_y2,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
            self.draw.ellipse([(self.line_x1,self.line_y1),(self.line_x2,self.line_y2)],fill=self.stroke_color.get(),outline=self.stroke_color.get())
        
    def arc_draw(self,event=None):
        if None not in (self.line_x1,self.line_y1,self.line_x2,self.line_y2):
            coords = self.line_x1,self.line_y1,self.line_x2,self.line_y2
            event.widget.create_arc(coords,start=0,extent=180,style=ARC,fill=self.stroke_color.get())
            self.draw.arc([(self.line_x1,self.line_y1),(self.line_x2,self.line_y2)],start=0,end=180,style=ARC,fill=self.stroke_color.get())
    
    def clear_up(self,event=None):
        self.canvas.delete("all")
        self.logger += f"Canvas cleared.\n"
        
    def bind_shortcuts(self):
        root.bind("<Command-s>",self.save_file)
        root.bind("<Command-o>",self.open_file)
        root.bind("<Command-Key-1>",lambda e: self.drawing_tool.set("Pencil"))
        root.bind("<Command-Key-2>",lambda e: self.drawing_tool.set("Line"))
        root.bind("<Command-Key-3>",lambda e: self.drawing_tool.set("Arc"))
        root.bind("<Command-Key-4>",lambda e: self.drawing_tool.set("Rectangle"))
        root.bind("<Command-Key-5>",lambda e: self.drawing_tool.set("Oval"))
        root.bind("<Command-Key-6>",lambda e: self.drawing_tool.set("Text"))
        
        root.bind("<Command-l>",lambda e: print(self.logger))
        
        root.bind("<Command-equal>",self.increment_size)
        root.bind("<Command-minus>",self.decrease_size)
        
        root.bind("<Command-b>",lambda e: self.text_weight.set("bold") if self.text_weight.get()=="normal" else self.text_weight.set("normal"))
        root.bind("<Command-i>",lambda e: self.text_slant.set("italic") if self.text_slant.get()=="roman" else self.text_slant.set("roman"))
        root.bind("<Command-u>",lambda e: self.text_underline.set(1) if self.text_underline.get()==0 else self.text_underline.set(0))
        self.canvas.bind("<Command-c>",self.clear_up)
        
    def bind_events(self):
        self.canvas.bind("<Motion>",self.motion)
        self.canvas.bind("<ButtonPress-1>",self.lmb_down)
        self.canvas.bind("<ButtonRelease-1>",self.lmb_up)
        
    def setup_tools(self):
        self.text_weight.set("normal")
        self.text_slant.set("roman")
        self.text_underline.set(0)
        self.text_font.set("Times")
        self.text_size.set(16)
        self.drawing_tool.set("Pencil")
        self.stroke_size.set(3)
        self.stroke_color.set("#000000")
        self.fill_color.set("")
        
    def __init__(self,root):
        self.text_font = StringVar()
        self.text_size = IntVar()
        
        self.text_weight = StringVar()
        self.text_slant = StringVar()
        self.text_underline = IntVar()
        
        self.drawing_tool = StringVar()
        self.stroke_size = IntVar()
        self.fill_color = StringVar()
        self.stroke_color = StringVar()
        
        self.canvas.pack(fill="both", expand=True)
        self.canvas.focus_force()
        self.setup_tools()
        self.setup_menu_bar()
        self.bind_shortcuts()
        self.bind_events()
        
#MAIN WINDOW CONFIG
x_pos = int(root.winfo_screenwidth() / 4)
y_pos = int(root.winfo_screenheight() / 6)
root.geometry(f"800x600+{x_pos}+{y_pos}")
root.title("Paint App")

app = Painter(root)

# Check if we're on OS X, first.
if platform == 'darwin':
    from Foundation import NSBundle
    bundle = NSBundle.mainBundle()
    if bundle:
        info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
        if info and info['CFBundleName'] == 'Python':
            info['CFBundleName'] = "PaintApp"

root.mainloop()
