# Install package 'locust'
# Run 'locustfile.py'
# Terminal to type 'locust'
# Browse points to 'http://localhost:8089/'

from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

    def on_start(self):
        response = self.client.post("/login/index.php", {"username":"input_username", "password":"input_password"})
        # print("Response status code:", response.status_code)
        # print("Response text:", response.text)

    @task
    def test1(self):
        self.client.get("/course/view.php?id=3016")

    @task
    def test2(self):
        self.client.get("/mod/resource/view.php?id=103051")

    # @task(3)
    # def view_item(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")