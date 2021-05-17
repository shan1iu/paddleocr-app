import os
import sys
import threading

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.append(os.path.abspath(os.path.join(__dir__, '../')))

import math
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from PIL import Image, ImageTk

import tools.infer.predict_system as predict_sys
import tools.infer.utility as utility


class App:
    # 选择图片路径按钮
    def clickSelectedImageBtn(self):
        # 选择图片
        global path
        path = askopenfilename(filetypes=[("请选择图片",'.jpg'),("请选择图片",'.png')])
        if path:
            image = Image.open(path)
            image_ratio = image.width/image.height
            image_width = math.ceil(400*image_ratio)
            image_height = 400
            image_resized = image.resize((image_width, image_height), Image.ANTIALIAS)
            tkImage = ImageTk.PhotoImage(image_resized)
            # 添加标签（存放图片）
            self.tkImageLabel.configure(image=tkImage)
            self.tkImageLabel.configure(width=image_width)
            self.tkImageLabel.configure(height=image_height)
            self.tkImageLabel.image = tkImage
            self.tkImageLabel.grid(row=1, column=0, columnspan=2)
        
    def clickAnalyseImageBtn(self):
        try:
            print('🎀 图片路径 ==>', path, '\n')
            args = utility.parse_args()
            args.image_dir = path
            result = predict_sys.main(args)
            print('计算结果', result)
        except NameError:
            showerror(title="Error", message="Please choose an image")

    def __init__(self):
        # 初始化窗口
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.minsize(400, 300)
        self.root.title('Optical character recognition')
        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        positionRight = int(self.root.winfo_screenwidth()/2 - windowWidth/2 - 100)
        positionDown = int(self.root.winfo_screenheight()/2 - windowHeight/2 - 50) 
        self.root.geometry("+{}+{}".format(positionRight, positionDown))
        
        # 存放按钮frame
        self.operationFrame = Frame(self.root)
        self.operationFrame.grid(row=0, column=0, sticky="nsew")
        # 选择图片按钮
        self.selectedImageBtn = Button(self.operationFrame, text="choose image", command=self.clickSelectedImageBtn).grid(row=0, column=0)
        # 处理图片按钮
        self.analyseImageBtn = Button(self.operationFrame, text="analyse image", command=self.clickAnalyseImageBtn).grid(row=0, column=1)
        # 显示图片Label
        self.tkImageLabel = Label(self.root, image="")
        self.root.mainloop()


if __name__=='__main__':
    app=App()