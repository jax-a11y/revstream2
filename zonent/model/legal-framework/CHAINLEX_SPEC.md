# Legal Framework: ChainLex/LexRex Specification

## Overview

The legal framework layer provides a **hypergraph of legal principles and rules** with
GNN-trainable weighted edges and inference chain support. It maps 63 foundational legal
principles to 2,215 jurisdiction-specific rules across 28 legal domains.

## Architecture

```
Principles (Level 1)  -- 63 foundational legal principles
    │
    ├─ derivation edges (confidence: 0.90-0.95)
    │
    ▼
Rules (Level 2+)      -- 2,215 jurisdiction-specific rules
    │
    ├─ relationship edges
    │
    ▼
Domains (28)           -- Legal domain categories
```

## Core Tables

### scmlex_nodes (2,306 nodes)
```sql
CREATE TABLE scmlex_nodes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    node_id TEXT UNIQUE NOT NULL,
    node_type TEXT NOT NULL CHECK (node_type IN ('principle', 'rule', 'concept', 'domain')),
    level INTEGER,
    name TEXT NOT NULL,
    description TEXT,
    provenance TEXT,              -- Principle-specific
    application_context TEXT,     -- Principle-specific
    jurisdiction TEXT,            -- Rule-specific
    legal_domain TEXT,            -- Rule-specific
    confidence DECIMAL(3,2) DEFAULT 1.0,
    inference_type TEXT,
    domains TEXT[],
    derived_from TEXT[],
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### scmlex_edges (80 edges)
```sql
CREATE TABLE scmlex_edges (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    edge_id TEXT UNIQUE,
    edge_type TEXT NOT NULL CHECK (edge_type IN ('relationship', 'derivation', 'domain_membership')),
    source_node_id TEXT REFERENCES scmlex_nodes(node_id),
    target_node_id TEXT REFERENCES scmlex_nodes(node_id),
    relationship_name TEXT,
    inference_type TEXT,          -- deductive, inductive, abductive, analogical
    confidence_impact DECIMAL(3,2),
    strength DECIMAL(3,2),
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### scmlex_hyperedges (20 hyperedges)
```sql
CREATE TABLE scmlex_hyperedges (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    hyperedge_id TEXT UNIQUE NOT NULL,
    hyperedge_type TEXT NOT NULL,
    source_nodes TEXT[] NOT NULL,
    target_node TEXT,
    target_nodes TEXT[],
    inference_type TEXT,
    confidence_impact DECIMAL(3,2),
    relationship_name TEXT,
    strength DECIMAL(3,2),
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

## GNN Support (Weighted Schema)

### weighted_edges
```sql
weight = repetition_count * avg_confidence * avg_strength
normalized_weight for GNN input
UNIQUE(source_id, target_id, edge_type)
```

### node_embeddings
```
6-dimensional: [4 one-hot node type] + [level] + [confidence]
Stored as FLOAT[] with model_version tracking
```

### inference_chains
```
path: TEXT[]          -- Array of node IDs forming the inference path
path_length: INTEGER
confidence: FLOAT     -- Path-level confidence
gnn_score: FLOAT      -- GNN-predicted relevance
reasoning_steps: TEXT[]
```

### gnn_predictions
```
prediction_type: 'confidence' | 'classification'
predicted_value, actual_value, error
model_version tracking
```

## Query Functions

```sql
-- Find principles by legal domain
SELECT * FROM find_principles_by_domain('trust_law');

-- Find rules derived from a principle
SELECT * FROM find_rules_from_principle('Fiduciary Duty');

-- Full-text search across all nodes
SELECT * FROM search_nodes('intercompany transfer');
```

## Views

```sql
-- Level 1 principles
v_level1_principles

-- Rule counts by jurisdiction
v_rules_by_jurisdiction

-- Principle-to-rule derivation chains
v_principle_rule_derivations

-- Hypergraph statistics
v_hypergraph_statistics
```

## 8 Legal Branches

| Branch | Code | Domain |
|--------|------|--------|
| Civil | civ | Contract, property, damages |
| Criminal | cri | Fraud, theft, forgery |
| Trust | trs | Trust law, fiduciary duty |
| Administrative | adm | SARS, CIPC, regulatory |
| Environmental | env | Environmental compliance |
| Professional Ethics | prof-eth | SAICA, auditor duties |
| Constitutional | con | Rights, equality |
| Commercial | com | Companies Act, insolvency |

## Integration with Case Management

The `legal_principles` table in ad-res-j7 maps ChainLex principles to AD paragraphs:

```sql
CREATE TABLE legal_principles (
    id SERIAL PRIMARY KEY,
    principle_name TEXT NOT NULL UNIQUE,
    principle_location TEXT,         -- e.g., "trs/za/enhanced_v3.scm"
    description TEXT,
    confidence DECIMAL(3,2),
    ad_paragraph_refs TEXT[],        -- Array of AD paragraph numbers
    created_at TIMESTAMP DEFAULT NOW()
);
```

## Source Files
- Schema: `chainlex/hypergraph/database/schema.sql`
- Weighted: `chainlex/hypergraph/database/weighted_schema.sql`
- Integration: `chainlex/hypergraph/db_integration.py`
- Docs: `chainlex/hypergraph/SCHEMA.md`, `chainlex/hypergraph/README.md`
- Neural QL: `chainlex/hypergraph/LEX_HYPERGRAPH_NEURAL_NET_QL.md`
- Mirror: `lexrex/chainlex/hypergraph/` (identical structure)
- Case link: `ad-res-j7/lex/hypergraph/`
