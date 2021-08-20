import os

if __name__ == "__main__":
    directory = "D:\\Projects\\PythonProjects\\Learn\\data\\stickers_anime"
    files = os.listdir(directory)
    [(lambda name: os.remove(f"{directory}\\{name}"))(name) for name in files if name[-3:] != 'jpg']
