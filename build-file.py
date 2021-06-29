from PIL import Image
import os

# args = sys.argv[1:]

key = (0,0,0)

if __name__ == "__main__":
    outFileName = 'output/data.txt'
    print(f"Writing to {outFileName} with {key}")
    outFile = open(outFileName, 'w')
    directory = "output"
    frame = 0
    
    list_of_files = os.listdir(directory)
    list_of_files.sort()

    for filename in sorted(list_of_files):
        if filename.endswith(".png"): 
            path = os.path.join(directory, filename)
            img = Image.open(path)
            print(f"Reading {path} as {img.mode}")
            frame = frame + 1
            for y in range(img.height):
                for x in range(img.width):
                    px = img.getpixel((x,y))
                    
                    px =  tuple(map(lambda i: (px[i] + (key[i] + x * img.height + y) * (frame * 21)) % 256, range(3)))

                    txt = '%02x%02x%02x' % px
                    outFile.write(txt)
                    outFile.write(' ')
                outFile.write("\n")
            outFile.write("\n")
            continue
        else:
            continue

    # # Read image
    
    # # Output Images
    # img.show()
    
    # # prints format of image
    # print(img.format)
    
    # # prints mode of image
    # print(img.mode)
