"""REST client handling, including HightouchStream base class."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class HightouchStream(RESTStream):
    """Hightouch stream class."""

    url_base = "https://api.hightouch.io/api/v2/rest"

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {
            "Authorization": f"Bearer {self.config['api_key']}"
        }
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers
