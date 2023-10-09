def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(phone_numbers):
    # Initialize dictionaries to store phone numbers for each country
    country_phone_numbers = {
        "JP": [],
        "SG": [],
        "TW": [],
        "UA": []
    }

    # Define the country prefixes and their corresponding ISO codes
    country_prefixes = {
        "+81": "JP",
        "+65": "SG",
        "+886": "TW",
        "+380": "UA"
    }

    # Iterate through the phone numbers
    for phone_number in phone_numbers:
        # Sanitize (normalize) the phone number
        sanitized_number = sanitize_phone_number(phone_number)

        # Determine the country based on the prefix
        country_code = None
        for prefix, iso_code in country_prefixes.items():
            if sanitized_number.startswith(prefix):
                country_code = iso_code
                break

        # If no matching country is found, default to "UA"
        if country_code is None:
            country_code = "UA"

        # Add the sanitized phone number to the corresponding country's list
        country_phone_numbers[country_code].append(sanitized_number)

    return country_phone_numbers

    if country_code is None:
            country_code = "UA"

        # Add the sanitized phone number to the corresponding country's list
    country_phone_numbers[country_code].append(sanitized_number)

    return country_phone_numbers
    