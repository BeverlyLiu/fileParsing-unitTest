import os, glob, shutil

os.chdir('D:/Script/ForInterview')
for file in glob.glob('*.py'):
    shutil.copy(file, "C:/Users/beile/PycharmProjects/Script//")
