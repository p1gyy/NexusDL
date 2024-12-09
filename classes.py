import threading
from tkinter import *
from tkinter import ttk
from time import sleep

class ModDownloader:
    def __init__(self):
        pass

class ProgressBarGUI:
    def __init__(self, threadCount, totalmodcount):
        self.threadCount = threadCount
        self.titleFont = ("Segoe UI", 14, "bold")
        self.modsDownloaded = 0
        self.totalmodcount = totalmodcount

        self.root = Tk()
        self.root.title("NexusDL - Downloading mods...")
        self.root.iconbitmap("icon.ico")

        #self.root.geometry("400x")
        self.root.resizable(0,0)

        self.root.protocol("WM_DELETE_WINDOW", self.disable_event)

        self.threadLabels = []
        self.threadProgress = []

        #widgets
        Label(self.root, text="Mods currently downloading", font=self.titleFont).grid(row=0, column=0, padx=5, pady=5, sticky='w')

        for i in range(threadCount):
            lbl = Label(self.root, text=f"{i + 1}: Idle")
            lbl.grid(row=i + 1, column=0, padx=15, pady=0, sticky='w')
            self.threadLabels.append(lbl)
        
        Label(self.root, text="Downloads", font=self.titleFont).grid(row=threadCount + 1, column=0, padx=5, pady=5, sticky='w')

        for i in range(threadCount):
            bar = ttk.Progressbar(self.root, orient="horizontal", length=370, mode="determinate")
            bar.grid(row=threadCount + i + 2, column=0, padx=15, pady=1, sticky='w')
            self.threadProgress.append(bar)

        self.totalMods = Label(self.root, text="Total downloaded: ", font=self.titleFont)
        self.totalMods.grid(row=(threadCount * 2) + 2, column=0, padx=5, pady=(5, 20), sticky='w')

    def mainloop(self, threads):
        mainloopThread = threading.Thread(target=self.mainLoopThreaded,  args=[threads])
        mainloopThread.start()
        self.root.mainloop()
    
    def mainLoopThreaded(self, threads):
        self.threads = threads
        if any(thread.is_alive() for thread in self.threads):
            # main loop
            sleep(1)
        else:
            self.root.destroy()

    def disable_event(self):
        pass

    def updateTotalMods(self):
        self.totalMods.config(text=f"Total downloaded: {self.modsDownloaded}/{self.totalmodcount}")