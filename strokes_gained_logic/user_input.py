import argparse
from strokes_gained import strokes_gained
from sg_utils import *


# --------------------------------------------------
# example user input for one hole
# python user_input.py "1:[1,'T',400],[2,'F',100];2:[1,'T',300]"
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

    round_dict = convert_raw_input_to_shot(args.shots)

    statistical_round = strokes_gained(round_dict)

    # TODO this output is fine for now, will eventually be a load into a database or somewhere
    print(
        statistical_round,
        statistical_round.cumulative_ott,
        statistical_round.cumulative_app,
        statistical_round.cumulative_atg,
        statistical_round.cumulative_put,
    )


# --------------------------------------------------
if __name__ == "__main__":
    main()
