from numpy import linspace


def float_range(start, end, step=0.1, endpoint=False):
    float_values = []
    iterations = int((end - start) / step) + 1
    for i in linspace(start, end, iterations, endpoint=endpoint):
        float_values.append(float(f"{i:.1f}"))
    return float_values


dictionary = {
    (48, 49): "Minimumweight",
    (49, 50): "Light Flyweight",
    (50, 52): "Flyweight",
    (52, 53.5): "Super Flyweight",
    (53.5, 55): "Bantamweight",
    (55, 57): "Super Bantamweight",
    (57, 59): "Featherweight",
    (59, 61): "Super Featherweight",
    (61, 63.5): "Lightweight",
    (63.5, 67): "Super Lightweight",
    (67, 70): "Welterweight",
    (70, 72.5): "Super Welterweight",
    (72.5, 76): "Middleweight",
    (76, 79): "Super Middleweight",
    (79, 91): "Lightweight Heavyweight",
    (91, 101.6): "Cruiserweight",
    (101.6, 300): "Heavyweight",
}

"""
NOTE:
    This code is bad and will/must be REWRITTEN
    But for testing purpose i left it hanging.
"""


def define_weight_category(weight):
    for values, key in dictionary.items():
        match weight:
            case _ if weight in float_range(*values):
                return key
            case _ if isinstance(weight, (int, float)) is False:
                return "String type is not (int, float)"
            case _ if weight > 300:
                return "Weight is overestimated"


#
# win_choices = (
#     ("KO", "Knockout"),
#     ("TKO", "Technical Knockout"),
#     ("UD", "Unanonimous Decision"),
#     ("SD", "Split Decision"),
#     ("MD", "Majority Decision"),
#     ("Draw", "Draw"),
#     ("NC", "No Contest"),
# )
# win_method = models.CharField(max_length=50, choices=win_choices, blank=True)
#
