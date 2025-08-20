import re
import string

templatefile = "template.html"
infile = "disco_in.txt"
outfile = "disco_out.html"

def to_class(text):
    name = ""
    for letter in text:
        if letter in string.ascii_uppercase:
            name += letter
    return name.lower()

assert to_class("PERCEPTION (TOUCH)") == "perceptiontouch"

def replace(matchobj):
    m =  matchobj.group(0)
    skill =  matchobj.group(1) or ""
    check =  matchobj.group(2) or ""
    text =  matchobj.group(3) or ""
    skill_span = "<span class='" + to_class(skill) + "'>" + skill + "</span> "
    check_span = "<span class='check'>" + check + "</span> " 
    return "<p>" + skill_span + check_span + text + "</p>"

with open(infile, encoding="utf-8") as f:
    lines = f.readlines()

out_lines = []
for line in lines:  
    if line.strip() == "":
        continue

    search = (  r"^([/()A-Z ]+) +"  # First CAPITALISED words 
              + r"(\[[^]]+\])?"     # optional [check] text
              + r"([^\n]+)")        # rest of line
    html_line = re.sub(search, replace, line)
    out_lines.append(html_line)

out = "\n".join(out_lines)

with open(templatefile) as f:
    template = f.read()
header,footer = template.split("====")
html = header + out + footer

with open(outfile, "w", encoding="utf-8") as f:
    f.write(html)

print(out[:2000])  # check first few lines