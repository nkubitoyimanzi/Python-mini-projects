import qrcode

data = input("Enter data : ")
filename = input("What will be the name of your file : ").strip()
if not filename.endswith(".png"):
    filename += ".png"

img = qrcode.make(data)
img.save(filename)

print(f"Your image has been saved as {filename}")
