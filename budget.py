#!/usr/bin/python3

flights = [600, 34, 88, 912]
rooms = [158, 154, 193, 105]
things = []
food = []
events = [16.84, 22.5, 9.14, 65, 16]
gifts = []

if __name__ == "__main__":
	flight_cost = sum(flights)
	room_cost = sum(rooms)
	food_cost = sum(food)
	events_cost = sum(events)
	gifts_cost = sum(gifts)
	total = flight_cost + room_cost + food_cost + events_cost + gifts_cost
	print("Flights: $" + str(flight_cost))
	print("Rooms: $" + str(room_cost))
	print("Food: $" + str(food_cost))
	print("Events: $" + str(events_cost))
	print("Gifts: $" + str(gifts_cost))
	print("Total (per person): $" + str(total))
