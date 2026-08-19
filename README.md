# MyZubster Photos

**Canonical public evidence and photographic archive for the MyZubster ecosystem.**

Questo repository non è una semplice raccolta di immagini.

Le fotografie pubblicate qui possono rappresentare **artefatti di evidenza verificabili** collegati a osservazioni reali, dataset geografici, attività di ricerca autorizzata, contributi alla piattaforma e, quando previsto da una bounty, alla dimostrazione del lavoro svolto.

Ogni foto può quindi essere collegata a più livelli di informazione:

```text
FOTO / OSSERVAZIONE REALE
        |
        v
FILE SANITIZZATO
        |
        v
SHA-256 + METADATI + PROVENIENZA
        |
        v
OSSERVAZIONE / BOUNTY / DELIVERABLE
        |
        v
REVIEW CONTRO I CRITERI DI ACCETTAZIONE
        |
        v
VERIFIED
        |
        v
REWARD_RECORDED IN MYZ
        |
        +------------------------------+
        |                              |
        v                              v
MYZ INTERNAL LEDGER            OPTIONAL EXTERNAL SETTLEMENT
                               XMR / TOKEN / BLOCKCHAIN
                                      |
                                      v
                              INDEPENDENT VERIFICATION
                                      |
                                      v
                                  PAID / SETTLED
```

> **Principio fondamentale:** una fotografia può essere una prova del lavoro, ma la sua sola presenza in questo repository non significa automaticamente che una bounty sia stata verificata, che un reward sia stato assegnato o che un pagamento blockchain sia avvenuto.

---

## 1. Cosa rappresentano queste fotografie

Una fotografia MyZubster può essere contemporaneamente:

- una **osservazione del mondo reale**;
- una **prova fotografica** collegata a un'attività autorizzata;
- un elemento di un dataset geografico o ambientale;
- un deliverable richiesto da una bounty;
- un artefatto identificabile tramite hash crittografico;
- una fonte per mappe, timeline, gallery e registry MyZubster;
- un elemento di provenienza collegato a Git/GitHub;
- un contenuto eventualmente indirizzabile tramite IPFS/CID;
- un riferimento per una bounty successivamente verificata;
- un artefatto collegabile a un reward registrato nel ledger MYZ;
- quando realmente previsto e verificato, un artefatto collegabile anche a un settlement esterno XMR/token/blockchain.

Quindi **l'immagine è il contenuto visibile**, mentre il valore di verifica deriva dall'insieme di immagine, metadati, hash, provenienza, criteri della bounty e review.

---

## 2. Repository canonico

Repository:

```text
MyZubster-Ecosystem/MyZubster-Photos
```

Le fotografie reali pubbliche vengono centralizzate qui invece di essere distribuite nei repository applicativi.

Il core MyZubster può continuare a conservare:

- registry delle osservazioni;
- riferimenti ai media;
- coordinate autorizzate;
- stato dell'osservazione;
- bounty ID;
- reward reference;
- settlement reference quando applicabile.

Il file fotografico canonico vive invece in questo repository.

---

## 3. Struttura

Struttura generale prevista:

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

La struttura geografica può essere usata quando il luogo è pubblico e la precisione pubblicata è appropriata.

---

## 4. Metadati: perché sono importanti

Una foto senza contesto è soltanto un file binario.

Una foto MyZubster può invece avere un record strutturato che permette di capire **cosa rappresenta, da dove proviene, quale file esatto è stato verificato e a quale lavoro è eventualmente collegata**.

Un record può includere, dove applicabile:

| Campo | Significato |
|---|---|
| `photoId` / `observation_id` | identificatore stabile dell'evidenza |
| `filename` | nome canonico del file |
| `destinationPath` | percorso pubblico nel repository Photos |
| `sha256` | impronta crittografica del file esatto |
| `sizeBytes` | dimensione del file verificato |
| `mimeType` | tipo MIME |
| `category` | categoria dell'osservazione |
| `capturedAt` | data/ora di acquisizione, solo se realmente disponibile |
| `publishedAt` | data di pubblicazione |
| `city` / `region` / `country` | localizzazione pubblicabile |
| `latitude` / `longitude` | coordinate solo quando autorizzate e appropriate |
| `source` | provenienza dichiarata |
| `repositoryCommit` | commit Git che registra il cambiamento |
| `cid` | eventuale CID IPFS del contenuto |
| `metadataCid` | eventuale CID del record metadata |
| `bountyId` | bounty collegata, se esiste |
| `evidenceStatus` | stato della prova |
| `reviewStatus` | stato della review |
| `rewardAsset` | MYZ/XMR/token previsto dalla bounty |
| `rewardAmount` | quantità prevista/registrata |
| `rewardRecordId` | riferimento al ledger interno MyZubster |
| `settlementStatus` | stato del settlement esterno |
| `network` | blockchain/network, solo se esiste un settlement esterno |
| `txHash` | transaction hash verificato, solo quando realmente disponibile |

I campi sconosciuti devono rimanere `null` o assenti. **Non devono essere inventati.**

---

## 5. SHA-256: identità crittografica della foto

Ogni foto pubblicata dovrebbe avere un digest SHA-256.

Esempio:

```json
{
  "destinationPath": "photos/italy/emilia-romagna/rimini/landmarks/fontana-della-pigna/fontana-della-pigna-001.jpg",
  "sha256": "3ef2fbae7b97524b629d7729f6260d2b3d36b17defbbfb1bebe9a43852feca3e",
  "sizeBytes": 571976
}
```

Lo SHA-256 permette di verificare che due sistemi stiano parlando **dello stesso identico file**.

Se anche un solo byte cambia, cambia anche l'hash.

Questo consente di collegare in modo deterministico:

```text
foto
  <-> SHA-256
  <-> metadata
  <-> observation record
  <-> bounty evidence
  <-> review
  <-> reward record
```

Lo SHA-256 però **non dimostra da solo che la bounty è stata completata**. Dimostra l'identità del contenuto verificato.

---

## 6. Sanitizzazione e privacy

Il repository è pubblico.

Le immagini destinate alla pubblicazione devono essere sottoposte a controllo privacy e, quando necessario, ricodificate prima dell'ingresso nel repository canonico.

La pipeline attuale può registrare proprietà come:

```json
{
  "privacy": {
    "exifStripped": true,
    "gpsMetadataPublished": false
  }
}
```

### Non devono essere pubblicati automaticamente

- EXIF non revisionato;
- GPS incorporato non necessario;
- JWT, token o credenziali;
- seed o chiavi private;
- percorsi filesystem locali;
- identificatori privati degli utenti;
- infrastruttura sensibile;
- luoghi privati/restricted non autorizzati;
- materiale di review confidenziale;
- raw uploads non revisionati.

La rimozione EXIF/GPS dal file non significa che qualsiasi contenuto visibile nella fotografia sia automaticamente sicuro: il contenuto deve comunque essere appropriato per la pubblicazione.

---

## 7. Migrazione verificata dal core MyZubster

Una prima migrazione canonica ha trasferito **12 fotografie già pubbliche** dal core MyZubster a questo repository.

Il manifest è:

```text
metadata/github-core-migration.json
```

Il manifest registra:

- repository sorgente;
- branch sorgente;
- percorso sorgente;
- percorso destinazione;
- numero di file;
- SHA-256 di ogni copia sanitizzata;
- dimensione in byte;
- stato privacy;
- rimozione del file sorgente dal core;
- commit che ha completato lo spostamento.

Stato registrato:

```json
{
  "mode": "sanitized-copy",
  "sourceDeletion": true,
  "sourceDeletionCommit": "edd564aeede93b9049ec184e815e05da33f0497a",
  "count": 12
}
```

Il core MyZubster usa ora gli URL del repository Photos e gli SHA-256 delle versioni sanificate.

---

## 8. Foto come evidence di una bounty

Una bounty MyZubster rappresenta **lavoro verificabile**.

Per una bounty fotografica, la foto può essere uno degli elementi richiesti dai criteri di accettazione.

Esempi di criteri possibili:

- numero minimo di fotografie;
- soggetto richiesto;
- area pubblica/autorizzata;
- qualità minima;
- caption o descrizione;
- coordinate consentite;
- original-file requirement;
- timestamp, quando realmente disponibile;
- assenza di informazioni sensibili;
- rispetto delle regole di sicurezza e privacy.

La catena logica corretta è:

```text
bounty definita
   -> contributor raccoglie evidence
   -> foto + metadata vengono presentati
   -> review contro acceptance criteria
   -> VERIFIED
   -> reward registrato
```

Non è corretta questa equivalenza:

```text
foto caricata = bounty completata = pagamento eseguito
```

---

## 9. Lifecycle ufficiale della bounty

Il lifecycle canonico MyZubster è:

```text
PROPOSED
  -> VALIDATED
  -> APPROVED
  -> FUNDED          # quando serve una funding reservation
  -> ACTIVE
  -> SUBMITTED
  -> UNDER_REVIEW
  -> VERIFIED | REJECTED
  -> REWARD_RECORDED
  -> SETTLEMENT_PENDING | SETTLED/PAID
```

Per una foto bounty, il file può entrare come evidence durante `SUBMITTED`.

Il passaggio a `VERIFIED` richiede una review reale contro i criteri della bounty.

Un merge GitHub, un issue chiuso o una foto presente nel repository **non sostituiscono questa verifica**.

---

## 10. MYZ e completamento bounty

### Stato attuale di MYZ

**MYZ è attualmente una unità di reward/accounting registrata nel ledger interno della piattaforma MyZubster.**

Quando una bounty viene verificata, il sistema può registrare un reward MYZ, ad esempio:

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

Questo record significa che il reward è stato **registrato nella contabilità/ledger MyZubster**.

Non significa automaticamente che sia avvenuta una transazione su una blockchain pubblica.

### Collegamento evidence -> MYZ

Il modello concettuale è:

```text
photoId
   |
   +-- sha256
   +-- metadata
   +-- observationId
   +-- bountyId
           |
           v
        VERIFIED
           |
           v
    rewardRecordId
           |
           v
        amount MYZ
           |
           v
    MyZubster internal ledger
```

Questo crea una **catena di audit applicativa** tra evidenza e reward.

---

## 11. Blockchain: cosa può essere registrato e cosa no

È importante distinguere **MYZ ledger** da una **blockchain esterna**.

### MYZ

Attualmente:

```text
MYZ = internal-platform-ledger
```

Quindi un reward MYZ non deve essere descritto come `on-chain` senza una prova blockchain indipendente.

### Settlement esterno

Una bounty può eventualmente prevedere XMR o un token blockchain oltre a MYZ.

In quel caso, il record di settlement può includere:

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

Per poter dichiarare `PAID` o `SETTLED`, il sistema deve verificare in modo indipendente almeno, quando applicabile:

- destinatario previsto;
- asset corretto;
- network/chain corretta;
- contract address del token;
- amount canonico;
- transaction hash;
- stato della transazione;
- conferme richieste.

Un `txHash` non deve mai essere inventato.

---

## 12. Settlement lifecycle

Il settlement esterno è separato dalla verifica della bounty:

```text
PENDING
  -> RESERVED / ACCEPTED
  -> SUBMITTED
  -> CONFIRMED
  -> PAID
```

Possibili stati di eccezione:

```text
FAILED
UNSETTLED
DISPUTED
CANCELLED
```

Questo significa che può esistere una situazione perfettamente valida come:

```text
Bounty: VERIFIED
MYZ reward: REWARD_RECORDED
External settlement: PENDING
```

La bounty è stata verificata e il reward interno registrato, ma il pagamento esterno non è ancora stato confermato.

---

## 13. Git, GitHub, hash e blockchain sono livelli diversi

MyZubster utilizza più strumenti di audit, ma non devono essere confusi.

### Git/GitHub

Registrano:

- storia dei cambiamenti;
- commit;
- review;
- PR;
- provenienza repository;
- timestamp della storia Git.

### SHA-256

Identifica il contenuto esatto del file.

### IPFS/CID

Quando utilizzato, rende il contenuto indirizzabile tramite il suo contenuto.

Un CID dimostra quale contenuto è recuperato, non che una bounty sia stata verificata.

### MYZ ledger

Registra la contabilità/reward interno della piattaforma.

### Blockchain esterna

Quando realmente utilizzata per un settlement, registra una transazione sul network specifico e richiede verifica indipendente.

Questi livelli possono essere collegati, ma **uno non sostituisce automaticamente gli altri**.

---

## 14. Modello completo di evidence record

Un record esteso futuro può assumere questa forma:

```json
{
  "schemaVersion": "1.0.0",
  "photoId": "rimini-example-001",
  "observationId": "rimini-example-001",
  "path": "photos/italy/emilia-romagna/rimini/example/example-001.jpg",
  "mimeType": "image/jpeg",
  "sha256": "...",
  "sizeBytes": 123456,
  "privacy": {
    "reviewed": true,
    "exifStripped": true,
    "gpsMetadataPublished": false
  },
  "provenance": {
    "repository": "MyZubster-Ecosystem/MyZubster-Photos",
    "commit": "...",
    "cid": null,
    "metadataCid": null
  },
  "bounty": {
    "bountyId": null,
    "evidenceStatus": "PUBLISHED",
    "reviewStatus": null,
    "verifiedAt": null
  },
  "reward": {
    "rewardRecordId": null,
    "asset": "MYZ",
    "amount": null,
    "ledger": "internal-platform-ledger",
    "status": null
  },
  "settlement": {
    "required": false,
    "asset": null,
    "network": null,
    "txHash": null,
    "status": null
  }
}
```

Questo schema rende evidente la separazione tra **foto**, **verifica**, **reward** e **settlement**.

---

## 15. Esempio di catena di prova completa

Una bounty fotografica può produrre una catena verificabile di questo tipo:

```text
1. Bounty #123 definisce cosa fotografare
2. Contributor produce la fotografia
3. La fotografia viene sanitizzata
4. Viene calcolato SHA-256
5. Il file entra in MyZubster-Photos
6. Il metadata record collega photoId + SHA-256 + bountyId
7. La submission entra in UNDER_REVIEW
8. Un reviewer controlla acceptance criteria + evidence
9. La bounty passa a VERIFIED
10. Il reward viene scritto nel ledger MYZ -> REWARD_RECORDED
11. Se esiste un reward esterno:
      SETTLEMENT_PENDING
      -> transaction submitted
      -> independent verification
      -> SETTLED / PAID
```

È questa catena che rende la fotografia **parte di un sistema di evidence e reward**, e non una semplice immagine caricata online.

---

## 16. Sicurezza delle photo bounty

Una bounty non deve richiedere o premiare:

- trespassing;
- ingresso in aree ristrette;
- aggiramento di barriere o controlli d'accesso;
- fotografie di sistemi di sicurezza sensibili;
- infrastrutture critiche o dettagli operativi sensibili;
- coordinate precise che creano rischi di sicurezza o privacy;
- materiale confidenziale;
- esposizione di persone o dati privati senza base appropriata.

L'osservazione da luoghi pubblici e autorizzati è il default.

---

## 17. Policy per i raw uploads

I raw uploads dell'applicazione non devono essere copiati automaticamente in questo repository pubblico.

Prima della pubblicazione serve un passaggio di:

```text
raw upload
   -> validation
   -> privacy review
   -> EXIF/GPS review
   -> sanitization
   -> SHA-256
   -> publication
```

---

## 18. File machine-readable

### `metadata/photo-catalog.json`

Definisce categorie e policy generali del repository.

La policy attuale prevede:

```json
{
  "privacyReviewRequired": true,
  "exifReviewRequired": true,
  "rawUploadsAllowed": false
}
```

### `metadata/github-core-migration.json`

Audit della migrazione delle fotografie già pubblicate dal core MyZubster.

Contiene per ogni foto:

- `sourcePath`;
- `destinationPath`;
- `sha256`;
- `sizeBytes`;
- stato di sanitizzazione privacy.

### `metadata/photos.json`

Catalogo generato dal publisher per nuove fotografie sanificate.

### `metadata/skipped.json`

Registra eventuali file che il publisher non ha potuto o non ha voluto pubblicare.

---

## 19. Principio di verificabilità

La filosofia del repository può essere riassunta così:

```text
DON'T TRUST THE FILENAME.
VERIFY THE CONTENT.
VERIFY THE METADATA.
VERIFY THE HASH.
VERIFY THE BOUNTY.
VERIFY THE REWARD RECORD.
VERIFY THE EXTERNAL SETTLEMENT SEPARATELY.
```

MyZubster vuole conservare una storia verificabile che permetta di rispondere a domande concrete:

- Quale fotografia è stata presentata?
- Qual è il suo hash?
- Da dove proviene?
- Quando è stata pubblicata?
- A quale osservazione appartiene?
- Era collegata a una bounty?
- Quali acceptance criteria sono stati verificati?
- Chi/che cosa ha registrato lo stato VERIFIED?
- È stato registrato un reward MYZ?
- Esiste un settlement esterno?
- Se sì, qual è la prova indipendente della transazione?

---

## 20. Regola finale

**Queste non sono semplici foto.**

Sono potenziali **unità di evidenza digitale** collegate al mondo reale e inserite in un sistema che può combinare:

```text
REAL-WORLD OBSERVATION
+ PUBLIC PHOTO
+ SANITIZED METADATA
+ SHA-256 INTEGRITY
+ GIT PROVENANCE
+ OPTIONAL IPFS CONTENT ADDRESSING
+ BOUNTY EVIDENCE
+ HUMAN / AUTHORIZED REVIEW
+ MYZ REWARD ACCOUNTING
+ OPTIONAL VERIFIED BLOCKCHAIN SETTLEMENT
```

Ma ogni livello deve essere dichiarato solo quando esiste realmente.

In particolare:

- **photo published != bounty verified**
- **PR merged != bounty verified**
- **bounty verified != external payment completed**
- **MYZ reward recorded != on-chain transaction**
- **transaction submitted != PAID**
- **PAID/SETTLED requires independent verification**

Questa separazione rende l'intero sistema più auditabile, più sicuro e più credibile.

---

## MyZubster

**MyZubster-Photos** è il layer canonico per le fotografie pubbliche e gli artefatti visuali di evidenza reale.

Il valore non è soltanto nell'immagine: è nella relazione verificabile tra **contenuto, metadata, integrità, provenienza, bounty, reward e — quando realmente presente — settlement esterno verificato**.
