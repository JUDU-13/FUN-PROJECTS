import csv
from PIL import Image, ImageDraw, ImageFont

# Open the CSV or Excel file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Iterate through the rows of the file
    for row in reader:
        name = row[0]
        date = row[1]
        # Open the image
        image = Image.open('certificate.jpg')
        # Create an ImageDraw object
        draw = ImageDraw.Draw(image)
        # Set the font and size
        font = ImageFont.truetype('arial.ttf', 32)
        # Draw the name and date on the image
        draw.text((250, 250), name, font=font)
        draw.text((250, 350), date, font=font)
        # Save the image with the name and date
        image.save(f'{name}-{date}.jpg')

#This code assumes that the CSV or Excel file is in the same format as the following example:       
#Name, Date
#John Doe, 01-01-2022
#Jane Smith, 02-01-2022
