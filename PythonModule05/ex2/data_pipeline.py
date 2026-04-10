#!/usr/bin/env python3
"""Complete data pipeline with stream routing and export plugins."""

from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    """Common processor interface used by the stream router."""

    def __init__(self) -> None:
        self._data: list[str] = []
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
        value = self._data.pop(0)
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


class ExportPlugin(Protocol):
    """Duck-typed export plugin contract used by the output pipeline."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Consume output tuples and export in a plugin-specific format."""


class CSVExportPlugin:
    """Simple CSV exporter using manual string generation."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [self._csv_escape(value) for _, value in data]
        print("CSV Output:")
        print(",".join(values))

    @staticmethod
    def _csv_escape(value: str) -> str:
        if any(char in value for char in [",", '"', "\n"]):
            escaped = value.replace('"', '""')
            return f'"{escaped}"'
        return value


class JSONExportPlugin:
    """Simple JSON exporter using manual string generation."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        entries: list[str] = []
        for rank, value in data:
            key = self._json_escape(f"item_{rank}")
            safe_value = self._json_escape(value)
            entries.append(f'"{key}": "{safe_value}"')
        print("JSON Output:")
        print("{" + ", ".join(entries) + "}")

    @staticmethod
    def _json_escape(value: str) -> str:
        escaped = value.replace("\\", "\\\\")
        escaped = escaped.replace('"', '\\"')
        escaped = escaped.replace("\n", "\\n")
        escaped = escaped.replace("\t", "\\t")
        return escaped


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Extract up to nb outputs per processor and send them to plugin."""
        for proc in self._processors:
            payload: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.pending_count() == 0:
                    break
                payload.append(proc.output())
            if payload:
                plugin.process_output(payload)

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
        consumed += 1


def main() -> None:
    """Demonstrate complete pipeline: stream routing then plugin exports."""
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")

    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    first_batch: list[Any] = [
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

    print(f"Send first batch of data on stream: {first_batch}\n")
    stream.process_stream(first_batch)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    print()
    stream.print_processors_stats()

    second_batch: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"\nSend another batch of data: {second_batch}\n")
    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
