from enum import Enum


class UserRole(str, Enum):
    RESEARCHER = "researcher"
    ORGANIZER = "organizer"
    ADMIN = "admin"
