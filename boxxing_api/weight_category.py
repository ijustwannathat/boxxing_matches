from numpy import linspace


def float_range(start, end, step=0.1, endpoint=False):
    data = []
    iterations = int((end - start) / step) + 1
    for i in linspace(start, end, iterations, endpoint=endpoint):
        data.append(float(f"{i:.1f}"))
    return data


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


def define_weight_category(weight):
    for values, key in dictionary.items():
        match weight:
            case _ if weight in float_range(*values):
                return key
            case _ if isinstance(weight, (int, float)) is False:
                return "Stringtype is not (int, float)"
            case _ if weight > 300:
                return "Weight is overestimated"


# def define_weight_category(weight: float) -> str:
#     match weight:
#         case _ if weight in float_range(48, 49):
#             return "Minimumweight"
#         case _ if weight in float_range(49, 50):
#             return "Light Flyweight"
#         case _ if weight in float_range(50, 52):
#             return "Flyweight"
#         case _ if weight in float_range(52, 53.5):
#             return "Super Flyweight"
#         case _ if weight in float_range(53.5, 55):
#             return "Bantamweight"
#         case _ if weight in float_range(55, 57):
#             return "Super Bantamweight"
#         case _ if weight in float_range(57, 59):
#             return "Featherweight"
#         case _ if weight in float_range(59, 61):
#             return "Super Featherweight"
#         case _ if weight in float_range(61, 63.5):
#             return "Lightweight"
#         case _ if weight in float_range(63.5, 67):
#             return "Super Lightweight"
#         case _ if weight in float_range(67, 70):
#             return "Welterweight"
#         case _ if weight in float_range(70, 72.5):
#             return "Super Welterweight"
#         # case _ if weight in float()
