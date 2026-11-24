"""Write one code review comment that approves a pull request with
quiet existential dread, for bounty
u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018.

The line approves in earnest first: clean diff, green tests, merging.
The dread comes from the code itself, stated flatly — one day this
very diff will be legacy code that outlives us all. The reviewer is
not scared of the code; the code will simply still be here when we
are not, and the approval goes through anyway. No exclamation marks,
no melodrama, no cry for help; just a tired engineer noting that
today's careful work becomes tomorrow's immortal fossil, and merging.

Gate guard: the entry must be UTF-8 text of 1 to 140 characters, a
single line, and not only white space - the same gate the sealed
scorer applies to /output/entry.txt. Refuse to write anything that
fails it, so a bad line can never reach the judge.
"""

from pathlib import Path

ENTRY = (
    "LGTM. Clean diff, green tests, and one day this will be legacy "
    "code that outlives us all. Merging."
)

MIN_CHARS = 1
MAX_CHARS = 140


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 and ch not in ("\n", "\r") for ch in text):
        raise SystemExit("entry must not contain control characters")
    if text != text.strip():
        raise SystemExit("entry must not have leading or trailing space")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
