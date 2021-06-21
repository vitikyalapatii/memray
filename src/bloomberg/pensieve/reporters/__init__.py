from typing import TextIO

from bloomberg.pensieve import Metadata

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore


class BaseReporter(Protocol):
    def render(
        self,
        outfile: TextIO,
        metadata: Metadata,
        show_memory_leaks: bool,
    ) -> None:
        ...
