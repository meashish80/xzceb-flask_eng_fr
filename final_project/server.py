from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchtext = language_translator.translate(text='english_text',model_id='en-fr').get_result()
    return frenchtext.get("translations")[0].get("translations")

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishtext = language_translator.translate(text='french_text',model_id='fr-en').get_result()
    return englishtext.get("translations")[0].get("translations")

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
