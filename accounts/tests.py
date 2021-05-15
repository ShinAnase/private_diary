from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver

class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='C:/Users/hfuis/venv_private_diary/chromedriver_win32')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

        # ログイン
        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys('<ユーザー登録済みのメールアドレス>')
        passward_input = self.selenium.find_element_by_name("password")
        username_input.send_keys('<ログインパスワード>')
        self.selenium.find_element_by_class_name('btn').click()

        #ページタイトルの検証
        self.assertEquals('日記一覧|Private Diary', self.selenium.title)
