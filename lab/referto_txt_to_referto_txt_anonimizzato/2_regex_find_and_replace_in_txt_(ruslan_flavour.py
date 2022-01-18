import os
import re

for filename in os.listdir('Refertibanana'):
    if filename.endswith('.txt'):
        with open(os.path.join('Refertibanana', filename)) as f:
            content = f.read()
# f = open("Refertibanana/Referto.txt", "r")

# txt = f.read()
            x = re.sub("Sig.[\s\S]*Data Nascita", "Data Nascita", content)
            # print(x)
            newfilename = filename[:-4]+"_regex.txt"
            print(newfilename)
            with open(newfilename, 'w') as i:
                i.write(x)
