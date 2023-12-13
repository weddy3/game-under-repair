class StrokesGainedRound:
    """Represents the strokes gained value of eavh shot in a given round"""

    # TODO have methods for calculating per hole and total round, not just category

    def __init__(self):
        self.statistical_round = {
            "OTT": [[] for x in range(18)],
            "APP": [[] for x in range(18)],
            "ATG": [[] for x in range(18)],
            "PUT": [[] for x in range(18)],
        }
        self.cumulative_ott = 0.0
        self.cumulative_app = 0.0
        self.cumulative_atg = 0.0
        self.cumulative_put = 0.0
        self.total_strokes_gained = 0.0

    def set_cumulative_strokes_gained(self):
        """set cumulative strokes gained for round to correct category"""

        total_sg = 0.0

        for key in self.statistical_round:
            total_sg_by_category = round(
                sum(list(map(sum, self.statistical_round[key]))), 2
            )

            total_sg += total_sg_by_category

            match key:
                case "OTT":
                    self.cumulative_ott = total_sg_by_category
                case "APP":
                    self.cumulative_app = total_sg_by_category
                case "ATG":
                    self.cumulative_atg = total_sg_by_category
                case "PUT":
                    self.cumulative_put = total_sg_by_category

        self.total_strokes_gained = total_sg

    # TODO this will be meaningless if the set_cumulative_strokes isn't preemptively run
    def __str__(self):
        return f"Total strokes gained: {self.total_strokes_gained}"
