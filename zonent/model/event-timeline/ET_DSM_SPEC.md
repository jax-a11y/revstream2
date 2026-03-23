# Event-Timeline: Discrete State Model (ET-DSM) Specification

## Overview

The ET-DSM paradigm implements a **discrete event simulation** with event-driven state
transitions, causality tracking, and chronological event processing.

## Event Types
```
STATEMENT_PERIOD_START    # Opening of a bank statement period
STATEMENT_PERIOD_END      # Closing of a bank statement period
BALANCE_UPDATED           # Balance change event
PAYMENT_INITIATED         # Outgoing payment started
PAYMENT_COMPLETED         # Outgoing payment finished
CREDIT_RECEIVED           # Incoming credit
DEBIT_PROCESSED           # Outgoing debit
FEE_SCHEDULED             # Fee scheduled for future
FEE_ACCRUED               # Fee accrued
FEE_CHARGED               # Fee charged to account
ACCOUNT_OPENED            # New account opened
ACCOUNT_CLOSED            # Account closed
DAY_START / DAY_END       # Day boundaries
MONTH_END                 # Month boundary
STATEMENT_GENERATED       # Statement issued
PORTFOLIO_SNAPSHOT        # Full portfolio capture
RATE_CHANGE               # Interest rate change
ENTITY_CREATED            # New entity registered
TRANSACTION_PROCESSED     # Generic transaction event
```

## State Machines

### AccountStateMachine
```
States: OPENING, ACTIVE_CREDIT, ACTIVE_DEBIT, DORMANT, SUSPENDED, CLOSED

Transitions:
  OPENING       -> [ACTIVE_CREDIT, ACTIVE_DEBIT]
  ACTIVE_CREDIT -> [ACTIVE_DEBIT, DORMANT, SUSPENDED, CLOSED]
  ACTIVE_DEBIT  -> [ACTIVE_CREDIT, SUSPENDED, CLOSED]
  DORMANT       -> [ACTIVE_CREDIT, ACTIVE_DEBIT, CLOSED]
  SUSPENDED     -> [ACTIVE_CREDIT, ACTIVE_DEBIT, CLOSED]
  CLOSED        -> [] (terminal)

Trigger: update_balance(amount, event)
  - If balance >= 0: transition to ACTIVE_CREDIT
  - If balance < 0:  transition to ACTIVE_DEBIT
```

### TransactionStateMachine
```
States: INITIATED, PENDING, PROCESSING, COMPLETED, FAILED, REVERSED

Transitions:
  INITIATED  -> [PENDING, FAILED]
  PENDING    -> [PROCESSING, FAILED]
  PROCESSING -> [COMPLETED, FAILED]
  COMPLETED  -> [REVERSED]
  FAILED     -> [] (terminal)
  REVERSED   -> [] (terminal)
```

### FeeStateMachine
```
States: SCHEDULED, ACCRUED, CHARGED, WAIVED, REFUNDED

Transitions:
  SCHEDULED -> [ACCRUED, WAIVED]
  ACCRUED   -> [CHARGED, WAIVED]
  CHARGED   -> [REFUNDED]
  WAIVED    -> [] (terminal)
  REFUNDED  -> [] (terminal)
```

### PortfolioStateMachine
```
States: UNKNOWN, SNAPSHOT_CAPTURED, ANALYZED, RECONCILED

Transitions:
  UNKNOWN           -> SNAPSHOT_CAPTURED
  SNAPSHOT_CAPTURED -> ANALYZED
  ANALYZED          -> RECONCILED
```

### PersonStateMachine / EntityStateMachine
```
Person States:  CREATED, ACTIVE, INACTIVE, SUSPENDED
Entity States:  CREATED, ACTIVE, INACTIVE, DEREGISTERED, LIQUIDATION
```

## DiscreteEventSimulator

```python
class DiscreteEventSimulator:
    event_queue: List[BaseEvent]            # Priority queue by timestamp
    processed_events: List[BaseEvent]
    state_machines: Dict[str, StateMachine]
    event_handlers: Dict[EventType, List[Callable]]
    current_time: Optional[datetime]

    def schedule_event(event)
    def process_event(event)       # Dispatch to registered handlers
    def step() -> BaseEvent        # Process next event from queue
    def run_all()                  # Process all queued events
    def run_until(end_time)        # Process until timestamp
    def get_timeline() -> List     # Export chronological events
    def get_causality_chains()     # Export event causality graph
```

## Default Event Processing
- **CREDIT_RECEIVED**: AccountStateMachine.update_balance(+amount)
- **DEBIT_PROCESSED**: AccountStateMachine.update_balance(-amount)
- **FEE_CHARGED**: AccountStateMachine.update_balance(-amount)

## Case Event Phases (revstream2)

| Phase | Name | Date Range | Events | Pattern |
|-------|------|-----------|--------|---------|
| 000 | Historical Foundation | 2017-06 to 2021-12 | 22 | Infrastructure establishment |
| 001 | Foundation | 2025-03-01 to 2025-03-30 | 7 | Trust manipulation |
| 002 | Initial Theft | 2025-04-01 to 2025-04-14 | 5 | Payment redirection |
| 003 | Escalation | 2025-05-02 to 2025-05-29 | 9 | Confrontation triggers |
| 004 | Consolidation | 2025-06-06 to 2025-06-30 | 11 | Card cancellations |
| 005 | Control Seizure | 2025-07-08 to 2025-07-25 | 10 | Operational destruction |
| 006 | Cover-up | 2025-08-10 to 2025-09-11 | 8 | Evidence concealment |

## Transaction Index Format
```
{account_number}-{statement_number:03d}-{sequence_number:03d}
Example: "62432501494-101-001"
```

Composite unique constraint: `(account_number, statement_number, sequence_number)`

## Neon Schema

```sql
-- Schema: event_timeline
CREATE TABLE events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_type TEXT NOT NULL,
    entity_id TEXT NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    payload JSONB DEFAULT '{}',
    caused_by UUID,
    transaction_index VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE state_machines (
    id TEXT PRIMARY KEY,
    machine_type TEXT NOT NULL,
    current_state TEXT NOT NULL,
    attributes JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE state_transitions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    state_machine_id TEXT REFERENCES state_machines(id),
    from_state TEXT NOT NULL,
    to_state TEXT NOT NULL,
    triggered_by UUID,
    timestamp TIMESTAMPTZ NOT NULL,
    metadata JSONB DEFAULT '{}'
);

CREATE TABLE transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    transaction_index VARCHAR(20) UNIQUE,
    account_number VARCHAR(20),
    statement_number INTEGER,
    sequence_number INTEGER,
    transaction_date DATE,
    description TEXT,
    amount DECIMAL(15,2),
    transaction_type TEXT,
    balance_after DECIMAL(15,2),
    category TEXT,
    counterparty TEXT,
    entity_code VARCHAR(10),
    currency VARCHAR(3) DEFAULT 'ZAR',
    payload JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(account_number, statement_number, sequence_number)
);
```

## Source Files
- Model: `fincosys/models/event_timeline/discrete_state_model.py`
- Data: `fincosys/event_timeline/timeline_data.json`
- SQL: `fincosys/sql_batches/03_events.sql` (3,740 lines)
- SQL: `fincosys/sql_batches/04_state_machines.sql` (100 lines)
- SQL: `fincosys/sql_batches/05_state_transitions.sql` (1,065 lines)
- Revstream2: `revstream2/data_models/events/events_refined_2025_11_18.json` (62 events)
- Revstream2: `revstream2/data_models/timelines/timeline_refined_2025_11_18.json` (8 phases)
