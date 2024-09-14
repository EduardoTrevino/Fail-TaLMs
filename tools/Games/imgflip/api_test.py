import unittest
from api import get_memes, caption_image

class TestImgflipAPI(unittest.TestCase):

    def test_get_memes(self):
        result = get_memes()
        self.assertTrue('success' in result)
        self.assertTrue('data' in result)
        self.assertTrue('memes' in result['data'])

    def test_caption_image(self):
        # Using the Imgflip hubot account as in the documentation.
        username = "imgflip_hubot"
        password = "imgflip_hubot"
        template_id = "61579"
        result = caption_image(template_id=template_id, username=username, password=password, text0="Hello", text1="World")
        
        self.assertTrue('success' in result)
        if result['success']:
            self.assertTrue('data' in result)
            self.assertTrue('url' in result['data'])


if __name__ == '__main__':
    unittest.main()