# CTF Challenge Specification: Follow the Metadata

## Challenge information

| Field | Value |
|---|---|
| Title | Follow the Metadata |
| Category | Forensics |
| Subcategory | File Signature & Metadata |
| Difficulty | Easy |
| Suggested points | 100 (adjust to the event's scoring model) |
| Attachment | `evidence.jpg` |
| Flag format | `FLAG{...}` |
| Author | Challenge Team / Panitia |
| Dynamic flag | No |
| Tags | PNG, XMP, Metadata, Hexadecimal |

## Participant-facing description (English)

An image recovered from an unknown device was catalogued as a JPEG.

The file appears ordinary at first glance, but its label may not tell the whole story. Examine the evidence and recover the flag.

**Flag format:** `FLAG{...}`

## Deskripsi untuk peserta (Bahasa Indonesia)

Sebuah gambar yang ditemukan dari perangkat tak dikenal tercatat sebagai file JPEG.

Sekilas, file tersebut tampak biasa saja. Namun, nama file belum tentu menceritakan keseluruhan isi bukti. Periksa file tersebut dan temukan flag yang tersembunyi.

**Format flag:** `FLAG{...}`

## Hints (intentionally subtle)

1. **A filename is a claim, not proof.**
2. **The visible pixels are not the whole file.**

Do not publish the solution, fragment values, or final flag in participant-facing fields.

## Flag (organizer only)

`FLAG{metadata_tells_a_story}`

## Intended learning objectives

- Distinguish a file's extension from its actual format.
- Verify a PNG signature using magic bytes.
- Inspect embedded XMP metadata.
- Recognize hexadecimal text and decode it.
- Reassemble ordered fragments into a complete flag.

## Expected solve path

1. Run `file evidence.jpg` and identify the actual format as PNG.
2. Optionally verify the PNG signature with `xxd -l 8 evidence.jpg`.
3. Inspect metadata using `exiftool -a -G1 -s evidence.jpg`.
4. Find three numbered hexadecimal fragments in XMP Dublin Core fields: Creator, Title, and Description.
5. Decode each fragment from hex, preserve the `01`, `02`, `03` order, and concatenate the decoded text.

## Metadata layout (organizer only)

| Order | XMP field | Stored value | Decoded fragment |
|---:|---|---|---|
| 01 | `XMP-dc:Creator` | `01:464c41477b6d657461` | `FLAG{meta` |
| 02 | `XMP-dc:Title` | `02:646174615f74656c6c73` | `data_tells` |
| 03 | `XMP-dc:Description` | `03:5f615f73746f72797d` | `_a_story}` |

## Validation checklist

- [ ] Attachment is named `evidence.jpg`.
- [ ] `file evidence.jpg` identifies PNG data.
- [ ] First 8 bytes are `89 50 4E 47 0D 0A 1A 0A`.
- [ ] The image opens normally.
- [ ] ExifTool can read the three XMP Dublin Core fields.
- [ ] Decoding and concatenating fragments produces the organizer flag.
- [ ] No solution file or flag is included in the participant ZIP.

## Deployment notes

- Upload **only** `follow_the_metadata_participant.zip` (or extract and upload `evidence.jpg`) to the challenge attachment field.
- Copy the participant-facing description into the platform description field.
- Add the two hints separately if the platform supports staged hints.
- Keep `follow_the_metadata_organizer_pack.zip` private. It contains the flag and write-up.
- The suggested 100 points is a starting value, not a universal CTF standard; tune it against your event's scoring model and other challenges.
