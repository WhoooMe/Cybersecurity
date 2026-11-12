# CTF Challenge Specification: Follow the Metadata

## Challenge information

| Field | Value |
|---|---|
| Title | Follow the Metadata |
| Category | Forensics |
| Subcategory | File Signature & Metadata |
| Difficulty | Easy |
| Attachment | `evidence.png` |
| Flag format | `TecFest26{...}` |
| Dynamic flag | No |
| Tags | PNG, XMP, Metadata, Hexadecimal |

## Participant-facing description (English)

An image recovered from an unknown device was catalogued as a JPEG.

The file appears ordinary at first glance, but its label may not tell the whole story. Examine the evidence and recover the flag.

**Flag format:** `TecFest26{...}`

## Deskripsi untuk peserta (Bahasa Indonesia)

Sebuah gambar yang ditemukan dari perangkat tak dikenal tercatat sebagai file JPEG.

Sekilas, file tersebut tampak biasa saja. Namun, nama file belum tentu menceritakan keseluruhan isi bukti. Periksa file tersebut dan temukan flag yang tersembunyi.

**Format flag:** `TecFest26{...}`

## Hints

1. **A filename is a claim, not proof.**
2. **The visible pixels are not the whole file.**

Do not publish the solution, fragment values, or final flag in participant-facing fields.

## Flag

`TecFest26{metadata_tells_a_story}`

## Intended learning objectives

- Distinguish a file's extension from its actual format.
- Verify a PNG signature using magic bytes.
- Inspect embedded XMP metadata.
- Recognize hexadecimal text and decode it.
- Reassemble ordered fragments into a complete flag.

## Expected solve path

1. Run `file evidence.png` and identify the actual format as PNG.
2. Optionally verify the PNG signature with `xxd -l 8 evidence.jpg`.
3. Inspect metadata using `exiftool -a -G1 -s evidence.png`.
4. Find three numbered hexadecimal fragments in XMP Dublin Core fields: Creator, Title, and Description.
5. Decode each fragment from hex and concatenate the decoded text.

## Metadata layout (Admin only)

| Order | XMP field | Stored value | Decoded fragment |
|---:|---|---|---|
| 01 | `XMP-dc:Creator` | `5465634665737432367b6d657461` | `TecFest26{meta_` |
| 02 | `XMP-dc:Title` | `646174615f74656c6c73` | `data_tells` |
| 03 | `XMP-dc:Description` | `5f615f73746f72797d` | `_a_story}` |
