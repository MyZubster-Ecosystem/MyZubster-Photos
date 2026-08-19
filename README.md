# MyZubster Photos

> 🌍 **Understand MyZubster in your language:** [Global multilingual guide](https://github.com/MyZubster-Ecosystem/myzubster/blob/main/docs/i18n/README.md) — English, Italiano, Español, Français, Deutsch, Português, 中文, 日本語, 한국어, العربية, हिन्दी, Русский, Türkçe, Bahasa Indonesia, Polski, Українська, বাংলা, اردو, فارسی, Kiswahili.
>
> **MyZubster is an open-source ecosystem that connects real-world observations, verifiable evidence, collaborative bounties and platform rewards.** MYZ is currently an internal reward/accounting ledger; external XMR/token/blockchain settlement is separate and independently verified.

**Canonical public photographic evidence repository for the MyZubster ecosystem.**

These are not just pictures.

A MyZubster photo can be a verifiable evidence artifact connected to a real-world observation, public dataset, authorized research activity, contributor task or bounty deliverable. Its meaning comes from the combination of the image, metadata, cryptographic hash, provenance, review and — when applicable — reward and settlement records.

```text
REAL-WORLD PHOTO / OBSERVATION
            ↓
      SANITIZED FILE
            ↓
 SHA-256 + METADATA + PROVENANCE
            ↓
 OBSERVATION / BOUNTY / DELIVERABLE
            ↓
   REVIEW AGAINST ACCEPTANCE RULES
            ↓
         VERIFIED
            ↓
    REWARD_RECORDED (MYZ)
            ↓
     MYZ INTERNAL LEDGER
            ↓
 OPTIONAL EXTERNAL SETTLEMENT
      XMR / TOKEN / CHAIN
            ↓
  INDEPENDENT VERIFICATION
            ↓
       PAID / SETTLED
```

> **Core rule:** a photo can be evidence of work, but the presence of a photo in this repository does not automatically prove bounty verification, reward assignment or blockchain payment.

---

## 1. What a MyZubster photo can represent

A public photo may be:

- a real-world observation;
- authorized photographic evidence;
- part of a geographic or environmental dataset;
- a bounty deliverable;
- an artifact identified by a cryptographic hash;
- a source for maps, timelines, galleries or registries;
- a Git/GitHub provenance record;
- content that may also be addressed through IPFS/CID;
- evidence linked to a later verified bounty;
- evidence linked to a reward recorded in the MYZ internal ledger;
- when independently verified, evidence associated with an external XMR/token/blockchain settlement.

The image is the visible content. Verification value comes from the **image + metadata + hash + provenance + acceptance criteria + review**.

---

## 2. Canonical repository

```text
MyZubster-Ecosystem/MyZubster-Photos
```

Public real-world photographs are centralized here instead of being duplicated throughout application repositories.

The MyZubster core may store:

- observation records;
- media references;
- authorized coordinates;
- observation state;
- bounty references;
- reward references;
- settlement references when applicable.

The canonical public photographic file belongs in this repository.

---

## 3. Repository structure

```text
MyZubster-Photos/
├── photos/
│   ├── plants/
│   ├── gardens/
│   ├── urban/
│   ├── nature/
│   ├── heritage/
│   ├── robots/
│   ├── observations/
│   ├── bounties/
│   └── italy/
│       └── emilia-romagna/
│           └── rimini/
├── processed/
│   ├── thumbnails/
│   └── web/
├── metadata/
│   ├── photo-catalog.json
│   ├── github-core-migration.json
│   ├── photos.json
│   └── skipped.json
├── docs/
│   └── PHOTO-POLICY.md
└── scripts/
```

Geographic paths are used only when the location is appropriate for public disclosure.

---

## 4. Metadata model

A photo without context is only a binary file. A MyZubster evidence record can explain what the file represents, where it came from, which exact bytes were reviewed and what workflow it belongs to.

Possible fields include:

| Field | Meaning |
|---|---|
| `photoId` / `observationId` | stable evidence identifier |
| `filename` | canonical filename |
| `destinationPath` | canonical path in this repository |
| `sha256` | cryptographic fingerprint of the exact file |
| `sizeBytes` | verified byte size |
| `mimeType` | media type |
| `category` | observation/evidence category |
| `capturedAt` | capture date/time only when actually known |
| `publishedAt` | publication timestamp |
| `city` / `region` / `country` | publishable location metadata |
| `latitude` / `longitude` | coordinates only when authorized and appropriate |
| `source` | declared provenance |
| `repositoryCommit` | Git commit recording the artifact/state |
| `cid` | optional IPFS content identifier |
| `metadataCid` | optional CID for metadata |
| `bountyId` | linked bounty, if any |
| `evidenceStatus` | evidence lifecycle state |
| `reviewStatus` | review state |
| `rewardAsset` | MYZ/XMR/token declared by the bounty |
| `rewardAmount` | declared or recorded amount |
| `rewardRecordId` | internal MyZubster ledger reference |
| `settlementStatus` | external settlement state |
| `network` | external chain/network only when applicable |
| `txHash` | independently verified transaction identifier only when available |

Unknown values remain `null` or absent. **They must never be invented.**

---

## 5. SHA-256 and file identity

Published evidence should have a SHA-256 digest.

Example:

```json
{
  "destinationPath": "photos/italy/emilia-romagna/rimini/landmarks/fontana-della-pigna/fontana-della-pigna-001.jpg",
  "sha256": "3ef2fbae7b97524b629d7729f6260d2b3d36b17defbbfb1bebe9a43852feca3e",
  "sizeBytes": 571976
}
```

SHA-256 lets independent systems verify that they are referring to the **same exact file**. If one byte changes, the hash changes.

```text
photo
  ↔ SHA-256
  ↔ metadata
  ↔ observation record
  ↔ bounty evidence
  ↔ review
  ↔ reward record
```

A hash proves file identity. It does **not** by itself prove that a bounty was completed.

---

## 6. Privacy and sanitization

This is a public repository. Images intended for publication must be reviewed and, when necessary, re-encoded before entering the canonical archive.

Metadata may record properties such as:

```json
{
  "privacy": {
    "exifStripped": true,
    "gpsMetadataPublished": false
  }
}
```

Do not automatically publish:

- unreviewed EXIF;
- unnecessary embedded GPS;
- JWTs, tokens or credentials;
- wallet seeds or private keys;
- local filesystem paths;
- private user identifiers;
- sensitive infrastructure;
- unauthorized private/restricted locations;
- confidential review material;
- unreviewed raw uploads.

Removing EXIF/GPS does not automatically make the visible content safe. The actual image content must also be suitable for public publication.

---

## 7. Verified migration from MyZubster core

The first canonical migration moved **12 already-public photographs** from the MyZubster core into this repository as sanitized copies.

Machine-readable evidence is stored in:

```text
metadata/github-core-migration.json
```

The manifest records:

- source repository and branch;
- source path;
- destination path;
- file count;
- SHA-256 of each sanitized copy;
- file size;
- privacy state;
- source deletion state;
- core commit completing the move.

Recorded migration state includes:

```json
{
  "mode": "sanitized-copy",
  "sourceDeletion": true,
  "sourceDeletionCommit": "edd564aeede93b9049ec184e815e05da33f0497a",
  "count": 12
}
```

The MyZubster core registry now references the Photos repository and the SHA-256 hashes of the sanitized versions.

---

## 8. Photos as bounty evidence

A MyZubster bounty represents **verifiable work**.

For a photo bounty, acceptance criteria may require:

- a minimum number of photographs;
- a specific subject;
- a public/authorized area;
- minimum quality;
- a caption or description;
- allowed location precision;
- an original-file requirement;
- a timestamp when genuinely available;
- absence of sensitive information;
- compliance with privacy and safety rules.

Correct logic:

```text
bounty defined
  → contributor collects evidence
  → photo + metadata submitted
  → review against acceptance criteria
  → VERIFIED
  → reward recorded
```

Incorrect logic:

```text
photo uploaded = bounty completed = payment executed
```

---

## 9. Canonical bounty lifecycle

```text
PROPOSED
  → VALIDATED
  → APPROVED
  → FUNDED          # when funding reservation is required
  → ACTIVE
  → SUBMITTED
  → UNDER_REVIEW
  → VERIFIED | REJECTED
  → REWARD_RECORDED
  → SETTLEMENT_PENDING | SETTLED / PAID
```

A photo can become evidence at `SUBMITTED`. `VERIFIED` requires an actual review against the bounty's acceptance criteria.

A GitHub merge, a closed issue or a file in this repository does not replace verification.

Canonical policy: [MyZubster Bounty System](https://github.com/MyZubster-Ecosystem/myzubster/blob/main/BOUNTIES.md).

---

## 10. MYZ and bounty completion

### Current MYZ model

**MYZ is currently an internal reward/accounting ledger unit in the MyZubster platform.**

After a bounty is verified, an internal reward record may look like:

```json
{
  "bountyId": "photo-bounty-123",
  "evidenceId": "rimini-fontana-della-pigna-001",
  "rewardType": "photo_bounty",
  "amount": 500,
  "currency": "MYZ",
  "status": "approved"
}
```

This means the reward was recorded in MyZubster's internal accounting/reward ledger.

It does **not** automatically mean a public blockchain transaction occurred.

```text
photoId
  ├─ sha256
  ├─ metadata
  ├─ observationId
  └─ bountyId
        ↓
     VERIFIED
        ↓
  rewardRecordId
        ↓
     amount MYZ
        ↓
 MyZubster internal ledger
```

This creates an auditable application-level chain between evidence and reward.

---

## 11. Blockchain and external settlement

MYZ and an external blockchain are different layers.

```text
MYZ = internal-platform-ledger
```

A MYZ reward must not be described as `on-chain` unless independent chain evidence actually exists.

A bounty may separately include XMR or a blockchain token. In that case, settlement metadata may include:

```json
{
  "bountyId": "photo-bounty-123",
  "rewardRecordId": "reward-456",
  "asset": "TOKEN_OR_XMR",
  "network": "verified-network",
  "amount": "canonical-amount",
  "destination": "public-destination-address",
  "txHash": "verified-transaction-id",
  "status": "CONFIRMED"
}
```

Before declaring `PAID` or `SETTLED`, independent verification should confirm, where applicable:

- intended recipient;
- correct asset;
- correct network/chain;
- token contract/asset identity;
- canonical amount;
- transaction identifier;
- transaction status;
- required confirmations.

A `txHash` must never be invented.

---

## 12. External settlement lifecycle

```text
PENDING
  → RESERVED / ACCEPTED
  → SUBMITTED
  → CONFIRMED
  → PAID
```

Exception/reconciliation states can include:

```text
FAILED
UNSETTLED
DISPUTED
CANCELLED
```

A valid state can therefore be:

```text
Bounty: VERIFIED
MYZ reward: REWARD_RECORDED
External settlement: PENDING
```

The work is verified and the internal reward recorded, while external payment is still awaiting confirmation.

---

## 13. Git, SHA-256, IPFS, MYZ and blockchain are different layers

### Git / GitHub

Provides change history, commits, reviews, pull requests and repository provenance.

### SHA-256

Identifies the exact file bytes.

### IPFS / CID

When used, content-addresses a specific object. A CID identifies content; it does not prove bounty acceptance.

### MYZ ledger

Records internal platform reward/accounting state.

### External blockchain/payment rail

When actually used, records settlement on a specific external network and requires independent verification.

These layers can reference each other, but one does not automatically prove the others.

---

## 14. Example extended evidence record

```json
{
  "schemaVersion": "1.0.0",
  "photoId": "rimini-example-001",
  "observationId": "rimini-example-001",
  "path": "photos/italy/emilia-romagna/rimini/example/example-001.jpg",
  "sha256": "...",
  "sizeBytes": 123456,
  "privacy": {
    "exifStripped": true,
    "gpsMetadataPublished": false
  },
  "provenance": {
    "repository": "MyZubster-Ecosystem/MyZubster-Photos",
    "commit": "..."
  },
  "bounty": {
    "bountyId": null,
    "evidenceStatus": "PUBLISHED",
    "reviewStatus": null
  },
  "reward": {
    "rewardRecordId": null,
    "asset": null,
    "amount": null,
    "myzModel": "internal-platform-ledger"
  },
  "settlement": {
    "status": null,
    "network": null,
    "txHash": null
  }
}
```

Null means unknown/not applicable — not failed, paid or verified.

---

## 15. What this repository proves — and what it does not

### It can prove or support

- that a specific public file exists in Git history;
- its canonical repository path;
- its SHA-256 identity;
- its machine-readable metadata;
- recorded migration/provenance facts;
- that it has been published as potential evidence;
- linkage to a bounty/reward/settlement record when such references exist.

### It does not automatically prove

- authorship of the real-world scene;
- exact capture time when not independently available;
- exact GPS location when not verified;
- bounty acceptance;
- MYZ reward approval;
- external payment;
- blockchain settlement.

Those require their own evidence and lifecycle states.

---

## 16. Safety rules for physical/photo bounties

MyZubster photo work must not require or reward:

- trespassing;
- entry into restricted/private areas;
- bypassing barriers or access controls;
- photographing sensitive security systems or operational infrastructure;
- unsafe intervention on machinery/utilities;
- confidential research collection;
- unnecessary disclosure of private residences or sensitive locations;
- publication of wallet secrets, credentials or personal data.

Public and authorized observation from safe locations is the default.

---

## 17. Machine-readable sources

Important files include:

- [`metadata/photo-catalog.json`](metadata/photo-catalog.json) — repository category/publication policy catalog;
- [`metadata/github-core-migration.json`](metadata/github-core-migration.json) — verified migration/provenance manifest;
- [`docs/PHOTO-POLICY.md`](docs/PHOTO-POLICY.md) — photo publication and privacy policy;
- [core `data/observations.json`](https://github.com/MyZubster-Ecosystem/myzubster/blob/main/data/observations.json) — public observation records;
- [canonical `BOUNTIES.md`](https://github.com/MyZubster-Ecosystem/myzubster/blob/main/BOUNTIES.md) — authoritative bounty and settlement rules;
- [ecosystem architecture](https://github.com/MyZubster-Ecosystem/myzubster/blob/main/docs/ECOSYSTEM.md) — repository boundaries and responsibilities.

---

## 18. Project status and transparency

MyZubster is an evolving open-source ecosystem. Documentation must distinguish:

- operational functionality;
- development/validation;
- prototypes and simulation;
- planned features;
- internal MYZ accounting;
- independently verified external settlement.

Historical issues, labels, reward amounts, commits or screenshots are project evidence/context, but are not automatic proof of deployment, funding or payment.

---

## 19. Contributing translations

The global guide is maintained here:

**[MyZubster Universal / Multilingual Guide](https://github.com/MyZubster-Ecosystem/myzubster/blob/main/docs/i18n/README.md)**

Human translations are welcome. Every translation must preserve the same technical truth, especially:

1. evidence is not automatic bounty verification;
2. MYZ is currently an internal reward/accounting ledger;
3. MYZ is not automatically an on-chain transfer;
4. external settlement is separate;
5. `PAID`/`SETTLED` requires independent verification;
6. privacy, authorization and safety remain mandatory.

If a language is not yet listed, browser translation can be used as an accessibility fallback until a reviewed human translation is contributed.
