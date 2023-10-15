import re


def replace_spam_words(text, spam_words):
       text = text.lower()
       spam_words = [word.lower() for word in spam_words] 
    for word in spam_words:
        if not space_around:
            if word in text:
                return True
        else:
            if text.startswith(word + " ") or text.endswith(" " + word) or text.endswith(" " + word + "."):
                return True
            if (" " + word + " ") in text:
                return True
            if (" " + word + ".") in text:
                return True

    return False
        
    