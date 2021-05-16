from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import Questions, Options
from application.forms import AddQuestion

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 # test port, doesn't need to be open

    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            LIVESERVER_PORT=self.TEST_PORT,
            
            DEBUG=True,
            TESTING=True
        )

        return app

    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all() # create schema before we try to get the page
        newquest = Questions(question="Test")
        db.session.add(newquest)
        db.session.commit()

        self.driver.get(f'http://localhost:{self.TEST_PORT}/update-question/1')

    def tearDown(self):
        self.driver.quit()

        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/update-question/1')
        self.assertEqual(response.code, 200)

class TestAdd(TestBase):
    def submit_input(self, case): # custom method
        self.driver.find_element_by_xpath('/html/body/div/form/input[2]').send_keys(case)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_create(self):
         self.submit_input("updatedvalue")

         entry = Questions.query.filter_by(question="updatedvalue").first()
         self.assertNotEqual(entry, None) 

    def test_empty_validation(self):
        self.submit_input('')
        self.assertIn(url_for('update_q', qid=1), self.driver.current_url)
        entry = Questions.query.filter_by(id=1).first()
        self.assertNotEqual(entry.question, None)
