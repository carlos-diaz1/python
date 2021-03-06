from simpleimage import SimpleImage


def sepia_pixel(pixel):
    R = pixel.red
    G = pixel.green
    B = pixel.blue
    pixel.red = 0.393 * R + 0.769 * G + 0.189 * B
    pixel.green = 0.349 * R + 0.686 * G + 0.168 * B
    pixel.blue = 0.272 * R + 0.534 * G + 0.131 * B

def main():


    imagen=input("Ingrese el nombre de su imagen: ")
    image = SimpleImage('images/' + imagen)
    image.show()
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            sepia_pixel(pixel)
    image.show()
if __name__ == '__main__':
    main()