travel_log = [
    {
        "country": "France",
        "cities": ["Paris", "Lille", "Dijon"],
        "visits": 12,
    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
        "visits": 5,
    }
]


def add_new_country(country,  visits, cities):
    travel_log.append({
        "country": country,
        "cities": cities,
        "visits": visits
    })


add_new_country("Russia", 2, ['Moscow', "Saint Petersburg"])
print(travel_log)
