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
    ]

    TENS = [
        "",
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

        base_digit = number % 10
        base_ten_digit = number // 10
        if base_ten_digit == 0:
            return cls.UNITS[base_digit]
        else:
            return cls.TENS[base_ten_digit] + cls.UNITS[base_digit]
