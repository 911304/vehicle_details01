def vehicle_details(name, vehicle_id, vehicle_type, price):
    result = (
        f"Vehicle Name : {name}\n"
        f"Vehicle ID   : {vehicle_id}\n"
        f"Type         : {vehicle_type}\n"
        f"Price        : {price}"
    )
    return result


if __name__ == "__main__":
    name = "Car"
    vehicle_id = "V101"
    vehicle_type = "Sedan"
    price = 850000

    print(vehicle_details(name, vehicle_id, vehicle_type, price))