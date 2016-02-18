from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import vcr as _vcr

from RIBBIT.client import RIBBITClient

vcr = _vcr.VCR(
    cassette_library_dir='tests/cassettes',
    record_mode='once',
)


@vcr.use_cassette
def test_croak():
    client = RIBBITClient()
    croak = client.croak()

    assert 130 in croak
    assert croak[130] == ('IF FROG FAILS POSIX COMPLIANCE, PLEASE RETURN FOR '
                          'A REFUND AND/OR REPLACEMENT')


@vcr.use_cassette
def test_random_frog_tip():
    client = RIBBITClient()
    tip = client.frog_tip()

    assert 'FROG' in tip
