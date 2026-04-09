#!/usr/bin/env python3
"""Data stream router using abstract data processors."""

from abc import ABC, abstractmethod
from collections import deque
from typing import Any


class DataProcessor(ABC):
    """Common processor interface used by the stream router."""

    def __init__(self) -> None:
        self._data: deque[str] = deque()
        self._output_count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Return True when this processor can ingest the provided data."""

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Ingest valid data and store normalized values internally."""

    def output(self) -> tuple[int, str]:
        """Return oldest stored value with rank, then remove it."""
        if not self._data:
            raise ValueError("No data to extract from processor")
        value = self._data.popleft()
        rank = self._output_count
        self._output_count += 1
        return rank, value

    def pending_count(self) -> int:
        """Return the number of values currently waiting in this processor."""
        return len(self._data)


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
        self._data.append(data)


class LogProcessor(DataProcessor):
    """Processor for log dictionaries and lists of log dictionaries."""

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
            for item in data:
                self._data.append(self._format_log(item))
            return
        self._data.append(self._format_log(data))

    @staticmethod
    def _format_log(log_entry: dict[str, str]) -> str:
        level = log_entry.get("log_level", "UNKNOWN")
        message = log_entry.get("log_message", "")
        return f"{level}: {message}"


class DataStream:
    """Receive mixed data and route each element to a matching processor."""

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        self._totals: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        """Register a processor instance used to route stream data."""
        self._processors.append(proc)
        self._totals[proc] = 0

    def process_stream(self, stream: list[Any]) -> None:
        """Route each stream element to the first matching processor."""
        for element in stream:
            if not self._route_element(element):
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        """Display processed totals and pending values for each processor."""
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            label = proc.__class__.__name__.replace("Processor", " Processor")
            print(
                f"{label}: total {self._totals[proc]} items processed, "
                f"remaining {proc.pending_count()} on processor"
            )

    def _route_element(self, element: Any) -> bool:
        """Try to send one element to a processor. Return True when routed."""
        for proc in self._processors:
            if not proc.validate(element):
                continue
            pending_before = proc.pending_count()
            proc.ingest(element)
            pending_after = proc.pending_count()
            self._totals[proc] += pending_after - pending_before
            return True
        return False


def _consume_values(label: str, processor: DataProcessor, amount: int) -> None:
    """Consume up to amount values from processor and print each one."""
    consumed = 0
    while consumed < amount and processor.pending_count() > 0:
        rank, value = processor.output()
        print(f"{label} value {rank}: {value}")
        consumed += 1


def main() -> None:
    """Demonstrate stream processing with progressive registration."""
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    logs = LogProcessor()

    batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print("Registering Numeric Processor")
    stream.register_processor(numeric)
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Registering other data processors")
    stream.register_processor(text)
    stream.register_processor(logs)
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    _consume_values("Numeric", numeric, 3)
    _consume_values("Text", text, 2)
    _consume_values("Log", logs, 1)
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
