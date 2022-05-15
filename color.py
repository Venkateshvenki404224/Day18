import colorgram

colors = colorgram.extract('image.jpg', 100)
# Add the image you want to get the all the colors in it
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)

