from os import system, getcwd

root_dir = getcwd()
with open(f'{root_dir}\\site_list.txt', 'r') as src_list:
    for line in src_list.readlines():
        print(line[:-1])

        system(f"powershell -C Start-Process chrome.exe -ArgumentList @('-incognito','{line[:-1]}')")

