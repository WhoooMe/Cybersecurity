# Official Write-up: Follow the Metadata

**Category:** Forensics  
**Difficulty:** Easy  
**Flag:** `FLAG{metadata_tells_a_story}`

## 1. Identify the real file type

The attachment is named `evidence.jpg`, but the extension is not authoritative.

```bash
file evidence.jpg
```

Expected result: a PNG image. The signature can also be checked directly:

```bash
xxd -l 8 evidence.jpg
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
[XMP-dc] Creator     : 01:464c41477b6d657461
[XMP-dc] Title       : 02:646174615f74656c6c73
[XMP-dc] Description : 03:5f615f73746f72797d
```

The numeric prefixes indicate the fragment order. The values after the colon are hexadecimal text.

## 3. Decode the fragments

```bash
echo -n '464c41477b6d657461' | xxd -r -p
echo -n '646174615f74656c6c73' | xxd -r -p
echo -n '5f615f73746f72797d' | xxd -r -p
```

Outputs:

```text
FLAG{meta
data_tells
_a_story}
```

## 4. Reassemble the flag

Concatenate the decoded fragments in order 01, 02, 03:

```text
FLAG{meta_tells_a_story}
```

**Final flag:** `FLAG{metadata_tells_a_story}`

## Alternative: decode with Python

```python
fragments = [
    "464c41477b6d657461",
    "646174615f74656c6c73",
    "5f615f73746f72797d",
]
flag = "".join(bytes.fromhex(part).decode("utf-8") for part in fragments)
print(flag)
```
