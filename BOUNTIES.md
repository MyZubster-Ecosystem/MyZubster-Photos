# MyZubster Photos Bounties

This repository accepts public-safe photographic evidence bounties that comply with the canonical MyZubster bounty contract:

https://github.com/MyZubster-Ecosystem/myzubster/blob/main/BOUNTIES.md

## Scope

Typical photo bounties may cover:

- public/authorized real-world observations;
- plants, gardens, heritage, urban details, nature, robots and documented discoveries;
- photographic series linked to MyZubster observations or comic/story artifacts;
- metadata and integrity records;
- privacy-safe geospatial evidence;
- optional IPFS content addressing after publication.

## GPS and privacy

Exact embedded EXIF/GPS must not be published automatically. A public bounty may require location evidence, but publication precision must be appropriate to the subject.

Recommended public location modes:

- `none` — no public coordinate;
- `city` — city/municipality only;
- `approximate` — reduced-precision coordinates;
- `exact-public` — exact coordinate only for a public, non-sensitive place where exact publication is explicitly approved.

Sensitive/private locations, homes, vulnerable people, protected wildlife, security infrastructure and restricted areas must never be exposed merely to satisfy a bounty.

## Reward truth

An image, metadata record, GitHub commit, issue closure or merge does not prove payment.

- MYZ is currently an internal platform reward/accounting ledger.
- XMR rewards are external settlement and require an independently verified Monero transaction before `PAID` or `SETTLED`.
- Funding reservation, wallet address collection and transaction submission are separate steps.
- Never publish wallet seeds, private keys or wallet passwords.

## Lifecycle

```text
PROPOSED
 -> VALIDATED
 -> APPROVED
 -> FUNDED          # required before an XMR bounty becomes active
 -> ACTIVE
 -> SUBMITTED
 -> UNDER_REVIEW
 -> VERIFIED
 -> SETTLEMENT_PENDING
 -> SUBMITTED       # XMR transaction submitted
 -> CONFIRMED
 -> PAID / SETTLED
```

See `docs/PHOTO-POLICY.md` for publication requirements.
