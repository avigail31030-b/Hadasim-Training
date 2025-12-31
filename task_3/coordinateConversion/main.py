def dd_to_dms(value, coord_type):

    direction = ""

    if coord_type == "lat":
        direction = "N" if value >= 0 else "S"

    elif coord_type == "lon":
        direction = "E" if value >= 0 else "W"

    value = abs(value)
    degrees = int(value)
    minutes_float = (value - degrees) * 60
    minutes = int(minutes_float)
    seconds = round((minutes_float - minutes) * 60, 2)

    return[degrees, minutes, seconds, direction]

if __name__ == "__main__":
    latitude = 34.0552
    longitude = -118.2437

    lat_dms = dd_to_dms(latitude, "lat")
    lon_dms = dd_to_dms(longitude, "lon")

    print("Latitude DMS:", lat_dms)
    print("Longitude DMS:", lon_dms)
