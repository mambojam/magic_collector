import pandas as pd

# Read CSV file
cards_df = pd.read_csv("mtg_cards.csv")

# Mapping a new dictionary with keys Set and Name
cards_name_and_set = cards_df[["Set", "Name"]].to_dict(orient='records')
print(cards_name_and_set)

# Create an empy list for the cleaned names to go into
my_cards = []

# Clean the name and set text to comply with URL conventions
for card in cards_name_and_set:
    if card["Set"] == "LTC":
        card["Set"] = "tales-of-middle-earth-commander"
    elif card["Set"] == "LTR":
        card["Set"] = "the-lord-of-the-rings-tales-of-middle-earth"
    elif card["Set"] == "LOR":
        card["Set"] = "the-lord-of-the-rings-tales-of-middle-earth"
    elif card["Set"] == "LCC":
        card["Set"] = "the-lost-caverns-of-ixalan-commander"
    elif card["Set"] == "LCI":
        card["Set"] = "the-lost-caverns-of-ixalan"
    elif card["Set"] == "CSP":
        card["Set"] = "coldsnap"
    elif card["Set"] == "SPG":
        card["Set"] = "special-guests"
    elif card["Set"] == "REX":
        card["Set"] = "jurassic_world_collection"
    elif card["Set"] == "AFR":
        card["Set"] = "adventures-in-the-forgotten-realms"
    elif card["Set"] == "MIC":
        card["Set"] = "midnight-hunt-commander"
    elif card["Set"] == "WOE":
        card["Set"] = "wilds-of-eldraine"
    else:
        break

    card["Name"] = card["Name"].replace(" ", "-")
    my_cards.append(card)

print(my_cards)