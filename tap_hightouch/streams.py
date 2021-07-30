"""Stream type classes for tap-hightouch."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hightouch.client import HightouchStream


class SyncStream(HightouchStream):
    """Define custom stream."""
    name = "sync"
    path = "/sync/21265"
    primary_keys = ["id"]

    @property
    def sync_id_list(self):
        return self.config.get("sync_id_list", [])

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

    def get_next_page_token(self, response, previous_token):
        if previous_token is None:
            previous_token = self.sync_id_list[0]
        try:
            current_index = self.sync_id_list.index(previous_token)
            next_page_token = self.sync_id_list[current_index + 1]
            return next_page_token
        except IndexError as e:
            self.logger.info("Reached end of sync list.")
            return None
