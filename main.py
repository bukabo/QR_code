from PIL import Image
import pyqrcode
import cv2
from gradient import gradien_img


def qr_generator(text, logo=None):
    """
    Функция генерирует QR-код. \n
    Также на вход можно подать логотип в .png формате, который будет размещен в центре QR-кода. \n
    :param text: текст для преобразования в QR-код
    :param logo: путь к логотипу
    """
    url = pyqrcode.create(text, error='H', version=2)
    url.png('qr.png', scale=20,
            module_color=[50, 28, 150, 0],
            background=[255, 255, 255, 255],
            quiet_zone=2)
    im = Image.open('qr.png')
    im = im.convert("RGBA")
    im.save('qr.png')

    if logo:
        im = Image.open('qr.png')
        width, height = im.size
        logo_size = 150
        im = im.convert("RGBA")
        logo = Image.open(logo)
        xmin = ymin = int((width / 2) - (logo_size / 2))
        xmax = ymax = int((width / 2) + (logo_size / 2))
        logo = logo.resize((xmax - xmin, ymax - ymin))
        im.paste(logo, (xmin, ymin, xmax, ymax), logo)
        im.save('qr_logo.png')


def qr_read_data(qr_code_file):
    img = cv2.imread(qr_code_file)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    return data


if __name__ == '__main__':
    text = 'simple text'
    logo = 'manchester_united_PNG26.png'
    # logo = 'logo.png'
    qr_generator(text, logo=logo)
    gradien_img("qr_logo.png")
    data = qr_read_data("qr_logo_grad.png")
    print(data)
