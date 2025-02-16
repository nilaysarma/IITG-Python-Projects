# Week 6 Lab: : Words Into Emojis
# Description: an interactive command-line interface (CLI) application using python that: translates words into emojis (including auto-filling mood-based emojis.

import random

emoji_dict = {
    "happy": "😃",
    "love": "❤️",
    "fire": "🔥",
    "sad": "😢",
    "angry": "😡",
    "cool": "😎",
    "food": "🍔",
    "dog": "🐶",
    "cat": "🐱"
}

def emoji_translate(sentence):
    words = sentence.split()
    return " ".join([emoji_dict.get(word, word) for word in words])

mood_emojis = {
    "happy": ["😃", "🎉", "🥳", "😊", "🌞"],
    "sad": ["😢", "💔", "😭", "😔"],
    "excited": ["🤩", "🔥", "🎊", "🚀"],
    "angry": ["😡", "🤬", "💢", "👿"],
    "love": ["❤️", "😍", "😘", "💕"]
}

def mood_fill(sentence):
    mood = None

    # Detect mood request
    for key in mood_emojis:
        if f"(fill with {key} emojis)" in sentence:
            mood = key
            # words.remove(f"(fill with {key} emojis)")
            sentence = sentence.replace(f"(fill with {key} emojis)", "").strip()
            break

    words = sentence.split()

    # Append random emojis if mood detected
    if mood:
        words.append("".join(random.choices(mood_emojis[mood], k=3)))
    
    return " ".join(words)

while True:
    print("\n🎉 Welcome to Emoji Translator 🎉")
    print("1. Emoji Tanslator")
    print("2. Mood-Fill Emoji Generator")
    print("5. Exit")

    choice = input("Choose an option: (1-5): ")

    if choice == "1":
        text = input("Enter a sentence to translate: ")
        print("📝 Translated: ", emoji_translate(text))
    elif choice == "2":
        text = input("Enter a sentence with mood (e.g., 'I love coding! (fill with happy emojis)'): ")
        print("😊 Mood-Filled: ", mood_fill(text))
    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please try again.")