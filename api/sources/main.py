import os
import random

from json import load
from typing import Optional

from faker import Faker
from requests import Response, Session


class AutomatedBot:
    _faker = Faker()

    def __init__(self, path: str) -> None:
        with open(path) as configuration_file:
            self.__configuration = load(configuration_file)

        self._session = Session()
        self.__token: Optional[str] = None

    @property
    def base_url(self) -> str:
        return self.__configuration.get("BASE_URL", "http://localhost:8000/api/v1")

    @property
    def headers(self) -> dict:
        if not self.__token:
            return {}

        return {"Authorization": f"Bearer {self.__token}"}

    def __post(self, endpoint: str, payload: Optional[dict] = None) -> Response:
        response = self._session.post(f"{self.base_url}{endpoint}", json=payload, headers=self.headers)
        response.raise_for_status()
        return response

    def __authenticate(self, profile: dict) -> None:
        response = self.__post(
            "/accounts/token/",
            {
                "email": profile["email"],
                "password": profile["password"],
            },
        )
        self.__token = response.json()["access"]

    def __register_random_user(self) -> dict:
        payload = {
            "email": self._faker.email(),
            "first_name": self._faker.first_name(),
            "last_name": self._faker.last_name(),
            "password": self._faker.password(),
        }
        self.__post("/accounts/registration/", payload)
        return payload

    def __create_random_post(self) -> Response:
        payload = {
            "title": self._faker.sentence(),
            "content": self._faker.text(),
        }

        return self.__post("/posts/", payload)

    def _create_posts(self) -> list[int]:
        posts_ids = []
        for _ in range(random.randint(1, self.__configuration.get("MAX_POSTS_PER_USER", 1))):  # noqa: S311
            response = self.__create_random_post()
            posts_ids.append(response.json()["pk"])

        return posts_ids

    def __like_post(self, post_id: int) -> None:
        self.__post(f"/posts/{post_id}/like/")

    def _like_posts(self, profile: dict, posts_ids: list[int]):
        user_likes = random.randint(1, self.__configuration.get("MAX_LIKES_PER_USER", 1))  # noqa: S311
        self.__authenticate(profile)
        for post_id in random.sample(posts_ids, user_likes):
            self.__like_post(post_id)

    def run(self) -> None:
        users = []
        posts_ids = []

        for _ in range(self.__configuration.get("USERS_COUNT", 0)):
            users.append(self.__register_random_user())
            self.__authenticate(users[-1])
            posts_ids.extend(self._create_posts())

        for user in users:
            self._like_posts(user, posts_ids)


if __name__ == "__main__":
    CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")
    bot = AutomatedBot(CONFIG_PATH)
    bot.run()
