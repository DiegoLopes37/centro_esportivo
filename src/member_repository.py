class MemberRepository:
    def __init__(self):
        self._members = {
            10: {"name": "Ana", "blocked": False, "overdue_fee": False},
            20: {"name": "Bruno", "blocked": True, "overdue_fee": False},
            30: {"name": "Carla", "blocked": False, "overdue_fee": True},
            40: {"name": "Diego", "blocked": False, "overdue_fee": False},
        }

    def exists(self, member_id: int) -> bool:
        return member_id in self._members

    def is_blocked(self, member_id: int) -> bool:
        if member_id not in self._members:
            return False
        return self._members[member_id]["blocked"]

    def has_overdue_fee(self, member_id: int) -> bool:
        if member_id not in self._members:
            return False
        return self._members[member_id]["overdue_fee"]
