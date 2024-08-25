import unittest
from api import generate_chart

class TestQuickChartAPI(unittest.TestCase):
    
    def test_generate_chart_get(self):
        chart_config = "{type:'bar',data:{labels:[2012,2013,2014,2015,2016],datasets:[{label:'Users',data:[120,60,50,180,120]}]}}"
        response = generate_chart(chart_config)
        
        self.assertIsInstance(response, bytes)  # Should return image data for URL encoding by default.

    def test_generate_chart_post(self):
        chart_config = "{type:'bar',data:{labels:[2012,2013,2014,2015,2016],datasets:[{label:'Users',data:[120,60,50,180,120]}]}}"
        response = generate_chart(chart_config, method='POST')
        
        self.assertIsInstance(response, bytes)  # Should return image data for URL encoding by default.

    def test_generate_chart_with_options(self):
        chart_config = "{type:'line',data:{labels:[2012,2013,2014,2015,2016],datasets:[{label:'Sales',data:[30,20,50,60,90]}]}}"
        response = generate_chart(chart_config, width=800, height=600, device_pixel_ratio=1, encoding='base64', method='POST')
        
        self.assertIsInstance(response, bytes)  # Base64 encoded data should be returned as bytes.

    def test_generate_chart_invalid_method(self):
        chart_config = "{type:'pie',data:{labels:['Red','Blue','Yellow'],datasets:[{data:[10,20,30]}]}}"
        response = generate_chart(chart_config, method='UPDATE')
        
        self.assertDictEqual(response, {"error": "Invalid HTTP method: UPDATE"})  # Invalid method should return an error.

if __name__ == '__main__':
    unittest.main()