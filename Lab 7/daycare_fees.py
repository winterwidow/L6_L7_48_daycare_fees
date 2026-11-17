import math


def parse_enrolment(text):
    if not isinstance(text, str) or text.count(":") != 1:
        return None

    age_group, hours_text = (part.strip() for part in text.split(":"))
    if not age_group or not hours_text:
        return None

    try:
        hours = float(hours_text)
    except (TypeError, ValueError, OverflowError):
        return None

    if not math.isfinite(hours) or hours < 0:
        return None
    return age_group.title(), hours

def hours_average(hours_csv):
    if not isinstance(hours_csv, str) or not hours_csv.strip():
        return None

    values = []
    for raw_value in hours_csv.split(","):
        value = raw_value.strip()
        if not value:
            return None
        try:
            parsed_value = int(value)
        except (TypeError, ValueError, OverflowError):
            return None
        if parsed_value < 0:
            return None
        values.append(parsed_value)

    return sum(values) // len(values)

def payable_fee(text):
    if not isinstance(text, str) or text.count("|") != 1:
        return None

    fee_text, discount_text = (part.strip() for part in text.split("|"))
    if not fee_text or not discount_text:
        return None

    try:
        fee = float(fee_text)
        discount = float(discount_text)
    except (TypeError, ValueError, OverflowError):
        return None

    if (
        not math.isfinite(fee)
        or not math.isfinite(discount)
        or fee < 0
        or discount < 0
    ):
        return None

    total = fee * 1.18 - discount
    return max(total, 0)

def main():
    print("==== Running parse_enrolment ====")
    user_input = input("Enter age group:hours (e.g. toddler:25): ")
    result = parse_enrolment(user_input)
    print("Age Group and Hours:", result)

    print("\n==== Running hours_average ====")
    user_input = input("Enter weekly hours as CSV (e.g. 20,25,30): ")
    result = hours_average(user_input)
    print("Average Hours:", result)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 3000|250): ")
    result = payable_fee(user_input)
    print("Payable Fee:", result)

if __name__ == "__main__":
    main()
