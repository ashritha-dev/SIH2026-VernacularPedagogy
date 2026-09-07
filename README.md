# AI-Powered Vernacular Pedagogy — SIH 2026 Prototype

## Run in VS Code

1. Install Python 3.10+.
2. Open this folder in VS Code.
3. Open Terminal.
4. Create a virtual environment:
   - Windows: `python -m venv .venv`
   - Activate: `.venv\Scripts\activate`
5. Install packages: `pip install -r requirements.txt`
6. Run: `python app.py`
7. Open Chrome and visit `http://127.0.0.1:5000`

## Demo flow

1. Select Ho, Mundari or Santhali.
2. Enter a Hindi classroom sentence.
3. Click Translate.
4. Try the voice button in Chrome.
5. Generate a bilingual worksheet.
6. Download the demo worksheet.

## Important

This is a hackathon prototype. The current translation layer is a small example dictionary used to demonstrate the end-to-end workflow. Do not present it as a production-quality translation model. For the final system, replace it with linguistically validated datasets/models and native-speaker evaluation, plus a real offline TTS/ASR stack.
