class BookingRepository:
    def __init__(self):
        self._active_bookings = []

    def create_booking(self, member_id: int, court_id: int) -> None:
        self._active_bookings.append({"member_id": member_id, "court_id": court_id})

    def has_active_booking(self, court_id: int) -> bool:
        return any(booking["court_id"] == court_id for booking in self._active_bookings)

    def is_court_with_member(self, member_id: int, court_id: int) -> bool:
        return any(
            booking["member_id"] == member_id and booking["court_id"] == court_id
            for booking in self._active_bookings
        )

    def count_active_bookings(self, member_id: int) -> int:
        return sum(1 for booking in self._active_bookings if booking["member_id"] == member_id)

    def close_booking(self, member_id: int, court_id: int) -> None:
        for booking in list(self._active_bookings):
            if booking["member_id"] == member_id and booking["court_id"] == court_id:
                self._active_bookings.remove(booking)
                return
        raise ValueError("Active booking not found")
