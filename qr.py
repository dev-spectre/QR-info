import cv2


def get_data(qr):
    img = cv2.imread(qr, 0)
    qr_detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = qr_detector.detectAndDecode(img)
    if vertices_array is None:
        return None
    if data == '':
        data = None
    return data
