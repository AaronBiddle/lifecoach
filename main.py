from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class PatternEntry:
    """Represents a single journal entry or reflection associated with a pattern."""
    timestamp: str  # Could use datetime objects, but strings are simpler for now
    content: str
    intensity: int  # Intensity rating for this specific entry


@dataclass
class ActivePattern:
    """Represents a pattern a user is actively working with."""
    title: str  # User-defined title (e.g., "The Tuesday Afternoon Restlessness")
    created_at: str  # Timestamp when the pattern was first recorded
    frequency: int = 0  # How many times the pattern has been logged
    entries: List[PatternEntry] = field(default_factory=list)
    intensity_over_time: Dict[str, int] = field(default_factory=dict)
    # A history of intensity ratings over time
    # Key: timestamp string, Value: intensity (int)


# --- Functions to interact with the data model ---

def add_pattern(title: str, created_at: str) -> ActivePattern:
    """Creates a new ActivePattern."""
    return ActivePattern(title=title, created_at=created_at)


def get_pattern(title: str, patterns: List[ActivePattern]) -> Optional[ActivePattern]:
    """Retrieves a pattern by its title."""
    for pattern in patterns:
        if pattern.title == title:
            return pattern
    return None


def add_entry_to_pattern(pattern: ActivePattern, timestamp: str, content: str, intensity: int = 0):
    """Adds a new entry to a pattern and updates frequency/intensity."""
    pattern.entries.append(PatternEntry(timestamp=timestamp, content=content, intensity=intensity))
    pattern.frequency += 1
    pattern.intensity_over_time[timestamp.split(" ")[0]] = intensity  # Use date part only


def update_pattern_title(pattern: ActivePattern, new_title: str):
    """Updates the title of a pattern."""
    pattern.title = new_title


def get_all_patterns() -> List[ActivePattern]:
    """Retrieves all patterns.  (Currently uses an in-memory list.)"""
    # In a real app, this would fetch from a database or file.
    # For now, we'll assume patterns are stored in a list called 'all_patterns'
    global all_patterns
    return all_patterns


# --- Example Usage and Initialization ---
all_patterns: List[ActivePattern] = [] # Initialize an empty list to hold patterns

# Example: Adding a pattern
new_pattern = add_pattern(title="The Sunday Evening Blues", created_at="2024-02-20")
all_patterns.append(new_pattern)

# Example: Adding an entry
add_entry_to_pattern(new_pattern, "2024-02-25 18:00", "Felt down and anxious thinking about the week ahead.", 3)

# Example: Retrieving all patterns and printing the new one
patterns = get_all_patterns()
for pattern in patterns:
    print(pattern)
