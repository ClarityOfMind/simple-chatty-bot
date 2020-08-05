duration = int(input())
food_cost = int(input())
one_way_flight_cost = int(input())
hotel_cost = int(input())

total_cost = (one_way_flight_cost * 2) + (food_cost + hotel_cost) * duration - hotel_cost

print(total_cost)
