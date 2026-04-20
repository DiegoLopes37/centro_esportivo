import pytest
from src.booking_repository import BookingRepository


def test_create_booking_registers_active_booking():
    repo = BookingRepository()
    repo.create_booking(10, 1)
    assert repo.has_active_booking(1) is True


def test_count_active_bookings_counts_only_member_bookings():
    repo = BookingRepository()
    repo.create_booking(10, 1)
    repo.create_booking(10, 2)
    repo.create_booking(40, 3)
    assert repo.count_active_bookings(10) == 2


def test_is_court_with_member_returns_true_for_matching_booking():
    repo = BookingRepository()
    repo.create_booking(10, 1)
    assert repo.is_court_with_member(10, 1) is True


def test_close_booking_removes_active_booking():
    repo = BookingRepository()
    repo.create_booking(10, 1)
    repo.close_booking(10, 1)
    assert repo.has_active_booking(1) is False


def test_close_booking_raises_for_unknown_booking():
    repo = BookingRepository()
    with pytest.raises(ValueError, match="Active booking not found"):
        repo.close_booking(10, 1)
