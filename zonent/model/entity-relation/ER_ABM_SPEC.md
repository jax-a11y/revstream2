# Entity-Relation: Agent-Based Model (ER-ABM) Specification

## Overview

The ER-ABM paradigm models each entity as an **autonomous agent** with state, behaviors,
message passing, and interaction rules. The financial ecosystem is an environment where
agents act and react through discrete time steps.

## Type System

### Entity Types
```
ORGANIZATION          # Companies, CCs, Trusts
FINANCIAL_INSTITUTION # Banks (FNB, ABSA, Lloyds, Investec)
ACCOUNT               # Bank accounts
TRANSACTION           # Financial transactions
NATURAL_PERSON        # Individual humans
JURISTIC_PERSON       # Legal entities
REGULATORY_BODY       # SARS, CIPC, SAICA
SERVICE               # Banking services, platforms
EXTERNAL_PARTY        # Counterparties
GOVERNMENT            # Government entities
INTERNAL_TRANSFER     # Intercompany transfers
```

### Relation Types
```
OWNS                  # Entity ownership of accounts/entities
OPERATES              # Operational control
TRANSACTS_WITH        # Financial transaction relationship
PROVIDES_SERVICE      # Service provision (bank -> account)
REGULATES             # Regulatory oversight
CHARGES_FEE           # Fee charging relationship
CREDITS               # Incoming transfer relationship
DEBITS                # Outgoing transfer relationship
HOLDS                 # Asset holding
ACCOUNT_HOLDER        # Account ownership
MEMBER_OF             # Membership
DIRECTOR_OF           # Directorship
SHAREHOLDER_OF        # Shareholding
HAS_STATEMENT         # Statement issuance
FOLLOWS               # Temporal sequence
CONTAINS              # Containment
ISSUED_BY             # Issuance
INTER_COMPANY_ACCOUNT # Intercompany loan/account
BANKS_WITH            # Banking relationship
```

### Agent States
```
AgentState: ACTIVE, INACTIVE, PENDING, SUSPENDED, TERMINATED
```

## Agent Types

### OrganizationAgent
- **Attributes**: registration_number, balance, total_income, total_expenses
- **Messages handled**: CREDIT_NOTIFICATION, DEBIT_NOTIFICATION, FEE_NOTIFICATION
- **Behavior**: Monitors for low balance alerts

### FinancialInstitutionAgent
- **Attributes**: vat_number, total_fees_collected, accounts_managed
- **Methods**: set_fee_schedule(fee_type, amount), charge_fee(account, fee_type)
- **Messages handled**: ACCOUNT_OPENED, TRANSACTION_PROCESSED

### AccountAgent
- **Attributes**: account_number, account_type, balance, debit_rate
- **Methods**: credit(amount, description, source_id), debit(amount, description, target_id), apply_fee(amount, fee_type)
- **Messages handled**: CHARGE_FEE, CREDIT, DEBIT
- **Tracks**: Full transaction list with details

### TransactionAgent
- **Attributes**: transaction_type, amount, description, status
- **Methods**: execute(source_account, target_account)

### PersonAgent
- **Attributes**: full_name, roles (list), total_holdings
- **Methods**: add_role(role)

### ServiceAgent
- **Attributes**: fee_amount, usage_count
- **Methods**: use_service(account, bank)

## FinancialEcosystem (Environment)

```python
class FinancialEcosystem:
    agents: Dict[str, Agent]
    relations: List[BaseRelation]
    time_step: int

    def add_agent(agent)
    def get_agent(agent_id) -> Agent
    def get_agents_by_type(entity_type) -> List[Agent]
    def add_relation(source_id, target_id, relation_type, attributes, weight)
    def step()          # Execute one time step for all agents
    def run(steps: int) # Run simulation for N steps
    def get_entity_relation_graph() -> Dict  # Export graph
```

## Neon Schema

```sql
-- Schema: entity_relation
CREATE TABLE entities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    state TEXT,
    attributes JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE relations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_id UUID REFERENCES entities(id),
    target_id UUID REFERENCES entities(id),
    relation_type TEXT NOT NULL,
    weight DECIMAL(3,2),
    attributes JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW()
);
```

## Key Indexes
- `entities(entity_type)`, `entities(state)`, `entities(name)`
- `entities USING gin(attributes)` for JSONB queries
- `relations(source_id)`, `relations(target_id)`, `relations(relation_type)`

## Source Files
- Model: `fincosys/models/entity_relation/agent_model.py`
- Data: `fincosys/entity_relation/ecosystem_graph.json`
- SQL: `fincosys/sql_batches/01_entities.sql` (2,645 lines)
- SQL: `fincosys/sql_batches/02_relations.sql` (249 lines)
- Revstream2: `revstream2/data_models/entities/entities_refined_2025_11_18.json` (27 entities)
- Revstream2: `revstream2/data_models/relations/relations_refined_2025_11_18.json` (54 relations)
