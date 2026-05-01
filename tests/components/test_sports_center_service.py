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

# 3. quadra inexistente
def test_court_not_found(service):
    assert service.reserve_court(10, 999) is False

# 4. membro bloqueado
def test_blocked_member(service):
    assert service.reserve_court(20, 1) is False

# 5. mensalidade em atraso
def test_overdue_member(service):
    assert service.reserve_court(30, 1) is False

# 6. limite de 2 reservas
def test_limit_reservations(service):
    assert service.reserve_court(10, 1) is True
    assert service.reserve_court(10, 2) is True
    assert service.reserve_court(10, 3) is False

# 7. fila de espera
def test_waitlist_success(service):
    service.reserve_court(10, 1)

    assert service.join_waitlist(40, 1) is True

# 8. fila duplicada
def test_waitlist_duplicate(service):
    service.reserve_court(10, 1)

    assert service.join_waitlist(40, 1) is True
    assert service.join_waitlist(40, 1) is False

# 9. liberação sem fila
def test_release_without_waitlist(service):
    service.reserve_court(10, 1)
    service.release_court(10, 1)

    assert service.court_repository.is_available(1) is True

# 10. liberação com fila mantém indisponível
def test_release_with_waitlist(service):
    service.reserve_court(10, 1)
    service.join_waitlist(40, 1)

    service.release_court(10, 1)

    assert service.court_repository.is_available(1) is False

# 11. reserva remove próprio da fila
def test_reservation_removes_self_from_waitlist(service):
    service.reserve_court(10, 1)
    service.join_waitlist(10, 1)

    service.release_court(10, 1)
    service.reserve_court(10, 1)

    assert service.waitlist_repository.has_waitlist(10, 1) is False

# 12. fluxo completo (cenário integrado)
def test_full_flow(service):
    service.reserve_court(10, 1)
    service.join_waitlist(40, 1)

    service.release_court(10, 1)
    
    service.court_repository.mark_available(1) 

    assert service.reserve_court(40, 1) is True


