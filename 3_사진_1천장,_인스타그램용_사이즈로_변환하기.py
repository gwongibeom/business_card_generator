from PIL import Image
new_image = Image.new("RGB",(30,30),"pink")
new_image.save("test.png")

# paste

a = Image.open("3a.png")
print(a.size)
new_image = Image.new("RGB",(a.size[1],a.size[1]),"black")
new_image.save("test3.png")
new_image.paste(a,(int((a.size[1]-a.size[0])/2),0))
print
new_image.save("test3.png")