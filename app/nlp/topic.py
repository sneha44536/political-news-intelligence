import re


def classify_topic(title, summary=""):

    text = f"{title} {summary}".lower()

    # Economy
    economy_keywords = [
        "gdp",
        "economy",
        "economic",
        "inflation",
        "budget",
        "tax",
        "employment",
        "unemployment",
        "market",
        "rupee",
        "growth",
        "finance"
    ]

    # Elections
    election_keywords = [
        "election",
        "elections",
        "poll",
        "polls",
        "voting",
        "vote",
        "ballot",
        "constituency",
        "campaign",
        "candidate",
        "assembly",
        "lok sabha"
    ]

    # Government
    government_keywords = [
        "government",
        "minister",
        "ministry",
        "cabinet",
        "parliament",
        "policy",
        "bill",
        "law",
        "prime minister",
        "chief minister"
    ]

    # Opposition
    opposition_keywords = [
        "opposition",
        "rahul gandhi",
        "congress",
        "bjp",
        "aap",
        "party",
        "leader"
    ]

    # National Security
    security_keywords = [
        "army",
        "military",
        "defence",
        "defense",
        "border",
        "terrorism",
        "terrorist",
        "security",
        "pakistan",
        "china",
        "war"
    ]

    if any(
        keyword in text
        for keyword in election_keywords
    ):
        return "Elections"

    if any(
        keyword in text
        for keyword in economy_keywords
    ):
        return "Economy"

    if any(
        keyword in text
        for keyword in security_keywords
    ):
        return "National Security"

    if any(
        keyword in text
        for keyword in opposition_keywords
    ):
        return "Opposition"

    if any(
        keyword in text
        for keyword in government_keywords
    ):
        return "Government"

    return "General Politics"