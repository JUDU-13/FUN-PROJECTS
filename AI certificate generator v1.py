from PIL import Image, ImageDraw, ImageFont

# Load the certificate template
template = Image.open("certificate_template.jpg")

# Create an ImageDraw object
draw = ImageDraw.Draw(template)

# Add the recipient's name to the certificate
name_font = ImageFont.truetype("arial.ttf", 36)
name_text = "John Doe"
name_width, name_height = draw.textsize(name_text, font=name_font)
name_x = (template.width - name_width) / 2
name_y = template.height / 3
draw.text((name_x, name_y), name_text, fill=(0, 0, 0), font=name_font)

# Add the date to the certificate
date_font = ImageFont.truetype("arial.ttf", 24)
date_text = "January 1, 2020"
date_width, date_height = draw.textsize(date_text, font=date_font)
date_x = (template.width - date_width) / 2
date_y = template.height / 2
draw.text((date_x, date_y), date_text, fill=(0, 0, 0), font=date_font)

# Add the event or course to the certificate
event_font = ImageFont.truetype("arial.ttf", 24)
event_text = "Introduction to Machine Learning"
event_width, event_height = draw.textsize(event_text, font=event_font)
event_x = (template.width - event_width) / 2
event_y = template.height / 2 + date_height + 10
draw.text((event_x, event_y), event_text, fill=(0, 0, 0), font=event_font)

# Save the certificate
template.save("certificate.jpg")
