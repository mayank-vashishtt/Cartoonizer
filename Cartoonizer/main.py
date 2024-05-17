import cv2
import os

def cartoonize(file, input_dir, output_dir):
    full_path = input_dir +"\\" + file
    img = cv2.imread(full_path)

    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

  
    output_path = output_dir + "\\" + file[:-4] + "_output.png"
    cv2.imwrite(output_path, edges)
    print(file + " files processed")


def main():
    input_directory = "xyz\\"  #write the file where the images are
    output_directory = "abc\\" #write the file where you want to store converted images

    files = os.listdir(input_directory)

    

    for i in range(len(files)):
        cartoonize(files[i], input_directory,output_directory)



    

if __name__ == "__main__":
    main()