# Forensic Investigation System - Quick Reference Guide

## Running Investigations

### Basic Command Format
```bash
cd d:\Documents\GitHub\revstream2
python investigate.py --workflow <workflow_name>
```

### Available Workflows

#### 1. **Complete Network Analysis** (Recommended First)
```bash
python investigate.py --workflow complete-analysis
```
**Generates:**
- Full perpetrator hierarchy with scoring
- Financial centrality analysis
- Escalation timeline
- Network structure
- **Output Files:**
  - `complete-analysis_timestamp.json` (data)
  - `2025-137857_FORENSIC_REPORT_timestamp.md` (narrative report)

**Best For:** Understanding the complete conspiracy structure

---

#### 2. **Fund Flow Tracing**
```bash
python investigate.py --workflow fund-tracing
```
**Generates:**
- Transfer chain analysis
- Perpetrator benefits breakdown
- Amount per event calculations
- **Output Files:**
  - `fund-tracing_timestamp.json`
  - `FUND_FLOW_ANALYSIS_timestamp.md`

**Best For:** Tracing money from sources → perpetrators

---

#### 3. **Escalation Timeline**
```bash
python investigate.py --workflow timeline
```
**Generates:**
- Crisis indicators with dates
- Event sequence analysis
- Acceleration pattern detection
- **Output:** Included in complete-analysis data

**Best For:** Understanding consciousness of guilt through rapid response

---

#### 4. **Weak Links & Interrogation Priorities**
```bash
python investigate.py --workflow weak-links
```
**Generates:**
- Node criticality scores (0-100)
- Interrogation target ranking
- Conflict of interest identification
- **Output Files:**
  - `weak-links_timestamp.json`
  - `INTERROGATION_PRIORITIES_timestamp.md`

**Best For:** Planning investigation interrogation sequence

---

## Understanding the Output

### Key Metrics Explained

| Metric | Meaning | Range | Interpretation |
|--------|---------|-------|-----------------|
| **Hierarchy Score** | Entity's position in organizational structure | 0-100 | 70+ = Apex, 40-70 = Facilitator, <40 = Operative |
| **Criticality Score** | How important entity is to network | 0-100 | Higher = more leverage for investigation |
| **Financial Benefit** | Money directly received by perpetrator | R | Direct evidence of participation |
| **Gini Coefficient** | Wealth concentration | 0-1 | 0 = equal, 1 = concentrated (0.206 = high concentration) |
| **Acceleration Factor** | How much activity increased | 1-100x | 12.6x = crisis much more active than baseline |
| **Network Connections** | How many entities linked to this person | 1-27 | Higher = more central to conspiracy |

---

### Key Findings Summary

**Revenue Stream Hijacking (2025-137857)**

- **Total Theft:** R14.546M documented
- **Perpetrators:** 3 identified (1 apex, 2 facilitators)
- **Network:** 27 entities, 54 relationships
- **Period:** March-August 2025 (6-month execution)

### Perpetrator Rankings

1. **Peter Faucitt** - APEX ORCHESTRATOR
   - R10.269M (70.6%)
   - 11 events
   - Score: 70.5/100
   - Role: Trustee authority abuse

2. **Rynette Farrar** - FACILITATOR
   - R4.276M (29.4%)
   - 8 events
   - Score: 54.5/100
   - Role: Payment redirection

3. **Danie Bantjies** - CONFLICTED FACILITATOR
   - R0 direct benefit
   - R18.685M debt motive
   - 3 events (critical: audit dismissal)
   - Score: 81.0/100 (HIGHEST CRITICALITY)
   - Role: Accountant, unknown trustee

---

## Interpreting Reports

### Forensic Report (2025-137857_FORENSIC_REPORT_*.md)

**Section 1: Executive Summary**
- Shows total theft amount and acceleration factor
- Gives quick overview of crisis timeline

**Section 2: Perpetrator Hierarchy**
- APEX: Decision-makers with highest financial benefit and network control
- FACILITATORS: Execution enablers with medium benefit and specific roles
- OPERATIVES: Direct executors (usually none in small conspiracies)

**Section 3: Financial Analysis**
- Gini Coefficient shows how concentrated wealth is
- HIGH concentration = evidence of central control
- Distribution percentages show each perpetrator's share

**Section 4: Escalation Timeline**
- Crisis indicators show when fraud was exposed and cover-up began
- Look for rapid response patterns (evidence destruction within days)

**Section 5: Network Structure**
- Shows entity types (perpetrators, victims, intermediaries, infrastructure)
- Relationship counts show interconnectedness

**Section 6: Legal Significance**
- Organization: Clear hierarchy indicates planning
- Coordination: Multiple perpetrators acting together
- Consciousness of Guilt: Rapid response to exposure
- Motive: Financial gain + debt avoidance

---

### Interrogation Report (INTERROGATION_PRIORITIES_*.md)

**Priority 1 = Highest Leverage Point**
- Look for high criticality scores (70+)
- Identify conflict of interest markers (⚠️)
- People with multiple roles have leverage (they know more)

**Strategy:**
1. Start with Priority 1 (highest criticality)
2. Identify contradictions in their story
3. Use their conflicts of interest against them
4. Work down the priority list

**Example:**
- Danie Bantjies: Criticality 81 + triple conflict + R18.685M motive
- If he talks: Could expose both Peter and Rynette
- Leverage point: His debt to the trust

---

### Fund Flow Report (FUND_FLOW_ANALYSIS_*.md)

**Traces money from:**
1. **Source** - Where legitimate funds came from
2. **Intermediary** - How they moved the money
3. **Perpetrator** - Who ended up with it

**Amount per Event** shows efficiency:
- High = concentrated theft in few events (planned)
- Low = spread out theft (opportunistic)

---

## Advanced Usage

### Comparing Multiple Runs
```bash
# Run investigation at different times
python investigate.py --workflow weak-links
# ... analyze report ...
python investigate.py --workflow weak-links
# Compare outputs in investigation_output/
```

### Automating Regular Analysis
**Windows Task Scheduler:**
1. Create batch file: `run_investigation.bat`
```batch
@echo off
cd d:\Documents\GitHub\revstream2
python investigate.py --workflow complete-analysis
```
2. Schedule to run daily/weekly

### Integration with Legal Document
1. Generate forensic report (complete-analysis)
2. Extract key findings into affidavit
3. Use hierarchy as organizational structure diagram
4. Use fund flow as theft quantification evidence

---

## Troubleshooting

### Issue: ModuleNotFoundError: No module named 'networkx'
**Solution:** System works without NetworkX, but doesn't calculate centrality metrics
- Optional enhancement (not required for Phase 1-3)
- Install if needed: `pip install networkx`

### Issue: FileNotFoundError on data_models/
**Solution:** Ensure you're running from `d:\Documents\GitHub\revstream2` directory
- Data files are in `data_models/entities/`, `relations/`, `events/`, `timelines/`

### Issue: UnicodeEncodeError in output
**Solution:** Already fixed in current version (uses UTF-8 encoding)
- Reports support special characters (⚠️)

---

## File Organization

```
investigation_output/
├── 2025-137857_FORENSIC_REPORT_*.md ← START HERE (narrative report)
├── complete-analysis_*.json (raw data)
├── INTERROGATION_PRIORITIES_*.md (priority ranking)
├── FUND_FLOW_ANALYSIS_*.md (money tracing)
├── fund-tracing_*.json (raw fund data)
├── weak-links_*.json (node criticality data)
└── timeline_*.json (if timeline workflow run)
```

**Recommended Reading Order:**
1. Forensic Report (narrative overview)
2. Interrogation Report (investigation strategy)
3. Fund Flow Report (evidence quantification)
4. JSON files (detailed data for legal review)

---

## Success Indicators

Your investigation is complete when you can:

- [ ] Name the apex perpetrator(s)
- [ ] Calculate total theft amount
- [ ] Explain the conspiracy hierarchy
- [ ] Trace fund flows from source to recipient
- [ ] Identify consciousness of guilt markers
- [ ] Explain perpetrator motives
- [ ] Rank interrogation priorities
- [ ] Present findings in narrative form

**This system helps with all 8!**

---

## Contact & Questions

For system improvements or additional analysis:
- Check INVESTIGATION_WORKFLOWS.md for detailed workflows
- Review Phase Implementation Summary for technical details
- Run any workflow to generate fresh analysis

---

**Ready to investigate? Start with:**
```bash
python investigate.py --workflow complete-analysis
```

**Then read:** `2025-137857_FORENSIC_REPORT_*.md`