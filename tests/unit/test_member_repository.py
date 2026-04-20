from src.member_repository import MemberRepository


def test_exists_returns_true_for_known_member():
    repo = MemberRepository()
    assert repo.exists(10) is True


def test_exists_returns_false_for_unknown_member():
    repo = MemberRepository()
    assert repo.exists(999) is False


def test_is_blocked_returns_true_when_member_is_blocked():
    repo = MemberRepository()
    assert repo.is_blocked(20) is True


def test_has_overdue_fee_returns_true_when_member_has_debt():
    repo = MemberRepository()
    assert repo.has_overdue_fee(30) is True
