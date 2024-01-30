from os.path                           import exists
from browsers                          import browsers
from shutil                            import copy, rmtree
from csv                               import reader, writer
from PIL                               import Image, ImageTk
from tkinter                           import Label, IntVar, Radiobutton, Tk, Button, Menu, Toplevel, messagebox
from numpy                             import ndarray, array, arange
from numpy.random                      import randint
from webbrowser                        import open_new
from selenium.webdriver                import EdgeOptions, Edge, ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service   import Service as EdgeService
from webdriver_manager.chrome          import ChromeDriverManager
from webdriver_manager.microsoft       import EdgeChromiumDriverManager

class SaTEP:
    def Label(self) -> None:
        text = array(["Good", "Moderate", "Little"])
        for i in arange(3):
            Label(self.root, text=text[i], bg=self.bg).grid(column=i+1, row=0)
            Label(self.root, text=text[i], bg=self.bg).grid(column=i+5, row=0)

    def TextRadio(self, text, var, St_col, col, row) -> None:
        Label(self.root, text=text, bg=self.bg).grid(column=St_col, row=row)
        val = 0
        for i in arange(St_col+1, St_col+col):
            Radiobutton(self.root, borderwidth=3, variable=var, value=val, bg=self.bg).grid(column=i, row=row)
            val += 1

    def Choice(self) -> None:
        self.choice = array([IntVar() for _ in arange(25)])
        for i in arange(1, 14):
            self.TextRadio(f"    {i}   ", self.choice[i-1], 0, 4, i)
            if i != 13:
                self.TextRadio(f"    {i+13}   ", self.choice[i+12], 4, 4, i)

    def GetChoice(self) -> ndarray:
        return array([self.choice[i].get() for i in arange(25)])

    def Check(self) -> None:
        try:
            column = array(["a", "b", "c"])
            choice = self.GetChoice()
            for i in arange(25):
                command = f"""document.querySelector("td[class='details input'] input[id='{column[choice[i]]}{i+1}']").checked = true;"""
                self.driver.execute_script(command)
        except: pass

    def Save(self) -> None:
        with open(self.saveCSV, mode='w') as csvFile:
            csv_writer = writer(csvFile)
            csv_writer.writerow(self.GetChoice())

    def Load(self) -> None:
        with open(self.saveCSV, mode='r') as csvFile:
            for row in reader(csvFile):
                if not row: return
                for col in arange(25):
                    self.choice[col].set(row[col])

    def Random(self) -> None:
        for col in arange(25):
            self.choice[col].set(randint(0, 3, dtype=int))

    def SavePath(self, driverManager) -> ndarray:
        driverPath = "data/driver.exe"
        if exists(driverPath):
            return array([driverPath, "True"])
        path = driverManager.install()
        copy(path, driverPath)
        return array([path, "False"])
    
    def About(self) -> None:
        about       = Toplevel(self.root)
        about['bg'] = self.bg
        about.iconbitmap("data/point.ico")
        about.title("About")
        about.geometry("450x100")
        about.resizable(width=False, height=False)
        Label(about, text="Semi-automatic Teacher Evaluation Program (SaTEP) for CKK.", bg=self.bg).place(relx=0.01, rely=0)
        y      = [0.3, 0.5, 0.7]
        text   = ["Authors : Logical05",
                  "Community : ASSEMBLY",
                  "Copyright & License :"]
        links  = [["https://www.github.com/Logical05",                       0.245],
                  ["https://discord.gg/Gtn9DN5UF5",                          0.309],
                  ["https://github.com/Logical05/SaTEP/blob/master/LICENSE", 0.272]]
        labels = [Label(about, text=links[i][0], fg="blue", bg=self.bg, cursor="hand2") for i in arange(3)]
        for i in arange(3):
            Label(about, text=text[i], bg=self.bg).place(relx=0.01, rely=y[i])
            labels[i].place(relx=links[i][1], rely=y[i])
        labels[0].bind("<Button-1>", lambda a: open_new(links[0][0]))
        labels[1].bind("<Button-1>", lambda a: open_new(links[1][0]))
        labels[2].bind("<Button-1>", lambda a: open_new(links[2][0]))

    def Donate(self) -> None:
        donate = Toplevel(self.root)
        donate.iconbitmap("data/point.ico")
        donate.title("Donate")
        donate.resizable(width=False, height=False)
        image = ImageTk.PhotoImage(Image.open("data/QR.png"))
        Label(donate, image=image).pack()
        donate.mainloop()

    def SaTEP(self) -> None:
        self.root       = Tk()
        self.root['bg'] = self.bg
        self.root.iconbitmap("data/point.ico")
        self.root.title("SaTEP")
        self.root.geometry("340x475")
        self.root.resizable(width=False, height=False)
        self.Label()
        self.Choice()
        Button(self.root, text="Start",  command=self.Check, bg="green").place(relx=0.5,  rely=0.85, anchor="center")
        Button(self.root, text="Save",   command=self.Save             ).place(relx=0.25, rely=0.85, anchor="center")
        Button(self.root, text="Load",   command=self.Load             ).place(relx=0.75, rely=0.85, anchor="center")
        Button(self.root, text="Random", command=self.Random           ).place(relx=0.5,  rely=0.93, anchor="center")
        menuBar = Menu(self.root)
        self.root.config(menu=menuBar)
        menuBar.add_cascade(label="About",  command=self.About)
        menuBar.add_cascade(label="Donate", command=self.Donate)
        
        self.root.mainloop()

    def GUI(self) -> None:
        for browser in browsers():
            type = browser["browser_type"]
            if type == "chrome":
                options = ChromeOptions()
                options.add_experimental_option("detach", True)
                path, exist = self.SavePath(ChromeDriverManager())
                self.driver = Chrome(service=ChromeService(path), options=options)
                break
            if type == "msedge":
                options = EdgeOptions()
                options.add_experimental_option("detach", True)
                path, exist = self.SavePath(EdgeChromiumDriverManager())
                self.driver = Edge(service=EdgeService(path), options=options)
                break
        else:
            messagebox.showerror("ERROR", "Please install Chrome or Microsoft Edge.")
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.chakkham.info/site/signin/")
        
        self.bg      = "#dedede"
        self.saveCSV = "data/save.csv"
        self.SaTEP()

        self.driver.quit()
        if (exist == "False"):
            index = path.find(".wdm") + 4
            rmtree(path[:index])

if __name__ == "__main__":
    SaTEP().GUI()