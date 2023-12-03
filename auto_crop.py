import cv2
from os import system, listdir, path, mkdir, getcwd
from shutil import rmtree

system("clear || cls")

print("Hey!\n\nI am Yasin Gourkani\n\nFind me on GitHub: https://github.com/yasin6606\n\n")

new_folder_name: str = input("What is the Session name (For E.X: session_6): ")

# Get source address
while True:
    folder_name_addr: str = input("\nEnter the Source Directory Address (For E.X. ./source): ")

    if path.exists(folder_name_addr) is False:
        print("\n! Entered source address not found")
        continue

    break

folder_new_addr: str = r"./{}".format(new_folder_name)

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
    tempImg = cv2.imread(path.join(sourceFolderAddr, firstImg))
    cv2.namedWindow(firstImg, flags=cv2.WINDOW_NORMAL)
    cv2.resizeWindow(firstImg, 1920, 1080)
    coors = cv2.selectROI(firstImg, tempImg)

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

# Make saving directory
if path.exists(folder_new_addr):
    rmtree(folder_new_addr)

mkdir(folder_new_addr)


# Load source files
def load_all_images(folder: str):
    images = []

    for filename in listdir(folder):

        # Read source images
        img = cv2.imread(path.join(folder, filename))

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
    cv2.imwrite(path.join(folder_new_addr, new_folder_name + "_{}.png".format(i + 1)), loaded[i])

print("\nThe result is saved in {}\n\nEnjoy!\n".format(folder_new_addr))
