print("Welcome to CityCab Fare Calculator")
rates = {"Economy": 10,"Premium": 18,"SUV": 25}
distance = float(input("Enter distance in km: "))
vehicle_type = input("Enter vehicle type (Economy/Premium/SUV): ")
duration = int(input("Enter duration in hours (0-23): "))
def calculate_fare(km, vehicle_type, hour):
    if vehicle_type not in rates:
        return "Service Not Available"

    base_fare = km * rates[vehicle_type]

    if 17 <= hour <= 20:
        surge = 1.5
    else:
        surge = 1

    final_price = base_fare * surge

    return final_price
result = calculate_fare(distance, vehicle_type, duration)
print("\n----- Ride Receipt -----")

if result == "Service Not Available":
    print(result)
else:
    print(f"Distance: {distance} km")
    print(f"Vehicle: {vehicle_type}")
    print(f"Time: {duration}:00 hrs")

    if 17 <= duration <= 20:
        print("Surge Applied: Yes (1.5x)")
    else:
        print("Surge Applied: No")

    print(f"Total Fare: ₹{result}")