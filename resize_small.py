from PIL import Image
import os

target_height = 900
target_width = 1600

# Load images
path = "."
exts = ["jpg", "bmp", "png", "gif", "jpeg"]
images = [(path + "/" + fn) for fn in os.listdir(path) if any(fn.endswith(ext) for ext in exts)]

print("{} images".format(len(images)))
i = 1
for fn in images:
	print("  {}/{}\t{}".format(i,len(images),fn))
	img = Image.open(fn)
	scale = min(target_width / img.width, target_height / img.height)
	new_width = int(img.width * scale)
	new_height = int(img.height * scale)
	img = img.resize((new_width, new_height), Image.ANTIALIAS)
	img.save(fn)
	i += 1

print("Done")
