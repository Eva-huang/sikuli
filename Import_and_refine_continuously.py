# Owner: Eva Huang
# Ctreated date: 2021-06-17
# Comment: import data, then refine and save

import shutil
import os

scanData = []

def readFiles(filePath):
    for filename in os.listdir(filePath):
        if ".scan" in filename:
            scanData.append(os.path.join(filePath, filename))

def importAndRefine():
    application = App.open(r"C:\Program Files\AlliedStar\ScanPro\ScanPro.exe")
    wait("logo.png", FOREVER)
    for i, file in enumerate(scanData):             
        #Import .scan file
        click("menu.png")
        wait("import.png", FOREVER)
        click("import.png")
        type(file)
        type(Key.ENTER)
        type(Key.ENTER)
        while exists("extracting.png"):
            wait(2)
        while exists("loading.png"):
            wait(2)
        wait(1)
        print "Import %s successfully." % repr(file).split('\\')[-1].split('.')[0]

        #Perform refinement
        click("refine.png")
        while exists("refine in progress.png"):
            wait(3)
        wait(2)
        
        #Take screenshot
        regionImage = capture(App.focusedWindow())
        name = repr(file).split('\\')[-1].split('.')[0] + '_screenshot.png'
        shutil.move(regionImage, os.path.join(r"D:\sikuli\Screenshots", name))
        wait(2)

        #Save STL file to local
        click("finish.png")
        wait(1)

        click(Location(642, 368))
        type(str(i+1))
        type(Key.TAB)
        type(str(i+1))
        wait(1)
        click("save_local.png")
        wait(1)
        click("save_button.png")
        wait(1)
        click("yes_button.png")
        while exists("wait_process.png"):
            wait(2)
    os.system('taskkill /f /im ScanPro.exe')
        
def main():
    addImagePath(r"D:\sikuli\Icons")
    readFiles(r'D:\sikuli\Scan')
    importAndRefine()

main()

        
        
        
    