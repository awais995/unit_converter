from typing import Optional # Optional is a type hint for an optional value
from units import UNIT_CATEGORIES # UNIT_CATEGORIES is a dictionary of dictionaries 


def convert(category: str, from_unit: str, to_unit: str, value: float) -> Optional[float]: # convert is a function that converts a value from one unit to another
    if category not in UNIT_CATEGORIES: # if the category is not in the UNIT_CATEGORIES dictionary
        return None # return None if the category is not in the UNIT_CATEGORIES dictionary

    units = UNIT_CATEGORIES[category] # get the units for the selected category
    if from_unit not in units or to_unit not in units: # if the from unit is not in the units dictionary or the to unit is not in the units dictionary
        return None # return None if the from unit is not in the units dictionary or the to unit is not in the units dictionary

    base_value = value * units[from_unit] # convert the value to the base unit    
    converted_value = base_value / units[to_unit] # convert the value to the to unit
    return converted_value # return the converted value
