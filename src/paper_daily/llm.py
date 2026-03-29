from __future__ import annotations

import json
import os
import re
import time
from typing import Any

import requests


class DeepSeekClient:
    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = "https://api.deepseek.com/chat/completions",
        timeout: int = 180,
    ) -> None:
        self.api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise ValueError("DEEPSEEK_API_KEY is not set.")
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
        )

    def chat_json(
        self,
        model: str,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int = 4000,
        temperature: float = 0.0,
        retries: int = 4,
    ) -> dict[str, Any]:
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "response_format": {"type": "json_object"},
            "temperature": temperature,
            "stream": False,
            "max_tokens": max_tokens,
        }
        backoff = 2.0
        for attempt in range(retries):
            response = self.session.post(
                self.base_url,
                data=json.dumps(payload).encode("utf-8"),
                timeout=self.timeout,
            )
            if response.status_code in {429, 500, 502, 503, 504}:
                if attempt == retries - 1:
                    response.raise_for_status()
                time.sleep(backoff)
                backoff *= 2
                continue
            response.raise_for_status()
            raw = response.json()
            content = raw["choices"][0]["message"]["content"]
            return _parse_json_object(content)
        raise RuntimeError("DeepSeek request failed after retries.")


def _parse_json_object(content: str) -> dict[str, Any]:
    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```[a-zA-Z0-9]*\s*", "", content)
        content = re.sub(r"\s*```$", "", content)
    return json.loads(content)
