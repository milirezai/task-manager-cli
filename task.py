from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str
    status: str
    created_at: str = None
    updated_at: str = None
    