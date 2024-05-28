import unittest
import warnings
from api import app


class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_index_page(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "<p>HELLO WORLD!</p>")

    def test_get_branches(self):
        response = self.app.get("/branches")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Main Branch" in response.data.decode())

    def test_get_branch_by_id(self):
        response = self.app.get("/branches/2")
        self.assertEqual(response.status_code, 200) 
        self.assertTrue("Downtown Branch" in response.data.decode())

    def test_create_branch(self):
        data = {
            "name": "New Branch",
            "location": "New Location",
            # Add other necessary data for creating a branch
        }
        response = self.app.post("/branches", json=data)
        self.assertEqual(response.status_code, 201)  # Assuming 201 is used for successful creation

        # Optionally, you can test if the created branch is retrievable
        # by querying the API with its ID and checking if the response contains expected data.

    def test_update_branch(self):
        branch_id = 2  # Assuming you want to update the branch with ID 2
        data = {
            "name": "Updated Name",
            # Add other fields you want to update
        }
        response = self.app.put(f"/branches/{branch_id}", json=data)
        self.assertEqual(response.status_code, 200)  # Assuming 200 is used for successful update

        # Optionally, you can retrieve the updated branch and check if the changes are reflected.

    def test_delete_branch(self):
        branch_id = 3  # Assuming you want to delete the branch with ID 3
        response = self.app.delete(f"/branches/{branch_id}")
        self.assertEqual(response.status_code, 204)  # Assuming 204 is used for successful deletion

        # Optionally, you can try to retrieve the deleted branch and expect a 404 or similar error.


if __name__ == "__main__":
    unittest.main()
