import pytest

from src.sports_center_service import SportsCenterService
from src.court_repository import CourtRepository
from src.member_repository import MemberRepository
from src.booking_repository import BookingRepository
from src.waitlist_repository import WaitlistRepository


@pytest.fixture
def service():
    return SportsCenterService(
        CourtRepository(),
        MemberRepository(),
        BookingRepository(),
        WaitlistRepository()
    )

    
def reserve_base(service):
    return service.reserve_court(10, 1)


# 1. reserva com sucesso
def test_reservation_success(service):
    assert reserve_base(service) is True


# 2. membro inexistente
def test_member_not_found(service):
    assert service.reserve_court(999, 1) is False


