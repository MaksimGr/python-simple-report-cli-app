import pytest
from simple_report_cli import build_report


def test_report():

    abb_str = '\n'.join([
        'DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER',
        'SVF_Sebastian Vettel_FERRARI',
        'LHM_Lewis Hamilton_MERCEDES'])

    start_str = '\n'.join([
        'DRR_2018-05-24_12:08:12.054',
        'SVF_2018-05-24_12:02:58.917',
        'LHM_2018-05-24_12:04:20.125'])

    end_str = '\n'.join([
        'DRR_2018-05-24_12:11:24.067',
        'SVF_2018-05-24_12:04:03.332',
        'LHM_2018-05-24_12:11:32.585'])

    data = {'abb': abb_str,
            'start': start_str,
            'end': end_str}

    report = build_report(data)

    assert len(report) == 3
