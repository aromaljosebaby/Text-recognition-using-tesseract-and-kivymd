from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.toast import toast
from helper import KV
from tkinter.filedialog import askdirectory, askopenfile,asksaveasfilename,askopenfilenames,askopenfilename,askopenfiles,asksaveasfile
from tkinter import Tk

import pytesseract
import cv2



class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class TestNavigationDrawer(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Green'
        self.screen=Builder.load_string(KV)
        self.shud_we_train=False
        self.if_img_selected=False
        self.if_txt_is_saved=False
        self.if_destination_folder_selected=False
        return self.screen

    def select_image_for_rec(self):
        files = [('text file', '*.txt')]
        root = Tk()
        root.withdraw()
        # file = askdirectory()
        source = askopenfile()
        if source==None:
            self.opening_dialogue_bos(title='Error',text='Please select image for recognition')

        else:
            self.img_src = source.name
            self.if_img_selected=True
            self.popup('Image Selected')


    def text_detection_start(self):
        # Mention the installed location of Tesseract-OCR in your system

        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

        # Read image from which text needs to be extracted

        if self.if_img_selected==False:
            self.opening_dialogue_bos(title='Error', text='Please select the image   to continue')
        elif self.if_destination_folder_selected==False:
            self.opening_dialogue_bos(title='Error', text='Please select  folder destination folder to continue')
        else:
            # Preprocessing the image starts

            # Convert the image to gray scale
            img = cv2.imread(self.img_src)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Performing OTSU threshold

            ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

            # Specify structure shape and kernel size.
            # Kernel size increases or decreases the area
            # of the rectangle to be detected.
            # A smaller value like (10, 10) will detect
            # each word instead of a sentence.

            rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

            # Appplying dilation on the threshold image

            dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

            # Finding contours

            contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,

                                                   cv2.CHAIN_APPROX_NONE)

            # Creating a copy of image

            im2 = img.copy()

            # A text file is created and flushed
            # destination = "E:\\things\\recognized.txt"
            destination = f"{self.destination}\\recognized.txt"

            a = []

            # Looping through the identified contours
            # Then rectangular part is cropped and passed on
            # to pytesseract for extracting text from it
            # Extracted text is then written into the text file

            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)

                # Drawing a rectangle on copied image

                rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Cropping the text block for giving input to OCR

                cropped = im2[y:y + h, x:x + w]

                # Open the file in append mode

                # Apply OCR on the cropped image

                text = pytesseract.image_to_string(cropped)
                a.append(text)

                # Appending the text into file

                # Close the file
                print(a)

            file = open(destination, "a")
            a.reverse()

            for i in a:

                file.write(i)
                if i != '':
                    file.write("\n")
            self.if_txt_is_saved=True
            self.popup('Text Recognition Comleted')


    def browse_directory_for_saving(self):
        files = [('text file', '*.txt')]
        root = Tk()
        root.withdraw()
        file = askdirectory()
        self.destination=file
        if self.destination=='':
            self.opening_dialogue_bos(title='Error',text='Select destination for saving')
        else:
            self.if_destination_folder_selected=True
            self.popup('Destination folder selected')
        #print(file)
        #print(' i printed')
        #print(file)  # gives output like E:/things

    def opening(self):
        import os

        #desination = 'E:\\things\\recognized.txt'
        if self.if_txt_is_saved:

            destination=f'{self.destination}\\recognized.txt'
            file = f'notepad.exe {destination}'
            os.system(file)
        else:

            self.opening_dialogue_bos(title='Error', text='No text file available try running the program first')
    def popup(self,text):
        toast(text)

    def check_for_blank_close(self, obj):
        self.blank_check_dialogue.dismiss()

    def opening_dialogue_bos(self,title,text):
        close_btn = MDRaisedButton(text='Close', on_release=self.check_for_blank_close)
        self.blank_check_dialogue = MDDialog(title=title,
                                             text=text,
                                             buttons=[close_btn])
        self.blank_check_dialogue.open()







TestNavigationDrawer().run()