import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

x = 60
y = 60


def crop(im):
    # Calculate the width and height of the image
    width, height = im.size

    # Crop the image
    cropped_im = im.crop((x, y, x + width, y + height))

    # Save the cropped image
    cropped_im.save("cropped_image.jpg")

    cropped_im1 = im.crop((0, 0, width / 2, height / 2))
    cropped_im1.save("cropped_image1.jpg")

    # Crop the top-right image
    cropped_im2 = im.crop((width / 2, 0, width, height / 2))
    cropped_im2.save("cropped_image2.jpg")

    # Crop the bottom-left image
    cropped_im3 = im.crop((0, height / 2, width / 2, height))
    cropped_im3.save("cropped_image3.jpg")

    # Crop the bottom-right image
    cropped_im4 = im.crop((width / 2, height / 2, width, height))
    cropped_im4.save("cropped_image4.jpg")

# convert image to triangle
def triangle(image):
    # Calculate the width and height of the image
    width, height = image.size

    # Create a new image with a white background and the same size as the original image
    new_image = Image.new("RGB", (width, height), (255, 255, 255))

    # Iterate over the pixels of the new image and set the pixel values to white
    for x in range(width):
        for y in range(height):
            new_image.putpixel((x, y), (255, 255, 255))

    # Calculate the center point of the image
    center_x = width // 2
    center_y = height // 2

    # Iterate over the pixels of the original image and check if the pixel is within the diamond shape
    for x in range(width):
        for y in range(height):
            # Calculate the distance from the center point
            distance = abs(center_x - x) + abs(center_y - y)
            # Check if the pixel is within the diamond shape
            if distance < width // 2:
                # Set the corresponding pixel in the new image to the value of the pixel in the original image
                new_image.putpixel((x, y), image.getpixel((x, y)))

    # Save the new image to a file
    return new_image

# concta 2 images
def conctat(image1, image2):
    # Create a new image that is twice the width of the original images
    result = Image.new("RGB", (image1.width * 2, image1.height))

    # Paste the images into the result image side by side
    result.paste(image1, (0, 0))
    result.paste(image2, (image1.width, 0))

    # Save the result image
    return result

# make squre from concated images
def fourScquere(image1, image2):
    # Crop the images into 4 squares
    square_size = image1.width // 2
    image1_square1 = image1.crop((0, 0, square_size, square_size))
    image1_square2 = image1.crop((square_size, 0, square_size * 2, square_size))
    image1_square3 = image1.crop((0, square_size, square_size, square_size * 2))
    image1_square4 = image1.crop((square_size, square_size, square_size * 2, square_size * 2))
    image2_square1 = image2.crop((0, 0, square_size, square_size))
    image2_square2 = image2.crop((square_size, 0, square_size * 2, square_size))
    image2_square3 = image2.crop((0, square_size, square_size, square_size * 2))
    image2_square4 = image2.crop((square_size, square_size, square_size * 2, square_size * 2))

    # Create a new image that is twice the width and height of the original images
    result = Image.new("RGB", (image1.width * 2, image1.height * 2))

    # Paste the images into the result image in a grid pattern
    result.paste(image1_square1, (0, 0))
    result.paste(image1_square2, (square_size, 0))
    result.paste(image2_square1, (0, square_size))
    result.paste(image2_square2, (square_size, square_size))
    result.paste(image1_square3, (0, square_size * 2))
    result.paste(image1_square4, (square_size, square_size * 2))
    result.paste(image2_square3, (0, square_size * 3))
    result.paste(image2_square4, (square_size, square_size * 3))
    return result

def addCentralText(img, text):
    # Call draw Method to add 2D graphics in an image
    draw = ImageDraw.Draw(img)
    # Custom font style and font size
    myFont = ImageFont.truetype('FreeMono.ttf', 45)

    # text_width, text_height = draw.textsize(text, font=myFont)
    #
    # # Calculate the x and y coordinates to center the text
    # x = (img.width - text_width) / 2
    # y = (img.height - text_height) / 2

    # Add Text to an image
    draw.text((130,200), text, font=myFont, fill=(255, 0, 0))

    return img

def save(img):
    img.save("result.jpg")

def convert(image):
    # crop 1 image into 4
    crop(image)

    # tringle images
    image1 = triangle(Image.open("cropped_image1.jpg"))
    image2 = triangle(Image.open("cropped_image2.jpg"))
    image3 = triangle(Image.open("cropped_image3.jpg"))
    image4 = triangle(Image.open("cropped_image4.jpg"))

    # concat images back 4 into 1
    res = conctat(image1, image2)
    res2 = conctat(image3, image4)
    res3 = fourScquere(res, res2)

    # add text
    res4 = addCentralText(res3, "My TEXT")


    # save result
    save(res4)

if __name__ == "__main__":
    # input image with 4 imaages in form
    image = Image.open("image1.jpg")
    convert(image)