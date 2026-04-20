class WaitlistRepository:
    def __init__(self):
        self._waitlist = []

    def add_to_waitlist(self, member_id: int, court_id: int) -> None:
        self._waitlist.append({"member_id": member_id, "court_id": court_id})

    def has_waitlist(self, member_id: int, court_id: int) -> bool:
        return any(
            entry["member_id"] == member_id and entry["court_id"] == court_id
            for entry in self._waitlist
        )

    def has_any_waitlist(self, court_id: int) -> bool:
        return any(entry["court_id"] == court_id for entry in self._waitlist)

    def next_member(self, court_id: int):
        for entry in self._waitlist:
            if entry["court_id"] == court_id:
                return entry["member_id"]
        return None

    def remove_from_waitlist(self, member_id: int, court_id: int) -> None:
        for entry in list(self._waitlist):
            if entry["member_id"] == member_id and entry["court_id"] == court_id:
                self._waitlist.remove(entry)
                return
        raise ValueError("Waitlist entry not found")
