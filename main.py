import pandas as pd

population_data = pd.read_csv("population.csv")
rest_data = pd.read_csv("fbi_rest_crime.csv")
# print(rest_data.head())
cities, population = population_data["Metropolitan Statistical Area"], population_data["Population"]
violent_crime = rest_data["Violent\ncrime"]
# print(violent_crime)


def city_2_geocoords():
    return


def find_city_indexes_geocords():
    indexes = []
    metro_areas = []
    res = {}

    for index, value in cities.items():
        if isinstance(value, str):
            indexes.append(index)
            metro_areas.append(value)

    # print(f"Index : {index}, Value : {value}")
    res['indexes'] = indexes
    res['metro_areas'] = metro_areas
    return res


def parse_population_data(city_indexes: list):
    values = []

    for index, value in population.items():
        if index in city_indexes:
            values.append(value)

    return values


def select_data(stat):
    if stat == "violent":
        return list(violent_crime.items())
    # elif stat == "rape":
    #     return list(rape.items())
    # elif stat == "robbery":
    #     return list(robbery.items())
    # elif stat == "aggr_assault":
    #     return list(aggr_assault.items())
    # elif stat == "property_crime":
    #     return list(property_crime.items())
    # elif stat == "burglary":
    #     return list(burglary.items())
    # elif stat == "larcency":
    #     return list(larcency.items())
    # elif stat == "motor":
    #     return list(motor.items())
    # else:
    #     return list(murder.items())


def parse_stats(stat):
    data = select_data(stat)
    values = []

    for index, currentValue in enumerate(data):
        current = currentValue[1]
        # previous = data[index - 1][1]

        if isinstance(current, str):
            if "." in current:
                values.append(current)
                print(current)
            # else:
                #     values.append("0")
                # print(current)
        # else:
            # print(current)

    return values

def build_stat_row(data):
    values = []
    city_indexes = city_data['indexes']

    for index, value in enumerate(city_indexes):
        currVal = data[index]
        if currVal:
            values.append(currVal)
        else:
            values.append("0")
            # rate = data[index + 4][1]


            # if "." in rate:
            #     print(rate)
            #     # values.append(rate)
            # else:
            #     print(data[index + 5][1])
                # values.append(data[index + 5][1])

    return values


city_data = find_city_indexes_geocords()
metro_areas = city_data['metro_areas']
population_values = parse_population_data(city_data['indexes'])
vcrime_values = parse_stats('violent')
vcrime = build_stat_row(vcrime_values)
# murder_values = parse_stats('murder')
# rape_values = parse_stats('rape')
# robbery_values = parse_stats('robbery')
# aggr_assault_values = parse_stats('aggr_assault')
# property_crime_values = parse_stats('property_crime')
# burglary_values = parse_stats('burglary')
# larcency_values = parse_stats('larcency')
# motor_values = parse_stats('motor')

# print(city_data)
print(len(population_values))
print(len(vcrime))


def build_rows():
    res = []

    for i in range(len(metro_areas)):
        city = metro_areas[i]
        population = population_values[i]
        vcrimes = vcrime_values[i]
        # murders = murder_values[i]
        # rapes = rape_values[i]
        # robberies = robbery_values[i]
        # aggr_assaults = aggr_assault_values[i]
        # property_crimes = property_crime_values[i]
        # burglaries = burglary_values[i]
        # larcencies = larcency_values[i]
        # motors = motor_values[i]

        # res.append([city, population, vcrimes, murders, rapes, robberies,
        #    aggr_assaults, property_crimes, burglaries, larcencies, motors])

        res.append([city, population, vcrimes])
    return res


_rows = build_rows()
print(_rows)


# create custom csv
filename = "crime.csv"
fields = ['City', 'Population', 'Violent Crime', 'Murder', "Rape", "Robbery",
          "Aggravated Assault", "Property Crime", "Burglary", "Larcency", "Motor Vehicle Theft", "Total Crimes"]
rows = _rows
