
bucketlist = ["Sumba", "Barcelona", "Zurich"]
cities = ["Amsterdam", "Jakarta", "Istanbul"]
cities[0] = "Hoorn"
cities.extend(bucketlist)
cities.insert(1, "Hong Kong")

cities.reverse()
print(cities)
print("I flew from " + cities[1] + ", made a transit in " + cities[2] + ", before eventually landing in " + cities[0])


