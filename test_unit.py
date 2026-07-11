import unittest
from flasktut import app, db, Project 

class FlaskAppUnitTest(unittest.TestCase):

    def setUp(self):
        """Executed before each test: Set up the test client."""
        app.config['TESTING'] = True
        self.client = app.test_client()
        
        with app.app_context():
            db.create_all()

    def tearDown(self):
        """Executed after each test: Clean up ONLY the test data so site.db stays intact."""
        with app.app_context():
            db.session.remove()
            Project.query.filter_by(name="Test Automation").delete()
            db.session.commit()

    def test_home_route(self):
        """Verify that the home page loads successfully (HTTP 200)."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_project_to_database(self):
        """Test database interaction by directly adding a Project model unit."""
        with app.app_context():
            project = Project(
                name="Test Automation", 
                description="Testing Flask apps",
                url="https://github.com"
            )
            db.session.add(project)
            db.session.commit()
            
            saved_project = Project.query.filter_by(name="Test Automation").first()
            self.assertIsNotNone(saved_project)
            self.assertEqual(saved_project.name, "Test Automation")

if __name__ == '__main__':
    unittest.main()