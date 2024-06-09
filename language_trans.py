import googletrans
from googletrans import Translator

translator = Translator()
s = googletrans.LANGUAGES


def translation():
    avail_lang = list(s.values())
    print(f'Available languages: {avail_lang}')
    user_input = input('Enter text: ')
    user_language = input('Enter language: ')
    for lang_code, lang_name in s.items():
        if user_language not in avail_lang:
            print('No such language found!')
            break
        if user_language == lang_name:
            d = f'{lang_code}'
            ans = translator.translate(user_input, dest=d)
            translated_ans = ans.text
            pronunciation_ans = ans.pronunciation
            print(f'{user_input} --> {translated_ans}')
            print(f'Pronunciation : {pronunciation_ans}')
            break


def detection(language):
    detect_lang = translator.detect(language).lang
    for la_code, la_name in s.items():
        if detect_lang == la_code:
            print(f'Detected language is: {la_name}')
            trans_lan = translator.translate(language, dest='en')
            print(f'Translation: {trans_lan.text}')
            break


def user_wish():
    print('Welcome! language enthusiast.')
    print('Enter \'t\' - Translation & \'d\' - Detection.')
    user = input()
    if user == 't':
        translation()
    elif user == 'd':
        detection(input('Enter: '))
    else:
        print('Invalid!! Try again.')


user_wish()
