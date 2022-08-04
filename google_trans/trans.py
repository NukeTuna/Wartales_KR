from bs4 import BeautifulSoup
from google.cloud import translate_v2 as translate
import fasttext as ft
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "wartales-translation-3f4291dfafcd.json"
EnableTranslation = True
IsExportFile = True

def getFilename():
    return "export_zh.xml" if IsExportFile else "texts_zh.xml"

def getFindTag():
    return ["text", "name", "desc"] if IsExportFile else "t"

def main():
    translator = translate.Client()
    detecter = ft.load_model("lid.176.ftz")

    infile = open(getFilename(), "r", encoding="utf-8")
    contents = infile.read()
    soup = BeautifulSoup(contents, "xml")
    elements = soup.find_all(getFindTag())

    totalCount = 0
    for element in elements:
        totalCount += len(element.text)
        print("original: " + element.text)
        if EnableTranslation == True:
            korean = isKorean(element.text, detecter)
            if korean == False:
                transText = transFromGoogle(element.text, translator)
                element.string = transText
                print("translated: " + element.text)
                print("-------------------")
            else:
                print("This sentence is korean")

    print("Charactor count: " + str(totalCount))
    infile.close()

    outfile = open(getFilename(), "w", encoding="utf-8")
    outfile.write(str(soup))
    outfile.close()

def transFromGoogle(text, translator):
    result = translator.translate(text, source_language='en', target_language='ko', format_='text')
    return result["translatedText"]

def isKorean(text, detector):
    replacedText = text.replace('\n', ' ')
    result = detector.predict(replacedText, k=1)
    label = result[0][0]
    return label == "__label__ko"


main()
