from PIL import ImageGrab, Image
img=ImageGrab.grab()
saveas='screenshot.png'
img.save(saveas)

image = Image.open('screenshot.png')
#area = (170, 50, 1500, 80)
area = (390, 50, 1500, 80)
cropped_img = image.crop(area)
cropped_img.save('screenshot.png')

cropped_img.show()