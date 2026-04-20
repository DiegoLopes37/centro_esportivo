class CourtRepository:
    def __init__(self):
        self._courts = {
            1: {"name": "Quadra Azul", "available": True},
            2: {"name": "Quadra Verde", "available": True},
            3: {"name": "Quadra Vermelha", "available": False},
        }

    def exists(self, court_id: int) -> bool:
        return court_id in self._courts

    def is_available(self, court_id: int) -> bool:
        if court_id not in self._courts:
            return False
        return self._courts[court_id]["available"]

    def mark_unavailable(self, court_id: int) -> None:
        if court_id not in self._courts:
            raise ValueError("Court not found")
        self._courts[court_id]["available"] = False

    def mark_available(self, court_id: int) -> None:
        if court_id not in self._courts:
            raise ValueError("Court not found")
        self._courts[court_id]["available"] = True
