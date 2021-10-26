import requests
from datetime import datetime, timezone, timedelta

class ingest:
    def __init__(self):
        self.base_url = ''

    def test(datasource, namespace):
        print("Ingest Model Test function: ", datasource, ", ", namespace)
