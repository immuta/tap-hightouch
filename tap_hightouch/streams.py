"""Stream type classes for tap-hightouch."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hightouch.client import HightouchStream


class SyncStream(HightouchStream):
    """Define custom stream."""
    name = "sync"
    path = "/sync/{sync_id}"
    primary_keys = ["id"]

    @property
    def partitions(self) -> Optional[List[dict]]:
        return [{"sync_id": s} for s in self.config.get("sync_id_list", [])]

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("model_id", th.IntegerType),
        th.Property("destination_id", th.IntegerType),
        th.Property("sync", th.ObjectType(
            th.Property("sync_id", th.IntegerType),
            th.Property("sync_paused", th.BooleanType),
            th.Property("sync_created_at", th.DateTimeType),
            th.Property("sync_created_by", th.IntegerType),
            th.Property("sync_schedule", th.StringType),
            th.Property("sync_status", th.StringType),
            th.Property("last_run_at", th.DateTimeType),
        )),
        th.Property("last_sync_run", th.ObjectType(
            th.Property("sync_run_id", th.StringType),
            th.Property("sync_run_created_at", th.StringType),
            th.Property("sync_run_finished_at", th.StringType),
            th.Property("sync_run_error", th.StringType),
        ))
    ).to_dict()
