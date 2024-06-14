class Converter:
    UNITS = [
        "zéro",
        "un",
        "deux",
        "trois",
        "quatre",
        "cinq",
        "six",
        "sept",
        "huit",
        "neuf",
        "dix",
        "onze",
        "douze",
        "treize",
        "quatorze",
        "quinze",
        "seize",
        "dix-sept",
        "dix-huit",
        "dix-neuf",
    ]

    TENS = [
        "zéro",
        "dix",
        "vingt",
        "trente",
        "quarante",
        "cinquante",
        "soixante",
        "soixante-dix",
        "quatre-vingt",
        "quatre-vingt-dix",
    ]

    def __init__(self): ...

    @classmethod
    def convert(cls, number):
        if not isinstance(number, int):
            raise ValueError("Only integers are supported")

        if number < 0:
            raise ValueError("Only positive integers are supported")

        if number < 20:
            return cls.UNITS[number]

        base_digit = number % 10
        base_ten_digit = number // 10

        if base_ten_digit in {7, 9}:
            base_digit += 10
            base_ten_digit -= 1

        if base_digit > 1:
            return cls.TENS[base_ten_digit] + "-" + cls.UNITS[base_digit]

        if base_digit == 1:
            return cls.TENS[base_ten_digit] + "-et-" + cls.UNITS[base_digit]

        if base_digit == 0:
            return cls.TENS[base_ten_digit]
