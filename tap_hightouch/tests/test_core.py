"""Tests standard tap features using the built-in SDK tests library."""

import os

from singer_sdk.testing import get_standard_tap_tests

from tap_hightouch.tap import TapHightouch

SAMPLE_CONFIG = {
    "api_key": os.environ["TAP_HIGHTOUCH_API_KEY"],
    "sync_id_list": [12345]
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapHightouch,
        config=SAMPLE_CONFIG
    )
    for test in tests:
        test()
