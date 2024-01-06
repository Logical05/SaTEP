from browsers                          import browsers
from os.path                           import exists
from csv                               import reader, writer
from tkinter                           import Label, IntVar, Radiobutton, Tk, Button, mainloop, messagebox
from numpy                             import ndarray, array, arange
from selenium.webdriver                import EdgeOptions, Edge, ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service   import Service as EdgeService
from webdriver_manager.chrome          import ChromeDriverManager
from webdriver_manager.microsoft       import EdgeChromiumDriverManager

class SaTEP:
    def Label(self) -> None:
        text = array(["Good", "Moderate", "Little"])
        for i in arange(3):
            Label(self.root, text=text[i]).grid(column=i+1, row=0)
            Label(self.root, text=text[i]).grid(column=i+5, row=0)

    def TextRadio(self, text, var, St_col, col, row) -> None:
        Label(self.root, text=text).grid(column=St_col, row=row)
        val = 0
        for i in arange(St_col+1, St_col+col):
            Radiobutton(self.root, borderwidth=3, variable=var, value=val).grid(column=i, row=row)
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
            self.Stbutton["state"] = "disabled"
            column = array(["a", "b", "c"])
            choice = self.GetChoice()
            for i in arange(25):
                command = f"""document.querySelector("td[class='details input'] input[id='{column[choice[i]]}{i+1}']").checked = true;"""
                self.driver.execute_script(command)
            self.Stbutton["state"] = "normal"
        except:
            self.Stbutton["state"] = "normal"

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

    def SavePath(self, driverManager) -> str:
        driverCSV = "data/driverpath.csv"
        with open(driverCSV, mode='r+') as csvFile:
            driverPath = csvFile.read()
            if exists(driverPath):
                return driverPath
            path = driverManager.install()
            csvFile.write(path)
            return path

    def GUI(self) -> None:
        for browser in browsers():
            type = browser["browser_type"]
            if type == "chrome":
                options = ChromeOptions()
                options.add_experimental_option("detach", True)
                self.driver = Chrome(service=ChromeService(self.SavePath(ChromeDriverManager())), options=options)
                break
            if type == "msedge":
                options = EdgeOptions()
                options.add_experimental_option("detach", True)
                self.driver = Edge(service=EdgeService(self.SavePath(EdgeChromiumDriverManager())), options=options)
                break
        else:
            messagebox.showerror("ERROR", "Please install Chrome or Microsoft Edge.")
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.chakkham.info/site/signin/")

        self.root = Tk()
        self.root.iconbitmap("data/point.ico")
        self.root.title("SaTEP")
        self.root.geometry("340x420")
        self.root.resizable(width=False, height=False)
        self.Label()
        self.Choice()
        self.saveCSV  = "data/save.csv"
        self.Stbutton = Button(self.root, text="Start", command=self.Check, bg="green")
        self.Sabutton = Button(self.root, text="Save",  command=self.Save)
        self.Lobutton = Button(self.root, text="Load",  command=self.Load)  
        self.Stbutton.place(relx=0.5,  rely=0.93, anchor="center")
        self.Sabutton.place(relx=0.25, rely=0.93, anchor="center")
        self.Lobutton.place(relx=0.75, rely=0.93, anchor="center")
        mainloop()

        self.driver.quit()

if __name__ == "__main__":
    SaTEP().GUI()