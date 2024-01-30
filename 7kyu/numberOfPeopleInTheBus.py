# - input: an array of integer pairs
# - each pair represent the number of people that get on and off the bus
# - return the number of people who are still on the bus after the last bus


def number(bus_stops):
    totalIn = 0
    totalOut = 0

    for stop in bus_stops:
        totalIn += stop[0]
        totalOut += stop[1]

    return totalIn - totalOut


print(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]))
