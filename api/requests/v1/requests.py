from dataclasses import dataclass

@dataclass
class Request:
    id: str
    data: str
    created_at: str

@dataclass
class RequestList:
    pass  # Empty message

@dataclass
class RequestStatus:
    id: str
    status: str

@dataclass
class Empty:
    pass  # Empty message
