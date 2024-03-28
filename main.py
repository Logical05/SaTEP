from sys                                 import exit
from os.path                             import exists
from browsers                            import browsers
from shutil                              import copy, rmtree
from numpy                               import ndarray, array, arange, arange, zeros, ndarray
from numpy.random                        import randint
from PIL                                 import Image
from PIL.ImageTk                         import PhotoImage
from tkinter                             import Label, Menu, Tk, Button, Toplevel, messagebox, Frame, Entry, TclError
from webbrowser                          import open_new
from selenium.webdriver                  import EdgeOptions, Edge, ChromeOptions, Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service   import Service as ChromeService
from selenium.webdriver.edge.service     import Service as EdgeService
from webdriver_manager.chrome            import ChromeDriverManager
from webdriver_manager.microsoft         import EdgeChromiumDriverManager

class Web():
    def __init__(self) -> None:
        self.driver  : WebDriver = None
        self.notExist: bool      = False
        self.path    : str       = "data/driver.exe"
        self.year    : str       = ""

    def Start(self, column: list, row: ndarray, radios: int) -> None:
        """Process การประเมินแบบอัตโนมัติ"""
        try:
            # Check ว่าจำนวนช่องที่จะประเมินตรงกับแบบประเมินไหม
            if self.driver.execute_script("""return document.getElementsByClassName("regular-radio").length""") != radios:
                raise
            for i in arange(len(row)):
                # Command ที่ใช้ในการเปลี่ยน Status ของช่องประเมิน
                command = f"""document.querySelector("input[id='{column[row[i]]}{i+1}']").checked = true;"""
                self.driver.execute_script(command)
        except: messagebox.showerror("ERROR", "เลือกการประเมินที่ถูกต้องที่ต้องการจะประเมิน")

    def Copy(self, column: list, numRow: int, radios: int) -> ndarray:
        """Process การ Copy แบบอัตโนมัติ"""
        try:
            # Check ว่าจำนวนช่องที่จะ Copy ตรงกับแบบประเมินไหม
            if self.driver.execute_script("""return document.getElementsByClassName("regular-radio").length""") != radios:
                raise
            output: list = []
            for i in arange(numRow):
                for j in arange(len(column)):
                    # Command ที่ใช้ในอ่าน Status ของช่องประเมิน
                    command: str = f"""return document.querySelector("input[id='{column[j]}{i+1}']").checked;"""
                    if self.driver.execute_script(command):
                        output.append(j)
                        break
            return array(output)
        except: messagebox.showerror("ERROR", "เลือกการประเมินที่ถูกต้องที่ต้องการจะประเมิน")

    def SavePath(self, driverManager: ChromeDriverManager|EdgeChromiumDriverManager) -> None:
        """Procoess ในการย้ายตำแหน่งของ Webdriver จาก C:\Users\ชื่อเครื่อง\.wdm มาที่ตำแหน่งที่ติดตั้งโปรแกรมนี้"""
        try:
            self.notExist = not exists(self.path)
            if self.notExist:
                newPath: str = driverManager.install()
                copy(newPath, self.path)
                self.path = newPath
                return
        except: messagebox.showerror("ERROR", " 1. ปิดโปรแกรมแล้วเปิดใหม่\n 2. เช็คว่า Wifi เชื่อมไหม\n 3. ลบแล้วโหลดใหม่")

    def WebGUI(self) -> None:
        """Procoess ในการหาว่าในเครื่องมี Webbrowser ตัวไหนบ้าง พร่อมกับใช้ Webbrowser นั้น"""
        for browser in browsers():
            type: str = browser["browser_type"]
            if type == "chrome":
                options: ChromeOptions = ChromeOptions()
                options.add_experimental_option("detach", True)
                self.SavePath(ChromeDriverManager())
                self.driver = Chrome(service=ChromeService(self.path), options=options)
                break
            if type == "msedge":
                options: EdgeOptions = EdgeOptions()
                options.add_experimental_option("detach", True)
                self.SavePath(EdgeChromiumDriverManager())
                self.driver = Edge(service=EdgeService(self.path), options=options)
                break
        else:
            messagebox.showerror("ERROR", "ไปโหลด Chrome หรือ Microsoft Edge ก่อน")
            exit()
        
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.chakkham.info/site/signin/")

    def QuitWeb(self) -> None:
        """Procoess ในการปิด Webbrowser แล้วถ้าเป็นการเปิดโปรแกรมครั้งแรกจะทำการลบ Webdriver ที่ C:\Users\ชื่อเครื่อง\.wdm"""
        self.driver.quit()
        if self.notExist: 
            rmtree(self.path[:(self.path.find(".wdm") + 4)])

    def CopyStart(self, column: list, numRow: int, radios: int, format: str) -> None:
        """Process การ Copy และประเมินแบบอัตโนมัติ"""
        try:
            if self.CheckURL():
                return
            # Check ว่าจำนวนช่องที่จะประเมินตรงกับแบบประเมินไหม
            if self.driver.execute_script("""return document.getElementsByClassName("regular-radio").length""") != radios:
                raise
            url  : str = self.driver.current_url
            index: int = url.find("&ChYear=")
            if index != -1:
                url = url[:index]
            y: str = self.year
            if format != 'Y':
                y = "1/" + y
            self.driver.get(url + "&ChYear=" + y)
            row: ndarray = self.Copy(column, numRow, radios)
            self.driver.back()
            self.Start(column, row, radios)
        except: messagebox.showerror("ERROR", "เลือกการประเมินที่ถูกต้องที่ต้องการจะประเมิน")

    def CheckURL(self) -> bool:
        """Process ในการ Check ว่าอยู่หน้าที่ต้องประเมินยัง"""
        url: str = self.driver.current_url
        if isFind := url.find("?feature=") == -1 or url.find("notification") != -1 or url.find("profile") != -1:
            messagebox.showerror("ERROR", "เปิดหน้าแบบประเมินที่ต้องการจะประเมินก่อน")
        return isFind
    
class Main(Web):
    def __init__(self) -> None:
        super().__init__()
        self.GUI : Tk    = Tk()
        self.root: Frame = Frame()
        self.year: str   = ""
        self.ETc : list  = ['a', 'b', 'c']
        self.ETr : ndarray = zeros(25, dtype=int)
        self.GUI.iconbitmap("data/logo.ico")
        self.GUI.title("SaTEP")
        self.GUI.geometry("380x205")
        self.GUI.resizable(width=False, height=False)

        self.WebGUI()
        self.MM(self.GUI)
        self.GUI.mainloop()
        
        self.QuitWeb()
    
    def Root(self, root: Frame) -> None:
        """กำหนดประเภท root กับใส่ Menu bar"""
        self.root: Frame = root
        root.grid()
        self.Menu()

    def Label(self, text: str, column: int, row: int, columnspan: int=1, rowspan: int=1, 
                                                      padx      : int=0, pady   : int=5) -> None:
        """Label Gadgets แบบย่อ"""
        Label(self.root, text=text).grid(column=column,         row=row,
                                         columnspan=columnspan, rowspan=rowspan,
                                         padx=padx,             pady=pady)

    def Button(self, text: str, command, column: int, row: int, columnspan: int=1,  rowspan: int=1, 
                                                                padx      : int=10, pady   : int=5, 
                                                                ipadx     : int=0,  ipady  : int=0, bg: str="white") -> None:
        """Button Gadgets แบบย่อ"""
        Button(self.root, text=text,  command=command, bg=bg).grid(column=column,         row=row, 
                                                                   columnspan=columnspan, rowspan=rowspan, 
                                                                   padx=padx,             pady=pady,
                                                                   ipadx=ipadx,           ipady=ipady)

    def ToPage(self, page: int, usedYear: bool=False) -> None:
        """เปลี่ยนไปหน้าต่างที่กำหนด"""
        self.year = ""
        if usedYear:
            self.year = self.Y.get()[:4]
        for widget in self.GUI.winfo_children():
            widget.destroy()
        pages: list = [self.MM, self.C, self.ET]
        pages[page](self.GUI)

    def CopyStart(self, column: list, numRow: int, radios: int, format: str='Y') -> None:
        if self.year == "":
            try: self.year = self.Y.get()[:4]
            except TclError: 
                messagebox.showerror("ERROR", "ใส่ปีที่ต้องการจะ Copy ในหน้าแรกด้วย") 
                return
        super().CopyStart(column, numRow, radios, format)

    def MM(self, root: Tk) -> None:
        """หน้าต่างหลัก"""
        MM: Frame = Frame(root)
        self.Root(MM)
        self.Label("ปีที่ต้องการจะ Copy : ", 0, 0)
        self.Y : Entry = Entry(MM)
        self.Y.place(relx=0.39, rely=0.045)
        self.Button("วิเคราะห์นักเรียนตามทฤษฎีพหุปัญญา",  lambda : self.CopyStart(['a', 'b'],                40, 80),
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
        self.Button("ประเมินตนเอง -->",             lambda : self.ToPage(1, True), 1, 2)
        self.Button("ประเมินครู -->",                lambda : self.ToPage(2), 1, 5)

    def C(self, root: Tk) -> None:
        """หน้าต่างประเมินตนเอง"""
        SE: Frame = Frame(root)
        self.Root(SE)
        self.Label("*** ใส่ปีที่ต้องการจะ Copy ในหน้าแรกด้วย ***", 0, 0, 2)
        self.Label("ภาคปฏิบัติ",   0, 1, padx=70)
        self.Label("ภาคความรู้สึก", 1, 1, padx=70)
        self.Button("Start",      lambda : self.CopyStart([f"capacity{i}" for i in arange(3)],    42, 126),
                    0, 2, ipadx=10, bg="#3bb14e")
        self.Button("Start",      lambda : self.CopyStart([f"capacity{i}" for i in arange(1, 6)], 30, 150),
                    1, 2, ipadx=10, bg="#3bb14e")
        self.Button("<--   Back", lambda : self.ToPage(0), 0, 3, 2, pady=15, ipadx=15)

    def StartET(self, row: ndarray) -> None:
        """ปุ่ม Start เฉพาะของประเมินครู"""
        try:
            if self.CheckURL():
                return
            self.Start(self.ETc, row, 75)
        except: messagebox.showerror("ERROR", "Start ให้ถูกที่ หรือไป Copy มาก่อน")

    def CopyET(self) -> None:
        """ปุ่ม Copy เฉพาะของประเมินครู"""
        try: 
            if self.CheckURL():
                return
            self.ETr = self.Copy(self.ETc, 25, 75)
        except: messagebox.showerror("ERROR", "Copy ให้ถูกที่")

    def ET(self, root) -> None:
        """หน้าต่างประเมินครู"""
        ET: Frame = Frame(root)
        self.Root(ET)
        self.Label(f"*** อ่านวิธีใช่ที่                         ***", 0, 0, 2)
        link = Label(ET, text="README.md", fg="blue", cursor="hand2")
        link.place(relx=0.47, rely=0.027)
        link.bind("<Button-1>", lambda a : open_new("https://github.com/Logical05/SaTEP/blob/master/README.md"))
        self.Button("Copy",                self.CopyET,
                    0, 1, 2, pady=10, ipadx=15)
        self.Button("Start",      lambda : self.StartET(self.ETr),
                    0, 2, padx=65, pady=10, ipadx=15, bg="#3bb14e")
        self.Button("Random",     lambda : self.StartET([randint(0, 3, dtype=int) for _ in arange(25)]),
                    1, 2, padx=65, pady=10, ipadx=5, bg="#3bb14e")
        self.Button("<--   Back", lambda : self.ToPage(0), 0, 3, 2, pady=10, ipadx=15)

    def Menu(self) -> None:
        """Menu Bar"""
        menuBar = Menu(self.GUI)
        self.GUI.config(menu=menuBar)
        menuBar.add_cascade(label="About",  command=self.About)
        menuBar.add_cascade(label="Donate", command=self.Donate)

    def About(self) -> None:
        """หน้าต่าง About"""
        about : Toplevel        = Toplevel(self.GUI)
        y     : list[float]     = [0.3, 0.5, 0.7]
        text  : list[str]       = ["Authors : Logical05",
                                   "Community : ASSEMBLY",
                                   "Copyright & License :"]
        links : list[list[str]] = [["https://www.github.com/Logical05",                       "0.245"],
                                   ["https://discord.gg/Gtn9DN5UF5",                          "0.309"],
                                   ["https://github.com/Logical05/SaTEP/blob/master/LICENSE", "0.272"]]
        labels: list[Label]     = [Label(about, text=links[i][0], fg="blue", cursor="hand2") for i in arange(3)]
        about.iconbitmap("data/logo.ico")
        about.title("About")
        about.geometry("450x100")
        about.resizable(width=False, height=False)
        Label(about, text="Semi-automatic Teacher Evaluation Program (SaTEP) for CKK.").place(relx=0.01, rely=0)
        for i in arange(3):
            Label(about, text=text[i]).place(relx=0.01, rely=y[i])
            labels[i].place(relx=links[i][1], rely=y[i])
        labels[0].bind("<Button-1>", lambda a: open_new(links[0][0]))
        labels[1].bind("<Button-1>", lambda a: open_new(links[1][0]))
        labels[2].bind("<Button-1>", lambda a: open_new(links[2][0]))
        about.mainloop()

    def Donate(self) -> None:
        """หน้าต่าง Donate"""
        donate: Toplevel   = Toplevel(self.GUI)
        image : PhotoImage = PhotoImage(Image.open("data/qr.png"))
        donate.iconbitmap("data/logo.ico")
        donate.title("Donate")
        donate.resizable(width=False, height=False)
        Label(donate, image=image).pack()
        donate.mainloop()

if __name__ == "__main__":
    Main()
