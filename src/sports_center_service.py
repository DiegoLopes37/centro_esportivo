class SportsCenterService:
    def __init__(self, court_repository, member_repository, booking_repository, waitlist_repository):
        self.court_repository = court_repository
        self.member_repository = member_repository
        self.booking_repository = booking_repository
        self.waitlist_repository = waitlist_repository

    def reserve_court(self, member_id: int, court_id: int) -> bool:
        if not member_id or not court_id:
            raise ValueError("Member ID and court ID are required")

        if not self.member_repository.exists(member_id):
            return False

        if not self.court_repository.exists(court_id):
            return False

        if self.member_repository.is_blocked(member_id):
            return False

        if self.member_repository.has_overdue_fee(member_id):
            return False

        if not self.court_repository.is_available(court_id):
            return False

        if self.booking_repository.count_active_bookings(member_id) >= 2:
            return False

        next_member = self.waitlist_repository.next_member(court_id)
        if next_member is not None and next_member != member_id:
            return False

        self.court_repository.mark_unavailable(court_id)
        self.booking_repository.create_booking(member_id, court_id)

        if self.waitlist_repository.has_waitlist(member_id, court_id):
            self.waitlist_repository.remove_from_waitlist(member_id, court_id)

        return True

    def release_court(self, member_id: int, court_id: int) -> bool:
        if not member_id or not court_id:
            raise ValueError("Member ID and court ID are required")

        if not self.booking_repository.is_court_with_member(member_id, court_id):
            return False

        self.booking_repository.close_booking(member_id, court_id)

        if not self.waitlist_repository.has_any_waitlist(court_id):
            self.court_repository.mark_available(court_id)

        return True

    def join_waitlist(self, member_id: int, court_id: int) -> bool:
        if not member_id or not court_id:
            raise ValueError("Member ID and court ID are required")

        if not self.member_repository.exists(member_id):
            return False

        if not self.court_repository.exists(court_id):
            return False

        if self.member_repository.is_blocked(member_id):
            return False

        if self.member_repository.has_overdue_fee(member_id):
            return False

        if self.court_repository.is_available(court_id):
            return False

        if self.waitlist_repository.has_waitlist(member_id, court_id):
            return False

        if self.booking_repository.is_court_with_member(member_id, court_id):
            return False

        self.waitlist_repository.add_to_waitlist(member_id, court_id)
        return True
