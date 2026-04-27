import datetime
import math

import data
import database
from locations import DORMS, BUILDINGS


def _station_map(stations: dict) -> dict:
    return {
        v["stationName"]: [v["lat"], v["lon"]]
        for v in stations.values()
    }


def _bus_map(trains: dict) -> dict:
    bus_map: dict[str, list] = {}
    for train_info in trains.values():
        name = train_info.get("line")
        load = train_info.get("extra", {}).get("load", 0)
        cap = train_info.get("extra", {}).get("cap", 1)
        pct = math.ceil((load / cap) * 100)
        for pred in train_info.get("predictions", []):
            stop = pred.get("stationName")
            eta = datetime.datetime.utcfromtimestamp(pred["actualETA"] / 1000)
            bus_map.setdefault(stop, []).append({
                "Bus Number": name,
                "ETA": eta,
                "Load Percentage": pct,
            })
    return bus_map


def _closest_stop(location: list, station_map: dict) -> str | None:
    return min(
        station_map,
        key=lambda s: (location[0] - station_map[s][0]) ** 2
                    + (location[1] - station_map[s][1]) ** 2,
        default=None,
    )


def _next_arriving(bus_timings: list, after: datetime.datetime) -> datetime.datetime | None:
    return next((t["ETA"] for t in bus_timings if t["ETA"] > after), None)


def check_class_timings(user_id: int, day: str) -> dict:
    trains = data.get_trains()
    stations = data.get_stations()
    smap = _station_map(stations)
    bmap = _bus_map(trains)

    conn = database.get_connection()
    cur = conn.cursor()

    cur.execute("SELECT dorm FROM housing WHERE id = %s", (user_id,))
    dorm_row = cur.fetchone()
    if dorm_row is None:
        return {"error": "No housing information found."}
    if dorm_row[0] not in DORMS:
        return {"error": f"Unknown dorm: {dorm_row[0]}"}

    cur.execute(
        "SELECT location, classname, starttime, endtime "
        "FROM classes WHERE id = %s AND day = %s ORDER BY starttime",
        (user_id, day),
    )
    rows = cur.fetchall()

    now = datetime.datetime.now()
    classes = []

    for location, classname, start_time, end_time in rows:
        if location not in BUILDINGS:
            continue
        stop = _closest_stop(BUILDINGS[location], smap)
        entry = {
            "Location": location,
            "Class Name": classname,
            "Day": day,
            "Start Time": start_time,
            "End Time": end_time,
            "Closest Bus Stop": stop,
        }
        if stop and stop in bmap:
            entry["Bus Timings"] = bmap[stop]
            arriving = _next_arriving(bmap[stop], now)
            if arriving:
                entry["Estimated Arrival"] = arriving.strftime("%H:%M")
        classes.append(entry)

    return {"classes": classes}
