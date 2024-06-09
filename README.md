# Language Translator and Detector

This project provides a simple command-line interface for language translation and detection using the `googletrans` library.

## Features

- **Translation**: Translate text from one language to another.
- **Language Detection**: Detect the language of the given text.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/language-translator.git
    cd language-translator
    ```

2. Install the required dependencies:
    ```bash
    pip install googletrans==4.0.0-rc1
    ```

## Usage

Run the script and follow the prompts:

```bash
python language_trans.py
```
**You will be presented with the following options:**

- **Translation:** Translate a given text to a specified language.
- **Detection:** Detect the language of the provided text.

  ## Translation
  1. The script will display a list of available languages.
  2. Enter the text you want to translate.
  3. Enter the target language.

  ## Detection
  1. Enter the text you want to detect the language of.
  2. The script will detect and display the language along with its English translation.

  ## Example
  **Translation**
  ```bash
  Welcome! language enthusiast.
  Enter 't' - Translation & 'd' - Detection.
  t
  Available languages: ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', ...]
  Enter text: Hello, how are you?
  Enter language: spanish
  Hello, how are you? --> Hola, ¿cómo estás?
  Pronunciation : Hola, ¿cómo estás?
  ```
  **Detection**
  ```bash
  Welcome! language enthusiast.
  Enter 't' - Translation & 'd' - Detection.
  d
  Enter: Hola, ¿cómo estás?
  Detected language is: spanish
  Translation: Hello, how are you?
