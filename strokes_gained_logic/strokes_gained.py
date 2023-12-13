from strokes_gained_round import StrokesGainedRound
from sg_utils import *


def strokes_gained(golf_round: dict) -> StrokesGainedRound:
    """
    INPUT: golf_round -> Dictionary containing shot classes
    OUTPUT: sg_df -> dataframe which contains SG shot value for each of your shots for every hole
    """

    # create StrokesGainedRound class to hold strokes gained info
    sg_df = StrokesGainedRound()

    # take golf_round and add expected strokes to hole out to each shot
    add_expected_strokes(golf_round)

    for hole in golf_round:
        # returns a tuple of loop index (used to get next shot for that hole) and shot
        for index, shot in enumerate(golf_round[hole]):
            # checks if there is another shot for this hole, sets next expected strokes accordingly
            next_expected_strokes = (
                golf_round[hole][index + 1].expected_strokes_to_hole_out
                if (index < len(golf_round[hole]) - 1)
                else 0
            )

            # append actual strokes gained value for current shot in pandas df, indexed by hole number and strokes gained category
            sg_df.statistical_round[shot.get_category()][int(hole) - 1].append(
                get_sg_for_shot(
                    shot.expected_strokes_to_hole_out,
                    next_expected_strokes,
                    shot.penalty,
                )
            )

    sg_df.set_cumulative_strokes_gained()

    return sg_df
