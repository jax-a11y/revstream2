# Cross-Paradigm Integration Specification

## Overview

The integration layer binds all 4 modeling paradigms through **canonical entity mappings**,
**cross-references**, and **analysis snapshots**. This ensures that every entity, event,
and relationship can be traced across all representations.

## Entity Mapping Table

The `integration.entity_mappings` table is the keystone:

```
canonical_id  | canonical_name              | entity_type  | agent_model_id    | event_model_id         | dynamics_model_id           | hypergraph_node_id
--------------+-----------------------------+--------------+-------------------+------------------------+-----------------------------+-------------------
AYMAC         | AYMAC INTERNATIONAL CC      | ORGANIZATION | AYMAC_001         | NULL                   | NULL                        | AYMAC
VILLA_VIA     | Villa Via Arcadia No 2 CC   | ORGANIZATION | VILLA_VIA_ARCADIA | ACC_62423540807         | account_balance_62423540807 | VILLA_VIA_ARCADIA
RST           | Regima Skin Treatments CC   | ORGANIZATION | ENTITY_RST        | ACCOUNT_STATE_RST      | STOCK_RST_BALANCE           | NODE_RST
FNB           | First National Bank         | FIN_INST     | FNB_001           | NULL                   | NULL                        | FNB
PERSON_JF     | Jacqueline Faucitt          | PERSON       | PERSON_JF         | natural_person_JF      | NULL                        | HG_PERSON_JF
```

## Cross-Reference Types

### OWNERSHIP
Links entity ownership across paradigms:
```
Entities: [AYMAC, ACCOUNT_62012990132, FNB]
ER Model:  AYMAC_001 --[OWNS]--> ACC_62012990132
Hypergraph: HE_OWNERSHIP_AYMAC (hyperedge connecting 3 nodes)
```

### TRANSACTION
Links financial transactions across paradigms:
```
Entities: [ACCOUNT_62012990132, KUNGWINI]
ER Model:  TX_001 transaction agent
Events:    PAYMENT_INITIATED -> PAYMENT_COMPLETED (causality chain)
Dynamics:  expense_flow_62012990132 (flow rate)
Hypergraph: HE_TX_001 DEBIT_TRANSACTION (multi-node edge)
```

### FEE
Links fee charging across paradigms:
```
Entities: [FNB, ACCOUNT_62012990132]
ER Model:  FNB_001 --[CHARGES_FEE]--> ACC_62012990132
Events:    FEE_SCHEDULED -> FEE_ACCRUED -> FEE_CHARGED (state machine)
Dynamics:  fee_flow_62012990132, accumulated_fees_62012990132
Hypergraph: HE_FEE_CHARGE (service fee hyperedge)
```

## Analysis Snapshots

Statement-level analysis snapshots capture cross-paradigm metrics:

```json
{
    "analysis_type": "statement_analysis",
    "entity_id": "ACC_62012990132",
    "snapshot_data": {
        "statement_number": 237,
        "account_number": "62012990132",
        "opening_balance": 39778.01,
        "closing_balance": 43212.48,
        "total_credits": 5055.0,
        "total_debits": 1477.53,
        "total_fees": 143.0,
        "net_change": 3434.47,
        "account_health_index": 0.7907,
        "fee_burden_ratio": 0.0283,
        "credit_count": 3,
        "debit_count": 5,
        "transaction_count": 8
    }
}
```

## Observer Pattern for Cross-Model Communication

The `BaseModel` class implements an observer pattern allowing models to notify
each other of changes:

```python
class BaseModel(ABC):
    _observers: List[Callable]

    def add_observer(callback: Callable)
    def notify_observers(event_type: str, data: Dict)
```

When an entity changes in one paradigm:
1. ER-ABM: Agent state change notifies observers
2. ET-DSM: Event processed, state transition recorded
3. SF-SDM: Stock/flow variable updated
4. NS-FH: Node truth value or embedding updated

## Revstream2 <-> Fincosys Entity Alignment

| Revstream2 ID | Fincosys Code | Entity |
|--------------|---------------|--------|
| PERSON_001 | PF | Peter Andrew Faucitt |
| PERSON_002 | - | Rynette Farrar |
| PERSON_003 | - | Adderory (Rynette's Son) |
| PERSON_004 | JF | Jacqueline Faucitt |
| PERSON_005 | DJF | Daniel James Faucitt |
| PERSON_007 | - | Danie Bantjies |
| ORG_001 | RWD | Regima Worldwide Distribution |
| ORG_002 | RST | Regima Skin Treatments CC |
| ORG_003 | RZA/RZI | RegimA Zone Ltd (UK) |
| ORG_004 | SLG | Strategic Logistics CC |
| ORG_005 | VVA | Villa Via Arcadia No 2 CC |
| ORG_006 | RSA | RegimA SA |
| ORG_008 | REZ | Rezonance (Pty) Ltd |
| TRUST_001 | FFT | Faucitt Family Trust |

## Neon Sync Pipeline

The fincosys membrane workflow Stage 6a orchestrates Neon sync:

```
Step 1: configure_neon_mcp_connection   (config)
Step 2: upsert_entity_relation_schema   (execute)
Step 3: upsert_event_timeline_schema    (execute)
Step 4: upsert_stock_flow_schema        (execute)
Step 5: upsert_hypergraph_schema        (execute)
Step 6: upsert_membrane_coa_schema      (execute)
Step 7: upsert_integration_schema       (execute)
Step 8: verify_record_counts            (validate)
```

All upserts use `ON CONFLICT` for idempotent re-execution.

## Source Files
- SQL: `fincosys/sql_batches/12_entity_mappings.sql` (531 lines)
- SQL: `fincosys/sql_batches/13_cross_references.sql` (80 lines)
- SQL: `fincosys/sql_batches/14_analysis_snapshots.sql` (36 lines)
- SQL: `fincosys/sql_batches/integrated_entities.sql` (549 lines, ON CONFLICT upserts)
- Pipeline: `fincosys/skills/fincosys-membrane-workflow/scripts/steps/stage_6a_*.py`
- Base: `fincosys/core/base.py` (observer pattern)
