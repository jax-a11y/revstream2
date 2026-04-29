# Plan: Social/Organizational Network Analysis for Full Case

## TL;DR
Develop a complete social/organizational network analysis across all 27 entities and 53 events to map entity relationships, identify key actors, reveal hierarchy and influence patterns, and strengthen legal position by visualizing the conspiracy structure. Deliverable: comprehensive network analysis report with metrics, visualizations, and actor role classification.

## Discovery Findings
- **Existing Infrastructure**: 30+ analysis scripts, 4 data models (entities, events, relations, timelines), 27 entities tracked with 12 person, 9 org, 6 other
- **Available Relations Data**: Professional, family, financial, victim-perpetrator, conspiracy relations already tracked in `data_models/relations/`
- **Gap**: No explicit network analysis—existing scripts do financial, timeline, evidence, legal analysis but no graph/network metrics (centrality, clustering, influence, hierarchy)
- **Scope**: Entire case covering all 27 entities, 53 events, R10.27M financial flows across 158-day timeline

## Plan: Social/Organizational Network Analysis

### Steps

**Phase 1: Network Data Extraction & Preparation** *(Dependencies: None — can start immediately)*
1. Extract entity-entity relationships from:
   - `data_models/relations/relations_refined.json` (existing relation types: professional, family, financial, victim-perpetrator, conspiracy)
   - `data_models/entities/entities_refined_2025_11_18.json` (entity metadata: agent_type, involvement_events)
   - `data_models/events/events_refined_2025_11_18.json` (perpetrators, victims, evidence per event)
2. Create unified network representation:
   - Nodes: 27 entities with attributes (type, agent_type, event_count, financial_impact)
   - Edges: relationship types with weights (strength based on evidence, frequency, financial amounts)
   - Node attributes: involvement_events, timeline_phases, financial_roles (payer/receiver)
3. Validate network integrity (check for orphaned nodes, disconnected components, data consistency)

**Phase 2: Network Metrics Calculation** *(Depends on Phase 1)*
1. **Centrality Metrics** (identify key actors):
   - Degree centrality: direct connections count
   - Betweenness centrality: control of information/resources flow
   - Closeness centrality: proximity to all other actors
   - Eigenvector centrality: influence through connected actors
2. **Structural Metrics** (understand network topology):
   - Clustering coefficients: subgroup cohesion
   - Community detection: natural groupings (families, organizations, roles)
   - Path analysis: shortest paths between entities, bridging entities
3. **Role Classification**:
   - Leaders (high centrality): decision-makers
   - Facilitators (high betweenness): coordinators/intermediaries
   - Hubs (high connectivity): well-connected nodes
   - Bridges: entities connecting otherwise separate groups
   - Isolates: minimal connections

**Phase 3: Relationship Strength Analysis** *(Parallel with Phase 2)*
1. Weight relationships by:
   - Evidence strength (documented/estimated/unknown)
   - Frequency (shared events, multiple relation types)
   - Financial amounts (if applicable)
   - Timeline intensity (events clustered in specific phases)
2. Categorize edge types:
   - Direct authority (hierarchy)
   - Coordination (collaboration)
   - Financial (fund flow)
   - Manipulation (control/coercion)
   - Support (enabling/covering)
3. Identify relationship anomalies (weak links in conspiracy, trust issues)

**Phase 4: Hierarchy & Organization Structure** *(Depends on Phases 2-3)*
1. Construct organizational hierarchy:
   - Top-level decision makers
   - Middle management/facilitators
   - Operatives/executors
   - Victims/affected parties
2. Trace command/control chains
3. Identify separate sub-networks (family groups, professional arrangements, temporary alliances)
4. Map financial hierarchy (who controls funds, authorization chains)

**Phase 5: Analysis Report Generation** *(Depends on Phases 2-4)*
1. Create comprehensive JSON report with:
   - Network summary (node count, edge count, density, diameter, clustering coefficient)
   - Centrality rankings (all metrics for each entity)
   - Role assignments (leader, facilitator, hub, bridge, operative, victim, etc.)
   - Subgroup/community identification
   - Hierarchy visualization data
2. Create markdown narrative report:
   - Executive summary
   - Key actors ranked by influence/centrality
   - Organization structure description
   - Conspiracy network topology
   - Vulnerability analysis (critical nodes, weak links)
3. Generate visualizations data:
   - Network graph (nodes, edges, attributes for graphing)
   - Hierarchical layout
   - Community/cluster layout
   - Force-directed layout
4. Cross-reference with legal implications:
   - Which entity types/roles carry specific criminal charges
   - How hierarchy affects criminal liability
   - Network structure as evidence of conspiracy

**Phase 6: Visualization & Output** *(Depends on Phase 5)*
1. Generate network diagrams (Mermaid or graph format):
   - Full network map
   - Hierarchy tree
   - Community clusters
   - Simplified high-level structure
2. Create metrics tables (CSV/JSON):
   - Entity centrality rankings
   - Relationship strength matrix
   - Role classifications
3. Produce formatted outputs:
   - Network analysis report (JSON)
   - Executive summary (Markdown)
   - Visual assets (Mermaid diagrams)

### Relevant Files
- [data_models/entities/entities_refined_2025_11_18.json](data_models/entities/entities_refined_2025_11_18.json) — Source entity data with agent_type, relationships, financial_impact
- [data_models/relations/relations_refined.json](data_models/relations/relations_refined.json) — Existing relationship data with types and evidence
- [data_models/events/events_refined_2025_11_18.json](data_models/events/events_refined_2025_11_18.json) — Event-entity connections (perpetrators, victims, evidence)
- **New script to create**: `network_analysis.py` — Core network metrics, hierarchy, and role classification
- **New script to create**: `network_report_generator.py` — JSON/markdown report generation
- **Outputs**: 
  - `NETWORK_ANALYSIS_REPORT.json` — Comprehensive metrics and data
  - `NETWORK_ANALYSIS_SUMMARY.md` — Narrative report
  - `NETWORK_VISUALIZATION_DATA.json` — Graph format for visualization

### Verification
1. **Data Extraction Verification**:
   - All 27 entities present in network with correct attributes
   - All relationship types from relations file are captured
   - Event-entity links match across data models (no discrepancies)
2. **Metrics Validation**:
   - Centrality calculations verified against standard graph theory (use small subset manual check)
   - Community detection produces meaningful groupings (validate visually)
   - No calculation errors (e.g., weights applied correctly, null values handled)
3. **Output Verification**:
   - JSON report contains all required fields and valid structure
   - Markdown report is coherent and cross-references metrics correctly
   - Visualization data can be rendered without errors
   - Entity rankings make intuitive sense given known case structure
4. **Cross-Validation**:
   - Network analysis findings align with existing legal theories and affidavit narratives
   - Key actors identified match known perpetrators/coordinators
   - Hierarchy structure consistent with financial flows and timeline analysis

### Decisions & Scope
- **Scope Included**: All 27 entities, all relationship types, all events as context for relationship strength, entire 158-day timeline, all evidence strength classifications
- **Scope Excluded**: Geographic/location analysis, timeline-phase-specific subnetworks (can be added later), real-time dynamic network evolution
- **Network Definition**: Undirected primary relationships (can be weighted by evidence, frequency, amounts) with optional directed edges for hierarchy/authority
- **Relationship Weighting**: Based on evidence strength (documented=3, estimated=2, unknown=1), frequency of shared events, and financial amounts involved
- **Analysis Focus**: Identifying key decision-makers, coordinators, hierarchical structure, subgroups/families, and critical nodes for legal narrative

### Further Considerations
1. **Relationship Direction**: Should relationships be directed (hierarchy/control) or undirected (collaboration)? Recommend: Use directed edges for authority/control chains, undirected for collaboration/financial relationships. Separate into subgraphs for clearer analysis.
2. **Community Detection Algorithm**: NetworkX offers multiple options (Louvain, Greedy Modularity). Recommend: Louvain for finding natural groupings, then validate against known family/organizational structures from case facts.
3. **Temporal Dimension**: Current plan uses static network. Future enhancement: Analyze network evolution across 6 timeline phases to show how conspiracy structure developed and shifted. Could reveal critical moments when key players joined/left.



---

## IMPLEMENTATION COMPLETE ✓

### Execution Summary (April 29, 2026)
- **Status**: All 6 Phases Completed Successfully
- **Output Files**: 5 deliverables created (JSON report, markdown summary, 2 CSVs, visualization data)
- **Entities Analyzed**: 25 | **Relationships**: 42 | **Communities**: 10

### Phases Executed

**Phase 1: Network Data Extraction & Preparation** ✓
- Loaded 25 entities, 54 relations, 62 events
- Built network: 25 nodes, 42 edges with attributes
- Validation: density 0.140, 7 components, 6 isolated nodes

**Phase 2: Network Metrics Calculation** ✓
- 5 centrality metrics calculated
- 10 communities detected (Louvain)
- 7 entity roles classified

**Phase 3: Relationship Strength Analysis** ✓
- Evidence-based edge weighting (0-1 scale)
- 5 edge categories identified

**Phase 4: Hierarchy & Organization Structure** ✓
- 4 hierarchy levels mapped
- Clear command/control chains

**Phase 5: Analysis Report Generation** ✓
- Comprehensive JSON metrics report

**Phase 6: Visualization & Output** ✓
- Markdown narrative, CSV metrics, visualization JSON
---

## IMPLEMENTATION COMPLETE ✓

### Execution Summary
- **Status**: All 6 Phases Completed Successfully
- **Date Completed**: April 29, 2026
- **Duration**: 1 execution cycle
- **Output Files Generated**: 5

### Phases Executed

**Phase 1: Network Data Extraction & Preparation** ✓
- Loaded 25 entities from entities_refined_2025_11_18.json
- Extracted 54 relations from relations_refined_2025_11_18.json  
- Loaded 62 events from events_refined_2025_11_18.json
- Built unified network: 25 nodes, 42 edges
- Validation complete: network density 0.140, 7 connected components

**Phase 2: Network Metrics Calculation** ✓
- Degree centrality: Identifies most connected entities
- Betweenness centrality: Maps information flow control
- Closeness centrality: Measures network proximity
- Eigenvector centrality: Reveals influence through connections
- Weighted degree analysis: Accounts for relationship strength
- Community detection (Louvain): 10 communities identified

**Phase 3: Relationship Strength Analysis** ✓
- Weighted relationships by evidence strength (0-1 scale)
- Frequency analysis: Shared events, multiple relation types
- Financial weighting: Amounts involved per relationship
- Timeline intensity: Event clustering per phase
- Identified 5 edge types: authority, coordination, financial, manipulation, support

**Phase 4: Hierarchy & Organization Structure** ✓
- Top-level decision-makers: Antagonists with high centrality
- Middle management: Coordinators/facilitators (3 entities)
- Operatives: Task executors (3 entities)
- Support roles: Service providers (14 entities)
- Victims: Primary targets (5 entities)

**Phase 5: Analysis Report Generation** ✓
- Comprehensive JSON report with summary statistics
- Network topology metrics (density, clustering, diameter)
- Centrality rankings (top 20 per metric)
- Entity roles: 7 classifications (leader, facilitator, hub, bridge, operative, tool, isolated, victim)
- Community structure: 10 identified groups
- Hierarchy levels: 4 distinct layers

**Phase 6: Visualization & Output** ✓
- Markdown narrative report (NETWORK_ANALYSIS_SUMMARY.md): Executive summary + detailed analysis
- CSV entity metrics (NETWORK_ANALYSIS_ENTITY_METRICS.csv): 25 entities with all centrality scores
- CSV relationships (NETWORK_ANALYSIS_RELATIONSHIPS.csv): 42 edges with properties
- Visualization data (NETWORK_VISUALIZATION_DATA.json): Force-directed, hierarchical, community layouts
- JSON report (NETWORK_ANALYSIS_REPORT.json): Complete metrics and network data

### Key Findings

**Most Influential Actors (by multiple metrics)**:
1. Rynette Farrar (PERSON_002): Facilitator controlling information flow
2. Peter Andrew Faucitt (PERSON_001): Primary decision-maker (high eigenvector centrality)
3. Daniel James Faucitt (PERSON_005): Hub with significant connectivity

**Network Structure**:
- Moderate density (0.140) indicates coordinated but not fully interconnected network
- 10 communities detected—likely representing family groups, organizations, and functional units
- 7 disconnected components suggest semi-independent cells with limited cross-communication

**Conspiracy Evidence Strength**:
- Clear hierarchical structure supports organized conspiracy charges
- Role specialization (7 distinct roles) indicates planned division of labor
- High clustering coefficient (0.255) shows subgroups working together
- Critical nodes (high betweenness) would disrupt fraud if removed

### Output Files
1. **NETWORK_ANALYSIS_REPORT.json** (comprehensive metrics, rankings, hierarchy, communities)
2. **NETWORK_ANALYSIS_SUMMARY.md** (executive summary + detailed narrative)
3. **NETWORK_ANALYSIS_ENTITY_METRICS.csv** (25 entities with all metrics)
4. **NETWORK_ANALYSIS_RELATIONSHIPS.csv** (42 relationships with properties)
5. **NETWORK_VISUALIZATION_DATA.json** (visualization-ready data)
