import cv2 as cv
import tools

images = [
    "data/naranja1.tif",
    "data/naranja2.tif",
    "data/naranja3.tif"
]
target_action = "q"
current_image = None


def parse_pair(str):
    s = str.split(",")
    return int(s[0]), int(s[1])


def read_image(name):
    global current_image
    current_image = cv.imread(name)


def show_image(image):
    (h, w, d) = image.shape
    print("width={}, height={}, depth={}".format(w, h, d))
    cv.imshow("Image", image)
    cv.waitKey(0)


def menu_home():
    print("Laboratorio de ruido en imágenes con OpenCV\nSeleccione una opción:\n"
          "1) Obtener RGB de píxel\n2) Extraer región de imagen\n"
          "3) Redimensionar imagen\n4) Redimensionar imagen (mantener proporción)\n"
          "5) Rotación de imagen\n6) Aplicar desenfoque gaussiano\nq) Salir")
    global target_action
    target_action = input("> ")

    if target_action == "x":
        pass
    elif target_action.isdigit() and 1 <= int(target_action) <= 6:
        menu_select_picture()


def menu_select_picture():
    global images
    for i in range(len(images)):
        print("{id}) {name}".format(id=i, name=images[i]))

    choice = int(input("> "))
    if 0 <= choice < len(images):
        read_image(images[choice])
        run_action()


def run_action():
    pass


def main():
    menu_home()


main()
