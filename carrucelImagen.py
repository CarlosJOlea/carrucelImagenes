import cv2


# Tipo de modificación
def on_type(a):

    if (0==a):
        img = cv2.imread("D:\Python\ImagenesIA\1.png")
        cv2.imshow("image",img)
    elif(1==a):
        img = cv2.imread("D:\Python\ImagenesIA\2.png")
        cv2.imshow("image",img)
    elif(2==a):
        img = cv2.imread("D:\Python\ImagenesIA\3.png")
        cv2.imshow("image",img)

def main():
    img = cv2.imread("D:\Python\ImagenesIA\1.png.png")
    cv2.namedWindow("image")
    cv2.imshow("image", img)
    # 3. Crear un control deslizante
    cv2.createTrackbar("type", "image", 0, 2, on_type)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()