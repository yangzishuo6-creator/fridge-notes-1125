# Write one UTF-8 fridge note within the contest's 200-character limit.
import os
from pathlib import Path

TEXT = "Leftovers labeled 'Tuesday.' I've added a year field."


def main() -> None:
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
