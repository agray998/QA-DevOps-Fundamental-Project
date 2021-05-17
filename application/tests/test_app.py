from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Questions, Options

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test question
        sample1 = Questions(question="Testq")

        # save question to database
        db.session.add(sample1)
        db.session.commit()

        sampleopt = Options(optletter = 'A', option = "This is a test option", status = 'correct', question_id = sample1.id)
        db.session.add(sampleopt)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

# Write a test class for testing that the questions page loads but we are not able to run a get request for delete and update routes.
class TestViews(TestBase):
    def test_qs_get(self):
        response = self.client.get(url_for('questions'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Testq', response.data)

class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

# Test sending a GET request to the add question page
class TestViewAddQ(TestBase):
    def test_addq_get(self):
        response = self.client.get(url_for('add_q'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add a New Question', response.data)

# Test adding a question
class TestAddq(TestBase):
    def test_add_q(self):
        response = self.client.post(
            url_for('add_q'),
            data = dict(q_name="Newquest"),
            follow_redirects=True
        )
        self.assertIn(b'Add Options',response.data)

# Test sending a GET request to the add options page
class TestViewAddO(TestBase):
    def test_addo_get(self):
        response = self.client.get(url_for('add_o', qid=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Options', response.data)

# Test adding an option
class TestAddo(TestBase):
    def test_add_o(self):
        response = self.client.post(
            url_for('add_o', qid=1),
            data = dict(o_letter='A', o_option="newoption", o_status='incorrect'),
            follow_redirects=True
        )
        self.assertIn(b'Add Options',response.data)

# Test updating a question
class TestUpq(TestBase):
    def test_up_q(self):
        response = self.client.post(
            url_for('update_q', qid=1),
            data = dict(q_name="Updated question"),
            follow_redirects=True
        )
        self.assertIn(b'Home',response.data)

# Test updating an option
class TestUpo(TestBase):
    def test_up_o(self):
        response = self.client.post(
            url_for('update_o', oid=1),
            data = dict(o_letter='A', o_option="updatedoption", o_status='correct'),
            follow_redirects=True
        )
        self.assertIn(b'updatedoption',response.data)

# Test Deleting an option
class TestDelo(TestBase):
    def test_del_o(self):
        response = self.client.get(url_for('delete_o', oid = 1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Testq', response.data)
        self.assertNotIn(b'This is a test option', response.data)

# Test Deleting a question
class TestDelq(TestBase):
    def test_del_q(self):
        response = self.client.get(url_for('delete_q', qid = 1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Testq', response.data)

# Test taking quiz
class Testquiz(TestBase):
    def test_take_quiz(self):
        response = self.client.post(
            url_for('answer_q', qid=1),
            data = dict(sel_opt='A'),
            follow_redirects=True
        )
        self.assertIn(b'You scored 1', response.data)

class Testquiz2(TestBase):
    def test_bad_opt(self):
        response = self.client.post(
            url_for('answer_q', qid=1),
            data = dict(sel_opt='B'),
            follow_redirects=True
        )
        self.assertIn(b'Please select a valid option', response.data)
