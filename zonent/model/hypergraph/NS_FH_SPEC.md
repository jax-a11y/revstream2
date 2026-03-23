# Hypergraph: Neuro-Symbolic Financial Hypergraph (NS-FH) Specification

## Overview

The NS-FH paradigm combines **symbolic knowledge representation** with **neural embeddings**
and **probabilistic inference**. Unlike ordinary graphs, hyperedges can connect any number
of nodes simultaneously, enabling representation of multi-party financial relationships.

## Node Types
```
ENTITY    # Organizations, persons, accounts
CONCEPT   # Abstract concepts (ownership, fraud)
VALUE     # Numerical values (amounts, ratios)
TEMPORAL  # Dates, periods, deadlines
RELATION  # Reified relationships
```

## Core Classes

### HyperNode
```python
@dataclass
class HyperNode:
    id: str
    node_type: NodeType
    label: str
    attributes: Dict[str, Any]
    embedding: Optional[np.ndarray]  # 64-dim vector
    truth_value: TruthValue          # (strength, confidence)
```

### HyperEdge
```python
@dataclass
class HyperEdge:
    id: str
    edge_type: str            # OWNERSHIP, TRANSACTION, PORTFOLIO_COMPOSITION, etc.
    nodes: List[str]          # Can connect ANY number of nodes
    roles: Dict[str, str]     # node_id -> role in this edge
    attributes: Dict[str, Any]
    truth_value: TruthValue
    tensor_representation: Optional[np.ndarray]

    def arity(self) -> int    # Number of connected nodes
```

### TruthValue (Probabilistic Logic Networks)
```python
@dataclass
class TruthValue:
    strength: float    # 0.0 - 1.0
    confidence: float  # 0.0 - 1.0

    def conjunction(other)  # AND
    def disjunction(other)  # OR
    def negation()          # NOT
```

### SymbolicRule (Datalog-like)
```python
@dataclass
class SymbolicRule:
    name: str
    head: Tuple[str, List[str]]           # (predicate, [variables])
    body: List[Tuple[str, List[str]]]     # conditions
    confidence: float
```

## Sample Symbolic Rules

```
Portfolio Health Assessment
  HEAD: portfolio_status = HEALTHY(X)
  BODY: total_zar_combined > 30,000,000
  CONFIDENCE: 0.9

Diversification Check
  HEAD: diversification_status = WELL_DIVERSIFIED(X)
  BODY: account_count >= 15 AND currency_count >= 3
  CONFIDENCE: 0.85

Interest Accrual
  BODY: account.type == 'Money On Call' AND account.balance > 0
  CONFIDENCE: 0.95
```

## Sample Hyperedges

```
HE_DAY_TO_DAY_SNAPSHOT_239 (PORTFOLIO_COMPOSITION)
  Nodes: [8 accounts]
  Total Value: R10,064,170.30

HE_SAVINGS_SNAPSHOT_239 (PORTFOLIO_COMPOSITION)
  Nodes: [5 accounts]
  Total Value: R29,091,403.16

HE_PORTFOLIO_SNAPSHOT_239 (COMPLETE_PORTFOLIO)
  Nodes: [temporal + value nodes]
  Total Accounts: 20
  Source: BFNBOView221206.pdf
```

## Inference Operations

```python
class NeuroSymbolicHypergraph:
    # Similarity: cosine distance between node embeddings
    def compute_similarity(node_id1, node_id2) -> float

    # Pattern matching: query edges by type with constraints
    def query_pattern(edge_type, constraints) -> List[HyperEdge]

    # Find similar nodes above threshold
    def find_similar_nodes(node_id, threshold, node_type) -> List[(id, sim)]
```

## ChainLex Legal Hypergraph (Layer 2 Integration)

The legal framework adds a second hypergraph layer:

```sql
scmlex_nodes:      2,306 nodes (63 principles + 2,215 rules + 28 domains)
scmlex_edges:      80 edges (21 derivation + 59 relationship)
scmlex_hyperedges: 20 hyperedges (multi-node legal relationships)
```

### Weighted Edges for GNN
```sql
weighted_edges:
  weight = repetition_count * avg_confidence * avg_strength
  normalized_weight for GNN input

node_embeddings:
  embedding FLOAT[]           -- 6-dim: 4 one-hot type + level + confidence
  embedding_dim INTEGER

inference_chains:
  path TEXT[]                 -- Array of node IDs
  path_length INTEGER
  confidence FLOAT
  gnn_score FLOAT
```

## EchoSelf Extension (Deep Tree Echo)

The echoself subsystem adds identity-aware hypergraph processing:

```
identity_role: observer, narrator, guide, oracle, fractal
memory_type:   declarative, procedural, episodic, intentional
hyperedge_type: symbolic, temporal, causal, feedback, pattern, entropy
```

With activation propagation, synergy metrics, and pattern language (OEIS patterns).

## Neon Schema

```sql
-- Schema: hypergraph
CREATE TABLE nodes (
    id TEXT PRIMARY KEY,
    node_type TEXT NOT NULL,
    label TEXT NOT NULL,
    attributes JSONB DEFAULT '{}',
    embedding REAL[],
    truth_strength DECIMAL(3,2) DEFAULT 1.0,
    truth_confidence DECIMAL(3,2) DEFAULT 1.0,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE hyperedges (
    id TEXT PRIMARY KEY,
    edge_type TEXT NOT NULL,
    node_ids TEXT[] NOT NULL,
    roles JSONB DEFAULT '{}',
    attributes JSONB DEFAULT '{}',
    truth_strength DECIMAL(3,2) DEFAULT 1.0,
    truth_confidence DECIMAL(3,2) DEFAULT 1.0,
    tensor_representation REAL[],
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE symbolic_rules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT UNIQUE NOT NULL,
    head_predicate TEXT,
    head_variables TEXT[],
    body JSONB,
    confidence DECIMAL(3,2),
    tensor_notation TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE type_hierarchy (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    subtype TEXT NOT NULL,
    supertype TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
```

## Source Files
- Model: `fincosys/models/hypergraph/neuro_symbolic_hypergraph.py`
- Data: `fincosys/hypergraph/hypergraph_data.json`
- SQL: `fincosys/sql_batches/09_hg_nodes.sql` (1,735 lines)
- SQL: `fincosys/sql_batches/10_hyperedges.sql` (570 lines)
- SQL: `fincosys/sql_batches/11_symbolic_rules.sql` (56 lines)
- ChainLex: `chainlex/hypergraph/database/schema.sql`
- Weighted: `chainlex/hypergraph/database/weighted_schema.sql`
- EchoSelf: `ad-res-j7/UPDATED_DRAFTS/analysis-main/deep_tree_echo_neon_migration.sql`
