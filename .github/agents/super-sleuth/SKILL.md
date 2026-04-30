---
name: "super-sleuth"
description: "Guides forensic network investigation for complex fraud/conspiracy cases using structured, evidence-based analysis."
---

# Super-Sleuth Network Investigation Skill

## Purpose
This skill enables forensic network investigation for complex fraud and conspiracy cases, using structured, evidence-based analysis. It guides the user through mapping entity relationships, identifying key actors, tracing fund flows, and revealing conspiracy patterns, based on documented case data.

## Workflow Steps
1. **Define Investigation Goal**
   - Specify what aspect to investigate (e.g., key actors, fund flows, family connections, hierarchy).
2. **Access Case Data**
   - Load entities, relationships, events, and timelines from the evidence cache.
3. **Analyze Network**
   - Map connections, calculate network metrics (centrality, communities, hierarchy), and identify roles.
4. **Trace Evidence**
   - Link entities to events, financial flows, and supporting documents.
5. **Synthesize Findings**
   - Structure findings with question, data accessed, key discoveries, supporting evidence, conspiracy implications, connections to other findings, and next steps.
6. **Iterate or Branch**
   - Based on findings, choose next investigation angle or refine the current question.

## Decision Points
- What is the investigation focus? (entity, relationship, fund flow, pattern)
- Is the evidence direct or circumstantial?
- Are there ambiguous connections needing clarification?
- Does the pattern fit known conspiracy structures?

## Quality Criteria
- All findings are supported by documented case data (no speculation or fake evidence)
- Outputs are structured, clear, and reference specific entities, events, and evidence
- Investigation steps are reproducible and auditable
- Legal judgments are avoided; only evidence and patterns are presented

## Completion Checks
- Top perpetrators and their roles are identified
- Conspiracy hierarchy is mapped
- Fund flows are traced with intermediaries
- Family involvement and escalation timing are explained
- Weak links and legal narrative are outlined

## Example Prompts
- "Map the network around [Entity Name]"
- "Trace the flow of funds from source to recipient"
- "Identify the key actors in the conspiracy hierarchy"
- "Show all events involving [Entity] as perpetrator or victim"
- "Reveal family connections and joint benefit patterns"

## Related Customizations
- Visualization skill for network graphs
- Timeline analysis skill for escalation patterns
- Evidence cross-referencing skill

## Scope
- Workspace-scoped: Only operates on the Revenue Stream Hijacking case data and analysis infrastructure

---
This skill is designed for use with the Super-Sleuth agent. For best results, pair with network analysis and report generation tools already present in the workspace.