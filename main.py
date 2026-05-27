import subprocess

if 'clear-cache.desktop' not in subprocess.check_output('ls ~/.local/share/applications/', shell=True).decode('utf-8'):
    subprocess.run("sudo cp clear-cache.desktop ~/.local/share/applications/clear-cache.desktop", shell=True)
    subprocess.run("sudo mkdir /usr/bin/ceche_cleaner", shell=True)
    subprocess.run("sudo cp main.py /usr/bin/ceche_cleaner/", shell=True)
    subprocess.run("sudo chmod +x ~/.local/share/applications/clear-cache.desktop", shell=True)


	
try:
    size_cache: str = subprocess.check_output('sudo du -sh /var/cache/pacman/pkg', shell=True).decode('utf-8')
except:
    print("For you Arch empty cache ")
    exit()

print("Auto clear cache for you Arch\n\n")
print(f"Cache wait to clear: {size_cache.split('\')[0]}\n")

ansfer = input("Do you wan to clear cache?\nYes/No >>>")

if ansfer.lower() == "yes" or ansfer.lower() == "y":
    subprocess.run("sudo rm -rf /var/cache/pacman/pkg", shell=True)
    print("Clear succes!")
elif ansfer.lower() == "no" or ansfer.lower() == "n":
    print("Clear canceled!")
