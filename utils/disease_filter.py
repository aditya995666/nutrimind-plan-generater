# utils/disease_filter.py

disease_rules = {
    "Diabetes": {
        "avoid": [
            "sugar", "white rice", "sweets", "soft drinks", "maida", "bakery",
            "juice", "banana shake", "sweet corn", "dessert", "rasgulla",
            "jam", "jaggery", "milkshake", "chocolate", "mithai"
        ],
        "prefer": {
            "breakfast": [
                "Moong dal chilla + green chutney",
                "Vegetable oats upma",
                "Ragi dosa + sambar",
                "Brown bread + peanut butter (no sugar)",
                "Idli + vegetable sambar"
            ],
            "lunch": [
                "Millet khichdi + salad",
                "Moong dal + 2 chapati + lauki sabzi",
                "Vegetable dalia + curd",
                "Brown rice + rajma (small portion)",
                "Methi paratha (less oil) + curd"
            ],
            "dinner": [
                "Lauki soup + veg salad",
                "Grilled paneer + stir-fry veggies",
                "Oats khichdi",
                "Sprouts salad + vegetable soup",
                "2 chapati + moong dal"
            ]
        }
    },

    "PCOS/PCOD": {
        "avoid": [
            "fried foods", "sugar", "white bread", "junk food", "cold drinks",
            "chocolate", "maida", "pasta", "pizza", "burger", "cream biscuits"
        ],
        "meals": {
            "breakfast": [
                "Oats + boiled eggs",
                "Vegetable poha (less oil)",
                "Paneer sandwich (wheat bread)",
                "Sprouts salad bowl",
                "Smoothie: spinach + curd"
            ],
            "lunch": [
                "Mixed veg + millet roti",
                "Quinoa pulao + curd",
                "Grilled paneer + dal soup",
                "Spinach dal + 2 rotis",
                "Vegetable oats khichdi"
            ],
            "dinner": [
                "Paneer tikka + salad",
                "Moong dal soup + veg salad",
                "Egg white omelette + stir veggies",
                "Curd + sautéed vegetables",
                "Lauki sabzi + 2 roti"
            ]
        }
    },

    "Thyroid": {
        "avoid": [
            "soya", "broccoli", "cabbage", "cauliflower", "millets excess",
            "peanuts", "mustard greens"
        ],
        "meals": {
            "breakfast": [
                "Egg omelette + salad",
                "Idli + coconut chutney",
                "Banana + oats porridge",
                "Upma + curd",
                "Moong dal chilla"
            ],
            "lunch": [
                "Fish curry + rice",
                "Moong dal + 2 chapati",
                "Dahi + sabzi + chapati",
                "Lemon rice + veg soup",
                "Dal khichdi"
            ],
            "dinner": [
                "Vegetable soup + salad",
                "Egg curry + 2 chapati",
                "Paneer bhurji + stir veggies",
                "Khichdi + curd",
                "Rice porridge + boiled veggies"
            ]
        }
    },

    "Kidney": {
        "avoid": [
            "high protein", "salt", "pickle", "chips", "processed food",
            "banana", "tomato gravy", "dry fruits"
        ],
        "meals": {
            "breakfast": [
                "Suji upma",
                "Poha (no peanuts)",
                "Rice idli",
                "Daliya porridge",
                "Vegetable sandwich"
            ],
            "lunch": [
                "Rice porridge + lauki sabzi",
                "Moong dal soup + 1 chapati",
                "Boiled vegetable plate",
                "Cucumber salad + khichdi",
                "Plain rice + curd"
            ],
            "dinner": [
                "Lauki soup",
                "Moong dal khichdi",
                "Rice upma",
                "Mixed vegetable stew",
                "Idli + mild sambar"
            ]
        }
    },

    "Heart": {
        "avoid": [
            "oily foods", "fried items", "trans fat", "butter excess",
            "cream", "fast food"
        ],
        "meals": {
            "breakfast": [
                "Oats porridge + apple",
                "Whole wheat toast + peanut butter",
                "Vegetable poha",
                "Upma + salad",
                "Sprouts chaat"
            ],
            "lunch": [
                "Dal + 2 chapati + salad",
                "Grilled fish + vegetables",
                "Vegetable khichdi",
                "Quinoa chapati + dal",
                "Brown rice + mix veg curry"
            ],
            "dinner": [
                "Vegetable soup + nuts (small)",
                "Paneer tikka + salad",
                "Moong dal chilla",
                "Vegetable oats bowl",
                "Steamed vegetables + roti"
            ]
        }
    },

    "Fat Loss / Overweight": {
        "avoid": [
            "fried foods", "sweets", "pizza", "burgers", "maida",
            "sweet drinks", "paratha", "puri"
        ],
        "meals": {
            "breakfast": [
                "Sprouts + 1 apple",
                "Oats + skim milk",
                "Egg whites + salad",
                "Daliya upma",
                "Vegetable poha"
            ],
            "lunch": [
                "Paneer salad bowl",
                "Dal + 2 chapati + salad",
                "Vegetable soup + sprouts",
                "Millet roti + sabzi",
                "Boiled vegetable plate + curd"
            ],
            "dinner": [
                "Grilled paneer/egg + salad",
                "Vegetable soup + oats",
                "Khichdi (less oil)",
                "Moong dal chilla",
                "Lauki soup + salad"
            ]
        }
    },

    "Acidity / Gas": {
        "avoid": [
            "spicy", "tea", "coffee", "pickle", "green chilli", "schezwan"
        ],
        "meals": {
            "breakfast": [
                "Banana + oats porridge",
                "Moong dal chilla",
                "Idli + coconut chutney",
                "Cold milk + toast",
                "Lauki paratha (less oil)"
            ],
            "lunch": [
                "Khichdi + curd",
                "Oats dalia + salad",
                "Rice + lauki sabzi",
                "Vegetable stew",
                "Moong dal + 2 roti (no spice)"
            ],
            "dinner": [
                "Lauki soup",
                "Daliya khichdi",
                "Vegetable soup",
                "Plain rice + curd",
                "Mashed sweet potato"
            ]
        }
    },

    "Fatty Liver": {
        "avoid": [
            "alcohol", "oily foods", "fast food", "cream", "fried",
            "biryani", "paneer butter masala"
        ],
        "meals": {
            "breakfast": [
                "Oats + fruits",
                "Sprouts salad",
                "Idli + veg stew",
                "Vegetable upma",
                "Paneer bhurji + brown bread"
            ],
            "lunch": [
                "Steamed rice + dal + veg",
                "Lauki sabzi + 2 roti",
                "Papaya salad + dal",
                "Khichdi + curd",
                "Vegetable pulao + salad"
            ],
            "dinner": [
                "Moong dal soup",
                "Vegetable stew",
                "Grilled paneer + veggies",
                "Rice porridge",
                "Lauki soup + salad"
            ]
        }
    }
}


def apply_disease_rules_to_text(plan_text, disease):
    """
    Optional helper: naive check for avoid words and return plan_text unchanged if none found.
    For now, this is a read-only helper so you can inspect matches without destructive filtering.
    """
    if disease == "None" or disease not in disease_rules:
        return plan_text
    avoid = disease_rules[disease].get("avoid", [])
    found = []
    lower_text = plan_text.lower()
    for a in avoid:
        if a.lower() in lower_text:
            found.append(a)
    # return original text; caller can decide what to do with 'found'
    return plan_text, found