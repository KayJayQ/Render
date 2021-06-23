import tkinter as tk
from Object import OBJ


if __name__ == '__main__':
    print("Start Running...")
    obj = OBJ()
    obj.parse_from_file("D:\\ML\\cube.obj")
    print(obj)