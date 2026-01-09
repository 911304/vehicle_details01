from vehicle import vehicle_details

def test_vehicle_details():
    expected_output = (
        "Vehicle Name : Bike\n"
        "Vehicle ID   : V202\n"
        "Type         : Sports\n"
        "Price        : 150000"
    )

    assert vehicle_details("Bike", "V202", "Sports", 150000) == expected_output