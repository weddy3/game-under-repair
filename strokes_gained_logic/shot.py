class Shot:
    """A simple class representing a user's golf shot"""

    def __init__(self, stroke: int, lie: str, distance_remaining: int, penalty=False):
        self.stroke = stroke
        self.lie = lie
        self.distance_remaining = distance_remaining
        self.penalty = penalty
        self.expected_strokes_to_hole_out = 0.0

    def __str__(self):
        unit_of_measurement = "feet" if self.lie == "P" else "yards"
        return f"This is shot number {self.stroke}, from {self.distance_remaining} {unit_of_measurement} away from {self.lie}."

    def get_category(self) -> str:
        """Returns the correct SG category to add shot info to (OTT, APP, ATG, PUT)"""
        if self.distance_remaining <= 99 and self.lie != "P":
            return "ATG"
        elif self.distance_remaining >= 100 and self.lie not in ["T", "P"]:
            return "APP"
        elif self.distance_remaining >= 100 and self.lie == "T":
            return "OTT"
        elif self.lie == "P":
            return "PUT"
        else:
            return "BAD"

    def set_expected_strokes_to_hole_out(self, expected_strokes: int):
        """Sets expected_strokes_to_hole_out"""
        self.expected_strokes_to_hole_out = expected_strokes
