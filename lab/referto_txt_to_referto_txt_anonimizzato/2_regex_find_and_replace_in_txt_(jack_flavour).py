f = open("Refertibanana/Referto.txt", "r")
text = f.read()
# print(text)


def find_between_r(s, first, last):
    try:
        start = s.rindex(first) + len(first)
        end = s.rindex(last, start)
        return s[start:end]
    except ValueError:
        return ""


name = find_between_r(text, "Sig.", "Data Nascita")
newtext = text.replace("Sig." + name, "")
print(newtext)
