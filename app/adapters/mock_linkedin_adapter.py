class MockLinkedInPublisher:
    platform = "mock_linkedin"

    def publish(self, *, variant_id: str, content: str, metadata: dict) -> dict:
        return {
            "platform": "mock_linkedin",
            "success": True,
            "post_url": f"https://mocklinkedin.local/posts/{variant_id}",
            "external_id": f"linkedin-{variant_id}",
        }
