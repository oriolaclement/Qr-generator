import pyqrcode
def qr_code():
    s = 'This is power python class'
    d = pyqrcode.create(s)
    d.png('My_ing.png', scale=8)
    print('Code executed properly')

if __name__ == '__main__':
    qr_code()