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


def loop_files_function(title, languages):
    try:
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


def select_languages(languages, extension):
    if extension in languages:
        languages.remove(extension)
    else:
        languages.append(extension)


def select_all_languages(all_languages):
    all_pressed = True
    for language in all_languages:
        if language.get() == 1:
            all_pressed = False
    if all_pressed:
        for language in all_languages:
            language.set(1)
    else:
        for language in all_languages:
            language.set(0)


def ventana_principal():
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')
    root.title("Resx Translator")

    frame = tk.Frame(root)
    frame.grid(column=0, row=1, padx=5, pady=5)

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

    all_languages = [language_es, language_es_ar, language_es_cl, language_es_uy, language_es_co,
                     language_es_ec, language_es_pa, language_es_pe, language_es_ve, language_en,
                     language_de, language_it, language_fr, language_pt, language_no]

    button_select_all = tk.Button(
        root, text="Select all", command=lambda: select_all_languages(all_languages))
    button_select_all.grid(column=0, row=0, padx=5, pady=5, sticky='W')

    tk.Checkbutton(frame, text="Spanish", variable=language_es, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es')).grid(column=0, row=0, sticky='W')

    tk.Checkbutton(frame, text="Spanish-AR", variable=language_es_ar, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-AR')).grid(column=0, row=1, sticky='W')

    tk.Checkbutton(frame, text="Spanish-CL", variable=language_es_cl, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-cl')).grid(column=0, row=2, sticky='W')

    tk.Checkbutton(frame, text="Spanish-UY", variable=language_es_uy, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-UY')).grid(column=0, row=3, sticky='W')

    tk.Checkbutton(frame, text="Spanish-CO", variable=language_es_co, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-CO')).grid(column=0, row=4, sticky='W')

    tk.Checkbutton(frame, text="Spanish-EC", variable=language_es_ec, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-ec')).grid(column=0, row=5, sticky='W')

    tk.Checkbutton(frame, text="Spanish-PA", variable=language_es_pa, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-pa')).grid(column=1, row=0, sticky='W')

    tk.Checkbutton(frame, text="Spanish-PE", variable=language_es_pe, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-PE')).grid(column=1, row=1, sticky='W')

    tk.Checkbutton(frame, text="Spanish-VE", variable=language_es_ve, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'es-VE')).grid(column=1, row=2, sticky='W')

    tk.Checkbutton(frame, text="English", variable=language_en, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'en')).grid(column=1, row=3, sticky='W')

    tk.Checkbutton(frame, text="Deutsche", variable=language_de, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'de')).grid(column=1, row=4, sticky='W')

    tk.Checkbutton(frame, text="French", variable=language_fr, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'fr')).grid(column=1, row=5, sticky='W')

    tk.Checkbutton(frame, text="Italian", variable=language_it, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'it')).grid(column=2, row=0, sticky='W')

    tk.Checkbutton(frame, text="Portuguese", variable=language_pt, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'pt')).grid(column=2, row=1, sticky='W')

    tk.Checkbutton(frame, text="Norwegian", variable=language_no, onvalue=1,
                   offvalue=0, command=lambda: select_languages(languages, 'no')).grid(column=2, row=2, sticky='W')

    file_name_to_translate = tk.StringVar()

    name_file = tk.Entry(
        root, width=40, textvariable=file_name_to_translate)
    name_file.grid(column=0, row=2, padx=5, pady=5)

    button_search_file = tk.Button(
        root, text="Search", command=lambda: browse_file(file_name_to_translate))
    button_search_file.grid(column=1, row=2, padx=5, pady=5)

    button_translate = tk.Button(
        root, text="Translate", command=lambda: loop_files_function(file_name_to_translate.get().split('.aspx.resx')[0], languages))
    button_translate.grid(column=0, row=3, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    ventana_principal()
