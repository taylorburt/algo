
airports = ["BGI", "CDG", "DEL", "DOH", "DSM", "DWR",
            "EYW", "HND", "ICN", "JFK", "LGA", "LHR",
            "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]

routes = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"]
]

startingAirport = "LGA"

for route in routes:
    start = route[0]
    dest = route[1]
    print("%s => %s" % (start, dest))