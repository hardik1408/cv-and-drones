import numpy as np
from PIL import Image, ImageDraw

def generate():
    flag = Image.new('RGB', (600, 600), (255, 255, 255))
    draw = ImageDraw.Draw(flag)

    saffron = (255, 153, 51)
    green = (19, 136, 8)
    blue = (0, 0, 255)
    white = (255, 255, 255)

    draw.rectangle([0, 0, 600, 200], fill=saffron)
    draw.rectangle([0, 200, 600, 400], fill=white)
    draw.rectangle([0, 400, 600, 600], fill=green)

    center = (300, 300)
    radius = 100
    width = 2
    spoke_width = 1
    num_spokes = 24 

    draw.ellipse([center[0] - radius - width, center[1] - radius - width,
                    center[0] + radius + width, center[1] + radius + width],
                    outline=blue, fill=white, width=width)
    angles = np.linspace(0, 2 * np.pi, num_spokes + 1)[:-1]

    for angle in angles:
        x1 = center[0] + radius * np.cos(angle)
        y1 = center[1] + radius * np.sin(angle)
        x2 = center[0] + (radius - spoke_width / 2) * np.cos(angle)
        y2 = center[1] + (radius - spoke_width / 2) * np.sin(angle)

        # Extend the spoke inwards slightly to meet at the center
        spoke_extension = 5  # Adjust this value for visual preference
        center_x = center[0] + spoke_extension * np.cos(angle)
        center_y = center[1] + spoke_extension * np.sin(angle)

        # Draw the complete spoke with connection to the center
        draw.line([x1, y1, center_x, center_y, x2, y2], fill=blue, width=spoke_width)

    draw.ellipse([center[0] - width, center[1] - width,
              center[0] + width, center[1] + width],
             fill=blue, width=width)
    flag.show()
    global generated_flag
    generated_flag = flag
    flag.save('indian_flag.png')
    

def rotate_image(image, degrees):
    rotated_image = image.rotate(degrees)
    rotated_image.save('rot3_indian_flag.png')
    return rotated_image

rotate_image(Image.open('indian_flag.png'), 270).show()


