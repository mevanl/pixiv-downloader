from unittest import TestCase
from modules.artwork import Artwork
from dotenv import load_dotenv
import os
from pixivpy3 import *

class TestArtwork(TestCase):
    def setUp(self) -> None:
        if load_dotenv():
            self.api = AppPixivAPI()
            REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
            self.api.auth(refresh_token=REFRESH_TOKEN)

            self.id = 110295094
            self.raw_json=self.api.illust_detail(self.id)

            self.a_obj = Artwork(self.raw_json['illust'], self.api.ugoira_metadata(self.id))

    def test_illust(self):
        self.assertEqual(self.raw_json['illust'] ,self.a_obj.illust)
        self.assertNotEqual(self.raw_json, self.a_obj.illust)

    def test_ugoira_metadata(self):
        error = self.api.ugoira_metadata(self.id)
        self.assertEqual(error, self.a_obj.ugoira_metadata)

    def test_id(self):
        self.assertEqual(110295094, self.a_obj.id)

    def test_type(self):
        self.assertEqual('illust', self.a_obj.type)
    
    def test_seriesID(self):
        self.assertEqual("No series", self.a_obj.seriesID)

    def test_seriesTitle(self):
        self.assertEqual("No series", self.a_obj.seriesTitle)

    def test_title(self):
        self.assertEqual("C102新刊『緑子がお供します』サンプル", self.a_obj.title)

    def test_pagecount(self):
        self.assertEqual(6, self.a_obj.page_count)
    
    def test_userID(self):
        self.assertEqual(10920404, self.a_obj.userID)

    def test_username(self):
        self.assertEqual("PINTA＠二日目チ-40a", self.a_obj.username)

    def test_filetype(self):
        self.assertEqual(".jpg", self.a_obj.filetype())

    def test_download_urls(self):
        url_list = ["https://i.pximg.net/img-original/img/2023/07/28/15/11/32/110295094_p0.jpg", 
                    "https://i.pximg.net/img-original/img/2023/07/28/15/11/32/110295094_p1.jpg", 
                    "https://i.pximg.net/img-original/img/2023/07/28/15/11/32/110295094_p2.jpg",
                    "https://i.pximg.net/img-original/img/2023/07/28/15/11/32/110295094_p3.jpg",
                    "https://i.pximg.net/img-original/img/2023/07/28/15/11/32/110295094_p4.jpg",
                    "https://i.pximg.net/img-original/img/2023/07/28/15/11/32/110295094_p5.jpg"]
        self.assertEqual(url_list, self.a_obj.download_urls())

    def test_remove_special_characters(self):
        text="?HELLO|"
        self.assertEqual("HELLO", self.a_obj.remove_specialChar(text))

    def test_single_page(self):
        self.raw_json = self.api.illust_detail(108532590)
        self.a_obj = Artwork(self.raw_json['illust'])

        self.assertEqual(["https://i.pximg.net/img-original/img/2023/05/29/01/27/02/108532590_p0.png"], self.a_obj.download_urls())

    def test_ugoira(self):
        self.raw_json = self.api.illust_detail(52592934)
        self.a_obj = Artwork(self.raw_json['illust'], self.api.ugoira_metadata(52592934))

        self.assertEqual(["https://i.pximg.net/img-zip-ugoira/img/2015/09/19/00/26/19/52592934_ugoira600x600.zip"], self.a_obj.download_urls())
        self.assertEqual(".gif", self.a_obj.filetype())

    def test_manga_series(self):
        self.raw_json = self.api.illust_detail(78386392)
        self.a_obj = Artwork(self.raw_json['illust'], self.api.ugoira_metadata(78386392))

        self.assertEqual('manga', self.a_obj.type)