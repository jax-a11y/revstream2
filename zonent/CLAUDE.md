# ZONENT - Zone Enterprise Master Digital Twin

## Purpose

This repository is the **canonical master model** of the Zone Enterprise ecosystem.
It defines the complete digital twin across 7 layers, 4 modeling paradigms, and 5 database schemas.

**Every study, analysis, filing, simulation, and report across ALL repositories MUST reference
this model as the single source of truth for entity definitions, relationships, events, state
machines, stock-flow dynamics, hypergraph topology, and legal framework mappings.**

## Architecture: 7-Layer Composable Model

```
Layer 7: Neural Inference    (GNN + Legal Attention Heads)
Layer 6: Hypergraph          (NS-FH: Neuro-Symbolic Financial Hypergraph)
Layer 5: Stock-Flow          (SF-SDM: System Dynamics Model)
Layer 4: Event-Timeline      (ET-DSM: Discrete State Model)
Layer 3: Entity-Relation     (ER-ABM: Agent-Based Model)
Layer 2: Legal Framework     (ChainLex/LexRex: Legal Principle Graph)
Layer 1: Case Management     (ad-res-j7: Affidavit + Evidence)
```

## Repository Map (Source Repos)

| Repo | Branch | Role |
|------|--------|------|
| **zonent** | main | Master digital twin model (THIS REPO) |
| **fincosys** | main | Financial ecosystem - 4 paradigm models, Neon sync, consolidation |
| **revstream2** | main | Revenue stream analysis - 27 entities, 62 events, 54 relations |
| **ad-res-j7** | main | Legal case management - affidavits, evidence, timeline |
| **chainlex** | main | Legal principle hypergraph - 2,306 nodes, GNN support |
| **lexrex** | main | Legal reasoning engine - ChainLex integration |
| **comcosys** | main | Commercial compliance system |

## Key Conventions

### Entity IDs
- Canonical entity codes: RST, RWD, RSA, SLG, VVA, REZ, AYM, COR, RZA, RZI, FFT, etc.
- Person codes: PF, DJF, JF (directors), PERSON_001-012 (revstream2 aliases)
- Account format: ACC_{account_number} (e.g., ACC_55270035642)
- Cross-paradigm mapping: canonical_id -> agent_model_id, event_model_id, dynamics_model_id, hypergraph_node_id

### Database
- **Neon PostgreSQL**: Project `calm-silence-72212970`, Database `neondb`, Region `us-east-2`
- 7 schemas: entity_relation, event_timeline, stock_flow, hypergraph, integration, consolidated_accounts, fund_flow

### 4-Shell Membrane CoA Topology
- **Arche** (10100): Director personal boundary - excluded from consolidation
- **Agent** (10200-20200): Entity internal operations - included in consolidation
- **Relatio** (10300-70400): Inter-entity group relations - subject to elimination
- **Arena** (40100-69900): External activity - survives consolidation

### Consolidation Hub
- **REZ (Rezonance)** is the consolidation point for all entities

## How to Use This Model

1. **New analysis?** Start from `model/SYSTEM_MODEL.md` for the 7-layer architecture
2. **Need entity data?** Check `registry/` for master entities, accounts, and Xero mappings
3. **Building a query?** Check `schema/` for Neon table definitions and indexes
4. **Writing a filing?** Cross-reference `model/entity-relation/` and `model/event-timeline/`
5. **Running simulations?** Use `model/stock-flow/` for system dynamics parameters
6. **Inference/reasoning?** Use `model/hypergraph/` for symbolic rules and patterns
7. **Consolidation?** Use `model/membrane-coa/` for 4-shell topology and elimination rules

## Refinement Protocol

When ANY repo discovers new entities, events, relations, or corrections:
1. Update the relevant model spec in this repo FIRST
2. Propagate changes to source repos
3. Sync to Neon via fincosys pipeline (Stage 6a)

This ensures the digital twin remains the single source of truth.

## Financial Summary (as of 2026-03-23)

| Metric | Value |
|--------|-------|
| Total Entities | 86+ (persons, orgs, accounts, trusts, platforms, domains) |
| Financial Events | 110,000+ transactions across 39 FNB accounts |
| Case Events | 130 (49 meeting criminal threshold) |
| Bank Statements | 4,353 PDFs + extracted JSON |
| Legal Nodes | 2,306 (63 principles + 2,215 rules across 28 domains) |
| Portfolio Value | R39,155,573.46 (snapshot 2022-12-06) |
| Direct Financial Impact | R10,269,727.90+ |
| Villa Via Capital Extraction | R22,800,000 |
| Bantjies Conflict Debt | R18,685,000 |
| Timeline Span | 1982-2026 |
| Currencies | ZAR, USD, GBP, EUR |
