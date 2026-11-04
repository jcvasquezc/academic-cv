import glob, re

files = glob.glob("content/publications/**/*.md", recursive=True) + \
        glob.glob("content/publication/**/*.md", recursive=True)

updated = 0
for path in set(files):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    # Skip files that are already migrated
    if re.search(r"(?m)^publication:\s*\n\s+name:", raw):
        continue
    if not re.search(r"(?m)^publication:", raw):
        continue

    has_crlf = "\r\n" in raw
    text = raw.replace("\r\n", "\n")
    orig = text

    # Case 1: YAML block scalars (publication: >- or publication: |)
    block_match = re.search(r"(?m)^publication:\s*([>|][+-]?)\s*\n((?:[ \t]+[^\n]*\n?)+)", text)
    if block_match:
        scalar = block_match.group(1)
        body = block_match.group(2)
        indented = "\n".join("  " + line if line.strip() else line for line in body.rstrip().split("\n"))
        replacement = f"publication:\n  name: {scalar}\n{indented}\n"
        text = text[:block_match.start()] + replacement + text[block_match.end():]
    else:
        # Case 2: Quoted strings (including multiline strings)
        quote_match = re.search(r"(?m)^publication:\s*(?:\"([^\"]*)\"|\x27([^\x27]*)\x27)\s*$", text)
        if quote_match:
            val = quote_match.group(1) if quote_match.group(1) is not None else quote_match.group(2)
            # Clean up linebreaks and escaped whitespace inside wrapped quotes
            clean_val = " ".join(val.split())
            clean_val = clean_val.replace("\"", "\\\"")
            replacement = f"publication:\n  name: \"{clean_val}\""
            text = text[:quote_match.start()] + replacement + text[quote_match.end():]
        else:
            # Case 3: Flat unquoted single-line strings
            text = re.sub(r"(?m)^publication:\s*([^\s\"\'{|>][^\n]*)$", r"publication:\n  name: \"\1\"", text)

    if has_crlf:
        text = text.replace("\n", "\r\n")

    if text != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        updated += 1

print(f"Successfully migrated {updated} publication files.")