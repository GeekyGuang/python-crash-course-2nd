def make_cars(manufacturer, model, **cars):
    cars['manufacturer'] = manufacturer
    cars['model'] = model

    return cars


car = make_cars('subaru', 'outback', color='blue', tow_package=True)
print(car)
