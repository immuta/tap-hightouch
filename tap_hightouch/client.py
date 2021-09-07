"""REST client handling, including HightouchStream base class."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class HightouchStream(RESTStream):
    """Hightouch stream class."""

    url_base = "https://api.hightouch.io/api/v2/rest"

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=self.config.get("api_key")
        )
