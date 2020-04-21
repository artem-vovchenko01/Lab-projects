import re
# Визначення власних виняткових ситуацій
class NoSuchFileOrDirectory(Exception):
    pass
class NoTagsFound(Exception):
    pass
class EmptyTagError(Exception):
    pass

try:
    with open("sample_dtml.dtml") as f:
        dtml = f.read()
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
tags_dtml = re.findall(pattern, dtml)
empty_dtml = re.findall(pattern_empty,dtml)
raw_tags = re.findall(pattern_tag, dtml)

# Обробка виняткових ситуацій
if len(empty_dtml) > 0:
    try:
        raise EmptyTagError("Empty tag found in DTML file! ")
    except EmptyTagError:
        print("Сталася помилка EmptyTagError в файлі DTML.")
if len(tags_dtml) == 0:
    try:
        raise NoTagsFound("No tags found in DTML file! ")
    except:
        print("Сталася помилка NoTagsFound у DTML файлі ")

print("\nDTML Tags: \n")
for tag in raw_tags:
    if "dtml" in tag:
        print(tag)
