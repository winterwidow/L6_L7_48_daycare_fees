import pytest
from daycare_fees import extra_hours_fee, enrolment_allowed, pickup_status

# Example test cases:
def test_within_included_hours():
    assert extra_hours_fee("toddler", 20, False) == 0

def test_enrolment_allowed():
    assert enrolment_allowed(24, 2, False) is True


def test_unknown_age_group():
    with pytest.raises(ValueError, match="unknown age group"):
        extra_hours_fee("school_age", 10, False)


def test_negative_hours():
    with pytest.raises(ValueError, match="invalid hours"):
        extra_hours_fee("infant", -1, False)


def test_infant_extra_hours():
    assert extra_hours_fee("infant", 21, False) == 14


def test_non_infant_extra_hours():
    assert extra_hours_fee("toddler", 26, False) == 9


def test_sibling_discount_for_non_infant():
    assert extra_hours_fee("toddler", 31, True) == 9


def test_preschool_extra_hours():
    assert extra_hours_fee("preschool", 31, False) == 9


def test_infant_large_extra_hours():
    assert extra_hours_fee("infant", 41, False) == 462


def test_non_infant_large_extra_hours():
    assert extra_hours_fee("toddler", 46, False) == 294


def test_pending_immunisation_allowed():
    assert enrolment_allowed(12, 0, True) is True


def test_pending_immunisation_too_young():
    assert enrolment_allowed(11, 5, True) is False


def test_enrolment_rejected_for_low_age():
    assert enrolment_allowed(5, 2, False) is False


def test_enrolment_rejected_without_vacancy():
    assert enrolment_allowed(24, 0, False) is False


def test_pickup_on_time_regular_day():
    assert pickup_status(10, False, False) == "on_time"


def test_pickup_late_aftercare_friday():
    assert pickup_status(20, True, True) == "late"


def test_pickup_overdue_regular_day():
    assert pickup_status(-6, False, False) == "overdue"
