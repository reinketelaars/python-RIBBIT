from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .definition import Croak
import json


def decode_CROAK(json_data):
    """
    Decode a sequence of DER encoded RIBBIT protocol FROG tips.

    Parameters
    ----------
    der : bytes
        Raw DER encoded FROG tips.

    Returns
    -------
    dict
        A dict of FROG tips, keyed by their number.
    """
    try:
        decoded = json.load(json_data)['tips'] 

        return {int(frog_tip['number']):str(frog_tip['tip']) for frog_tip in decoded}
    except:
        raise
