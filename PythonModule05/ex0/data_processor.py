#!/usr/bin/env python3
"""ABC architecture for specialized data processors."""

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class that defines the common processing interface."""

    def __init__(self) -> None:
        """Initialize internal queue and extraction rank state."""
        self._data: list[str] = []
        self._output_count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Return True if the provided data can be ingested by processor."""

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Ingest valid data and store it in normalized string form."""

    def output(self) -> tuple[int, str]:
        """Extract oldest stored item with its extraction rank."""
        if not self._data:
            raise ValueError("No data to extract from processor")
        data_value = self._data.pop(0)
        rank = self._output_count
        self._output_count += 1
        return rank, data_value


class NumericProcessor(DataProcessor):
    """Processor for int, float, and lists of numeric values."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._data.append(str(item))
            return
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    """Processor for str and lists of strings."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._data.append(item)
            return
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):
    """Processor for log dicts and lists of log dicts."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items()
                )
                for item in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for log_dict in data:
                self._data.append(self._format_log(log_dict))
        else:
            self._data.append(self._format_log(data))

    def _format_log(self, log_dict: dict[str, str]) -> str:
        """Format a log dictionary into a single display string."""
        level = log_dict.get("log_level", "UNKNOWN")
        message = log_dict.get("log_message", "")
        return f"{level}: {message}"


def main() -> None:
    """Demonstrate processor validation, ingestion and output extraction."""
    print("=== Code Nexus - Data Processor ===\n")
    # Test NumericProcessor
    print("Testing Numeric Processor...")
    num_processor = NumericProcessor()
    print(f"Trying to validate input '42': {num_processor.validate(42)}")
    print(
        "Trying to validate input 'Hello': "
        f"{num_processor.validate('Hello')}"
    )
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_processor.ingest("foo")  # type: ignore
    except ValueError as e:
        print(f"Got exception: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    num_processor.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        rank, value = num_processor.output()
        print(f"Numeric value {i}: {value}")

    # Test TextProcessor
    print("\nTesting Text Processor...")
    text_processor = TextProcessor()
    print(f"Trying to validate input '42': {text_processor.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text_processor.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    rank, value = text_processor.output()
    print(f"Text value {rank}: {value}")
    # Test LogProcessor
    print("\nTesting Log Processor...")
    log_processor = LogProcessor()
    print(
        "Trying to validate input 'Hello': "
        f"{log_processor.validate('Hello')}"
    )
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    log_processor.ingest(log_data)
    print("Extracting 2 values...")
    for i in range(2):
        rank, value = log_processor.output()
        print(f"Log entry {i}: {value}")


if __name__ == "__main__":
    main()
