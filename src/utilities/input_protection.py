def user_int_protection(
    u_input,
    default: int,
    in_dict: dict = None,
    positive: bool = False,
    negative: bool = False,
    integer: bool = False,
) -> int:
    if integer:
        try:
            # Float then int is the only way to ensure float strings can be interpreted
            u_input = int(float(u_input))
        except ValueError:
            print(
                f"Error inputing, unable to convert to number, setting result to {default}"
            )
            return default

    if positive:
        if u_input < 0:
            u_input *= -1
            print(
                f"User input is negative, only positive values allowed, setting positive {u_input}"
            )

    if negative:
        if u_input > 0:
            u_input *= -1
            print(
                f"User input is positive, only negative values allowed, setting positive {u_input}"
            )

    if in_dict is not None:
        if u_input not in in_dict:
            print(f"User input was not an available integer, setting default {default}")
            u_input = default
    return u_input


def user_float_protection(
    u_input,
    default: int,
    in_dict: dict = None,
    positive: bool = False,
    negative: bool = False,
    floatp: bool = False,
) -> int:
    if floatp:
        try:
            # Float then int is the only way to ensure float strings can be interpreted
            u_input = float(u_input)
        except ValueError:
            print(
                f"Error inputing, unable to convert to number, setting result to {default}"
            )
            return default

    if positive:
        if u_input < 0:
            u_input *= -1
            print(
                f"User input is negative, only positive values allowed, setting positive {u_input}"
            )

    if negative:
        if u_input > 0:
            u_input *= -1
            print(
                f"User input is positive, only negative values allowed, setting positive {u_input}"
            )

    if in_dict is not None:
        if u_input not in in_dict:
            print(f"User input was not an available integer, setting default {default}")
            u_input = default
    return u_input


def user_str_protection(
    u_input,
    default: str,
    in_dict: dict = None,
    forbidden_chars: list[chr] = None,
    min_length: int = None,
    max_length: int = None,
    t_string: bool = False,
) -> str:
    if t_string:
        if not isinstance(u_input, str):
            try:
                u_input = str(u_input)
            except ValueError:
                print(
                    f'User input cannot be interpreted as a string, setting to default -> "{default}"'
                )

    if forbidden_chars is not None:
        for character in forbidden_chars:
            if character in u_input:
                u_input.replace(character, "")

    if min_length is not None:
        if len(u_input) < min_length:
            print(f"User input too short, setting to default -> {default}")

    if max_length is not None:
        if len(u_input) > max_length:
            print(f"User input too long, setting to default -> {default}")

    if in_dict is not None:
        if u_input not in in_dict:
            print(f"User input was not an available string, setting default {default}")
            u_input = default
