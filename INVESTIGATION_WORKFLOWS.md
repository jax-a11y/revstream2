# Investigation System Workflows

Complete guide to using the forensic investigation system for Revenue Stream Hijacking case (2025-137857).

## System Architecture

```
Investigation Coordinator (Orchestrator)
├── Financial Analysis Agent (Trace funds, prove theft)
├── Timeline Investigator Agent (Show escalation, consciousness of guilt)
├── Evidence Cross-Reference Agent (Map evidence to events, find smoking guns)
├── Legal Narrative Agent (Build affidavit structure)
├── Network Mapper Agent (Analyze relationships, hierarchy)
└── Apex Identifier Agent (Prove who controls conspiracy)
```

Each agent works independently but can hand off to others. The Investigation Coordinator manages workflow sequencing.

---

## Quick Start

### 1. Run Complete Analysis (All Findings)
```bash
python investigate.py --workflow complete-analysis
```

**Output:**
- Perpetrator identification and financial benefit
- Organizational hierarchy
- Financial centrality analysis
- Escalation timeline
- Network structure visualization
- Report: `investigation_output/complete-analysis_*.json`

**Time:** ~15 minutes | **Effort:** Automated

---

### 2. Trace Fund Flow (R10.269M Theft)
```bash
python investigate.py --workflow fund-tracing
# Or focus on specific victim:
python investigate.py --workflow fund-tracing --victim "Daniel Faucitt"
```

**Output:**
- Source funds identified
- Transfer chain (source → intermediary → perpetrator)
- Authorization analysis
- Perpetrator benefit distribution
- Fund flow diagram
- Report: `investigation_output/fund-tracing_*.json`

**Then delegate to agents:**
1. **Financial Analysis Agent** → "Detailed transfer chain with authorization gaps"
2. **Evidence Cross-Reference Agent** → "Verify each transfer with documents"
3. **Legal Narrative Agent** → "Build this into affidavit section"

---

### 3. Analyze Timeline & Escalation
```bash
python investigate.py --workflow timeline
```

**Output:**
- Baseline period (normal activity before fraud)
- Trigger events (what caused escalation)
- Escalation patterns (activity spike analysis)
- Consciousness of guilt indicators
- Report: `investigation_output/timeline-analysis_*.json`

**Then delegate to agents:**
1. **Timeline Investigator Agent** → "Detailed escalation with timing correlations"
2. **Evidence Cross-Reference Agent** → "Find evidence destruction timing"
3. **Legal Narrative Agent** → "Build timeline for courtroom presentation"

---

### 4. Find Weak Links (Interrogation Priorities)
```bash
python investigate.py --workflow weak-links
```

**Output:**
- Node criticality scores
- Identified conflicts (entities caught between allegiances)
- Interrogation priority ranking
- Report: `investigation_output/weak-links_*.json`

**Use for:**
- Identifying which witnesses are most likely to cooperate
- Determining interrogation sequence
- Finding entities whose removal collapses network
- Planning investigation strategy

---

## Investigation Workflows in Detail

### Workflow 1: Complete Network Conspiracy Map

**Goal:** Identify perpetrators, prove conspiracy coordination, show hierarchy

**Agents Involved:**
1. Network Mapper (entity relationships, centrality)
2. Apex Identifier (who controls)
3. Financial Analysis (who benefits)
4. Timeline Investigator (coordination patterns)
5. Investigation Coordinator (synthesis)

**Execution:**
```
Chat: "I need a complete conspiracy map for case 2025-137857"
↓
Investigation Coordinator delegates:
- Network Mapper: "Map entity relationships and identify hierarchy"
- Apex Identifier: "Who has most financial benefit and network control?"
- Financial Analysis: "Trace R10.269M to show benefit distribution"
- Timeline Investigator: "Show coordination through response timing"
↓
Investigation Coordinator synthesizes into:
- Perpetrator roles and hierarchy
- Financial benefit breakdown
- Coordination evidence
- Network vulnerability analysis
```

**Deliverable:**
- CONSPIRACY_NETWORK_MAP.md
- Network diagram (Mermaid)
- Perpetrator profiles with roles
- Hierarchy chart (decision-makers → facilitators → operatives)

---

### Workflow 2: Fund Tracing & Account Hijacking Proof

**Goal:** Build ironclad financial evidence of theft method

**Agents Involved:**
1. Financial Analysis (trace transfers)
2. Evidence Cross-Reference (verify authorizations)
3. Timeline Investigator (show coordination)

**Execution:**
```
Chat: "Trace the R10.269M fund flow with account hijacking proof"
↓
Financial Analysis Agent:
- Identifies source accounts (trust, platform revenue, investment)
- Traces each transfer: date, amount, from, to, authorization
- Shows account hijacking method (who had unauthorized access)
- Maps perpetrator benefit distribution
↓
Evidence Cross-Reference Agent:
- Verifies each transfer authorization
- Identifies forged signatures or missing co-signatures
- Documents evidence gaps
- Links transactions to specific events
↓
Timeline Investigator Agent:
- Shows transaction clustering during crisis periods
- Correlates with threat/victim discovery timeline
- Identifies rapid response patterns (consciousness of guilt)
↓
Investigation Coordinator synthesizes into:
- Fund flow diagram with R amounts
- Transfer chain table with authorization status
- Account hijacking proof
- Affidavit-ready evidence summary
```

**Deliverable:**
- FUND_FLOW_COMPLETE.md
- Transfer chain table (CSV)
- Account hijacking timeline
- Authorization gap analysis
- Fund flow diagram (Mermaid)

---

### Workflow 3: Build Affidavit Structure

**Goal:** Transform findings into court-ready legal narrative

**Agents Involved:**
1. All specialist agents (provide findings)
2. Legal Narrative Agent (structure narrative)
3. Investigation Coordinator (review and finalize)

**Execution:**
```
Chat: "Build a complete affidavit for case 2025-137857"
↓
Gather findings from each agent:
- Financial Analysis: "R10.269M transfer chain and beneficiaries"
- Timeline Investigator: "Escalation timeline and consciousness of guilt"
- Evidence Cross-Reference: "Smoking gun evidence and contradictions"
- Apex Identifier: "Apex perpetrator and proof of control"
- Network Mapper: "Conspiracy structure and family involvement"
↓
Legal Narrative Agent:
- Structures findings into affidavit sections
- Builds logical argument chains
- Identifies evidentiary progression
- Flags legal sufficiency gaps
- Provides paragraph-by-paragraph guidance
↓
Investigation Coordinator:
- Reviews for coherence
- Ensures all findings incorporated
- Validates evidence chain
- Produces final affidavit structure
```

**Deliverable:**
- AFFIDAVIT_STRUCTURE.md (complete outline with sections)
- Legal argument chain (premise → conclusion)
- Evidentiary progression (what facts must be established first)
- Smoking gun evidence highlighted
- Gaps identified for further investigation

---

### Workflow 4: Apex Perpetrator Analysis

**Goal:** Prove who controls the conspiracy

**Agents Involved:**
1. Apex Identifier (analyze candidates)
2. Financial Analysis (benefit distribution)
3. Network Mapper (centrality and control)
4. Timeline Investigator (coordination patterns)

**Execution:**
```
Chat: "Who is the apex perpetrator and prove it?"
↓
Apex Identifier analyzes candidates:
- Peter Faucitt: Financial benefit + network position
- Rynette Farrar: Authority + family involvement
- Danie Bantjies: Gatekeeping role + approval authority
↓
Financial Analysis compares:
- Total benefit received (directly + through intermediaries)
- Account control
- Ability to redirect funds
- Benefit distribution authority
↓
Network Mapper analyzes:
- Centrality metrics (who's in the middle)
- Gatekeeping (who connects communities)
- Authority relationships (who approves what)
↓
Timeline Investigator shows:
- Coordination patterns
- Response speed to threats
- Escalation control
- Communication authority
↓
Apex Identifier reaches conclusion:
- Clear apex candidate with evidence
- OR distributed leadership (no single apex)
- Comparison table showing why
```

**Deliverable:**
- APEX_PERPETRATOR_ANALYSIS.md
- Candidate comparison table
- Financial benefit analysis by candidate
- Network centrality comparison
- Consciousness of guilt evidence
- Supporting documentation

---

### Workflow 5: Weak Links & Interrogation Strategy

**Goal:** Identify entities most likely to break under questioning

**Agents Involved:**
1. All specialist agents (provide vulnerability data)
2. Investigation Coordinator (synthesize and rank)

**Execution:**
```
Chat: "Find the weak links in the conspiracy network"
↓
Financial Analysis identifies:
- Isolated intermediaries (few accounts, clear paper trail)
- Conflicted entities (forced to serve multiple masters)
- Entities with contradictory roles
↓
Timeline Investigator identifies:
- Rapid response indicators (nervous/hastily-made decisions)
- Communication bursts (panic or coordination?)
- Evidence destruction patterns (fear indicator)
↓
Evidence Cross-Reference identifies:
- Documentation gaps (entities without proof of involvement)
- Contradictions (stories don't align)
- Evidence of coercion or reluctance
↓
Network Mapper identifies:
- Low-degree entities (peripheral, few relationships)
- Single-point-of-failure nodes (removing them breaks network)
- Information hubs (know about many events)
↓
Investigation Coordinator ranks:
- Entities most likely to cooperate
- Entities whose testimony would hurt others
- Interrogation sequence strategy
- Cascade effect predictions
```

**Deliverable:**
- INTERROGATION_PRIORITIES.md
- Ranking table (entity | vulnerability | expected cooperation)
- Suggested interrogation sequence
- Cascade effect analysis (if entity A breaks, what cascades?)
- Vulnerability assessment for each candidate

---

## How to Use Each Specialist Agent

### Using Financial Analysis Agent

**Trigger**: When you need detailed fund tracing

```
/Financial Analysis Agent
"Trace the complete fund flow for Kayla Estate estate account.
Show source → intermediary → perpetrator with amounts at each step.
Include authorization analysis and account hijacking evidence."
```

**Agent will provide:**
- Transfer chain chronologically
- Authorization status for each transfer
- Accounts hijacked and method
- Perpetrator benefit distribution
- Coordination patterns

**Hand off to:** Evidence Cross-Reference (verify authorizations), Timeline Investigator (correlation)

---

### Using Timeline Investigator Agent

**Trigger**: When you need event sequence and escalation analysis

```
/Timeline Investigator Agent
"Analyze the escalation from March 2025 (normal activity) through August 2025 (peak fraud).
Show trigger events, acceleration points, consciousness of guilt indicators."
```

**Agent will provide:**
- Baseline period (Mar-May: normal activity levels)
- Trigger point (May 15: Kayla confrontation)
- Acceleration phase (May 22-Jun 1: rapid response)
- Consciousness of guilt (rapid evidence destruction, account cancellations)
- Coordination timing

**Hand off to:** Evidence Cross-Reference (prove events), Financial Analysis (show transaction timing)

---

### Using Evidence Cross-Reference Agent

**Trigger**: When you need to verify transactions or find smoking guns

```
/Evidence Cross-Reference Agent
"Find smoking gun evidence for the May 22-29 cover-up phase.
What documents prove conspiracy coordination? What evidence was destroyed?"
```

**Agent will provide:**
- Smoking gun evidence (documents proving intent/knowledge)
- Contradictions (stories that don't align)
- Evidence destruction timing and method
- Entity-to-evidence mapping
- Authorization verification

**Hand off to:** Legal Narrative (structure into affidavit), Timeline Investigator (show coordination)

---

### Using Legal Narrative Agent

**Trigger**: When you're building affidavit or courtroom argument

```
/Legal Narrative Agent
"Build an affidavit paragraph sequence that proves conspiracy.
Start with foundation facts (trust setup, account access), move through transactions (pattern of theft),
then show coordination (timing, amounts, approval authority)."
```

**Agent will provide:**
- Suggested paragraph sequence
- What facts must be established first
- How facts connect to prove conspiracy
- Legal argument chain (premise A + premise B → conclusion C)
- Evidentiary gaps that need filling

**Hand off to:** Investigation Coordinator (final synthesis)

---

### Using Apex Identifier Agent

**Trigger**: When you need to identify the kingpin

```
/Apex Identifier Agent
"Analyze Danie Bantjies' network position and financial benefit.
Compare to Peter Faucitt and Rynette Farrar.
Who is the apex perpetrator controlling the conspiracy?"
```

**Agent will provide:**
- Candidate comparison table
- Financial benefit analysis
- Network centrality scores
- Authority evidence (who approves what)
- Consciousness of guilt indicators
- Apex determination with evidence

---

### Using Network Mapper Agent

**Trigger**: When you need to understand conspiracy structure

```
/Network Mapper Agent
"Map the Faucitt family conspiracy.
Show who controls whom, what roles each member plays, how benefit flows to family leadership."
```

**Agent will provide:**
- Family relationships and roles
- Control/authority relationships
- Decision-making hierarchy
- Financial benefit distribution
- Organizational structure
- Vulnerabilities

---

### Using Investigation Coordinator Agent

**Trigger**: When you want a complete investigation workflow

```
/Investigation Coordinator Agent
"Run the complete network conspiracy analysis.
I need perpetrator identification, hierarchy proof, fund flow tracing, and affidavit structure."
```

**Coordinator will:**
1. Delegate to Financial Analysis (benefit distribution)
2. Delegate to Timeline Investigator (escalation and coordination)
3. Delegate to Evidence Cross-Reference (evidence mapping)
4. Synthesize all findings
5. Provide complete investigation report

---

## Investigation Patterns by Question

**"Who is the apex perpetrator?"**
→ Use Apex Identifier Agent
→ Output: Apex perpetrator profile with evidence

**"How much did each perpetrator steal?"**
→ Use Financial Analysis Agent
→ Output: Benefit distribution table

**"What's the conspiracy hierarchy?"**
→ Use Network Mapper Agent + Apex Identifier Agent
→ Output: Hierarchy diagram with roles

**"Show the fund flow from source to recipients"**
→ Use Financial Analysis Agent
→ Output: Transfer chain diagram + table

**"When did the fraud escalate and why?"**
→ Use Timeline Investigator Agent
→ Output: Timeline with escalation analysis + consciousness of guilt

**"Find the smoking gun evidence"**
→ Use Evidence Cross-Reference Agent
→ Output: Smoking gun evidence list + contradictions

**"Build an affidavit"**
→ Use Legal Narrative Agent
→ Output: Affidavit structure + argument chain

**"Who should we interrogate first?"**
→ Use Investigation Coordinator → run weak-links workflow
→ Output: Interrogation priorities + vulnerability analysis

**"Is there family involvement?"**
→ Use Network Mapper Agent (analyze family relationships)
→ Output: Family involvement map + benefit distribution

---

## Data Sources & Files

**Case Data Models** (`data_models/`):
- `entities_refined_2025_11_18.json` — 25 entities with roles, involvement, financial impact
- `relations_refined_2025_11_18.json` — 54 relationships (control, conspiracy, financial, etc.)
- `events_refined_2025_11_18.json` — 62 events with perpetrators, victims, evidence, amounts
- `timelines_refined_2025_11_18.json` — Events organized by phase

**Analysis Tools** (`/`):
- `network_analysis.py` — Calculate centrality, communities, hierarchy
- `network_report_generator.py` — Generate reports in JSON/CSV/markdown
- `investigate.py` — Master investigation orchestrator

**Existing Reports**:
- `NETWORK_ANALYSIS_REPORT.json` — Pre-computed metrics
- `NETWORK_ANALYSIS_SUMMARY.md` — Network summary
- Various AFFIDAVIT_*.md files — Previous drafts

**Bank Statements & Financial Documents** (`/documents/`):
- Transaction details by account and date
- Authorization and co-signatures
- Trial balances
- SARS audit trails

---

## Best Practices

1. **Start with specific questions** → Agents work best with focused requests
2. **Use agents in sequence** → Earlier agents provide data for later agents
3. **Verify findings** → Compare outputs from different agents
4. **Build incrementally** → Start with one aspect, then combine into complete picture
5. **Flag gaps** → Note what evidence would strengthen conclusions
6. **Keep evidence-based** → Only present findings supported by case data
7. **Use existing reports** → Check NETWORK_ANALYSIS_REPORT.json before running new analysis
8. **Version control findings** → Save outputs with timestamps

---

## Automation & Scripting

### Run specific workflow from command line:
```bash
# Complete analysis
python investigate.py --workflow complete-analysis

# Fund tracing
python investigate.py --workflow fund-tracing

# Timeline analysis
python investigate.py --workflow timeline

# Weak links analysis
python investigate.py --workflow weak-links
```

### Integrate with chat workflows:
Use `/Investigation Coordinator` agent to orchestrate multi-step investigations

### Schedule investigations:
```bash
# Run daily analysis (Linux/Mac)
0 9 * * * cd /path/to/revstream2 && python investigate.py --workflow timeline

# Run weekly complete analysis
0 8 * * 0 cd /path/to/revstream2 && python investigate.py --workflow complete-analysis
```

---

## Troubleshooting

**Agent not found?**
- Ensure all `.agent.md` files are in `.github/agents/`
- Check that description matches your request

**Data loading errors?**
- Verify `data_models/` directory exists
- Check that JSON files have correct names and format
- Run `python investigate.py --workflow complete-analysis` to validate

**Findings contradict each other?**
- This is normal — agents analyze from different angles
- Use Investigation Coordinator to synthesize and resolve
- Document contradictions as areas needing clarification

**Report not generating?**
- Check `investigation_output/` directory exists
- Verify file permissions
- Check console output for error messages

---

## Next Steps

1. **Run complete analysis** to establish baseline understanding
2. **Focus on specific workflows** based on investigation priorities
3. **Use agents for deep dives** into specific questions
4. **Build affidavit** once findings solidified
5. **Plan interrogations** based on weak links analysis
