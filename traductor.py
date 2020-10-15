#!/usr/bin/python
# -*- coding: utf-8 -*-

from googletrans import Translator
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import re
import time


def translate_text_function(line, dst):
    text = line.split('<value>')[1].split('</value>')[0]
    translatedValue = Translator().translate(text, src='es', dest=dst)
    value = re.sub(text, translatedValue.text, line)
    return value


def loop_files_function(title, languages):
    try:
        if len(languages) > 0 and title != '':
            start_time = time.time()
            for language in languages:
                create_file_function(title, language)
            messagebox.showinfo("Translation completed", "Translations completed successfully in %s seconds." % (
                time.time() - start_time))
        else:
            if len(languages) == 0 and title != '':
                messagebox.showwarning(
                    "Warning", "You have to select any language before translate.")
            else:
                messagebox.showwarning(
                    "Warning", "You have to select any file before translate.")
    except:
        messagebox.showerror(
            "Error", "An unexpected error has occurred.\nContact the creator of this application: jesdomtri@gmail.com")


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
        initialdir="/", title="Select a File", filetypes=(("Resx files", "*.resx*"), ("all files", "*.*")))
    file_name_to_translate.set(file_dialog)
    print(file_name_to_translate.get().split('/')[-1].split('.')[0])


def select_languages(languages, extension):
    if extension in languages:
        languages.remove(extension)
    else:
        languages.append(extension)


def ventana_principal():
    root = tk.Tk()
    root.title("Resx Translator")

    frame = tk.Frame(root)
    frame.grid(column=0, row=0)

    languages = []

    language_es = tk.IntVar()
    language_es_ar = tk.IntVar()
    language_es_cl = tk.IntVar()
    language_es_uy = tk.IntVar()
    language_es_co = tk.IntVar()
    language_es_ec = tk.IntVar()
    language_es_pa = tk.IntVar()
    language_es_pe = tk.IntVar()
    language_es_ve = tk.IntVar()
    language_en = tk.IntVar()
    language_de = tk.IntVar()
    language_it = tk.IntVar()
    language_fr = tk.IntVar()
    language_pt = tk.IntVar()
    language_no = tk.IntVar()

    tk.Checkbutton(frame, text="Spanish", variable=language_es, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es')).grid(column=0, row=0)

    tk.Checkbutton(frame, text="Spanish-AR", variable=language_es_ar, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-AR')).grid(column=0, row=1)

    tk.Checkbutton(frame, text="Spanish-CL", variable=language_es_cl, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-cl')).grid(column=0, row=2)

    tk.Checkbutton(frame, text="Spanish-UY", variable=language_es_uy, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-UY')).grid(column=0, row=3)

    tk.Checkbutton(frame, text="Spanish-CO", variable=language_es_co, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-CO')).grid(column=0, row=4)

    tk.Checkbutton(frame, text="Spanish-EC", variable=language_es_ec, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-ec')).grid(column=0, row=5)

    tk.Checkbutton(frame, text="Spanish-PA", variable=language_es_pa, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-pa')).grid(column=1, row=0)

    tk.Checkbutton(frame, text="Spanish-PE", variable=language_es_pe, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-PE')).grid(column=1, row=1)

    tk.Checkbutton(frame, text="Spanish-VE", variable=language_es_ve, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-VE')).grid(column=1, row=2)

    tk.Checkbutton(frame, text="English", variable=language_en, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'en')).grid(column=1, row=3)

    tk.Checkbutton(frame, text="Deutsche", variable=language_de, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'de')).grid(column=1, row=4)

    tk.Checkbutton(frame, text="French", variable=language_fr, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'fr')).grid(column=1, row=5)

    tk.Checkbutton(frame, text="Italian", variable=language_it, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'it')).grid(column=2, row=0)

    tk.Checkbutton(frame, text="Portuguese", variable=language_pt, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'pt')).grid(column=2, row=1)

    tk.Checkbutton(frame, text="Norwegian", variable=language_no, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'no')).grid(column=2, row=2)

    file_name_to_translate = tk.StringVar()

    name_file = tk.Entry(
        root, width=50, textvariable=file_name_to_translate)
    name_file.grid(column=0, row=1)

    button_search_file = tk.Button(
        root, text="Search", command=lambda: browse_file(file_name_to_translate))
    button_search_file.grid(column=1, row=1)

    button_translate = tk.Button(
        root, text="Translate", command=lambda: loop_files_function(file_name_to_translate.get().split('/')[-1].split('.')[0], languages))
    button_translate.grid(column=0, row=2)

    root.mainloop()


if __name__ == "__main__":
    ventana_principal()
