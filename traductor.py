#!/usr/bin/python
# -*- coding: utf-8 -*-

from googletrans import Translator
from tkinter import *
from tkinter import filedialog
import re
import time


def translate_text_function(line, dst):
    text = line.split('<value>')[1].split('</value>')[0]
    translatedValue = Translator().translate(text, src='es', dest=dst)
    value = re.sub(text, translatedValue.text, line)
    return value


def loop_files_function(title, languages):
    for language in languages:
        start_time = time.time()
        create_file_function(title, language)
        print("TIEMPO PARA IDIOMA " + language + ": --- %s seconds ---" %
              (time.time() - start_time))


def create_file_function(title, language):
    originalFile = open(title + ".aspx.resx", "r", encoding="utf-8")
    newFile = open(title + '.aspx.' + language +
                   '.resx', "w+", encoding="utf-8")
    if 'es' in language:
        for line in originalFile:
            newFile.write(line)
    else:
        translate_file_function(originalFile, newFile, language)
    newFile.close()


def translate_file_function(originalFile, newFile, language):
    commentFinished = False
    resheaderReached = False
    dataReached = False
    for line in originalFile:
        if commentFinished and resheaderReached and dataReached:
            if '<value>' in line:
                newFile.write(translate_text_function(line, language))
            else:
                newFile.write(line)
        else:
            if '-->' in line:
                commentFinished = True
            if '<resheader' in line and commentFinished:
                resheaderReached = True
            if '<data' in line and resheaderReached:
                dataReached = True
            newFile.write(line)


def ventana_principal():

    def browse_file():
        file_dialog = filedialog.askopenfilename(
            initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        label_file_explorer.configure(text="File Opened: " + file_dialog)

    root = Tk()
    root.geometry('350x200')
    root.title("Resx Translator")
    menubar = Menu(root)
    select_language = Menu(root)

    menubar.add_command(label="Translate")

    menubar.add_separator()

    select_language.add_command(label="Spanish")
    select_language.add_command(label="English")
    select_language.add_command(label="Deutsch")
    select_language.add_command(label="French")

    menubar.add_cascade(label="Select language", menu=select_language)

    menubar.add_separator()

    menubar.add_command(label="Quit", command=root.quit)

    label_file_explorer = Label(root,
                                text="File Explorer using Tkinter",
                                width=100, height=4,
                                fg="blue")

    label_file_explorer.grid(column=1, row=1)

    name_file = Entry(root, width=30)
    name_file.grid(column=0, row=0)

    button_search_file = Button(root, text="Search")
    button_search_file.grid(column=1, row=0)

    root.config(menu=menubar)
    root.mainloop()


if __name__ == "__main__":
    start_time = time.time()
    languages = ['es', 'es-AR', 'es-cl', 'es-UY', 'es-CO', 'es-ec',
                 'es-pa', 'es-PE', 'es-VE', 'en', 'de', 'fr', 'it', 'pt']
    try:
        ventana_principal()
        #loop_files_function('Default', languages)
    except:
        print('HA HABIDO UN ERROR, BRO')
    print("TIEMPO TOTAL: --- %s seconds ---" % (time.time() - start_time))
