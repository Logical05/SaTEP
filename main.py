from sys                               import exit
from os.path                           import exists
from browsers                          import browsers
from shutil                            import copy, rmtree
from PIL                               import Image, ImageTk
from tkinter                           import Label, Tk, Button, Menu, Toplevel, messagebox, Frame, Entry
from numpy                             import ndarray, array, arange, zeros
from numpy.random                      import randint
from webbrowser                        import open_new
from selenium.webdriver                import EdgeOptions, Edge, ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service   import Service as EdgeService
from webdriver_manager.chrome          import ChromeDriverManager
from webdriver_manager.microsoft       import EdgeChromiumDriverManager

class Function:
    def __init__(self) -> None:
        self.root     = None
        self.driver   = None
        self.path     = 'data/driver.exe'
        self.notExist = False

    def SetRoot(self, root) -> None:
        self.root = root

    def Label(self, text, column, row, columnspan=1, rowspan=1, padx=0, pady=5) -> None:
        Label(self.root, text=text).grid(column=column,         row=row,
                                         columnspan=columnspan, rowspan=rowspan,
                                         padx=padx,             pady=pady)

    def Button(self, text, command, column, row, columnspan=1, rowspan=1, padx=10, pady=5, ipadx=0, ipady=0, bg="white") -> None:
        Button(self.root, text=text,  command=command, bg=bg).grid(column=column,         row=row, 
                                                                   columnspan=columnspan, rowspan=rowspan, 
                                                                   padx=padx,             pady=pady,
                                                                   ipadx=ipadx,           ipady=ipady)

    def SetDriver(self, driver) -> None:
        self.driver = driver

    def Start(self, column, row) -> None:
        for i in arange(len(row)):
            command = f"""document.querySelector("input[id='{column[row[i]]}{i+1}']").checked = true;"""
            self.driver.execute_script(command)

    def Copy(self, column, numRow) -> ndarray:
        output = []
        for i in arange(numRow):
            for j in arange(len(column)):
                command = f"""return document.querySelector("input[id='{column[j]}{i+1}']").checked;"""
                if self.driver.execute_script(command):
                    output.append(j)
                    break
        return array(output)

    def SavePath(self, driverManager) -> None:
        try:
            self.notExist = not exists(self.path)
            if self.notExist:
                newPath = driverManager.install()
                copy(newPath, self.path)
                self.path = newPath
                return
        except: messagebox.showerror("ERROR", " 1. ปิดโปรแกรมแล้วเปิดใหม่\n 2. เช็คว่า Wifi เชื่อมไหม\n 3. ลบแล้วโหลดใหม่")

class GUI(Function):
    def __init__(self) -> None:
        super().__init__()
        self.GUI = Tk()
        self.GUI.iconbitmap("data/logo.ico")
        self.GUI.title("SaTEP")
        self.GUI.geometry("380x205")
        self.GUI.resizable(width=False, height=False)
        self.driver = None

    def Root(self, root) -> None:
        root.grid()
        self.Menu()
        self.SetRoot(root)

    def Menu(self) -> None:
        menuBar = Menu(self.GUI)
        self.GUI.config(menu=menuBar)
        menuBar.add_cascade(label="About",  command=self.About)
        menuBar.add_cascade(label="Donate", command=self.Donate)

    def About(self) -> None:
        about = Toplevel(self.GUI)
        about.iconbitmap("data/logo.ico")
        about.title("About")
        about.geometry("450x100")
        about.resizable(width=False, height=False)
        Label(about, text="Semi-automatic Teacher Evaluation Program (SaTEP) for CKK.").place(relx=0.01, rely=0)
        y      = [0.3, 0.5, 0.7]
        text   = ["Authors : Logical05",
                    "Community : ASSEMBLY",
                    "Copyright & License :"]
        links  = [["https://www.github.com/Logical05",                       0.245],
                    ["https://discord.gg/Gtn9DN5UF5",                          0.309],
                    ["https://github.com/Logical05/SaTEP/blob/master/LICENSE", 0.272]]
        labels = [Label(about, text=links[i][0], fg="blue", cursor="hand2") for i in arange(3)]
        for i in arange(3):
            Label(about, text=text[i]).place(relx=0.01, rely=y[i])
            labels[i].place(relx=links[i][1], rely=y[i])
        labels[0].bind("<Button-1>", lambda a: open_new(links[0][0]))
        labels[1].bind("<Button-1>", lambda a: open_new(links[1][0]))
        labels[2].bind("<Button-1>", lambda a: open_new(links[2][0]))
        about.mainloop()

    def Donate(self) -> None:
        donate = Toplevel(self.GUI)
        donate.iconbitmap("data/logo.ico")
        donate.title("Donate")
        donate.resizable(width=False, height=False)
        image = ImageTk.PhotoImage(Image.open("data/qr.png"))
        Label(donate, image=image).pack()
        donate.mainloop()

    def Web(self) -> None:
        for browser in browsers():
            type = browser["browser_type"]
            if type == "chrome":
                options = ChromeOptions()
                options.add_experimental_option("detach", True)
                self.SavePath(ChromeDriverManager())
                self.driver = Chrome(service=ChromeService(self.path), options=options)
                break
            if type == "msedge":
                options = EdgeOptions()
                options.add_experimental_option("detach", True)
                self.SavePath(EdgeChromiumDriverManager())
                self.driver = Edge(service=EdgeService(self.path), options=options)
                break
        else:
            messagebox.showerror("ERROR", "ไปโหลด Chrome หรือ Microsoft Edge ก่อน")
            exit()
        
        self.SetDriver(self.driver)
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.chakkham.info/site/signin/")

class Main(GUI):
    def __init__(self) -> None:
        super().__init__()
        self.Y    = None
        self.year = ""
        self.ETc  = ['a', 'b', 'c']
        self.ETr  = zeros(25, dtype=int)

        self.Web()
        self.MM(self.GUI)
        self.GUI.mainloop()

        self.driver.quit()
        if self.notExist:
            index = self.path.find(".wdm") + 4
            rmtree(self.path[:index])
    
    def ToPage(self, page, y="") -> None:
        self.year = y
        for widget in self.GUI.winfo_children():
            widget.destroy()
        pages = [self.MM, self.C, self.ET]
        pages[page](self.GUI)

    def CopyStart(self, column, numRow, radios, page0=True, format='Y') -> None:
        try:
            url = self.driver.current_url
            self.CheckURL(url)
            if self.driver.execute_script("""return document.getElementsByClassName("regular-radio").length""") != radios:
                raise
            index = url.find("&ChYear=")
            if index != -1:
                url = url[:index]
            y = self.year
            if page0:
                y = self.Y.get()[:4]
            if format != 'Y':
                y = "1/" + y
            self.driver.get(url + "&ChYear=" + y)
            row = self.Copy(column, numRow)
            self.driver.back()
            self.Start(column, row)
        except: messagebox.showerror("ERROR", "เลือกการประเมินที่ถูกต้องที่ต้องการจะประเมิน")

    def CheckURL(self, url) -> None:
        if url.find("?feature=") == -1 or url.find("notification") != -1 or url.find("profile") != -1:
            messagebox.showerror("ERROR", "เปิดหน้าแบบประเมินที่ต้องการจะประเมินก่อน")

    def MM(self, root) -> None:
        MM = Frame(root)
        self.Root(MM)
        self.Label("ปีที่ต้องการจะ Copy : ", 0, 0)
        self.Y = Entry(self.GUI)
        self.Y.place(relx=0.39, rely=0.045)
        self.Button("วิเคราะห์นักเรียนตามทฤษฎีพหุปัญญา", lambda : self.CopyStart(['a', 'b'],                 40, 80),
                    0, 4)
        self.Button("ประเมินพฤติกรรม",               lambda : self.CopyStart(['a', 'b', 'c'],           25, 107, format="T/Y"), 
                    0, 2)
        self.Button("วิเคราะห์ผู้เรียนรายบุคคล 5 ด้าน",    lambda : self.CopyStart(['a', 'b', 'c'],           16, 48),
                    1, 4)
        self.Button("ประเมินความฉลาดทางอารมณ์",      lambda : self.CopyStart(['a', 'b', 'c', 'd'],      52, 208), 
                    0, 5)
        self.Button("วิเคราะห์นักเรียนแบบกราชา",        lambda : self.CopyStart(['a', 'b', 'c', 'd', 'e'], 60, 300), 
                    0, 3)
        self.Button("วิเคราะห์นักเรียนแบบเดวิด เอ คอล์บ", lambda : self.CopyStart(['a', 'b', 'c', 'd', 'e'], 32, 160), 
                    1, 3)
        self.Button("ประเมินตนเอง -->",             lambda : self.ToPage(1, self.Y.get()[:4]), 1, 2)
        self.Button("ประเมินครู -->",                lambda : self.ToPage(2, self.Y.get()[:4]), 1, 5)

    def C(self, root) -> None:
        SE = Frame(root)
        self.Root(SE)
        self.Label("*** ใส่ปีที่ต้องการจะ Copy ในหน้าแรกด้วย ***", 0, 0, 2)
        self.Label("ภาคปฏิบัติ",   0, 1, padx=70)
        self.Label("ภาคความรู้สึก", 1, 1, padx=70)
        self.Button("Start",      lambda : self.CopyStart([f"capacity{i}" for i in arange(3)],    42, 126, False),
                    0, 2, ipadx=10, bg="#3bb14e")
        self.Button("Start",      lambda : self.CopyStart([f"capacity{i}" for i in arange(1, 6)], 30, 150, False),
                    1, 2, ipadx=10, bg="#3bb14e")
        self.Button("<--   Back", lambda : self.ToPage(0), 0, 3, 2, pady=15, ipadx=15)

    def StartET(self, column, row) -> None:
        try: 
            url = self.driver.current_url
            self.CheckURL(url)
            self.Start(column, row)
        except: messagebox.showerror("ERROR", "Start ให้ถูกที่ หรือไป Copy มาก่อน")

    def CopyET(self) -> None:
        try: 
            url = self.driver.current_url
            self.CheckURL(url)
            self.ETr = self.Copy(self.ETc, 25)
        except: messagebox.showerror("ERROR", "Copy ให้ถูกที่")

    def ET(self, root) -> None:
        ET = Frame(root)
        self.Root(ET)
        self.Label(f"*** อ่านวิธีใช่ที่                         ***", 0, 0, 2)
        link = Label(ET, text="README.md", fg="blue", cursor="hand2")
        link.place(relx=0.47, rely=0.027)
        link.bind("<Button-1>", lambda a : open_new("https://github.com/Logical05/SaTEP/blob/master/README.md"))
        self.Button("Copy",                self.CopyET,
                    0, 1, 2, pady=10, ipadx=15)
        self.Button("Start",      lambda : self.StartET(self.ETc, self.ETr),
                    0, 2, padx=65, pady=10, ipadx=15, bg="#3bb14e")
        self.Button("Random",     lambda : self.StartET(self.ETc, [randint(0, 3, dtype=int) for _ in arange(25)]),
                    1, 2, padx=65, pady=10, ipadx=5, bg="#3bb14e")
        self.Button("<--   Back", lambda : self.ToPage(0), 0, 3, 2, pady=10, ipadx=15)

if __name__ == "__main__":
    Main()