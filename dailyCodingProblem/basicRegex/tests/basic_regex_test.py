import os

import pytest

from basicRegex import basic_regex


def test_short_regex_positive():
    regex_string = ".*."
    check_string_pos = "ab"
    assert (basic_regex.regex(regex_string, check_string_pos))


def test_short_regex_negative():
    regex_string = ".*."
    check_string_neg = "a"
    assert (not basic_regex.regex(regex_string, check_string_neg))


def test_medium_regex_positive():
    regex_string = ".cG1ab9*qq.l"
    check_string_pos = "acG1ab9lmnoqqfl"
    assert (basic_regex.regex(regex_string, check_string_pos))


def test_medium_regex_negative():
    regex_string = ".cG1ab9*qq.l"
    check_string_neg = ".cG1ab9q.l"
    assert (not basic_regex.regex(regex_string, check_string_neg))


def test_long_regex_positive():
    regex_string = ".a.a.a.ffl092424kqqq*ppqzZ.."
    check_string_pos = "Ya4aMaPffl092424kqqqawfjknawkjfnawklefnlawkjfnlawkfja\
wlekjfnwlkj     lawlfjnwlkajfalkjfnawljkfnlawkjnfdc,dzsm v,wfippqzZll"
    assert (basic_regex.regex(regex_string, check_string_pos))


def test_long_regex_negative():
    regex_string = ".a.a.a.ffl092424kqqq*ppqzZ.."
    check_string_neg = "Ya4aMaPffl092424kqqqawfjknawkjfnawklefnlawkjfnla\
wkfjawlekjfnwlkj     lawlfjnwlkajfalkjfnawljkfnlawkjnfdc,dzsm v,wfippqZll"
    assert (not basic_regex.regex(regex_string, check_string_neg))
