from cv2 import imread, imwrite, selectROI, namedWindow, resizeWindow, WINDOW_NORMAL
from os import system, listdir, path, mkdir, getcwd
from shutil import rmtree

system("clear || cls")

print("Hey!\n\nI am Yasin Gourkani\n\nFind me on GitHub: https://github.com/yasin6606\n\n")

new_folder_name: str = input("What is the Session name (For E.X: session_6): ")
extera_name: str = input("Enter extera name (If applicable): ")

# Get source address
while True:
    folder_name_addr: str = input("\nEnter the Source Directory Address (For E.X. source): ")

    if path.exists(folder_name_addr) is False:
        print("\n! Entered source address not found")
        continue

    break

folder_new_addr: str = r"./{}".format(new_folder_name)

# Make saving directory
while True:
    if path.exists(folder_new_addr):
        rm_dir = input("\nDo you want to remove same directory as you are entered? (y or n): ")

        if rm_dir == 'y' or rm_dir == "yes" or rm_dir == "Yes":
            rmtree(folder_new_addr)
            mkdir(folder_new_addr)

            break
        elif rm_dir == "n" or rm_dir == "no":
            break
    else:
        mkdir(folder_new_addr)
        break

# Coordination menu
print("\nWhich coordinate selection do you prefer:\n\t1-Auto\n\t2-Manual\n\n")
coordinateSelection: int = int(input("Select one: "))

coordinates = [
    {"text": "Start X axis: ", "value": 0},
    {"text": "Start Y axis: ", "value": 0},
    {"text": "End X axis: ", "value": 0},
    {"text": "End Y axis: ", "value": 0}
]

if coordinateSelection == 1:
    # Auto coordinating
    sourceFolderAddr = path.join(getcwd(), folder_name_addr)

    # Get the address of first image in images' source directory
    firstImg = listdir(sourceFolderAddr)[0]

    print("\nSelection Guidance:\n")
    tempImg = imread(path.join(sourceFolderAddr, firstImg))
    namedWindow(firstImg, flags=WINDOW_NORMAL)
    resizeWindow(firstImg, 1920, 1080)
    coors = selectROI(firstImg, tempImg)

    for i, v in enumerate(coors):
        coordinates[i]["value"] = v

elif coordinateSelection == 2:
    # Manual coordinating

    print("\n")
    for i in range(len(coordinates)):
        try:
            coordinates[i]["value"] = int(input(coordinates[i]["text"]))
        except:
            continue

else:
    print("\nEnter correct coordination option!\n")
    exit(0)


# Load source files
def load_all_images(folder: str):
    images = []

    for filename in listdir(folder):

        # Read source images
        img = imread(path.join(folder, filename))

        if img is not None:
            # Crop images
            img_cropped = img[
                          coordinates[1]["value"]:coordinates[1]["value"] + coordinates[3]["value"],
                          coordinates[0]["value"]:coordinates[0]["value"] + coordinates[2]["value"]
                          ]
            images.append(img_cropped)

    return images


loaded = load_all_images(folder_name_addr)

# Save new cropped images to new directory
for i, name in enumerate(listdir(folder_name_addr)):
    imwrite(path.join(folder_new_addr, new_folder_name + "_{}_{}.png".format(i + 1, extera_name)), loaded[i])

print("\nThe result is saved in {}\n\nEnjoy!\n".format(folder_new_addr))
