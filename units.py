from typing import Dict # Dict is a type hint for a dictionary

# Base units: meter, kilogram, second, etc.
# Length: meter, kilometer, centimeter, millimeter, inch, foot, yard, mile
# Mass: kilogram, gram, milligram, pound, ounce
# Time: second, minute, hour, day   

UNIT_CATEGORIES: Dict[str, Dict[str, float]] = { # UNIT_CATEGORIES is a dictionary of dictionaries
    "Length": { # Length is a key in the UNIT_CATEGORIES dictionary
        "Meter": 1, # Meter is a key in the Length dictionary
        "Kilometer": 1000, # Kilometer is a key in the Length dictionary
        "Centimeter": 0.01, # Centimeter is a key in the Length dictionary
        "Millimeter": 0.001, # Millimeter is a key in the Length dictionary
        "Inch": 0.0254, # Inch is a key in the Length dictionary
        "Foot": 0.3048, # Foot is a key in the Length dictionary
        "Yard": 0.9144, # Yard is a key in the Length dictionary
        "Mile": 1609.34 # Mile is a key in the Length dictionary
    },
    "Mass": { # Mass is a key in the UNIT_CATEGORIES dictionary
        "Kilogram": 1, # Kilogram is a key in the Mass dictionary
        "Gram": 0.001, # Gram is a key in the Mass dictionary
        "Milligram": 0.000001, # Milligram is a key in the Mass dictionary
        "Pound": 0.453592, # Pound is a key in the Mass dictionary
        "Ounce": 0.0283495 # Ounce is a key in the Mass dictionary
    },
    "Time": { # Time is a key in the UNIT_CATEGORIES dictionary
        "Second": 1, # Second is a key in the Time dictionary
        "Minute": 60, # Minute is a key in the Time dictionary
        "Hour": 3600, # Hour is a key in the Time dictionary
        "Day": 86400 # Day is a key in the Time dictionary          
    }
}
