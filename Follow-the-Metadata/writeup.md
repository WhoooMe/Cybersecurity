# Official Write-up: Follow the Metadata

**Category:** Forensics  
**Difficulty:** Easy  
**Flag:** `TecFest26{metadata_tells_a_story}`

## 1. Identify the real file type

The attachment is named `evidence.png`, but the extension is not authoritative.

```bash
file evidence.png
```

Expected result: a PNG image. The signature can also be checked directly:

```bash
xxd -l 8 evidence.png
```

Expected bytes:

```text
89 50 4e 47 0d 0a 1a 0a
```

## 2. Inspect the metadata

```bash
exiftool -a -G1 -s evidence.jpg
```

Look for the XMP Dublin Core fields:

```text
[XMP-dc] Creator     : 5465634665737432367b6d6574615f
[XMP-dc] Title       : 646174615f74656c6c73
[XMP-dc] Description : 5f615f73746f72797d
```

The numeric prefixes indicate the fragment order. The values after the colon are hexadecimal text.

## 3. Decode the fragments

```bash
echo -n '5465634665737432367b6d6574615f' | xxd -r -p
echo -n '646174615f74656c6c73' | xxd -r -p
echo -n '5f615f73746f72797d' | xxd -r -p
```

Outputs:

```text
TecFest26{meta_
data_tells
_a_story}
```

## 4. Reassemble the flag

Concatenate the decoded fragments in order 01, 02, 03:

```text
TecFest26{meta_tells_a_story}
```

**Final flag:** `TecFest26{metadata_tells_a_story}`

## Alternative: decode with Python

```python
fragments = [
    "5465634665737432367b6d6574615f",
    "646174615f74656c6c73",
    "5f615f73746f72797d",
]
flag = "".join(bytes.fromhex(part).decode("utf-8") for part in fragments)
print(flag)
```
