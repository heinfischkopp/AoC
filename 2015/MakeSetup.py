import os
from pathlib import Path


pfad =str(Path(os.path.dirname(os.path.realpath(__file__))))
template = pfad + os.sep +"template.py"

for i in range(1,5):
    file =  pfad + os.sep + "day" + str(i) + "_input.txt"
    if os.path.exists(file):
        print("skipping day %s's Input" %(i))
    else:
        with open(file, 'w') as f:
            f.write('')

    file =  pfad + os.sep + "day" + str(i) + "_testdata.txt"
    if os.path.exists(file):
        print("skipping day testdata %s's Input" %(i))
    else:
        with open(file, 'w') as f:
            f.write('')

    file =  pfad + os.sep + "day" + str(i) + ".py"
    if os.path.exists(file):
        print("skipping day %s's Code" %(i))
    else:
        with open(template, 'r') as f :
            filedata = f.read()

        filedata = filedata.replace('MyTools.AoC(1)', 'MyTools.AoC(%s)' %(i))

        # Write the file out again
        with open(file, 'w') as f:
            f.write(filedata)