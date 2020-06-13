import scrapy
from datetime import date
import pytesseract
import logging
try:
    from PIL import Image
except ImportError:
    import Image

class ProjectEulerSpider(scrapy.Spider):
    name = "euler"

    def start_requests(self):
        urls = [
            'https://projecteuler.net/profile/dark_shade.png',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        solved = self.getSolvedProjectEuler()
        yield {
            'solved': solved,
            'total': 700,
            'date': str(date.today())
        }

    def getSolvedProjectEuler(self, image_path):
        """Gets the number of questions solved by the user in Project Euler.
        It takes the image as input and extracts the data from the image.
        """

        # If you don't have tesseract executable in your PATH, include the following:
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

        data_string = ""

        try:
            data_string = pytesseract.image_to_string(Image.open('C:\\Users\\Sankul\\repos\\compcode.sankulrawat.github.io\\notebooks\\data\\project_euler_dark_shade.png'), timeout=2)
        except:
            logging.error("unable to convert image to string")
            return -1

        return int(data_string.split()[-1])