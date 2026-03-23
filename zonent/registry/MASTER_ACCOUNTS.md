# Master Accounts Registry

## FNB Account Portfolio (39 Accounts)

### Day-to-Day Accounts (Platinum Business)

| Account Number | Entity | Account Name | Currency | Statements |
|---------------|--------|-------------|----------|------------|
| 55270035642 | RST | Regima Skin Treatments | ZAR | 24 |
| 62012990132 | AYM | AYMAC International | ZAR | 248+ |
| 62060760404 | COR | Corpclo 2065 | ZAR | - |
| 62027933606 | JF | Jacqueline Faucitt | ZAR | - |
| 62323196362 | RWD | Regima Worldwide Distribution | ZAR | 121+ |
| 62423540807 | VVA | Villa Via Arcadia No 2 | ZAR | - |
| 62432501494 | SLG | Strategic Logistics | ZAR | 101+ |

### Savings / Money On Call

| Account Number | Entity | Account Name | Currency | Balance (snapshot) |
|---------------|--------|-------------|----------|--------------------|
| 62134839127 | RST | Regima Skin Treatments MOC | ZAR | High value |
| 62742245617 | - | - | ZAR | - |
| 62812835744 | VVA | Villa Via MOC | ZAR | R9,665,250.75 |
| 62593375829 | SLG | Strategic Logistics MOC | ZAR | R416,127.94 |
| 62836164880 | RWW | Regima Worldwide MOC | ZAR | R499,444.27 |

### CFC (Foreign Currency) Accounts

| Account Number | Entity | Currency |
|---------------|--------|----------|
| 62839603835 | RST | USD |
| 62839603827 | RST | GBP |
| 62839612323 | SLG | EUR |
| 62839612349 | SLG | USD |
| 62839612331 | SLG | GBP |

### Portfolio Summary (Snapshot 2022-12-06)

| Category | Value | Accounts |
|----------|-------|----------|
| Day-to-Day | R10,064,170.30 | 8 |
| Savings/MOC | R29,091,403.16 | 5 |
| CFC (USD) | Variable | 2 |
| CFC (GBP) | Variable | 2 |
| CFC (EUR) | Variable | 1 |
| **Total** | **R39,155,573.46** | **20** |

## Transaction Index Format

```
{account_number}-{statement_number:03d}-{sequence_number:03d}
```

Example: `62432501494-101-001` = SLG account, statement 101, first transaction

## Statement Coverage

| Account | Date Range Start | Date Range End | Statement Count |
|---------|-----------------|----------------|-----------------|
| 55270035642 | 2020-01-02 | 2021-12-24 | 24 |
| 62012990132 | varies | varies | 248+ |
| 62323196362 | varies | varies | 121+ |
| 62432501494 | varies | varies | 101+ |
| **Total** | **2020-01-02** | **2025+** | **4,353** |

## Account State Summary

All active accounts are in `ACTIVE_CREDIT` state as of latest snapshot.

State definitions:
- `OPENING`: Account just opened
- `ACTIVE_CREDIT`: Balance >= 0 (normal)
- `ACTIVE_DEBIT`: Balance < 0 (overdraft)
- `DORMANT`: No activity for extended period
- `SUSPENDED`: Account frozen
- `CLOSED`: Terminal state
