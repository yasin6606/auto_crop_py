import cv2
from os import system, listdir, path, mkdir
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

# Get crop coordinates
start_y_default: int = 1203
start_x_default: int = 370
end_y_default: int = 470
end_x_default: int = 422

# In order: start_y, start_x, end_y, end_x
coordinates = [
    {"text": "Start Y axis: ", "value": start_y_default},
    {"text": "Start X axis: ", "value": start_x_default},
    {"text": "End Y axis: ", "value": end_y_default},
    {"text": "End X axis: ", "value": end_x_default}
]

print("\nEnter the coordinates in order to crop!\n")
for i in range(len(coordinates)):
    try:
        coordinates[i]["value"] = int(input(coordinates[i]["text"]))
    except:
        continue

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
                          coordinates[0]["value"]:coordinates[0]["value"] + coordinates[2]["value"],
                          coordinates[1]["value"]:coordinates[1]["value"] + coordinates[3]["value"]
                          ]
            images.append(img_cropped)

    return images


loaded = load_all_images(folder_name_addr)

# Save new cropped images to new directory
for i, name in enumerate(listdir(folder_name_addr)):
    cv2.imwrite(path.join(folder_new_addr, new_folder_name + "_{}.png".format(i + 1)), loaded[i])

print("\nThe result is saved in {}\n\nEnjoy!\n".format(folder_new_addr))
