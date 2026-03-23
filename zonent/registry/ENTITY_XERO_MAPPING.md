# Entity-Xero-QBO Mapping (v8.0)

## Consolidation Configuration

| Property | Value |
|----------|-------|
| Consolidation Hub | REZ (Rezonance) |
| Method | Membrane-CoA Four-Shell Topology |
| QBO Entities | 22 (10 UK + 12 ZA/Sandbox) |
| Xero Org | Single org (ZA entities) |

## Shell Mapping

### Arche Shell (Code 10100)
| Entity | Xero | QBO Realm | Treatment |
|--------|------|-----------|-----------|
| DJF | - | - | Excluded from consolidation |
| JF | - | - | Excluded from consolidation |
| PF | - | - | Excluded from consolidation |

### Agent Shell (Code 10200-20200)
| Entity | Xero Org | QBO Realm | FNB Accounts | Treatment |
|--------|----------|-----------|-------------|-----------|
| RST | Yes | Yes | 55270035642, 62134839127, CFC x2 | Included |
| RSA | Yes | Yes | - | Included |
| SLG | Yes | Yes | 62432501494, 62593375829, CFC x3 | Included |
| REZ | Yes | Hub | - | Consolidation hub |
| RZA | - | Yes (UK) | - | Included |
| RZI | - | Yes (UK) | - | Included |
| AYM | Yes | Yes | 62012990132 | Included |
| COR | Yes | Yes | 62060760404 | Included |
| RDH | - | Yes (UK) | Lloyds | Included |
| RUK | - | Yes (UK) | - | Included |
| KCH | - | Yes (UK) | - | Included |
| KRN | - | Yes (UK) | - | Included |

### Relatio Shell (Code 10300-70400)
| Entity | Xero Org | QBO Realm | FNB Accounts | Treatment |
|--------|----------|-----------|-------------|-----------|
| RWD | Yes | Yes | 62323196362, 62836164880 | Intercompany elimination |
| VVA | Yes | Yes | 62423540807, 62812835744 | Intercompany elimination |
| FFT | Yes | Yes | Trust accounts | Intercompany elimination |

### Arena Shell (Code 40100-69900)
| Entity | Treatment |
|--------|-----------|
| PORT | External - survives consolidation |
| NEW | External - survives consolidation |

## Intercompany Elimination Pairs

| Source | Target | Nature | Volume |
|--------|--------|--------|--------|
| RST | SLG | Stock transfers + R13M loan | High |
| RST | RWD | Distribution, revenue recognition | High |
| VVA | Group | Rental charges, member loans | R22.8M |
| FFT | Beneficiaries | Trust distributions, loans | R2.85M+ |
| REZ | Group | IT services creditor | R1.035M |

**Total intercompany volume: R58.58M (largely unreconciled)**

## 88-Account Chart of Accounts

The Membrane CoA provisions 88 accounts in the REZ QBO consolidation hub,
structured to capture all 4-shell activity with proper elimination coding.

Account ranges correspond to membrane shells:
- 10100: Arche (personal)
- 10200-20200: Agent (operational)
- 10300-70400: Relatio (intercompany)
- 40100-69900: Arena (external)

## Data Sources

| Source | Type | Entities Covered |
|--------|------|-----------------|
| FNB Bank Statements | PDF + JSON | ZA entities with FNB accounts |
| Xero | API | ZA entities (single org) |
| QBO | API | All 22 entities (UK + ZA) |
| CIPC | Registry | ZA companies and CCs |
| Lloyds | UK Banking | RDH (UK) |
| Shopify | eCommerce | RegimA Zone Ltd platform |
