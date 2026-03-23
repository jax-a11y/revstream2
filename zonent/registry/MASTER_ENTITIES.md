# Master Entity Registry

## Canonical Entity Table (22 Entities)

### Organizations

| Code | Legal Name | Type | CIPC Reg | VAT | Founded | Country | Status |
|------|-----------|------|----------|-----|---------|---------|--------|
| RST | Regima Skin Treatments CC | CC | 1992/005371/23 | 4590131043 | 1992 | ZA | Active |
| RWD | Regima Worldwide Distribution Pty Ltd | Pty | - | - | - | ZA | Active |
| RSA | Regima SA Pty Ltd | Pty | - | - | - | ZA | Active |
| SLG | Strategic Logistics CC | CC | - | - | - | ZA | Active |
| VVA | Villa Via Arcadia No 2 CC | CC | - | 4790157558 | - | ZA | Active |
| REZ | Rezonance (Pty) Ltd | Pty | - | - | - | ZA | Active |
| AYM | AYMAC International CC | CC | CK 99/61687/23 | - | 1999 | ZA | Active |
| COR | Corpclo 2065 CC | CC | - | - | - | ZA | Active |
| RZA | RegimA Zone Academy Ltd | Ltd | - | - | - | UK | Active |
| RZI | RegimA Zone International | - | - | - | - | UK | Active |
| RDH | RegimA Dr Harriet Ltd | Ltd | - | - | - | UK | Active |
| RUK | RegimA UK Ltd | Ltd | - | - | - | UK | Active |
| KCH | Kerchoonz Ltd | Ltd | - | - | - | UK | Active |
| RWW | Regima Worldwide (UK) | - | - | - | - | UK | Active |

### Persons

| Code | Full Name | Role | Agent Type |
|------|-----------|------|-----------|
| PF | Peter Andrew Faucitt | Director/Trustee | Antagonist |
| JF | Jacqueline Faucitt | Director | Victim |
| DJF | Daniel James Faucitt | Director/Owner RegimA Zone Ltd | Victim |
| KRN | Karen Morris | Sole Trader | Neutral |

### Trusts

| Code | Name | Trustee | Beneficiaries | Conflict |
|------|------|---------|--------------|----------|
| FFT | Faucitt Family Trust | PF (+ Bantjies as unknown trustee) | JF, DJF | R18.685M Bantjies debt |

### Financial Institutions

| Code | Name | VAT | Branch | Accounts Managed |
|------|------|-----|--------|-----------------|
| FNB | First National Bank | 4210102051 | 250655 | 39 |

### Key Non-Entity Persons (revstream2)

| ID | Name | Role | Financial Impact |
|----|------|------|-----------------|
| PERSON_002 | Rynette Farrar | Co-Conspirator | R4,276,832.85 |
| PERSON_003 | Adderory (son) | Accomplice | Domain fraud |
| PERSON_006 | Linda | Bookkeeper (Rynette's sister) | - |
| PERSON_007 | Danie Bantjies | Accountant/Unknown Trustee | R18,685,000 debt |
| PERSON_008 | Kayla | Estate Creditor (Deceased) | - |
| PERSON_010 | Bernadine Wright | Financial Professional | - |
| PERSON_012 | Jax | CEO RST / Witness | - |

## Membrane Shell Assignment

### Arche (Excluded from consolidation)
DJF, JF, PF

### Agent (Included in consolidation)
RST, RSA, SLG, REZ, RZA, RZI, AYM, COR, RDH, RUK, KCH, KRN

### Relatio (Subject to intercompany elimination)
RWD, VVA, FFT

### Arena (Survives consolidation)
PORT, NEW

## Entity Relationships Summary

### Ownership/Control
- PF controls RWD (directorial), trustee of FFT
- DJF owns RegimA Zone Ltd (UK), operates Shopify platform
- JF operates Shopify platform
- Bantjies: trustee of FFT (unknown), accountant for group, debtor R18.685M

### Key Financial Flows
- RST -> SLG: R13M stock/loan (R5.4M unaccounted)
- VVA -> Group: R22.8M capital extraction (86% profit margin)
- RWD: invoices on infrastructure it neither owns nor funds
- REZ: R1,035,361.34 creditor (unpaid since Feb 2023)
- FFT: R2,851,247.35 trust violations

### Conspiracy Networks
1. PF <-> Rynette: 6+ shared events, systematic coordination
2. Rynette <-> Adderory: mother-son collusion (domain fraud)
3. PF <-> Bantjies: fraud concealment (R18.685M debt motive)
