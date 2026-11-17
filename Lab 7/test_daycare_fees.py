from hypothesis import given, strategies as st
from daycare_fees import parse_enrolment, hours_average, payable_fee

@given(st.text() | st.none())
def test_parse_enrolment_no_crash(s):
    parse_enrolment(s)

@given(st.text() | st.none())
def test_hours_average_no_crash(s):
    hours_average(s)

@given(st.text() | st.none())
def test_payable_fee_no_crash(s):
    payable_fee(s)
