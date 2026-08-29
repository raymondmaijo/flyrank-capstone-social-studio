from abc import ABC, abstractmethod


class SocialPublisher(ABC):
    @property
    @abstractmethod
    def platform(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def publish(self, *, variant_id: str, content: str, metadata: dict) -> dict:
        raise NotImplementedError
