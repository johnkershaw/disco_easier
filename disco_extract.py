import re
import string

infile = "disco_in.txt"
outfile = "disco_out.html"

def to_classname(text):
    name = ""
    for letter in text:
        if letter in string.ascii_uppercase:
            name += letter
    return name.lower()

assert to_classname("PERCEPTION (TOUCH)") == "perceptiontouch"

def replace(matchobj):
    m =  matchobj.group(0)
    skill =  matchobj.group(1) or ""
    check =  matchobj.group(2) or ""
    text =  matchobj.group(3) or ""
    return "<p><span class='" + to_classname(skill) + "'>" + skill + "</span> <span class='check'>" + check + "</span>" + text + "</p>"

with open(infile, encoding="utf-8") as f:
    lines = f.readlines()

out_lines = []
for line in lines:  
    if line.strip() == "":
        continue
    #print(line)
    search = (  r"^([/()A-Z ]+) +"  # First CAPITALISED words on line
              + r"(\[[^]]+\])?"     # optional [check] text
              + r"([^\n]+)")        # rest of line
    #replace = r"<p><span class='\1'>\1</span> <span class='check'>\2</span>\3</p>"
    html_line = re.sub(search, replace, line)


    out_lines.append(html_line)

out = "\n".join(out_lines)
#print(out)

header = """<head>
    <style>
        body {background-color: black; color: white;}
        .fys, .endurance, .physical, .pain {color:#cb476a}
        .mot, .interfacing, .savoir, .perception, .reaction {color:#e3b734}
        .psy, .volition, .inland, .esprit, .empathy{color:#7556cf}
    </style>
</head>
<body>
"""
footer = """</body>
</html>"""
out = header + out + footer
with open(outfile, "w", encoding="utf-8") as f:
    f.write(out)

print(out[:1000])