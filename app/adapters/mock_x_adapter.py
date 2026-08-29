class MockXPublisher:
    platform = "mock_x"

    def publish(self, *, variant_id: str, content: str, metadata: dict) -> dict:
        return {
            "platform": "mock_x",
            "success": True,
            "post_url": f"https://mockx.local/posts/{variant_id}",
            "external_id": f"mockx-{variant_id}",
        }
