from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import pytest

from RIBBIT.decoder import decode_CROAK
from RIBBIT.encoder import encode_CROAK


def test_encoding_valid_CROAK():
    croak = {
        55: '* OUTOFMEMORYERROR NO LONGER OCCURS IN FROGS UNDER 3CM IN GIRTH.',
        87: 'FROG IS IN BETA. DO NOT EXPECT ALL FEATURES OF FROG TO WORK',
    }

    encoded = encode_CROAK(croak)
    decoded = decode_CROAK(encoded)

    assert decoded == croak


def test_encoding_invalid_CROAK_raises_exception():
    with pytest.raises(ValueError) as excinfo:
        encode_CROAK({None: None})

    assert 'Error during FROG tip encoding' in str(excinfo.value)
