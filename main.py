# import modules
import qrcode
from PIL import Image
import pyqrcode
# import png


def pic_in_qr_1():
    # taking image which user wants
    # in the QR code center
    Logo_link = 'manchester_united_PNG26.png'

    logo = Image.open(Logo_link)

    # taking base width
    basewidth = 50

    # adjust image size
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    # logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    # taking url or text
    url = '123456789'

    # adding URL or text to QRcode
    QRcode.add_data(url)

    # generating QR code
    QRcode.make()

    # taking color name from user
    QRcolor = 'Green'

    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
           (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    # save the QR code generated
    QRimg.save('gfg_QR.png')

    print('QR code generated!')


def pic_in_qr_2(text, logo=None):
    # url = pyqrcode.QRCode('http://www.eqxiu.com', error='H')
    url = pyqrcode.create(text, error='H', version=2)
    url.png('test.png', scale=20,
            module_color=[250, 128, 0, 0],
            background=[0xcf, 0xbf, 0xcf],
            quiet_zone=2)

    if logo:
        im = Image.open('test.png')
        width, height = im.size
        logo_size = 150
        im = im.convert("RGBA")
        logo = Image.open(logo)
        xmin = ymin = int((width / 2) - (logo_size / 2))
        xmax = ymax = int((width / 2) + (logo_size / 2))
        region = logo
        region = region.resize((xmax - xmin, ymax - ymin))
        im.paste(region, (xmin, ymin, xmax, ymax), region)
        im.save('test.png')


if __name__ == '__main__':
    logo = 'manchester_united_PNG26.png'
    text = '12494054524'
    pic_in_qr_2(text, logo=logo)
