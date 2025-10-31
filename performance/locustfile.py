from locust import HttpUser, task, between
class CheckoutUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://api.demoblaze.com"
    @task
    def flow(self):
        # Add to cart using the SAME static id every time
        self.client.post("/addtocart", json={
            "id": "f91886cd-b628-3779-653b-41d0f8c2e62f",
            "cookie": "bWlsYW5hXzEyMzE3NjI0NTM=",
            "prod_id": 5,
            "flag": True
        }, name="/addtocart")
        # Checkout
        self.client.post("/deletecart", json={"cookie": "milana_123"}, name="/deletecart")
