# Zone Enterprise: 7-Layer Composable System Model

## Overview

The Zone Enterprise digital twin is a **multi-paradigm financial ecosystem model** for
forensic accounting analysis of 22+ corporate entities spanning South Africa and the UK.
It integrates 4 modeling paradigms across 7 composable layers, unified through cross-paradigm
entity mapping and a 4-shell membrane chart of accounts topology.

## Layer Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 7: NEURAL INFERENCE                                         │
│  ├─ 7 Legal Attention Heads (Causal, Temporal, Normative,          │
│  │   Evidential, Procedural, Contextual, Meta-Legal)               │
│  ├─ Guilt Determination: softmax(QK^T/sqrt(d))V                   │
│  ├─ GRIP 12-dimensional fitness optimization                      │
│  ├─ GNN predictions + node embeddings (64-dim)                     │
│  └─ Weighted edges: weight = repetition x confidence x strength    │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 6: HYPERGRAPH (NS-FH)                                      │
│  ├─ HyperNodes: entity, concept, value, temporal, relation         │
│  ├─ HyperEdges: ownership, transaction, portfolio, fee             │
│  ├─ Symbolic Rules: Datalog-like inference (head :- body)          │
│  ├─ TruthValue(strength, confidence) with PLN operations           │
│  └─ ChainLex: 2,306 legal nodes (63 principles + 2,215 rules)     │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 5: STOCK-FLOW (SF-SDM)                                     │
│  ├─ Variables: STOCK (balances), FLOW (rates), AUXILIARY, CONSTANT │
│  ├─ Flows: income_flow, expense_flow, fee_flow (ZAR/day)          │
│  ├─ Feedback Loops: REINFORCING (positive) / BALANCING (negative)  │
│  ├─ Simulation: compute_aux -> compute_flows -> update_stocks      │
│  └─ Metrics: account_health_index, fee_burden_ratio, net_cash_flow │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 4: EVENT-TIMELINE (ET-DSM)                                  │
│  ├─ Events: 15+ types (credit, debit, fee, statement, etc.)       │
│  ├─ StateMachines: Account, Transaction, Fee, Portfolio, Person    │
│  ├─ Causality chains: event.caused_by -> parent event              │
│  ├─ 62 case events across 8 phases (revstream2)                    │
│  └─ 110K+ financial transactions (fincosys)                        │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 3: ENTITY-RELATION (ER-ABM)                                 │
│  ├─ Agents: Organization, Account, Person, Transaction, Service    │
│  ├─ Relations: OWNS, OPERATES, TRANSACTS_WITH, CREDITS, DEBITS    │
│  ├─ Message passing: send_message() / receive_message()            │
│  ├─ 20 core entities (fincosys) / 27 entities (revstream2)        │
│  └─ 54 relations (revstream2) / 20+ relation types                 │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 2: LEGAL FRAMEWORK (ChainLex/LexRex)                       │
│  ├─ scmlex_nodes: 63 principles + 2,215 rules + 28 domains        │
│  ├─ 8 legal branches: civ, cri, trs, adm, env, prof-eth, etc.     │
│  ├─ Weighted edges for GNN training                                │
│  ├─ Inference chains with path confidence                          │
│  └─ Functions: find_principles_by_domain, search_nodes             │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 1: CASE MANAGEMENT (ad-res-j7)                              │
│  ├─ 141 AD paragraphs -> JR responses -> DR responses              │
│  ├─ Annexures: JF01-16, SF1-8+, PF series, DF series              │
│  ├─ Evidence: file_hash integrity, OCR processing                  │
│  ├─ 125 timeline entries spanning 1982-2026                        │
│  └─ Cases, compliance monitoring, legal relationships              │
└─────────────────────────────────────────────────────────────────────┘
```

## Data Flow Between Layers

```
Raw Data Sources
  ├─ FNB Bank Statements (4,353 PDFs)
  ├─ Xero Accounting (trial balances, AFS)
  ├─ CIPC Company Registrations
  ├─ Email Evidence (EML files)
  ├─ Court Documents (affidavits, orders)
  └─ Shopify / eCommerce data
       │
       ▼
Layer 1: Case Management (evidence intake, paragraph tracking)
       │
       ▼
Layer 2: Legal Framework (principle-to-rule derivation)
       │
       ▼
Layer 3: Entity-Relation (agent creation, relationship mapping)
       │
       ▼
Layer 4: Event-Timeline (event scheduling, state transitions)
       │
       ▼
Layer 5: Stock-Flow (balance dynamics, flow rates, feedback)
       │
       ▼
Layer 6: Hypergraph (multi-way relationships, symbolic inference)
       │
       ▼
Layer 7: Neural Inference (embeddings, attention, GNN predictions)
       │
       ▼
Outputs: Filings, Reports, Simulations, Visualizations
```

## Cross-Paradigm Entity Mapping

Every entity exists simultaneously in all 4 paradigms, linked by canonical ID:

```
canonical_id: "RST"
  ├─ agent_model_id:     "AGENT_RST"          (Layer 3: ER-ABM)
  ├─ event_model_id:     "ACCOUNT_STATE_RST"  (Layer 4: ET-DSM)
  ├─ dynamics_model_id:  "STOCK_RST_BALANCE"  (Layer 5: SF-SDM)
  └─ hypergraph_node_id: "NODE_RST"           (Layer 6: NS-FH)
```

The `integration` schema in Neon provides the `entity_mappings` table that
binds all paradigm-specific IDs to a single canonical entity.

## Key Design Principles

1. **Single Source of Truth**: This model is canonical. All repos reference it.
2. **Composable Layers**: Each layer can operate independently or compose with others.
3. **Temporal Validity**: Relations have `valid_from`/`valid_to` for point-in-time queries.
4. **Probabilistic Logic**: TruthValue(strength, confidence) on all hypergraph nodes/edges.
5. **Idempotent Sync**: All Neon upserts use ON CONFLICT for safe re-execution.
6. **Forensic Grade**: File hashes, access logs, audit trails on all evidence.
7. **4-Shell Consolidation**: Membrane CoA ensures proper intercompany elimination.

## File Layout

```
zonent/
├── CLAUDE.md                          # Master instructions for all agents
├── model/
│   ├── SYSTEM_MODEL.md                # This file - 7-layer architecture
│   ├── entity-relation/
│   │   └── ER_ABM_SPEC.md             # Agent-Based Model specification
│   ├── event-timeline/
│   │   └── ET_DSM_SPEC.md             # Discrete State Model specification
│   ├── stock-flow/
│   │   └── SF_SDM_SPEC.md             # System Dynamics Model specification
│   ├── hypergraph/
│   │   └── NS_FH_SPEC.md              # Neuro-Symbolic Hypergraph specification
│   ├── integration/
│   │   └── CROSS_PARADIGM_SPEC.md     # Cross-paradigm binding specification
│   ├── membrane-coa/
│   │   └── MEMBRANE_COA_SPEC.md       # 4-shell topology specification
│   └── legal-framework/
│       └── CHAINLEX_SPEC.md           # Legal principle graph specification
├── schema/
│   └── NEON_SCHEMA_REFERENCE.md       # Complete Neon database schema
├── registry/
│   ├── MASTER_ENTITIES.md             # Canonical entity registry
│   ├── MASTER_ACCOUNTS.md             # FNB account registry
│   └── ENTITY_XERO_MAPPING.md        # Xero/QBO mapping with membrane shells
└── docs/
    └── (future: guides, tutorials, API docs)
```
