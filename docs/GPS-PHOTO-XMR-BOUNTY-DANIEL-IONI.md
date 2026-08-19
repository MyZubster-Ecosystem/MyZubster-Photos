# Daniel Ioni — GPS Photo Metadata XMR Bounty Roadmap

## Purpose

Create a verifiable photographic discovery trail for Daniel Ioni using MyZubster: public-safe photos, structured metadata, controlled GPS/location evidence, cryptographic integrity and an auditable XMR settlement path.

This roadmap is a **bounty specification**, not proof of payment.

## Core principle

```text
REAL-WORLD DISCOVERY
        ↓
PHOTO / EVIDENCE
        ↓
PRIVACY REVIEW
        ↓
PUBLIC-SAFE GPS / LOCATION METADATA
        ↓
SHA-256 + CANONICAL METADATA
        ↓
MYZUBSTER OBSERVATION / STORY / BOUNTY LINK
        ↓
MANUAL REVIEW
        ↓
VERIFIED
        ↓
XMR SETTLEMENT_PENDING
        ↓
TRANSACTION SUBMITTED
        ↓
INDEPENDENT MONERO VERIFICATION
        ↓
PAID / SETTLED
```

## Beneficiary / contributor

- Contributor: **Daniel Ioni**
- GitHub identity used for project work: `DanielIoni-creator`
- Reward asset: **XMR**
- Reward amount: **TBD before approval/funding**
- Current bounty state: **PROPOSED**
- Review mode: **manual**
- Evidence required: **yes**

No wallet address is stored in this document. A destination address should be collected only when settlement is authorized and should never include wallet secrets.

## Roadmap milestones

### Milestone 1 — Metadata foundation — 15% of approved XMR pool

Deliverables:

- stable `photoId` / `observationId` scheme;
- metadata schema for filename, MIME, bytes, SHA-256, publication date and source;
- location policy with privacy modes;
- validation rules for required/optional fields.

Acceptance:

- schema is machine-readable;
- unknown values remain `null`/absent rather than invented;
- no private identifiers or secrets in public metadata.

### Milestone 2 — GPS/location evidence — 20%

Deliverables:

- location metadata for eligible photographs;
- explicit `location.mode` (`none`, `city`, `approximate`, `exact-public`);
- coordinates only where appropriate and authorized;
- public place label/city/region/country where available.

Acceptance:

- no raw EXIF GPS is blindly published;
- sensitive/private/restricted locations are excluded or reduced in precision;
- exact coordinates require explicit public-safety approval.

### Milestone 3 — Photo integrity and provenance — 20%

Deliverables:

- SHA-256 for each canonical published photo;
- source/destination path provenance;
- Git commit reference;
- optional IPFS CID when publication occurs;
- privacy/sanitization status.

Acceptance:

- hashes match the exact published files;
- originals are not rewritten merely to satisfy metadata requirements unless the publication pipeline explicitly creates a sanitized derivative;
- provenance is reproducible.

### Milestone 4 — Discovery/story linking — 20%

Deliverables:

- link eligible photos to Daniel's MyZubster discoveries, observations, bounty records or cyberpunk-story artifacts;
- metadata fields such as `storyId`, `episodeId`, `bountyId` or `discoveryId` only when the referenced record actually exists;
- human-readable captions/context.

Acceptance:

- real evidence and fictional cyberpunk narrative are clearly distinguished;
- no invented bounty, reward, chain or transaction identifiers.

### Milestone 5 — Public index and QA — 15%

Deliverables:

- machine-readable public index;
- human-readable summary/README linkage;
- privacy QA;
- integrity QA;
- duplicate/error report.

Acceptance:

- records are internally consistent;
- every public photo has required integrity fields;
- sensitive evidence remains excluded;
- skipped/rejected items are documented without leaking sensitive data.

### Milestone 6 — Final verification and XMR settlement readiness — 10%

Deliverables:

- reviewer confirms all acceptance criteria;
- bounty moves to `VERIFIED`;
- approved XMR amount and funding state are recorded;
- settlement record prepared with expected recipient and canonical XMR amount.

Settlement can proceed only after funding is explicitly confirmed.

## XMR settlement contract

External settlement lifecycle:

```text
PENDING
 -> RESERVED / ACCEPTED
 -> SUBMITTED
 -> CONFIRMED
 -> PAID
```

A transaction may be marked `PAID` only after independent verification appropriate to Monero confirms the expected settlement data. A GitHub merge, application record, wallet RPC response or transaction-submission response is not sufficient by itself.

The settlement record should contain, where safely appropriate:

```json
{
  "asset": "XMR",
  "amount": "<approved canonical amount>",
  "recipientRef": "<settlement recipient reference>",
  "txId": "<verified transaction id after submission>",
  "status": "CONFIRMED"
}
```

No `txId` may be invented or pre-populated.

## Public metadata model

Example:

```json
{
  "schemaVersion": "1.0.0",
  "photoId": "daniel-rimini-001",
  "creatorAlias": "Daniel Ioni",
  "path": "photos/.../image.jpg",
  "mimeType": "image/jpeg",
  "sizeBytes": 123456,
  "sha256": "...",
  "publishedAt": "...",
  "location": {
    "mode": "approximate",
    "city": "Rimini",
    "region": "Emilia-Romagna",
    "country": "Italy",
    "latitude": null,
    "longitude": null,
    "precisionMeters": null
  },
  "privacy": {
    "exifStripped": true,
    "gpsMetadataPublished": false,
    "humanReviewRequired": true
  },
  "links": {
    "observationId": null,
    "discoveryId": null,
    "storyId": null,
    "episodeId": null,
    "bountyId": null,
    "cid": null,
    "gitCommit": null
  },
  "verification": {
    "status": "SUBMITTED",
    "reviewMode": "manual"
  },
  "settlement": {
    "asset": "XMR",
    "amount": null,
    "status": "PENDING",
    "txId": null
  }
}
```

## Privacy and GPS rules

Do not publish exact coordinates for:

- private homes;
- minors/vulnerable people;
- protected wildlife or sensitive ecological sites;
- security systems or critical infrastructure;
- restricted/private property;
- confidential research or bounty locations;
- any location where precision creates a reasonable safety risk.

The public metadata record is intentionally separate from raw EXIF. A photo may be sanitized while its approved public location is recorded separately at a safe precision.

## Bounty state

At creation this roadmap is:

```text
status: PROPOSED
asset: XMR
amount: TBD
funding: NOT CONFIRMED
settlement: NOT STARTED
```

Do not represent this bounty as funded, verified or paid until the corresponding evidence exists.

## Canonical references

- MyZubster bounty contract: https://github.com/MyZubster-Ecosystem/myzubster/blob/main/BOUNTIES.md
- Photo publication policy: `PHOTO-POLICY.md`
- Repository bounty policy: `../BOUNTIES.md`
