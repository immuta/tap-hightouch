"""Hightouch tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_hightouch.streams import (
    SyncStream,
)

STREAM_TYPES = [
    SyncStream,
]


class TapHightouch(Tap):
    """Hightouch tap class."""
    name = "tap-hightouch"

    config_jsonschema = th.PropertiesList(
        th.Property("api_key", th.StringType, required=True),
        th.Property("sync_id_list", th.ArrayType(th.IntegerType), required=True)
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
