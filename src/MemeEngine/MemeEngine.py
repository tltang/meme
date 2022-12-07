"""Resize image, and Quote and Author on it"""
from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine:
    """class to resize image, and add Quote and Author on it"""
    def __init__(self, img_out_path='./static'):
        """Initialize instance.
        Arguments:
            img_out_path {str} -- edited images output location
        """
        self.img_out_path = img_out_path

    def generate_postcard(self, img_path, quotebody=None, author=None, width=500) -> str:
        """Create a Postcard With a Text Greeting
        Arguments:
            img_path {str} -- the file location for the input image
            quotebody {str} -- quote from quote engine
            author {str} -- author from quote engine
            width {int} -- The pixel width value. Default=500
        Returns:
            str -- the file path to the output image
        """

        # open image
        with Image.open(img_path) as img:
            # The crop method from the Image module takes four coordinates as input.
            # The right can also be represented as (left+width)
            # and lower can be represented as (upper+height).

            # get input image file extension
            extension = img_path.split('.')[-1]

            # if width input value is not a valid value, change it to max allowed number
            if width > 500 or width <= 0 or width is None:
                width = 500

            # adjust and resize the img
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.Resampling.NEAREST)

            if quotebody is not None and author is not None:
                draw = ImageDraw.Draw(img)
                font_size = int(height / 16)
                font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=font_size)
                # get text display x axis
                x_min = 0
                x_max = int(img.size[0] / 12)
                x_range = random.randint(x_min, x_max)

                lines = [quotebody, " > " + author]
                line_height = font.getsize('hg')[1]
                # get text display y axis
                y_min = int(img.size[1] / 24)
                y_max = int(img.size[1])
                # leave some space below text to avoid text getting out of image
                y_max -= ((len(lines) + 1) * line_height)
                y_range = random.randint(y_min, y_max)

                for line in lines:
                    draw.text((x_range, y_range), line, font=font)
                    y_range += line_height

                out_path = f'{self.img_out_path}/' \
                           f'{random.randint(0, 10000000)}.{extension}'

                img.save(out_path)

        return out_path

    def __repr__(self):
        return f'Image Output Path: {self.img_out_path}'


if __name__ == '__main__':
    # instantiate a MemeEngine object
    post_card = MemeEngine('./static')
    print(post_card)
    post_card.generate_postcard('./_data/photos/dog/xander_1.jpg', quotebody='Hello World', author='anonymous', width=500)


