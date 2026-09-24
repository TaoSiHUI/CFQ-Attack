"""Show the main components of CFQ-Attack."""

from __future__ import annotations

import argparse

from . import METHOD_NAME, STAGES


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--show-stages", action="store_true")
    args = parser.parse_args()

    print(METHOD_NAME)
    if args.show_stages:
        for index, stage in enumerate(STAGES, start=1):
            print(f"{index}. {stage}")


if __name__ == "__main__":
    main()

