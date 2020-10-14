#!/usr/bin/python
# -*- coding: utf-8 -*-

from googletrans import Translator
import tkinter
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


if __name__ == "__main__":
    start_time = time.time()
    languages = ['es', 'es-AR', 'es-cl', 'es-UY', 'es-CO', 'es-ec',
                 'es-pa', 'es-PE', 'es-VE', 'en', 'de', 'fr', 'it', 'pt']
    try:
        loop_files_function('Default', languages)
    except:
        print('HA HABIDO UN ERROR, BRO')
    print("TIEMPO TOTAL: --- %s seconds ---" % (time.time() - start_time))
