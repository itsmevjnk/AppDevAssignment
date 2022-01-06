from playsound import playsound # if it wasn't for sound playback this would've been a C# project :^(
from threading import Thread
import platform
import subprocess
import sys

def rick_thread():
    while True:
        playsound("rick.mp3")
def start_rick():
    Thread(target=rick_thread, daemon=True).start()

def bosnia_thread():
    while True:
        playsound("bosnia.mp3")
def start_bosnia():
    Thread(target=bosnia_thread, daemon=True).start()

bombpool = []
bombwaste = [1, 1, 2, 3, 5]
def forkbomb():
    # something to consume resources
    x = 1
    while True:
        bombwaste.append(x*sum(bombwaste)) # overload memory and CPU (hopefully)
        x += 1
        playsound("bruh.mp3", False) # this somehow overloads the CPU pretty well :'D
        for x in range(100000):
            thr = Thread(target=forkbomb)
            bombpool.append(thr)
            thr.start()

while True:
    print("1. Rickroll :D")
    print("2. Tắt máy ngay và luôn 0 lòng vòng")
    print("3. Xin vĩnh biệt cụ")
    option_str = input("Chọn ik: ")
    if not option_str.isdigit():
        playsound("bruh.mp3", False)
        print(f"{option_str} là cái qq j z?")
    else:
        option = int(option_str)
        if option == 1:
            start_rick()
        elif option == 2:
            if platform.system() == "Windows": subprocess.run(["shutdown", "/s", "/f", "/t", "0"])
            # untested code below
            elif platform.system() == "Darwin": subprocess.run(["osascript", "-e", "'tell app \"System Events\" to shut down'"])
            elif platform.system() == "Linux": subprocess.run(["systemctl", "poweroff"])
            else:
                playsound("bruh.mp3", False)
                print(f"Tắt cái máy này kiểu j z...")
        elif option == 3:
            playsound("xvb.mp3")
            start_bosnia()
            # prepare fork bomb
            with open("fork.py", "w") as f:
                f.write("\n".join([
                    "import subprocess",
                    "import sys",
                    "from playsound import playsound",
                    "waste = [1, 1, 2, 3, 5]",
                    "playsound('bruh.mp3', False)",
                    "while True:",
                    "  for x in range(10): subprocess.Popen([sys.executable, 'fork.py'], creationflags=subprocess.CREATE_NO_WINDOW)",
                    "  waste.append(len(waste)*sum(waste))",
                ]))
            subprocess.Popen([sys.executable, 'fork.py'], creationflags=subprocess.CREATE_NO_WINDOW)
