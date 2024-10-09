# You may need to install the following libraries:
# * google-auth
# * requests

import json
from typing import Any

import google.auth
import google.auth.credentials
import google.auth.transport.requests


class Chatbot:
    def __init__(
            self,
            credentials: google.auth.credentials.Credentials,
            project: str,
            region: str,
        ):
        self._url = (
            f"https://{region}-aiplatform.googleapis.com"
            f"/v1/projects/{project}/locations/{region}"
            "/publishers/google/models/gemini-pro:streamGenerateContent"
        )
        self._headers = {
            "Content-Type": "application/json; charset=utf-8",
        }
        self._session = google.auth.transport.requests.AuthorizedSession(
            credentials,
        )

    def submit(self, request: dict[str, Any]) -> None:
        response = self._session.request(
            "POST", self._url, headers=self._headers, json=request,
        )
        if response.status_code != 200:
            raise RuntimeError(f"{response.status_code}: {response.json()}")
        return response.json()


def main():
    credentials, project = google.auth.default()
    region = "asia-northeast1"
    chatbot = Chatbot(credentials, project, region)

    request = {
        "contents": {
            "role": "user",
            "parts": {
                "text": "Give me a recipe for banana bread.",
            }
        },
        "safety_settings": {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_LOW_AND_ABOVE",
        },
        "generation_config": {
            "temperature": 0.2,
            "topP": 0.8,
            "topK": 40,
            "maxOutputTokens": 200,
            "stopSequences": [".", "?", "!"],
        }
    }

    print(json.dumps(chatbot.submit(request), indent=2))


if __name__ == "__main__":
    main()
