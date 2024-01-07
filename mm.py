#!/usr/bin/python
import sys

def mm_to_inches(mm):
    return mm * 0.0393701

def inches_to_mm(inches):
    return inches * 25.4

def ounce_to_grams(ounce):
    return ounce * 28.3495

def grams_to_ounce(grams):
    return grams / 28.3495

def lbs_to_kg(lbs):
    return lbs * 0.453592

def kg_to_lbs(kg):
    return kg / 0.453592

def miles_to_km(miles):
    return miles * 1.60934

def km_to_miles(km):
    return km / 1.60934

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

# Mapping of unit variations to standardized unit names
unit_mappings = {
    'mm': 'mm',
    'millimeter': 'mm',
    'millimeters': 'mm',
    'inch': 'inch',
    'inches': 'inch',
    'in': 'inch',
    'ounce': 'ounce',
    'ounces': 'ounce',
    'oz': 'ounce',
    'gram': 'gram',
    'grams': 'gram',
    'g': 'gram',
    'lbs': 'lbs',
    'pound': 'lbs',
    'pounds': 'lbs',
    'kg': 'kg',
    'kilogram': 'kg',
    'kilograms': 'kg',
    'mile': 'mile',
    'miles': 'mile',
    'km': 'km',
    'kilometer': 'km',
    'kilometers': 'km',
    'fahrenheit': 'fahrenheit',
    'f': 'fahrenheit',
    'celsius': 'celsius',
    'c': 'celsius',
}

def set_result_unit(r_unit):
    global result_unit
    result_unit = r_unit
    return

# Perform conversions based on command-line arguments
def perform_conversion(value, unit):
    standardized_unit = unit_mappings.get(unit.lower())
    if standardized_unit == 'mm':
        set_result_unit('in')
        return mm_to_inches(value)
    elif standardized_unit == 'inch':
        set_result_unit('mm')
        return inches_to_mm(value)
    elif standardized_unit == 'ounce':
        set_result_unit('g')
        return ounce_to_grams(value)
    elif standardized_unit == 'gram':
        set_result_unit('oz')
        return grams_to_ounce(value)
    elif standardized_unit == 'lbs':
        set_result_unit('kg')
        return lbs_to_kg(value)
    elif standardized_unit == 'kg':
        set_result_unit('lbs')
        return kg_to_lbs(value)
    elif standardized_unit == 'mile':
        set_result_unit('km')
        return miles_to_km(value)
    elif standardized_unit == 'km':
        set_result_unit('mi')
        return km_to_miles(value)
    elif standardized_unit == 'fahrenheit':
        set_result_unit('°C')
        return fahrenheit_to_celsius(value)
    elif standardized_unit == 'celsius':
        set_result_unit('°F')
        return celsius_to_fahrenheit(value)
    else:
        return "Unsupported unit for conversion"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <value> <unit>")
    else:
        value = float(sys.argv[1])
        unit = sys.argv[2]
        result = perform_conversion(value, unit)
        if isinstance(result, str):
            print(result)
        else:
            standardized_unit = unit_mappings.get(unit.lower(), unit)
            print(f"{value} {unit} is equivalent to {result:.2f} {result_unit}")
