from PIL import Image, ImageOps
import errno
import os


class ImageConverter:

    def __init__(self, input_path):
        # initiating variables
        base_path = '../staticfiles/img/masks/'
        filenames = [
            'small_thumbnail_img_mask.png',
            'big_thumbnail_img_mask.png',
        ]

        input_img = {
            'path': input_path,
            'img_object': None,
            'width': 0,
            'height': 0,
            'aspect_ratio': 0,
        }
        small_mask = {
            'path': base_path + filenames[0],
            'img_object': None,
            'width': 0,
            'height': 0,
            'aspect_ratio': 0,
        }
        big_mask = {
            'path': base_path + filenames[1],
            'img_object': None,
            'width': 0,
            'height': 0,
            'aspect_ratio': 0,
        }

        # open images
        input_img = self.try_open(input_img['path'])
        small_mask = self.try_open(small_mask['path'])
        big_mask = self.try_open(big_mask['path'])

        # convert masks to grayscale
        small_mask = small_mask.convert('L')
        big_mask = big_mask.convert('L')

        # threshold and invert the colors (white will be transparent)
        small_mask = small_mask.point(lambda x: x < 100 and 255)
        big_mask = big_mask.point(lambda x: x < 100 and 255)

        # resize and crop images to fit
        small_thumbnail = ImageOps.fit(input_img, small_mask.size)
        big_thumbnail = ImageOps.fit(input_img, big_mask.size)
        baground_img = ImageOps.fit(input_img, (1920, 1080))

        small_thumbnail.putalpha(small_mask) # Modifies the original image without return
        big_thumbnail.putalpha(big_mask)

        small_thumbnail.save('./static/img/chuj1.png')
        big_thumbnail.save('./static/img/chuj2.png')

        # 3. brightness/contrast
        # 2. blue tint
        # 1. resize for the big image and the other two small ones
        # 4. crop for each image
        # 5. apply mask for two small images
        # 6. save all in database

    def try_open(self, path):
        try:
            img = Image.open(path)
        except IOError:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

        return img


path1 = '../mediafiles/Slide1.JPG'   # correct path
path2 = '../mediafiless/Slide1.JPG'  # wrong path
img = ImageConverter(path1)
