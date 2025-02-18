from enum import Enum


class WordLevel(str, Enum):
    BEGINNER = "A1"
    ELEMENTARY = "A2"
    INTERMEDIATE = "B1"
    UPPER_INTERMEDIATE = "B2"
    ADVANCED = "C1"
    PROFICIENT = "C2"


class DownloadStatus(str, Enum):
    PENDING = "pending"
    DOWNLOADED = "downloaded"
    FAILED = "failed"
