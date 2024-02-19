from sys                               import exit
from os.path                           import exists
from browsers                          import browsers
from shutil                            import copy, rmtree
from PIL                               import Image, ImageTk
from tkinter                           import Label, Tk, Button, Menu, Toplevel, messagebox, Frame
from numpy                             import ndarray, array, arange, zeros, ones, full
from numpy.random                      import randint
from webbrowser                        import open_new
from selenium.webdriver                import EdgeOptions, Edge, ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service   import Service as EdgeService
from webdriver_manager.chrome          import ChromeDriverManager
from webdriver_manager.microsoft       import EdgeChromiumDriverManager

class SaTEP:
    class Function:
        def __init__(self) -> None:
            self.root     = None
            self.driver   = None
            self.path     = 'data/driver.exe'
            self.notExist = False

        def SetRoot(self, root) -> None:
            self.root = root

        def Label(self, text, column, row, padx=0, pady=5) -> None:
            Label(self.root, text=text).grid(column=column, row=row, padx=padx, pady=pady)

        def Button(self, text, command, column, row, columnspan=1, rowspan=1, padx=0, pady=5, bg="white") -> None:
            Button(self.root, text=text,  command=command, bg=bg).grid(column=column,         row=row, 
                                                                       columnspan=columnspan, rowspan=rowspan, 
                                                                       padx=padx,             pady=pady)

        def SetDriver(self, driver) -> None:
            self.driver = driver

        def Start(self, column, row) -> None:
            try:
                for i in arange(len(row)):
                    command = f"""document.querySelector("input[id='{column[row[i]]}{i+1}']").checked = true;"""
                    self.driver.execute_script(command)
            except: messagebox.showerror("ERROR", "Start ให้ถูกที่ หรือไป Copy มาก่อน")

        def Copy(self, column, numRow) -> ndarray:
            try:
                output = []
                for i in arange(numRow):
                    for j in arange(len(column)):
                        command = f"""return document.querySelector("input[id='{column[j]}{i+1}']").checked;"""
                        if self.driver.execute_script(command):
                            output.append(j)
                            break
                return array(output)
            except: messagebox.showerror("ERROR", "Copy ให้ถูกที่")

        def SavePath(self, driverManager) -> None:
            try:
                self.notExist = not exists(self.path)
                if self.notExist:
                    newPath = driverManager.install()
                    copy(newPath, self.path)
                    self.path = newPath
                    return
            except: pass
    
    class GUI(Function):
        def __init__(self) -> None:
            super().__init__()
            self.GUI = Tk()
            self.GUI.iconbitmap("data/logo.ico")
            self.GUI.title("SaTEP")
            self.GUI.geometry("215x175")
            self.GUI.resizable(width=False, height=False)
            self.driver  = None
            self.pageNum = 1
            self.ETc     = ['a', 'b', 'c']
            self.EYSE1c  = [f"capacity{i}" for i in arange(3)]
            self.EYSE2c  = [f"capacity{i}" for i in arange(1, 6)]
            self.ETr     = zeros(25,    dtype=int)
            self.EYSE1r  = ones (42,    dtype=int)
            self.EYSE2r  = full (30, 2, dtype=int)

            self.Web()
            self.ET(self.GUI)
            self.GUI.mainloop()

            self.driver.quit()
            if self.notExist:
                index = self.path.find(".wdm") + 4
                rmtree(self.path[:index])

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

        def ChangePage(self) -> None:
            for widget in self.GUI.winfo_children():
                widget.destroy()
            if self.pageNum == 1:
                self.EYSE(self.GUI)
                self.pageNum = 2
                return
            self.ET(self.GUI)
            self.pageNum = 1

        def StartET(self) -> None:
            self.Start(self.ETc, self.ETr)
        
        def CopyET(self) -> None:
            self.ETr = self.Copy(self.ETc, 25)

        def Random(self) -> None:
            self.Start(self.ETc, [randint(0, 3, dtype=int) for _ in arange(25)])

        def ET(self, root) -> None:
            ET = Frame(root)
            ET.grid()
            self.Menu()
            self.SetRoot(ET)
            self.Button("Copy",         self.CopyET,     0, 0, padx=90)
            self.Button("Start",        self.StartET,    0, 1, bg="green")
            self.Button("Random",       self.Random,     0, 2, bg="green")
            self.Button("ประเมินตนเอง ->", self.ChangePage, 0, 3, 2)

        def StartEYSE1(self) -> None:
            self.Start(self.EYSE1c, self.EYSE1r)

        def CopyEYSE1(self) -> None:
            self.EYSE1r = self.Copy(self.EYSE1c, 42)

        def StartEYSE2(self) -> None:
            self.Start(self.EYSE2c, self.EYSE2r)

        def CopyEYSE2(self) -> None:
            self.EYSE2r = self.Copy(self.EYSE2c, 30)

        def EYSE(self, root) -> None:
            EYSE = Frame(root)
            EYSE.grid()
            self.Menu()
            self.SetRoot(EYSE)
            self.Label("ภาคปฏิบัติ",   0, 0, 25)
            self.Label("ภาคความรู้สึก", 1, 0, 25)
            self.Button("Copy",       self.CopyEYSE1,  0, 1)
            self.Button("Start",      self.StartEYSE1, 0, 2, bg="green")
            self.Button("Copy",       self.CopyEYSE2,  1, 1)
            self.Button("Start",      self.StartEYSE2, 1, 2, bg="green")
            self.Button("<- ประเมินครู", self.ChangePage, 0, 3, 2)

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

if __name__ == "__main__":
    SaTEP().GUI()