import pytest
from src.waitlist_repository import WaitlistRepository


def test_add_to_waitlist_registers_entry():
    repo = WaitlistRepository()
    repo.add_to_waitlist(10, 1)
    assert repo.has_waitlist(10, 1) is True


def test_has_any_waitlist_returns_true_when_court_has_queue():
    repo = WaitlistRepository()
    repo.add_to_waitlist(10, 1)
    assert repo.has_any_waitlist(1) is True


def test_next_member_returns_first_member_in_queue():
    repo = WaitlistRepository()
    repo.add_to_waitlist(10, 1)
    repo.add_to_waitlist(40, 1)
    assert repo.next_member(1) == 10


def test_remove_from_waitlist_removes_entry():
    repo = WaitlistRepository()
    repo.add_to_waitlist(10, 1)
    repo.remove_from_waitlist(10, 1)
    assert repo.has_waitlist(10, 1) is False


def test_remove_from_waitlist_raises_for_unknown_entry():
    repo = WaitlistRepository()
    with pytest.raises(ValueError, match="Waitlist entry not found"):
        repo.remove_from_waitlist(10, 1)
