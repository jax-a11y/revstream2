#!/usr/bin/env python3
"""
Investigation Orchestrator
Master script for running complete forensic investigations on Revenue Stream Hijacking case (2025-137857)

Usage:
    python investigate.py --workflow complete-analysis
    python investigate.py --workflow fund-tracing --output fund-flow-analysis.md
    python investigate.py --workflow timeline --perpetrator "Rynette Farrar"
"""

import json
import argparse
from pathlib import Path
from datetime import datetime
import subprocess
import sys

# Configuration
CASE_ID = "2025-137857"
DATA_DIR = Path("data_models")
REPORT_DIR = Path("reports")
OUTPUT_DIR = Path("investigation_output")

# Create output directory
OUTPUT_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)

def load_case_data():
    """Load all case data models"""
    data = {}
    try:
        with open(DATA_DIR / "entities_refined_2025_11_18.json") as f:
            data['entities'] = json.load(f)
        with open(DATA_DIR / "relations_refined_2025_11_18.json") as f:
            data['relations'] = json.load(f)
        with open(DATA_DIR / "events_refined_2025_11_18.json") as f:
            data['events'] = json.load(f)
        with open(DATA_DIR / "timelines_refined_2025_11_18.json") as f:
            data['timelines'] = json.load(f)
        print(f"✓ Loaded case data: {len(data['entities'])} entities, {len(data['relations'])} relationships, {len(data['events'])} events")
        return data
    except FileNotFoundError as e:
        print(f"✗ Failed to load case data: {e}")
        sys.exit(1)

def run_complete_analysis(data):
    """Run complete network conspiracy analysis"""
    print("\n" + "="*60)
    print("WORKFLOW: Complete Network Conspiracy Analysis")
    print("="*60)
    
    output = {
        "case_id": CASE_ID,
        "workflow": "complete-analysis",
        "timestamp": datetime.now().isoformat(),
        "findings": {}
    }
    
    # Step 1: Identify key perpetrators
    print("\n[1/5] Analyzing perpetrator network and financial benefits...")
    perpetrators = analyze_perpetrators(data)
    output["findings"]["perpetrators"] = perpetrators
    
    # Step 2: Analyze hierarchy
    print("[2/5] Identifying organizational hierarchy...")
    hierarchy = analyze_hierarchy(data, perpetrators)
    output["findings"]["hierarchy"] = hierarchy
    
    # Step 3: Financial centrality
    print("[3/5] Computing financial centrality and benefit distribution...")
    financials = analyze_financial_centrality(data, perpetrators)
    output["findings"]["financial_analysis"] = financials
    
    # Step 4: Timeline escalation
    print("[4/5] Analyzing escalation timeline and consciousness of guilt...")
    escalation = analyze_escalation(data)
    output["findings"]["escalation"] = escalation
    
    # Step 5: Network structure
    print("[5/5] Generating network structure visualization...")
    network = analyze_network_structure(data)
    output["findings"]["network_structure"] = network
    
    # Generate report
    report_file = generate_report(output, "complete-analysis")
    print(f"\n✓ Report saved to: {report_file}")
    
    return output

def run_fund_tracing(data, victim=None):
    """Trace R10.269M fund flow from source to perpetrators"""
    print("\n" + "="*60)
    print("WORKFLOW: Fund Flow Tracing")
    print("="*60)
    
    output = {
        "case_id": CASE_ID,
        "workflow": "fund-tracing",
        "timestamp": datetime.now().isoformat(),
        "findings": {}
    }
    
    print("\n[1/4] Identifying source funds...")
    sources = identify_source_funds(data, victim)
    output["findings"]["sources"] = sources
    
    print("[2/4] Tracing transfer chain...")
    transfers = trace_transfer_chain(data, sources)
    output["findings"]["transfers"] = transfers
    
    print("[3/4] Analyzing perpetrator benefit distribution...")
    distribution = analyze_benefit_distribution(data, transfers)
    output["findings"]["distribution"] = distribution
    
    print("[4/4] Generating fund flow diagram...")
    diagram = generate_fund_flow_diagram(transfers)
    output["findings"]["diagram"] = diagram
    
    report_file = generate_report(output, "fund-tracing")
    print(f"\n✓ Report saved to: {report_file}")
    
    return output

def run_timeline_analysis(data):
    """Analyze timeline, escalation, and consciousness of guilt"""
    print("\n" + "="*60)
    print("WORKFLOW: Timeline & Escalation Analysis")
    print("="*60)
    
    output = {
        "case_id": CASE_ID,
        "workflow": "timeline-analysis",
        "timestamp": datetime.now().isoformat(),
        "findings": {}
    }
    
    print("\n[1/4] Establishing baseline activity...")
    baseline = extract_baseline_period(data)
    output["findings"]["baseline"] = baseline
    
    print("[2/4] Identifying trigger events...")
    triggers = identify_trigger_events(data)
    output["findings"]["triggers"] = triggers
    
    print("[3/4] Analyzing escalation patterns...")
    escalation = analyze_escalation_patterns(data, triggers)
    output["findings"]["escalation"] = escalation
    
    print("[4/4] Computing consciousness of guilt indicators...")
    guilt = analyze_consciousness_of_guilt(data, escalation)
    output["findings"]["guilt_indicators"] = guilt
    
    report_file = generate_report(output, "timeline-analysis")
    print(f"\n✓ Report saved to: {report_file}")
    
    return output

def run_weak_links_analysis(data):
    """Identify weak links and interrogation priorities"""
    print("\n" + "="*60)
    print("WORKFLOW: Weak Links & Interrogation Priorities")
    print("="*60)
    
    output = {
        "case_id": CASE_ID,
        "workflow": "weak-links",
        "timestamp": datetime.now().isoformat(),
        "findings": {}
    }
    
    print("\n[1/3] Calculating node criticality...")
    criticality = calculate_node_criticality(data)
    output["findings"]["criticality"] = criticality
    
    print("[2/3] Identifying conflicted entities...")
    conflicts = identify_conflicts(data)
    output["findings"]["conflicts"] = conflicts
    
    print("[3/3] Ranking interrogation priorities...")
    priorities = rank_priorities(data, criticality, conflicts)
    output["findings"]["priorities"] = priorities
    
    report_file = generate_report(output, "weak-links")
    print(f"\n✓ Report saved to: {report_file}")
    
    return output

# Helper functions (placeholder implementations)

def analyze_perpetrators(data):
    perpetrators = {}
    for entity in data['entities']:
        if entity.get('agent_type') == 'perpetrator':
            perpetrators[entity['id']] = {
                'name': entity['name'],
                'financial_impact': entity.get('financial_impact', 0),
                'involvement_events': entity.get('involvement_events', []),
                'relationships': [r for r in data['relations'] if r['source'] == entity['id'] or r['target'] == entity['id']]
            }
    return perpetrators

def analyze_hierarchy(data, perpetrators):
    return {"status": "placeholder", "details": "Hierarchy analysis would go here"}

def analyze_financial_centrality(data, perpetrators):
    return {"status": "placeholder", "details": "Financial centrality analysis would go here"}

def analyze_escalation(data):
    return {"status": "placeholder", "details": "Escalation analysis would go here"}

def analyze_network_structure(data):
    return {"status": "placeholder", "details": "Network structure analysis would go here"}

def identify_source_funds(data, victim=None):
    sources = []
    for entity in data['entities']:
        if entity.get('agent_type') in ['trust', 'account', 'platform']:
            sources.append({'entity': entity['name'], 'type': entity['agent_type']})
    return sources

def trace_transfer_chain(data, sources):
    return {"status": "placeholder", "details": "Transfer chain analysis would go here"}

def analyze_benefit_distribution(data, transfers):
    return {"status": "placeholder", "details": "Benefit distribution analysis would go here"}

def generate_fund_flow_diagram(transfers):
    return {"status": "placeholder", "details": "Fund flow diagram would go here"}

def extract_baseline_period(data):
    return {"status": "placeholder", "details": "Baseline period extraction would go here"}

def identify_trigger_events(data):
    return {"status": "placeholder", "details": "Trigger event identification would go here"}

def analyze_escalation_patterns(data, triggers):
    return {"status": "placeholder", "details": "Escalation pattern analysis would go here"}

def analyze_consciousness_of_guilt(data, escalation):
    return {"status": "placeholder", "details": "Consciousness of guilt analysis would go here"}

def calculate_node_criticality(data):
    return {"status": "placeholder", "details": "Node criticality calculation would go here"}

def identify_conflicts(data):
    return {"status": "placeholder", "details": "Conflict identification would go here"}

def rank_priorities(data, criticality, conflicts):
    return {"status": "placeholder", "details": "Priority ranking would go here"}

def generate_report(output, workflow_type):
    """Generate investigation report"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = OUTPUT_DIR / f"{workflow_type}_{timestamp}.json"
    
    with open(report_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    return report_file

def main():
    parser = argparse.ArgumentParser(
        description="Forensic investigation orchestrator for Revenue Stream Hijacking case"
    )
    parser.add_argument(
        "--workflow",
        choices=["complete-analysis", "fund-tracing", "timeline", "weak-links"],
        default="complete-analysis",
        help="Investigation workflow to run"
    )
    parser.add_argument(
        "--victim",
        help="Specific victim to focus on (for fund-tracing)"
    )
    parser.add_argument(
        "--output",
        help="Output report filename"
    )
    
    args = parser.parse_args()
    
    print(f"\n{'='*60}")
    print(f"FORENSIC INVESTIGATION SYSTEM")
    print(f"Case: {CASE_ID}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"{'='*60}")
    
    # Load case data
    data = load_case_data()
    
    # Run requested workflow
    if args.workflow == "complete-analysis":
        run_complete_analysis(data)
    elif args.workflow == "fund-tracing":
        run_fund_tracing(data, args.victim)
    elif args.workflow == "timeline":
        run_timeline_analysis(data)
    elif args.workflow == "weak-links":
        run_weak_links_analysis(data)
    
    print(f"\n{'='*60}")
    print("Investigation complete!")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
