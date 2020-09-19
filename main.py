import cv2 as cv
import tools

images = [
    "data/naranja1.tif",
    "data/naranja2.tif",
    "data/naranja3.tif",
    "data/jocote1.tif",
    "data/jocote2.tif",
    "data/jocote3.tif"
]
target_action = "q"
current_image = None


def parse_pair(string):
    s = string.split(",")
    return int(s[0]), int(s[1])


def read_image(name):
    global current_image
    current_image = cv.imread(name)


def show_image(image):
    (h, w, d) = image.shape
    print("width={}, height={}, depth={}".format(w, h, d))
    cv.imshow("Image", image)
    cv.waitKey(0)


def menu_rgb_pixel():
    print("====| Obtener RGB de píxel |\n"
          "Introdúzca del píxel deseado...")
    xy = input("X,Y: ")
    xy_split = parse_pair(xy)

    (R, G, B) = tools.get_pixel_rgb(current_image, xy_split[0], xy_split[1])

    print("El píxel ({}) tiene la siguiente información:".format(xy),
          "R={}, G={}, B={}".format(R, G, B))

    menu_home()


def menu_extract_image_region():
    print("====| Extraer región de imagen |\n")
    p1 = input("Punto de partida (x,y): ")
    p2 = input("Punto final (x,y): ")
    p1s = parse_pair(p1)
    p2s = parse_pair(p2)

    result = tools.get_image_region(current_image,
                                    (p1s[1], p2s[1]),
                                    (p1s[0], p2s[0]))
    show_image(current_image)
    show_image(result)

    menu_home()


def menu_resize_image():
    print("====| Redimensionar imagen |\n"
          "Introdúzca una nueva resolución...")
    new_dimens = input("X,Y: ")
    (x, y) = parse_pair(new_dimens)
    resized = tools.resize(current_image, x, y)
    show_image(resized)

    menu_home()


def menu_resize_with_aspect_ratio():
    print("====| Redimensionar imagen (mantener proporción) |\n")
    x = input("Introdúzca el ancho de la imagen: ")
    resized = tools.resize_with_aspect_ratio(current_image, int(x))
    show_image(resized)

    menu_home()


def menu_rotate_picture():
    print("====| Rotación de imagen |")
    degrees = input("Grados de rotación: ")
    rotated = tools.rotate(current_image, int(degrees))
    show_image(rotated)

    menu_home()


def menu_gaussian_blur():
    print("====| Aplicar desenfoque gaussiano |")
    kernel = input("Tamaño de kernel: ")
    blurred = tools.gaussian_blur(current_image, int(kernel))
    show_image(blurred)

    menu_home()


def menu_home():
    print("Laboratorio de ruido en imágenes con OpenCV\nSeleccione una opción:\n"
          "1) Obtener RGB de píxel\n2) Extraer región de imagen\n"
          "3) Redimensionar imagen\n4) Redimensionar imagen (mantener proporción)\n"
          "5) Rotación de imagen\n6) Aplicar desenfoque gaussiano\nq) Salir")
    global target_action
    target_action = input("> ")

    if target_action == "q":
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
    if target_action == "1":
        menu_rgb_pixel()
    if target_action == "2":
        menu_extract_image_region()
    if target_action == "3":
        menu_resize_image()
    if target_action == "4":
        menu_resize_with_aspect_ratio()
    if target_action == "5":
        menu_rotate_picture()
    if target_action == "6":
        menu_gaussian_blur()


menu_home()
