#!/usr/bin/python
# -*- coding: utf-8 -*-

from googletrans import Translator
import re

def translateText(line, dst):
    text = line.split('<value>')[1].split('</value>')[0]
    translatedValue = Translator().translate(text, src='es',dest=dst)
    value = re.sub(text, translatedValue.text, line)
    return value

def principal_function(title):
    originalFile = open(title + ".aspx.resx", "r", encoding="utf-8")
    spanishFile = open(title + ".aspx.es.resx", "w+", encoding="utf-8")
    argentinaFile = open(title + ".aspx.es-AR.resx", "w+", encoding="utf-8")
    chileFile = open(title + ".aspx.es-cl.resx", "w+", encoding="utf-8")
    colombiaFile = open(title + ".aspx.es-CO.resx", "w+", encoding="utf-8")
    ecuadorFile = open(title + ".aspx.es-ec.resx", "w+", encoding="utf-8")
    panamaFile = open(title + ".aspx.es-pa.resx", "w+", encoding="utf-8")
    peruFile = open(title + ".aspx.es-PE.resx", "w+", encoding="utf-8")
    uruguayFile = open(title + ".aspx.es-UY.resx", "w+", encoding="utf-8")
    venezuelaFile = open(title + ".aspx.es-VE.resx", "w+", encoding="utf-8")
    englishFile = open(title + ".aspx.en.resx", "w+", encoding="utf-8")
    germanFile = open(title + ".aspx.de.resx", "w+", encoding="utf-8")
    italianFile = open(title + ".aspx.it.resx", "w+", encoding="utf-8")
    portugueseFile = open(title + ".aspx.pt.resx", "w+", encoding="utf-8")

    commentFinished = False
    resheaderReached = False
    dataReached = False
    for line in originalFile:
        if commentFinished and resheaderReached and dataReached:
            if '<value>' in line:
                englishFile.write(translateText(line, 'en'))
                germanFile.write(translateText(line, 'de'))
                italianFile.write(translateText(line, 'it'))
                portugueseFile.write(translateText(line, 'pt'))
                spanishFile.write(line)
                argentinaFile.write(line)
                chileFile.write(line)
                colombiaFile.write(line)
                ecuadorFile.write(line)
                panamaFile.write(line)
                peruFile.write(line)
                uruguayFile.write(line)
                venezuelaFile.write(line)
            else:
                englishFile.write(line)
                germanFile.write(line)
                italianFile.write(line)
                portugueseFile.write(line)
                spanishFile.write(line)
                argentinaFile.write(line)
                chileFile.write(line)
                colombiaFile.write(line)
                ecuadorFile.write(line)
                panamaFile.write(line)
                peruFile.write(line)
                uruguayFile.write(line)
                venezuelaFile.write(line)
        else:
            if '-->' in line:
                commentFinished = True
            if '<resheader' in line and commentFinished:
                resheaderReached = True
            if '<data' in line and resheaderReached:
                dataReached = True
            englishFile.write(line)
            germanFile.write(line)
            italianFile.write(line)
            portugueseFile.write(line)
            spanishFile.write(line)
            argentinaFile.write(line)
            chileFile.write(line)
            colombiaFile.write(line)
            ecuadorFile.write(line)
            panamaFile.write(line)
            peruFile.write(line)
            uruguayFile.write(line)
            venezuelaFile.write(line)

    originalFile.close()
    englishFile.close()
    germanFile.close()
    italianFile.close()
    portugueseFile.close()
    spanishFile.close()
    argentinaFile.close()
    chileFile.close()
    colombiaFile.close()
    ecuadorFile.close()
    panamaFile.close()
    peruFile.close()
    uruguayFile.close()
    venezuelaFile.close()

if __name__ == "__main__":
    principal_function('Default')