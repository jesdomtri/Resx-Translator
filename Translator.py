#!/usr/bin/python
# -*- coding: utf-8 -*-

from googletrans import Translator
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import re
import time
import logging


def translate_text_function(line, dst):
    text = line.split('<value>')[1].split('</value>')[0]
    translatedValue = Translator().translate(text, src='es', dest=dst)
    value = re.sub(text, translatedValue.text, line)
    return value


def loop_files_function(title, extension_languages, variables_languages):
    try:
        languages = check_languages(extension_languages, variables_languages)
        if len(languages) > 0 and title != '':
            start_time = time.time()
            for language in languages:
                create_file_function(title, language)
            messagebox.showinfo("Translation completed", "Translations completed successfully in %s seconds." % str(
                round((time.time() - start_time), 4)))
        else:
            if len(languages) == 0 and title != '':
                messagebox.showwarning(
                    "Warning", "You have to select any language before translate.")
            else:
                messagebox.showwarning(
                    "Warning", "You have to select any file before translate.")
    except Exception as e:
        logging.basicConfig(filename='app.log', filemode='w',
                            format='%(name)s - %(levelname)s - %(message)s\n')
        logging.warning(e)
        messagebox.showerror(
            "Error", "An unexpected error has occurred. A log was created.\nContact the creator of this application: jesdomtri@gmail.com")


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


def browse_file(file_name_to_translate):
    file_dialog = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("Resx files", "*.aspx.resx*"), ("all files", "*.*")))
    file_name_to_translate.set(file_dialog)


def select_languages(variables_languages, extension_languages):
    for i in range(len(variables_languages)):
        variables_languages[i].set(1)


def deselect_languages(variables_languages, extension_languages):
    for i in range(len(variables_languages)):
        variables_languages[i].set(0)


def check_languages(extension_languages, variables_languages):
    languages = [extension_languages[i] for i in range(
        len(extension_languages)) if variables_languages[i].get() == 1]
    return languages


def ventana_principal():
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')
    root.title("Resx Translator")

    frame = tk.Frame(root)
    frame.grid(column=0, row=1, padx=5, pady=5)

    frame_top = tk.Frame(root)
    frame_top.grid(column=0, row=0, padx=5, pady=5, sticky='W')

    name_languages = ["Spanish", "Spanish-AR", "Spanish-CL", "Spanish-UY", "Spanish-CO", "Spanish-EC", "Spanish-PA",
                      "Spanish-PE", "Spanish-VE", "English", "Deutsche", "French", "Italian", "Portuguese", "Norwegian"]

    extension_languages = ['es', 'es-AR', 'es-cl', 'es-UY', 'es-CO',
                           'es-ec', 'es-pa', 'es-PE', 'es-VE', 'en', 'de', 'fr', 'it', 'pt', 'no']

    variables_languages = [tk.IntVar() for x in name_languages]

    cont = 0
    column = 0
    row = 0
    while(cont < len(name_languages)):
        if row == 5:
            row = 0
            column += 1
        tk.Checkbutton(frame, text=name_languages[cont], variable=variables_languages[cont], onvalue=1, offvalue=0).grid(
            column=column, row=row, sticky='W')
        cont += 1
        row += 1

    button_select_all = tk.Button(
        frame_top, text="Select all", command=lambda: select_languages(variables_languages, extension_languages))
    button_select_all.grid(column=0, row=0, sticky='W')

    button_deselect_all = tk.Button(
        frame_top, text="Deselect all", command=lambda: deselect_languages(variables_languages, extension_languages))
    button_deselect_all.grid(column=1, row=0, sticky='W')

    file_name_to_translate = tk.StringVar()

    name_file = tk.Entry(
        root, width=40, textvariable=file_name_to_translate)
    name_file.grid(column=0, row=2, padx=5, pady=5)

    button_search_file = tk.Button(
        root, text="Search", command=lambda: browse_file(file_name_to_translate))
    button_search_file.grid(column=1, row=2, padx=5, pady=5, sticky='W')

    button_translate = tk.Button(
        root, text="Translate", command=lambda: loop_files_function(file_name_to_translate.get().split('.aspx.resx')[0], extension_languages, variables_languages))
    button_translate.grid(column=0, row=3, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    ventana_principal()
