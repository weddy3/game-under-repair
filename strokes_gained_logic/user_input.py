import argparse
from strokes_gained import strokes_gained
from sg_utils import *


# --------------------------------------------------
# example user input for one hole
# python user_input.py "1:(1,'T',400),(2,'F',100);2:(1,'T',300)"
def get_user_input():
    """Get shot information from the CLI"""

    parser = argparse.ArgumentParser(
        description="Take in user's shot information for strokes gained calculations",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # this is shots OR the path to a csv with shot info
    parser.add_argument("shots", metavar="shots", help="shot info", type=str)

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_user_input()

    statistical_round = strokes_gained(args.shots)

    print(
        statistical_round,
        statistical_round.cumulative_ott,
        statistical_round.cumulative_app,
        statistical_round.cumulative_atg,
        statistical_round.cumulative_put,
    )

    #     # each hole is represented by list of shot classes
    # # TODO how will this be populated? Initially via cli input? Or from excel file?
    # golf_round = {
    #     "1": [
    #         Shot(1, "T", 400),
    #         Shot(2, "F", 100, True),
    #         Shot(4, "P", 10),
    #         Shot(5, "F", 5),
    #     ],
    #     "2": [Shot(1, "T", 400), Shot(2, "F", 100), Shot(3, "F", 105)],
    #     "3": [Shot(1, "T", 400), Shot(2, "F", 100), Shot(3, "P", 10)],
    # }


# --------------------------------------------------
if __name__ == "__main__":
    main()
