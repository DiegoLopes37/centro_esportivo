import pytest
from src.court_repository import CourtRepository


def test_exists_returns_true_for_existing_court():
    repo = CourtRepository()
    assert repo.exists(1) is True


def test_is_available_returns_true_for_available_court():
    repo = CourtRepository()
    assert repo.is_available(1) is True


def test_is_available_returns_false_for_unavailable_court():
    repo = CourtRepository()
    assert repo.is_available(3) is False


def test_mark_unavailable_changes_court_state():
    repo = CourtRepository()
    repo.mark_unavailable(1)
    assert repo.is_available(1) is False


def test_mark_available_changes_court_state():
    repo = CourtRepository()
    repo.mark_available(3)
    assert repo.is_available(3) is True


def test_mark_unavailable_raises_for_unknown_court():
    repo = CourtRepository()
    with pytest.raises(ValueError, match="Court not found"):
        repo.mark_unavailable(999)
