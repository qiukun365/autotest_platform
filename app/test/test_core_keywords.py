from app.core import keywords
import unittest

class TestKeywords(unittest.TestCase):
    def test_keyword_fill(self):
        paraCount, template, elementTemplate=keywords.keywords().getPara('悬浮点击')
        # print(paraCount, template, elementTemplate)
        self.assertEqual(paraCount,2)
        self.assertEqual(template,'driver.find_element_by_$para1("$para2").click()')

    def test_keyword_fill2(self):
        paraCount, template, elementTemplate=keywords.keywords().getPara('填写日期')
        # print(paraCount, template, elementTemplate)
        self.assertEqual(paraCount,4)

if __name__ == '__main__':
    unittest.main()