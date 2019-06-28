import os
import subprocess
import time
from utils.splunk_search_util import get_session_key, preprocess_search, run_search, get_search_response


def test_plugin_devnull(eventgen_test_helper):
    """Test output plugin devnull"""
    events = eventgen_test_helper("eventgen_plugin_devnull.conf").get_events()
    # assert the events size is 0
    assert len(events) == 0


def test_plugin_file(eventgen_test_helper):
    """Test output plugin file"""
    events = eventgen_test_helper("eventgen_plugin_file.conf").get_events()
    # assert the events size is 12 when end = 1
    assert len(events) == 12


def test_plugin_httpevent(eventgen_test_helper):
    """Test output plugin httpevent"""
    eventgen_test_helper("eventgen_plugin_httpevent.conf").get_events()

    session_key = get_session_key()
    search_job_id = run_search(session_key, preprocess_search('index=main sourcetype=httpevent'))
    events = get_search_response(session_key, search_job_id)
    assert len(events) == 12
