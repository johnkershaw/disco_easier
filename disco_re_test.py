import re
import string

def to_classname(text):
    name = ""
    for letter in text:
        if letter in string.ascii_uppercase:
            name += letter
    return name.lower()
assert to_classname("PERCEPTION (TOUCH)") == "perceptiontouch"

def convert_func(matchobj):
    m =  matchobj.group(0)
    map = {'7': 'seven',
           '8': 'eight',
           '9': 'nine'}
    return map[m]

def replace(matchobj):
    m =  matchobj.group(0)
    skill =  matchobj.group(1)
    check =  matchobj.group(2)
    text =  matchobj.group(3)
    return "<p><span class='" + to_classname(skill) + "'>" + skill + "</span> <span class='check'>" + check + "</span>" + text + "</p>"

line = "7 ate 9"
new_line =  re.sub("[7-9]", convert_func, line)

line = "PERCEPTION (SIGHT) [Medium: Success] - You’re standing on a small island of bluish-grey stone, surrounded on all sides by a sheer drop into an impenetrable darkness. The sky above you is similarly pitch-black, yet despite the lack of sunlight or other illumination, you can see without hindrance."
search = (  r"^([/()A-Z ]+) +"  # First CAPITALISED words on line
            + r"(\[[^]]+\])?"     # optional [check] text
            + r"([^\n]+)")        # rest of line

html_line = re.sub(search, replace, line)

print(html_line)