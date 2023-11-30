import pandas as pd
from pprint import pprint
from shot import Shot
from sg_utils import *


def strokes_gained(golf_round: dict) -> pd.DataFrame:
    """
    INPUT: golf_round -> Dictionary containing shot classes
    OUTPUT: sg_df -> dataframe which contains SG shot value for each of your shots for every hole
    TODO account for penalty strokes
    TODO do we want to add stroke gained result in the shot class? Then sum shot.values across dict?
    """

    # create empty pandas dataset to hold data
    sg_df = make_sg_df()

    # take golf_round and add expected strokes to each shot
    add_expected_strokes(golf_round)

    for hole in golf_round:
        # returns a tuple of loop index and shot, used to get next shot in hole
        for index, shot in enumerate(golf_round[hole]):

            # checks if there is another shot for this hole, sets next expected strokesaccordingly
            next_expected_strokes = golf_round[hole][index+1].expected_strokes_to_hole_out if (index < len(golf_round[hole]) - 1) else 0

            # append actual strokes gained value for current shot, indexed by hole number and strokes gained category
            sg_df.at[int(hole)-1, shot.get_category()].append(get_sg_for_shot(shot.expected_strokes_to_hole_out, next_expected_strokes))
      
    return sg_df


def main():
    # each hole is represented by list of shot classes
    golf_round = {
        '1': [Shot(1, 'T', 400), Shot(2, 'F', 100), Shot(3, 'P', 10), Shot(4, 'P', 1)],
        '2': [Shot(1, 'T', 400), Shot(2, 'F', 100), Shot(3, 'F', 105)],
        '3': [Shot(1, 'T', 400), Shot(2, 'F', 100), Shot(3, 'P', 10)]
    }

    sg_df = strokes_gained(golf_round)
    pprint(sg_df)

if __name__ == '__main__':
    main()
