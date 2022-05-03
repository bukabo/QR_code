from PIL import Image
import pyqrcode
import cv2


def qr_generator(text, logo=None):
    """
    Функция генерирует QR-код. \n
    Также на вход можно подать логотип в .png формате, который будет размещен в центре QR-кода. \n
    :param text: текст для преобразования в QR-код
    :param logo: путь к логотипу
    """
    # url = pyqrcode.QRCode('http://www.eqxiu.com', error='H')
    url = pyqrcode.create(text, error='H')
    url.png('test.png', scale=20,
            # module_color=[250, 128, 0, 0],
            # background=[0xcf, 0xbf, 0xcf],
            quiet_zone=2)

    if logo:
        im = Image.open('test.png')
        width, height = im.size
        logo_size = 150
        im = im.convert("RGBA")
        logo = Image.open(logo)
        xmin = ymin = int((width / 2) - (logo_size / 2))
        xmax = ymax = int((width / 2) + (logo_size / 2))
        logo = logo.resize((xmax - xmin, ymax - ymin))
        im.paste(logo, (xmin, ymin, xmax, ymax), logo)
        im.save('test.png')


def qr_read_data():
    img = cv2.imread("test.png")
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    return data


if __name__ == '__main__':
    logo = 'manchester_united_PNG26.png'
    text = 'simple text'
    qr_generator(text, logo=logo)
    data = qr_read_data()
    print(data)
