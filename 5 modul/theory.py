'''s = "I am learning strings in Python. Some new methods got now. I am Oleh and it is very difficult, but funny at the same time to learn Computer Science. "
sentences = s.split(". ")

print(sentences[0]) 
print(sentences[1])
print(sentences[2])'''

'''sentences = ["I am learning strings in Python", "Some new methods got now."]
text = ". ".join(sentences)
print(text)'''

'''clean = '                          spacious   kuzi kuzi'             .rstrip()
print(clean)  # spacious'''

'''dogs_text = "All dogs bark like dogs."
cats_text = dogs_text.replace("dogs", "cats")
print(cats_text) '''

'''map = {ord('з'): 'z', ord('ю'): 'u', ord("е"): "e", ord("л"): "l",ord("н"): "n", ord("к"): "K", ord("с"): "s", ord("и"): "y", ord("й"): "i"}
translated = 'зеленський'.translate(map)
print(translated) '''

'''s = "{name} {last_name}".format(last_name="Petryshyn", name="Oleh")
print(s)'''

print("|{:<5}|{:-^10}|{:>5}|".format('left', 'center', 'right'))  

def is_check_name(fullname, first_name):
    # Check if the fullname starts with the first_name
    return fullname.startswith(first_name)