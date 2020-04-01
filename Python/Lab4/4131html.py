import re
# Визначення власних виняткових ситуацій
class NoSuchFileOrDirectory(Exception):
    pass
class NoTagsFound(Exception):
    pass
class EmptyHTMLTagError(Exception):
    pass

try:
    with open("sample_html.html") as f:
        html = f.read()
except:
    raise NoSuchFileOrDirectory("No such file or directory.")

# Робота з РВ
pattern = re.compile(r"<.[^<>]*>")
pattern_empty = re.compile(r"<\s*>")
tags = re.findall(pattern, html)
empty = re.findall(pattern_empty,html)

# Обробка виняткових ситуацій
if len(empty) > 0:
    raise EmptyHTMLTagError("Empty HTML tag found!")
if len(tags) == 0:
    raise NoTagsFound("No HTML tags found!")

for tag in tags:
    print(tag)