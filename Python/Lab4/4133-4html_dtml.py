import re
# Визначення власних виняткових ситуацій
class NoSuchFileOrDirectory(Exception):
    pass
class NoTagsFound(Exception):
    pass
class EmptyTagError(Exception):
    pass

try:
    with open("sample_html.html") as f:
        html = f.read()
    with open("sample_dtml.dtml") as f2:
        dtml = f2.read()
except:
    try:
        raise NoSuchFileOrDirectory("No such file or directory.")
    except NoSuchFileOrDirectory: 
        print("Сталася помилка NoSuchFIleOrDirectory")
        quit()

# Робота з РВ
pattern = re.compile(r"<.*>.*<.*>")
pattern_empty = re.compile(r"<\s*>")
pattern_tag = re.compile(r"</?[^<>]*>")
tags_html = re.findall(pattern, html)
tags_dtml = re.findall(pattern, dtml)
empty_html = re.findall(pattern_empty,html)
empty_dtml = re.findall(pattern_empty,dtml)
raw_tags = re.findall(pattern_tag, html)

# Обробка виняткових ситуацій
if len(empty_html) > 0:
    try:
        raise EmptyTagError("Empty tag found in HTML file! ")
    except EmptyTagError:
        print("Сталася помилка EmptyTagError в HTML файлі. ")
if len(empty_dtml) > 0:
    try:
        raise EmptyTagError("Empty tag found in DTML file! ")
    except EmptyTagError:
        print("Сталася помилка EmptyTagError в файлі DTML.")
if len(tags_html) == 0:
    try:
        raise NoTagsFound("No tags found in HTML file! ")
    except:
        print("Сталася помилка NoTagsFound в файлі HTML")
if len(tags_dtml) == 0:
    try:
        raise NoTagsFound("No tags found in DTML file! ")
    except:
        print("Сталася помилка NoTagsFound у DTML файлі ")

print("HTML Tags: \n")
for tag in raw_tags:
    tag_type = re.search(r"\w+",tag)
    if "dtml" not in tag:
        print(str(tag).ljust(20) + "\tTag type is:\t" + tag_type.group())

print("\nDTML Tags: \n")
for tag in raw_tags:
    if "dtml" in tag:
        print(tag)
