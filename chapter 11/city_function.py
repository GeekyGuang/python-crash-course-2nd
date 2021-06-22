def city_info(city, country, population=''):
    if population:
        total_name = f"{city}, {country} - population {population}"
    else:
        total_name = f"{city}, {country}"
    return total_name.title()
