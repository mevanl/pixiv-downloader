from unittest import TestCase
from modules.novel import Novel
from dotenv import load_dotenv
from pixivpy3 import *
import os 

class TestNovel(TestCase):
    def setUp(self) -> None:
       self.api = AppPixivAPI()
       REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
       self.api.auth(refresh_token=REFRESH_TOKEN)

       self.id = 14497768
       self.raw_json = self.api.novel_detail(self.id)

       self.n_obj = Novel(self.raw_json['novel'], self.api.novel_text(self.id)['novel_text'])

    def test_remove_special_characters(self):
        text="?HELLO|"
        self.assertEqual("HELLO", self.n_obj.remove_specialChar(text))

    def test_novel(self):
        self.assertEqual(self.raw_json['novel'], self.n_obj.novel)
    
    def test_id(self):
        self.assertEqual(self.id, self.n_obj.id)
    
    def test_title(self):
        self.assertEqual("私にだけ見える選択肢が人生強制終了しかないんだけど　01", self.n_obj.title)

    def test_text(self):
        self.assertEqual(self.api.novel_text(self.id)['novel_text'], self.n_obj.text)

    def test_text_length(self):
        self.assertEqual(1654, self.n_obj.text_length)
    
    def test_series(self):
        self.assertEqual(1481801, self.n_obj.seriesID)
        self.assertEqual("選択肢が人生強制終了を出してくる【完結】", self.n_obj.seriesTitle)
    
    def test_author(self):
        self.assertEqual(53012298, self.n_obj.userID)
        self.assertEqual("高福あさひ", self.n_obj.username)

    def test_no_series(self):
        self.raw_json = self.api.novel_detail(20086410)
        self.n_obj = Novel(self.raw_json['novel'], self.api.novel_text(20086410)['novel_text'])
        self.assertEqual("No series", self.n_obj.seriesID)
        self.assertEqual("No series", self.n_obj.seriesTitle)