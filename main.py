from PIL import Image
import numpy as np
from colorama import Fore, init; init()

def progress_bar(percent, text="", bar_len=30):
    SYMBOL = "━"
    done = round(percent*bar_len)
    left = bar_len - done
    print(f"   {Fore.GREEN}{SYMBOL*done}{Fore.RESET}{SYMBOL*left} {f'[{round(percent*100,2)}%]'.ljust(8)} {Fore.MAGENTA}{text}{Fore.RESET}", end='\r')
    if percent == 1: print("✅")

def create_transition(path1, path2, new_path):
    img1 = np.array(Image.open(path1))
    img2 = np.array(Image.open(path2))
    images = []

    for iter in range(256):
        for i,line in enumerate(img1):
            progress_bar((i+1+(img1.shape[0]*iter))/img1.shape[0]/256)
            for j,pixel in enumerate(line):
                for k,channel in enumerate(pixel):
                    if img2[i][j][k] > channel:
                        img1[i][j][k] += 1
                    elif img2[i][j][k] < channel:
                        img1[i][j][k] -= 1
        
        images.append(Image.fromarray(img1))
    
    images[0].save(new_path, save_all=True, append_images=images[1:], duration=1, loop=0)
    

create_transition("images/polar-bear-1.jpg", "images/polar-bear-2.jpg", "output/transition.gif")
