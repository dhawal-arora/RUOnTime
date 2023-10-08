import datetime
import mysql.connector as sqltor
import data
import math


# Define dorms and buildings as you did in your code
dorms = {
        "Allen Hall": [40.524590, -74.461220],
        "Barr Hall": [40.5220529,-74.4562879],
        "BEST Hall": [40.5222929,-74.4571605],
        "Buell Hall": [40.5207678,-74.4585353],
        "Crosby Suites": [40.5207878,-74.4662869],
        "Johnson Apartments": [40.5274068,-74.4669565],
        "Judson Suites": [40.5256208,-74.4615301],
        "Mattia Hall": [40.5216124,-74.4568062],
        "Marvin Apartments": [40.5203235,-74.4569748],
        "McCormick Suites": [40.5248451,-74.4613865],
        "Metzger Hall": [40.5210489,-74.4576206],
        "Morrow Suites": [40.5253483,-74.4625428],
        "Nichols Apartments": [40.5276979,-74.469996],
        "Richardson Apartments": [40.5264011,-74.470713],
        "Silvers Apartments": [40.5194576,-74.4576115],
        "Thomas": [40.5251491,-74.4616842],
        "Winkler Suites": [40.5253784,-74.4632452],
        "Brett Hall": [40.5025475,-74.452111],
        "Campbell Hall": [40.505478,-74.4537233],
        "Clothier Hall": [40.5033283,-74.4510539],
        "Demarest Hall": [40.503514,-74.4529202],
        "Frelinghuysen Hall": [40.5039639,-74.4510017],
        "Hardenbergh Hall": [40.5047458,-74.4523494],
        "Hegeman Hall": [40.5034291,-74.4514878],
        "Honors College": [40.5025532,-74.4496017],
        "Leupp Hall": [40.5038343,-74.4522082],
        "Mettler Hall": [40.5028238,-74.4532562],
        "Pell Hall": [40.503875,-74.4519229],
        "Sojourner Truth Apartments": [40.4991954,-74.4507508],
        "Stonier Hall": [40.5031972,-74.453782],
        "Tinsley Hall": [40.5024545,-74.4526242],
        "Eastern Ave Apartments": [40.4968804,-74.4501969],
        "Wessels Hall": [40.5036314,-74.4523371],
        "Helyar House": [40.4718778,-74.4381751],
        "Henderson Apartments": [40.4811939,-74.4298617],
        "Lippincott Hall": [40.4815395,-74.4330567],
        "New Gibbons Hall": [40.4856565,-74.4340755],
        "Newell Apartments": [40.4775086,-74.4324266],
        "Nicholas Hall": [40.4810583,-74.4348346],
        "Perry Hall": [40.4769685,-74.4362269],
        "Starkey Apartments": [40.4760057,-74.432793],
        "Voorhees Hall": [40.4764703,-74.4360691],
        "Woodbury Bunting-Cobb Hall": [40.4809281,-74.4335898],
        "Lynton Towers North": [40.5231819,-74.4379687],
        "Lynton Towers South": [40.522974,-74.4387047],
        "Quad 1": [40.5203244,-74.4384908],
        "Quad 2": [40.5202988,-74.437845],
        "Quad 3": [40.5202988,-74.437845],

    }

buildings = {

        "(ARC) Allison Road Classroom": [40.5238717,-74.4676495],
        "(BME) Biomedical Engineering Building": [40.5244354,-74.4631845],
        "(BST) BEST West Residence Hall": [40.5222995,-74.4571924],
        "(CCB) Chemistry & Chemical Biology": [40.5245481,-74.4647658],
        "(CoRE) Computing Research & Education Building": [40.521315,-74.4639909],
        "(EN) Engineering Building": [40.5225221,-74.4636459],
        "(HLL) Hill Center": [40.5220967,-74.4652776],
        "(PH) Pharmacy Building (William Levin Hall)": [40.523526,-74.4702237],
        "(PHY) Physics Building": [40.522433,-74.4660233],
        "(RWH) Richard Weeks Hall of Engineering": [40.5245398,-74.4622151],
        "(SEC) Science & Engineering Resource Center (T. Alexander Pond)": [40.5227426,-74.4652637],
        "(WL) Wright Rieman Laboratories": [40.5238024,-74.4651848],
        "(BE) Beck Hall": [40.5228057,-74.4420143],
        "(LSH) Lucy Stone Hall": [40.5219613,-74.4374646],
        "(LSH-AUD) Lucy Stone Hall Auditorium": [40.5219613,-74.4374646],
        "(RC) Rutgers Cinema": [40.5253919,-74.4400542],
        "(TIL) Tillett Hall": [40.5218973,-74.43857],
        "(AB) Rutgers Academic Building": [40.5016988,-74.4506972],
        "(BH) Bishop House": [40.5030575,-74.4523535],
        "(CA) Campbell Hall": [40.505478,-74.4537233],
        "(CI) School of Communication and Information": [40.5053025,-74.4557983],
        "(ED) Graduate School of Education": [40.5013173,-74.4488688],
        "(FH) Frelinghuysen Hall": [40.5039639,-74.4510017],
        "(HC) Honors College": [40.5025532,-74.4496017],
        "(MI) Milledoler Hall": [40.5010299,-74.4496016],
        "(MU) Murray Hall": [40.5006293,-74.4491858],
        "(SC) Scott Hall": [40.4998392,-74.4500895],
        "(VD) Van Dyck Hall": [40.5006899,-74.4505175],
        "(VH) Voorhees Hall": [40.2158352,-74.5494572],
        "(ZAM) Zimmerli Art Museum": [40.4997573,-74.44842],
        "(ARH) Art History Hall": [40.486212,-74.4377133],
        "(BIO) Biological Sciences": [40.4878269,-74.4401368],
        "(BL) Blake Hall": [40.4819845,-74.4420774],
        "(CDL) Cook Douglass Lecture Hall": [40.4800552,-74.4387149],
        "(DAV) Davison Hall": [40.4842052,-74.440007],
        "(FNH) Institude for Food Nutrition & Health": [40.4795689,-74.437532],
        "(FOR) Foran Hall": [40.4805702,-74.4378852],
        "(FS) Food Science Building": [40.4792277,-74.4387391],
        "(HCK) Hickman Hall": [40.4847718,-74.4367396],
        "(HSB) Heldrich Science Building": [40.4868104,-74.4409848],
        "(LOR) Loree Classroom Building": [40.4828318,-74.4379258],
        "(KLG) Kathleen W Ludwing Global Village Learning Center": [40.4841546,-74.4415872],
        "(RAB) Ruth Adams Building": [40.4874218,-74.4399623],
        "(TH) Thompson Hall": [40.481481,-74.4423702],
        "(WAL) Waller Hall": [40.4832717,-74.4405034],
    }

# Fetch train and station data
trains = data.getTrain()
stations = data.getStaton()

# Create a dictionary to store the simplified station information
simpleStation = {}
for key, val in stations.items():
    name = val.get('stationName')
    lat = val.get("lat")
    lon = val.get("lon")
    simpleStation[name] = [lat, lon]

# Create the simpleBus dictionary
simpleBus = {}

# Iterate through the train data to populate simpleBus
for train_id, train_info in trains.items():
    predictions = train_info.get("predictions")
    for prediction in predictions:
        station_name = prediction.get("stationName")
        eta = prediction.get("actualETA") / 1000
        date_time_eta = datetime.datetime.utcfromtimestamp(eta)
        load = train_info.get("extra").get("load")
        cap = train_info.get("extra").get("cap")
        percentage = (load // cap) * 100

        if station_name not in simpleBus:
            simpleBus[station_name] = []

        simpleBus[station_name].append({"ETA": date_time_eta, "Load Percentage": percentage})

# Define a function to calculate the closest bus stop to a location
def find_closest_bus_stop(location):
    min_distance = float('inf')
    closest_stop = None

    for stop, coordinates in simpleStation.items():
        distance = math.sqrt((location[0] - coordinates[0]) ** 2 + (location[1] - coordinates[1]) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_stop = stop

    return closest_stop


# # Define a function to check if you'll be late for classes
# def check_class_timings(class_id, day):
#     connector=sqltor.connect(host="na05-sql.pebblehost.com",user="customer_586593_ruontime", passwd="~8DRfiI~Y5e~V!Hv-ZND",database="customer_586593_ruontime")
#     cur = connector.cursor()
#     result = {}
#     cur.execute("SELECT dorm FROM housing WHERE id=(%s)", (class_id,))
#     dorm_result = cur.fetchone()
#
#     if dorm_result is not None:
#         dorm = dorm_result[0]
#         schedule = {dorm: dorms[dorm]}
#     else:
#         result["error"] = "Dorm information not found for class ID"
#         return result
#
#     cur.execute("SELECT location, starttime, endtime FROM classes WHERE id=(%s) AND day=(%s) ORDER BY id", (class_id, day))
#     class_results = cur.fetchall()
#
#     class_info_list = []
#
#     for class_info in class_results:
#         location = class_info[0]
#         start_time = class_info[1]
#         end_time = class_info[2]
#         
#         closest_bus_stop = find_closest_bus_stop(buildings[location])
#         
#         class_info_dict = {
#             "Location": location,
#             "Day": day,
#             "Start Time": start_time,
#             "End Time": end_time,
#             "Closest Bus Stop": closest_bus_stop
#         }
#
#         if closest_bus_stop is not None:
#             # Now, you can check the bus timings for the closest bus stop from simpleBus
#             if closest_bus_stop in simpleBus:
#                 bus_timings = simpleBus[closest_bus_stop]
#                 bus_info_list = []
#
#                 for i, timing in enumerate(bus_timings):
#                     bus_info = {
#                         "Bus Number": i + 1,
#                         "ETA": timing['ETA'].strftime("%Y-%m-%d %H:%M:%S"),
#                         "Load Percentage": timing['Load Percentage']
#                     }
#                     bus_info_list.append(bus_info)
#
#                 class_info_dict["Bus Timings"] = bus_info_list
#             else:
#                 class_info_dict["Bus Timings"] = "Bus timings not available for the closest bus stop."
#
#         class_info_list.append(class_info_dict)
#
#     result["classes"] = class_info_list
#     connector.close()
#     return result

# Define a function to calculate estimated arrival time
def calculate_estimated_arrival(bus_timings, current_time):
    for timing in bus_timings:
        bus_eta = timing['ETA']
        if bus_eta > current_time:
            return bus_eta
    return None

# Define a function to check if you'll be late for classes
def check_class_timings(class_id, day):
    connector = sqltor.connect(host="na05-sql.pebblehost.com", user="customer_586593_ruontime", passwd="~8DRfiI~Y5e~V!Hv-ZND", database="customer_586593_ruontime")
    cur = connector.cursor()
    result = {}
    
    # Fetch dorm information
    cur.execute("SELECT dorm FROM housing WHERE id=(%s)", (class_id,))
    dorm_result = cur.fetchone()

    if dorm_result is not None:
        dorm = dorm_result[0]
        schedule = {dorm: dorms[dorm]}
    else:
        result["error"] = "Dorm information not found for class ID"
        return result

    # Fetch class information
    cur.execute("SELECT location, starttime, endtime FROM classes WHERE id=(%s) AND day=(%s) ORDER BY id", (class_id, day))
    class_results = cur.fetchall()

    class_info_list = []

    for class_info in class_results:
        location = class_info[0]
        start_time = class_info[1]
        end_time = class_info[2]

        closest_bus_stop = find_closest_bus_stop(buildings[location])

        class_info_dict = {
            "Location": location,
            "Day": day,
            "Start Time": start_time,
            "End Time": end_time,
            "Closest Bus Stop": closest_bus_stop
        }

        if closest_bus_stop is not None:
            # Now, you can check the bus timings for the closest bus stop from simpleBus
            if closest_bus_stop in simpleBus:
                bus_timings = simpleBus[closest_bus_stop]
                bus_info_list = []

                # Calculate estimated arrival time
                current_time = datetime.datetime.now()
                estimated_arrival = calculate_estimated_arrival(bus_timings, current_time)

                if estimated_arrival is not None:
                    class_info_dict["Estimated Arrival"] = estimated_arrival.strftime("%Y-%m-%d %H:%M:%S")
                    if estimated_arrival <= start_time:
                        class_info_dict["Status"] = "On Time"
                    else:
                        class_info_dict["Status"] = "Late"
                else:
                    class_info_dict["Status"] = "No available bus before class"

            else:
                class_info_dict["Bus Timings"] = "Bus timings not available for the closest bus stop."
                class_info_dict["Status"] = "N/A"

        class_info_list.append(class_info_dict)

    result["classes"] = class_info_list
    connector.close()
    return result

# Call the check_class_timings function for a specific class and day
class_id = 102
day = "Thursday"
result = check_class_timings(class_id, day) # For testing, you can print the result, but you can return it to an external user as needed
print(result)

# Close the MySQL connection

