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

# Test adding a question
class TestAddq(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('add_q'),
            data = dict(q_name="Newquest"),
            follow_redirects=True
        )
        self.assertIn(b'Add Options',response.data)
