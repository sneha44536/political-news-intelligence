import re


PEOPLE = [
    "Narendra Modi",
    "Rahul Gandhi",
    "Amit Shah",
    "Mallikarjun Kharge",
    "Arvind Kejriwal",
    "Mamata Banerjee",
    "Yogi Adityanath",
    "Sonia Gandhi",
    "Priyanka Gandhi",
    "Nirmala Sitharaman"
]

ORGANIZATIONS = [
    "BJP",
    "Congress",
    "AAP",
    "CPI",
    "CPI(M)",
    "Shiv Sena",
    "NCP",
    "DMK",
    "TMC",
    "Lok Sabha",
    "Rajya Sabha"
]

LOCATIONS = [
    "India",
    "Delhi",
    "Mumbai",
    "Pune",
    "Maharashtra",
    "Karnataka",
    "Tamil Nadu",
    "West Bengal",
    "Uttar Pradesh",
    "Gujarat",
    "Bihar",
    "Punjab",
    "Rajasthan",
    "Kashmir",
    "Pakistan",
    "China"
]


def find_names(text, names):

    found = []

    for name in names:

        pattern = r"\b" + re.escape(name) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            found.append(name)

    return found


def extract_entities(text):

    if not text:
        return {
            "people": [],
            "organizations": [],
            "locations": []
        }

    return {
        "people": find_names(text, PEOPLE),
        "organizations": find_names(text, ORGANIZATIONS),
        "locations": find_names(text, LOCATIONS)
    }