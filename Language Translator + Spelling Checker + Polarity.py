import textblob
import langid

def check_polarity(sentence):
    blob_sentence = textblob.TextBlob(sentence, analyzer=textblob.sentiments.NaiveBayesAnalyzer())
    sentiment = blob_sentence.sentiment
    return sentiment

def spell_correct(sentence):
    blob_sentence = textblob.TextBlob(sentence)
    corrected_sentence = blob_sentence.correct()
    print("Corrected Sentence:", corrected_sentence)

def language_translator(sentence):
    blob_sentence = textblob.TextBlob(sentence)
    detected_language = langid.classify(sentence)[0]
    print("Detected Language:", detected_language)

    lang = input("Enter the language code (ISO 639-1) to Translate: ")
    if lang == detected_language:
        print("Already in the specified language.")
    else:
        translated_sentence = blob_sentence.translate(from_lang=detected_language, to=lang)
        print("Translated Sentence:", translated_sentence)

# Function to display the menu and get user choice
def show_menu():
    print("Menu:")
    print("1. Check Polarity")
    print("2. Spell Correction")
    print("3. Language Translation")
    choice = input("Enter your choice (1, 2, or 3): ")
    return choice

# Main program
sentence = input("Enter the Paragraph or Sentence You want To Check: ")
choice = show_menu()

if choice == "1":
    result = check_polarity(sentence)
    positivity_percentage = result.p_pos * 100
    negativity_percentage = result.p_neg * 100
    print(f"Positivity: {positivity_percentage:.2f}%")
    print(f"Negativity: {negativity_percentage:.2f}%")

elif choice == "2":
    spell_correct(sentence)

elif choice == "3":
    language_translator(sentence)

else:
    print("Invalid choice. Please enter 1, 2, or 3.")
