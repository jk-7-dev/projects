from flask import Flask, request, render_template
from googletrans import Translator

def translate_text(text, target_language):
    SystemExit

    # Create a translator object
    translator = Translator()

    # Translate a text from English to target_language
    translated_text = translator.translate(text, src='en', dest=target_language)

    # Print the translated text
    print(translated_text.text)
    return translated_text.text

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    text = request.form["text"]
    target_language = request.form["target_language"]
    # Call your translation function here and pass the text and target language
    translated_text = translate_text(text, target_language)
    return translated_text

if __name__ == "__main__":
    app.run(debug=True)
