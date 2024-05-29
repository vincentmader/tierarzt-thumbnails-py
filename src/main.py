import os
from pathlib import Path

from PIL import Image
from termcolor import colored

x_1, x_2, x_3, x_4 = 0, 0, 0, 0
print()

# Loop over all "Quartal" directories.
path_to_gallery = Path("../../../img-file-server/static/gallery/") # TODO Make sure path is correct.
for entry in sorted(os.listdir(path_to_gallery)):
    path_to_quarter = Path(path_to_gallery, entry)

    # Consider only directories that start with "Images_"
    if not entry.startswith("Images_"):
        continue
    if not os.path.isdir(path_to_quarter):
        continue

    # Loop over all images in "Quartal" directory.
    for entry_2 in sorted(os.listdir(path_to_quarter)):
        x_4 += 1
        if entry_2 in [".DS_Store", "thumbnails"]:
            continue
        path_to_image = Path(path_to_quarter, entry_2)

        # Determine path to newly-created thumbnail file.
        split = entry_2.split('.')
        filename, ext = '.'.join(split[:-1]), split[-1]
        path_to_thumbnail = Path(path_to_quarter, "thumbnails", f"{filename}_100.jpg")
        x_3 += 1

        # Save thumbnail if and only if file does not exist already.
        if os.path.exists(path_to_thumbnail):
            continue
        x_2 += 1

        try:
            img = Image.open(path_to_image)
            img.thumbnail((100, 100)) #, Image.ANTIALIAS)
            img.save(path_to_thumbnail)
        except Exception as e:
            msg  =   f"\tError: {entry_2}"
            msg += f"\n\t       {entry}"
            msg += f"\n\t       {e}"
            print(msg)
            continue

        print(f"\t{entry} {entry_2}")
        x_1 += 1

        # Ask user for confirmation before writing thumbnail file.
        # input(f"{path_to_image} -> {path_to_thumbnail}")

print()
print(f"{x_4} total files")
print(f"{x_3} total images")
print(colored(f"{x_2} thumbnails remaining to be created", "red"))
print(colored(f"{x_1} thumbnails successfully created", "green"))
