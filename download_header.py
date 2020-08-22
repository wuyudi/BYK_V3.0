from io import BytesIO

import requests
from PIL import Image, ImageStat

# good_color = {}
# export_dir = 'D:/'


class download_header:
    def __init__(self, good_color, export_dir):
        self.good_color = good_color
        self.export_dir = export_dir

    def download_header(self, uid, face_link):
        image = Image.open(BytesIO(requests.get(face_link).content))
        width = image.size[0]
        height = image.size[1]
        if min(width, height) > 240:
            image = image.resize((240, round(height * 240 / width)))
        image.save(self.export_dir + str(uid) + '.png')
        if uid in self.good_color:
            color = self.good_color[uid]
        else:
            mean = ImageStat.Stat(image).mean
            if len(mean) == 1:
                darker = [round(0.9 * mean[0]) for i in mean]
            else:
                darker = [round(0.9 * i) for i in mean]
            color = '0x{:02X}{:02X}{:02X}'.format(*darker)
        return color


if __name__ == "__main__":
    uid = 7275647
    face_link = 'http://i2.hdslb.com/bfs/face/ce1595b2d2bb472bb1f5437e49cb6a2415a44147.webp'
    download_header(uid, face_link)
