from PIL import Image, ImageDraw


def draw_forest(matrix: list[list[int]], box_size: int):
    height, width = len(matrix), len(matrix[0])

    image_width = width * box_size
    image_height = height * box_size

    image = Image.new("RGB", (image_width, image_height), color="white")
    draw = ImageDraw.Draw(image)

    for i in range(height):
        for j in range(width):
            x, y = j * box_size, i * box_size
            box_color = "green" if matrix[i][j] == 1 else "black" if matrix[i][j] == 0 else "red"
            draw.rectangle((x, y, x + box_size, y + box_size), fill=box_color)
    return image
