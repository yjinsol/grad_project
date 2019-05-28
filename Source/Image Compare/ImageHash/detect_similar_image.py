from PIL import Image
from scipy._lib.six import xrange
import imagehash
#from utility import dhash, hamming_distance

# img = Image.open('naver1.png')
# width, height = img.size
# pixels = list(img.getdata())
# for col in xrange(width):
#     print(pixels[col:col+width])
#
# difference = []
# for row in xrange(height):
#     for col in xrange(width):
#         if col != width:
#             difference.append(pixels[col+row] > pixels[(col+row)+1])
#
# for col in xrange(width-1):
#     print(difference[col:col+(width-1)])


# def dhash(image, hash_size = 8):
#     # Grayscale and shrink the image in one step.
#     image = image.convert('L').resize(
#         (hash_size + 1, hash_size),
#         Image.ANTIALIAS,
#     )
#
#     pixels = list(image.getdata())
#
#     # Compare adjacent pixels.
#     difference = []
#     for row in xrange(hash_size):
#         for col in xrange(hash_size):
#             pixel_left = image.getpixel((col, row))
#             pixel_right = image.getpixel((col + 1, row))
#             difference.append(pixel_left > pixel_right)
#
#     # Convert the binary array to a hexadecimal string.
#     decimal_value = 0
#     hex_string = []
#     for index, value in enumerate(difference):
#         if value:
#             decimal_value += 2**(index % 8)
#         if (index % 8) == 7:
#             hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
#             decimal_value = 0
#
#     return ''.join(hex_string)

hash = imagehash.average_hash(Image.open('naver1.png'))
print(hash)
hash2 = imagehash.average_hash(Image.open('naver2.png'))
print(hash2)
hash3 = imagehash.average_hash(Image.open('juniornaver.png'))
print(hash3)
hash4 = imagehash.average_hash(Image.open('wooribank.png'))
print(hash4)

print(hash == hash2)
print(hash - hash2)

print(hash == hash3)
print('juniornaver==hash', hash - hash3)

print(hash2==hash4)
print(hash-hash3)

hash8 = imagehash.average_hash(Image.open('bank1.png'))
print(hash8)

hash9 = imagehash.average_hash(Image.open('bank2.png'))
print(hash9)

print(hash8==hash9)
print(hash9-hash8)


hash10 = imagehash.average_hash(Image.open('chrome.png'))
print(hash10)

hash11 = imagehash.average_hash(Image.open('edge.png'))
print(hash11)

print(hash10==hash11)
print(hash10-hash11)
# orig = Image.open('naver1.png')
# modif = Image.open('naver2.png')
# dhash(orig)
# dhash(modif)