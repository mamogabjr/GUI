import os

pipe = os.popen("dir *.md")
print(pipe.read())
