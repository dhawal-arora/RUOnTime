import requests

_API_URL = "https://store.piemadd.com/passio_go/rutgers"


def get_trains() -> dict:
    raw = requests.get(_API_URL).json()
    trains = dict(raw.get("trains", {}))
    for train in trains.values():
        for field in ("heading", "lineCode", "lineColor", "lineTextColor"):
            train.pop(field, None)
        for prediction in train.get("predictions", []):
            prediction.pop("noETA", None)
        train.get("extra", {}).pop("info", None)
    return trains


def get_stations() -> dict:
    raw = requests.get(_API_URL).json()
    return dict(raw.get("stations", {}))
