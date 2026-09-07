from flask import Flask, render_template, request, jsonify, make_response
import json, io

app = Flask(__name__)

with open("data/languages.json", "r", encoding="utf-8") as f:
    LANGUAGES = json.load(f)

def translate_text(text, language):
    # Prototype translation layer. Replace/augment with a trained model + validated
    # language resources before field deployment.
    mapping = LANGUAGES.get(language, {})
    result = text
    for hindi, tribal in sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True):
        result = result.replace(hindi, tribal)
    return result

@app.route("/")
def home():
    return render_template("index.html", languages=list(LANGUAGES.keys()))

@app.post("/api/translate")
def translate():
    data = request.get_json(force=True)
    text = data.get("text", "").strip()
    language = data.get("language", "Ho")
    if not text:
        return jsonify({"error": "Enter Hindi text first."}), 400
    return jsonify({
        "source": text,
        "language": language,
        "translation": translate_text(text, language)
    })

@app.post("/api/worksheet")
def worksheet():
    data = request.get_json(force=True)
    topic = data.get("topic", "Numbers")
    grade = data.get("grade", "Class 1")
    language = data.get("language", "Ho")
    examples = {
        "Numbers": [
            "1. Count: ⭐ ⭐ ⭐",
            "2. Write the number: ______",
            "3. Match 1, 2, 3 with the correct quantities."
        ],
        "Animals": [
            "1. Identify: 🐘",
            "2. Match each animal with its name.",
            "3. Draw your favourite animal."
        ],
        "Colours": [
            "1. Identify: 🔴 🔵 🟢",
            "2. Name three colours.",
            "3. Colour the objects shown by your teacher."
        ],
        "My Family": [
            "1. Draw your family.",
            "2. Count the people in your family.",
            "3. Tell one thing about your family."
        ]
    }
    lines = examples.get(topic, examples["Numbers"])
    return jsonify({
        "title": f"{grade} • {topic} • Bilingual Worksheet",
        "language": language,
        "items": lines
    })

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/download/worksheet")
def download_worksheet():
    topic = request.args.get("topic", "Numbers")
    grade = request.args.get("grade", "Class 1")
    language = request.args.get("language", "Ho")
    content = [
        "AI-POWERED VERNACULAR PEDAGOGY",
        f"{grade} - {topic} - Bilingual Worksheet",
        f"Target language: {language}",
        "",
        "1. Count: 1  2  3",
        "2. Write the correct answer: __________",
        "3. Match the correct pair.",
        "4. Draw and explain your answer.",
        "",
        "Prototype generated for SIH 2026 demonstration."
    ]
    data = "\n".join(content).encode("utf-8")
    response = make_response(data)
    response.headers["Content-Type"] = "text/plain; charset=utf-8"
    response.headers["Content-Disposition"] = 'attachment; filename="bilingual_worksheet.txt"'
    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
