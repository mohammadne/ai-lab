def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def get_user_name(user):
    if not isinstance(user, dict):
        raise TypeError("user must be a dictionary")
    if "name" not in user:
        raise KeyError("user dictionary must contain a 'name' key")
    return user["name"].upper()
