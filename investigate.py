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

# Try to import NetworkX for Phase 2 analysis
try:
    import networkx as nx
    from networkx.algorithms import community
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False

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
        # Try refined versions first, fall back to standard versions
        entities_file = DATA_DIR / "entities" / "entities_refined_2025_11_18.json"
        if not entities_file.exists():
            entities_file = DATA_DIR / "entities" / "entities.json"
        
        relations_file = DATA_DIR / "relations" / "relations_refined_2025_11_18.json"
        if not relations_file.exists():
            relations_file = DATA_DIR / "relations" / "relations.json"
        
        events_file = DATA_DIR / "events" / "events_refined_2025_11_18.json"
        if not events_file.exists():
            events_file = DATA_DIR / "events" / "events.json"
        
        timelines_file = DATA_DIR / "timelines" / "timelines_refined_2025_11_18.json"
        if not timelines_file.exists():
            timelines_file = DATA_DIR / "timelines" / "timeline_enhanced.json"
        
        with open(entities_file) as f:
            entities_raw = json.load(f)
            # Handle nested structure: if entities_raw has 'entities' key, unwrap it
            if isinstance(entities_raw, dict) and 'entities' in entities_raw:
                # Flatten nested entity structure (persons, organizations, etc.)
                data['entities'] = []
                for category in entities_raw['entities'].values():
                    if isinstance(category, list):
                        data['entities'].extend(category)
            else:
                data['entities'] = entities_raw if isinstance(entities_raw, list) else []
        
        with open(relations_file) as f:
            relations_raw = json.load(f)
            if isinstance(relations_raw, dict) and 'relations' in relations_raw:
                data['relations'] = relations_raw['relations']
            else:
                data['relations'] = relations_raw if isinstance(relations_raw, list) else []
        
        with open(events_file) as f:
            events_raw = json.load(f)
            if isinstance(events_raw, dict) and 'events' in events_raw:
                data['events'] = events_raw['events']
            else:
                data['events'] = events_raw if isinstance(events_raw, list) else []
        
        with open(timelines_file) as f:
            timelines_raw = json.load(f)
            if isinstance(timelines_raw, dict) and 'timelines' in timelines_raw:
                data['timelines'] = timelines_raw['timelines']
            else:
                data['timelines'] = timelines_raw if isinstance(timelines_raw, list) else []
        
        print(f"✓ Loaded case data: {len(data['entities'])} entities, {len(data['relations'])} relationships, {len(data['events'])} events")
        return data
    except FileNotFoundError as e:
        print(f"✗ Failed to load case data: {e}")
        print(f"  Expected locations:")
        print(f"  - {DATA_DIR}/entities/*.json")
        print(f"  - {DATA_DIR}/relations/*.json")
        print(f"  - {DATA_DIR}/events/*.json")
        print(f"  - {DATA_DIR}/timelines/*.json")
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
    """Extract and rank perpetrators by financial benefit"""
    perpetrators = []
    
    for entity in data['entities']:
        # Identify perpetrators/antagonists
        if entity.get('agent_type') in ['antagonist', 'perpetrator']:
            # Extract financial amount
            financial_impact = entity.get('financial_impact', {})
            amount_str = financial_impact.get('direct_involvement', '0')
            
            # Parse amount (handle "R10,269,727.90" format)
            try:
                amount = float(amount_str.replace('R', '').replace(',', ''))
            except (ValueError, AttributeError):
                amount = 0
            
            perpetrators.append({
                'entity_id': entity.get('entity_id', 'UNKNOWN'),
                'name': entity.get('name', 'UNKNOWN'),
                'role': entity.get('role', 'unknown'),
                'financial_benefit': amount,
                'involvement_events': entity.get('involvement_events', 0),
                'primary_actions': entity.get('primary_actions', []),
                'relationships': entity.get('relationships', []),
                'conflict_of_interest': entity.get('conflict_of_interest', {}),
                'additional_notes': entity.get('additional_notes', '')
            })
    
    # Sort by financial benefit (descending)
    perpetrators.sort(key=lambda x: x['financial_benefit'], reverse=True)
    
    return perpetrators

def analyze_hierarchy(data, perpetrators):
    """Analyze organizational hierarchy with enhanced metrics (Phase 2)"""
    if not perpetrators:
        return {"status": "insufficient_data", "message": "No perpetrators identified"}
    
    hierarchy_levels = {
        'apex': [],  # Highest financial benefit + network control
        'facilitators': [],  # Medium benefit + specific execution roles
        'operatives': []  # Lower benefit + direct execution
    }
    
    # Calculate composite scores for better hierarchy classification
    for i, perp in enumerate(perpetrators[:10]):
        # Score based on multiple factors
        financial_score = min(perp['financial_benefit'] / 2000000 * 100, 100)
        involvement_score = min(perp['involvement_events'] * 5, 50)
        relationship_score = min(len(perp['relationships']) * 10, 50)
        action_count = len(perp.get('primary_actions', []))
        
        composite_score = financial_score * 0.5 + involvement_score * 0.25 + relationship_score * 0.25
        
        if composite_score >= 70:
            hierarchy_levels['apex'].append({**perp, 'hierarchy_score': composite_score})
        elif composite_score >= 40:
            hierarchy_levels['facilitators'].append({**perp, 'hierarchy_score': composite_score})
        else:
            hierarchy_levels['operatives'].append({**perp, 'hierarchy_score': composite_score})
    
    return {
        'hierarchy_analysis': hierarchy_levels,
        'hierarchy_scores': {
            'apex_threshold': 70,
            'facilitator_threshold': 40,
            'operative_threshold': 0
        },
        'total_identified': sum(len(level) for level in hierarchy_levels.values()),
        'apex_count': len(hierarchy_levels['apex']),
        'facilitator_count': len(hierarchy_levels['facilitators']),
        'operative_count': len(hierarchy_levels['operatives']),
        'role_description': 'Apex=Strategic control, Facilitators=Execution enablers, Operatives=Direct executors'
    }

def analyze_financial_centrality(data, perpetrators):
    """Compute financial centrality and benefit distribution (Phase 2: Enhanced)"""
    total_benefit = sum(p['financial_benefit'] for p in perpetrators)
    
    financial_analysis = {
        'total_stolen': total_benefit,
        'perpetrator_count': len(perpetrators),
        'perpetrators': [],
        'benefit_distribution_percent': [],
        'gini_coefficient': 0,
        'concentration_analysis': {}
    }
    
    for perp in perpetrators:
        if perp['financial_benefit'] > 0:
            pct = (perp['financial_benefit'] / total_benefit * 100) if total_benefit > 0 else 0
            financial_analysis['perpetrators'].append({
                'name': perp['name'],
                'entity_id': perp['entity_id'],
                'amount': perp['financial_benefit'],
                'percentage': round(pct, 2),
                'involvement_events': perp['involvement_events'],
                'amount_per_event': perp['financial_benefit'] / max(perp['involvement_events'], 1)
            })
            financial_analysis['benefit_distribution_percent'].append(pct)
    
    # Calculate Gini coefficient (wealth concentration)
    if financial_analysis['perpetrators']:
        sorted_pcts = sorted(financial_analysis['benefit_distribution_percent'])
        n = len(sorted_pcts)
        gini = (2 * sum((i+1) * pct for i, pct in enumerate(sorted_pcts))) / (n * sum(sorted_pcts)) - (n+1)/n if sum(sorted_pcts) > 0 else 0
        financial_analysis['gini_coefficient'] = min(max(gini, 0), 1)  # Clamp 0-1
    
    # Concentration analysis
    top_pct = financial_analysis['benefit_distribution_percent'][0] if financial_analysis['benefit_distribution_percent'] else 0
    top_2_pct = sum(financial_analysis['benefit_distribution_percent'][:2])
    
    financial_analysis['concentration_analysis'] = {
        'top_perpetrator_percentage': round(top_pct, 2),
        'top_2_perpetrators_percentage': round(top_2_pct, 2),
        'concentration_level': 'high' if top_pct > 60 else 'medium' if top_pct > 40 else 'distributed'
    }
    
    return {
        'financial_centrality': financial_analysis,
        'average_per_perpetrator': total_benefit / len(perpetrators) if perpetrators else 0,
        'max_benefit': max((p['financial_benefit'] for p in perpetrators), default=0),
        'min_benefit': min((p['financial_benefit'] for p in perpetrators if p['financial_benefit'] > 0), default=0),
        'wealth_inequality': financial_analysis['gini_coefficient']
    }

def analyze_escalation(data):
    """Analyze escalation timeline and consciousness of guilt (Phase 2: Enhanced)"""
    # Organize events by year/phase and category
    events_by_date = {}
    events_by_category = {}
    
    for event in data['events']:
        date = event.get('date', 'unknown')
        if date != 'unknown':
            year = date.split('-')[0]
            if year not in events_by_date:
                events_by_date[year] = []
            events_by_date[year].append(event)
        
        # Categorize by type
        category = event.get('category', 'unknown')
        if category not in events_by_category:
            events_by_category[category] = []
        events_by_category[category].append(event)
    
    # Find acceleration patterns
    escalation_data = {
        'timeline': {},
        'crisis_indicators': [],
        'rapid_response_patterns': [],
        'consciousness_of_guilt': [],
        'acceleration_factors': []
    }
    
    sorted_years = sorted(events_by_date.keys())
    
    # Analyze acceleration between periods
    baseline_count = 0
    crisis_count = 0
    for year in sorted_years:
        events = events_by_date[year]
        count = len(events)
        
        escalation_data['timeline'][year] = {
            'event_count': count,
            'events': [e.get('title', 'Unknown') for e in events[:3]]
        }
        
        if year < '2025':
            baseline_count += count
        else:
            crisis_count += count
    
    # Calculate acceleration factor
    baseline_avg = baseline_count / max(len([y for y in sorted_years if y < '2025']), 1)
    crisis_avg = crisis_count / max(len([y for y in sorted_years if y >= '2025']), 1)
    acceleration = crisis_avg / max(baseline_avg, 0.1)
    
    escalation_data['acceleration_factors'] = {
        'baseline_avg': baseline_avg,
        'crisis_avg': crisis_avg,
        'acceleration_factor': acceleration
    }
    
    # Identify crisis period events
    if '2025' in events_by_date:
        events_2025 = events_by_date['2025']
        escalation_data['crisis_indicators'] = [
            {
                'date': e.get('date', ''),
                'title': e.get('title', 'Unknown'),
                'significance': e.get('legal_significance', '')
            }
            for e in events_2025 
            if any(keyword in str(e.get('category', '')).lower() + ' ' + str(e.get('description', '')).lower()
                   for keyword in ['fraud', 'theft', 'exposed', 'destroyed', 'confrontation'])
        ]
    
    return {
        'escalation_analysis': escalation_data,
        'years_analyzed': sorted_years,
        'peak_activity_year': sorted_years[-1] if sorted_years else 'unknown',
        'total_events': len(data['events']),
        'baseline_period': f"{sorted_years[0]}-{sorted([y for y in sorted_years if y < '2025'], reverse=True)[0] if [y for y in sorted_years if y < '2025'] else 'N/A'}",
        'crisis_period': '2025+',
        'acceleration_detected': acceleration > 2
    }

def analyze_network_structure(data):
    """Generate network structure analysis with optional NetworkX metrics (Phase 2)"""
    entity_types = {}
    relationships = {
        'control': 0,
        'ownership': 0,
        'conspiracy': 0,
        'financial': 0,
        'other': 0
    }
    
    # Count entity types
    for entity in data['entities']:
        agent_type = entity.get('agent_type', 'unknown')
        if agent_type not in entity_types:
            entity_types[agent_type] = 0
        entity_types[agent_type] += 1
    
    # Count relationships
    rel_list = []
    for rel_category in data.get('relations', {}).values():
        if isinstance(rel_category, list):
            for rel in rel_category:
                rel_type = rel.get('relation_type', 'other')
                if 'control' in rel_type.lower():
                    relationships['control'] += 1
                elif 'own' in rel_type.lower():
                    relationships['ownership'] += 1
                elif 'conspir' in rel_type.lower():
                    relationships['conspiracy'] += 1
                elif 'financial' in rel_type.lower() or 'debtor' in rel_type.lower():
                    relationships['financial'] += 1
                else:
                    relationships['other'] += 1
                rel_list.append(rel)
    
    network_analysis = {
        'entity_types': entity_types,
        'relationship_types': relationships,
        'total_entities': len(data['entities']),
        'total_relationships': sum(relationships.values()),
        'network_density': 'medium' if sum(relationships.values()) > 10 else 'low'
    }
    
    # Phase 2: Enhanced NetworkX analysis if available
    if HAS_NETWORKX:
        try:
            # Build graph
            G = nx.Graph()
            entity_map = {e.get('entity_id', ''): e for e in data['entities']}
            
            # Add nodes with attributes
            for entity in data['entities']:
                entity_id = entity.get('entity_id', '')
                G.add_node(entity_id, 
                          name=entity.get('name', ''),
                          agent_type=entity.get('agent_type', ''))
            
            # Add edges from relationships
            for rel in rel_list:
                source = rel.get('source_entity', '')
                target = rel.get('target_entity', '')
                if source and target:
                    G.add_edge(source, target, 
                              rel_type=rel.get('relation_type', ''))
            
            # Calculate centrality metrics
            degree_cent = nx.degree_centrality(G)
            betweenness_cent = nx.betweenness_centrality(G)
            closeness_cent = nx.closeness_centrality(G) if nx.is_connected(G) else {}
            
            # Find communities
            communities_list = list(community.greedy_modularity_communities(G))
            
            network_analysis['centrality_metrics'] = {
                'top_degree': sorted(degree_cent.items(), key=lambda x: x[1], reverse=True)[:5],
                'top_betweenness': sorted(betweenness_cent.items(), key=lambda x: x[1], reverse=True)[:5],
                'communities': len(communities_list),
                'modularity': 'calculated'
            }
        except Exception as e:
            network_analysis['phase2_error'] = str(e)
    
    return network_analysis

def identify_source_funds(data, victim=None):
    """Identify legitimate source funds that were hijacked"""
    sources = []
    
    for entity in data['entities']:
        entity_type = entity.get('agent_type', '')
        # Look for entities that hold money (trusts, accounts, platforms)
        if entity_type in ['trust', 'account', 'platform', 'business'] or \
           'account' in entity.get('name', '').lower() or \
           'trust' in entity.get('name', '').lower():
            
            sources.append({
                'entity_id': entity.get('entity_id', ''),
                'name': entity.get('name', ''),
                'type': entity.get('agent_type', 'unknown'),
                'role': entity.get('role', ''),
                'financial_impact': entity.get('financial_impact', {}),
                'description': f"Potential source fund from {entity.get('name', 'unknown')}"
            })
    
    return sources if sources else [{'name': 'Trust Assets', 'type': 'trust'}, 
                                     {'name': 'Platform Revenue', 'type': 'platform'}]

def trace_transfer_chain(data, sources):
    """Trace fund flow from sources through intermediaries to perpetrators"""
    transfers = []
    
    # Build entity lookup map
    entity_map = {}
    for entity in data['entities']:
        entity_map[entity.get('entity_id', '')] = entity
    
    # Process all events to find financial transfers
    for event in data['events']:
        financial_impact = event.get('financial_impact', '')
        if not financial_impact or financial_impact == 'unknown':
            continue
        
        # Parse amount
        try:
            amount = float(str(financial_impact).replace('R', '').replace(',', ''))
        except (ValueError, AttributeError):
            continue
        
        # Build transfer record
        perpetrators = event.get('perpetrators', [])
        victims = event.get('victims', [])
        entities_involved = event.get('entities_involved', [])
        
        transfer = {
            'event_id': event.get('event_id', 'UNKNOWN'),
            'date': event.get('date', 'unknown'),
            'title': event.get('title', 'Unknown Transfer'),
            'amount': amount,
            'category': event.get('category', 'unknown'),
            'perpetrators': perpetrators,
            'victims': victims,
            'entities_involved': entities_involved,
            'description': event.get('description', ''),
            'legal_significance': event.get('legal_significance', ''),
            'evidence': event.get('evidence', []),
            'pattern': event.get('pattern', '')
        }
        transfers.append(transfer)
    
    # Sort by date
    transfers.sort(key=lambda x: x['date'] if x['date'] != 'unknown' else '2099-12-31')
    
    return {
        'total_transfers': len(transfers),
        'total_amount': sum(t['amount'] for t in transfers),
        'transfers': transfers[:20]  # Return top 20 transfers
    }

def analyze_benefit_distribution(data, transfers):
    """Analyze how stolen funds were distributed to perpetrators"""
    distribution = {
        'total_amount': transfers['total_amount'],
        'by_perpetrator': {},
        'transfer_count': transfers['total_transfers']
    }
    
    # Aggregate transfers by perpetrator
    if isinstance(transfers.get('transfers'), list):
        for transfer in transfers['transfers']:
            for perp in transfer.get('perpetrators', []):
                if perp not in distribution['by_perpetrator']:
                    distribution['by_perpetrator'][perp] = 0
                distribution['by_perpetrator'][perp] += transfer['amount']
    
    return {
        'distribution_analysis': distribution,
        'perpetrators_identified': len(distribution['by_perpetrator']),
        'largest_recipient': max(distribution['by_perpetrator'].items(), 
                                key=lambda x: x[1], 
                                default=('unknown', 0))[0]
    }

def generate_fund_flow_diagram(transfers):
    """Generate fund flow diagram description"""
    diagram = {
        'title': 'Revenue Stream Hijacking Fund Flow',
        'total_transfers': transfers.get('total_transfers', 0),
        'total_amount': transfers.get('total_amount', 0),
        'flow_description': 'Source Funds → Intermediary Accounts → Perpetrator-Controlled Accounts',
        'key_paths': [
            'Trust Assets → Unauthorized Transfers → Perpetrator Benefit',
            'Platform Revenue → Payment Redirection → Conspiracy Members',
            'Investment Accounts → Account Hijacking → Financial Manipulation'
        ]
    }
    return diagram

def extract_baseline_period(data):
    """Extract baseline activity period before fraud escalation"""
    # Identify events before 2025 (baseline) vs 2025+ (crisis)
    baseline_events = [e for e in data['events'] if e.get('date', '').startswith(('202', '201'))]
    crisis_events = [e for e in data['events'] if e.get('date', '').startswith('2025')]
    
    return {
        'baseline_period': 'Pre-2025',
        'baseline_event_count': len(baseline_events),
        'crisis_period': '2025',
        'crisis_event_count': len(crisis_events),
        'acceleration_factor': len(crisis_events) / max(len(baseline_events), 1)
    }

def identify_trigger_events(data):
    """Identify trigger events that caused escalation"""
    triggers = []
    
    for event in data['events']:
        # Look for events involving confrontation, discovery, threats
        keywords = ['confrontation', 'discovery', 'complaint', 'investigation', 'exposed', 'revealed']
        title = str(event.get('title', '')).lower()
        desc = str(event.get('description', '')).lower()
        
        if any(kw in title or kw in desc for kw in keywords):
            triggers.append({
                'event_id': event.get('event_id', ''),
                'date': event.get('date', ''),
                'title': event.get('title', ''),
                'significance': event.get('legal_significance', '')
            })
    
    return triggers

def analyze_escalation_patterns(data, triggers):
    """Analyze escalation patterns after trigger events"""
    return {
        'trigger_count': len(triggers),
        'key_triggers': triggers[:3] if triggers else [],
        'escalation_indicators': [
            'Rapid account closures',
            'Evidence destruction pattern',
            'Communication burst between perpetrators',
            'Unusual transaction clustering'
        ]
    }

def analyze_consciousness_of_guilt(data, escalation):
    """Analyze consciousness of guilt indicators"""
    guilt_indicators = {
        'evidence_destruction': [],
        'rapid_response': [],
        'coordinated_activity': [],
        'authorization_attempts': []
    }
    
    # Look for destruction events (Shopify, domains, etc)
    for event in data['events']:
        title = str(event.get('title', '')).lower()
        if any(word in title for word in ['destroyed', 'deleted', 'cancelled', 'closed', 'shutdown']):
            guilt_indicators['evidence_destruction'].append(event.get('title', ''))
    
    return {
        'guilt_indicators': guilt_indicators,
        'consciousness_score': 0.75 if guilt_indicators['evidence_destruction'] else 0.5
    }

def extract_amount(financial_obj):
    """Extract numeric amount from financial impact object"""
    if isinstance(financial_obj, dict):
        # Try direct_involvement first, then any field with amount
        for key in ['direct_involvement', 'victim_of_theft', 'debt_motive']:
            if key in financial_obj:
                value = financial_obj[key]
                try:
                    return float(str(value).replace('R', '').replace(',', '').split('-')[0].strip())
                except (ValueError, AttributeError):
                    pass
    elif isinstance(financial_obj, str):
        try:
            return float(str(financial_obj).replace('R', '').replace(',', '').split('-')[0].strip())
        except (ValueError, AttributeError):
            pass
    return 0

def calculate_node_criticality(data):
    """Calculate how critical each node is to network connectivity"""
    criticality_scores = {}
    
    # Build entity lookup and relationship map
    entity_map = {}
    entity_connections = {}
    
    for entity in data['entities']:
        entity_id = entity.get('entity_id', '')
        entity_map[entity_id] = entity
        entity_connections[entity_id] = []
    
    # Map relationships (both directions for connectivity)
    for rel_category in data.get('relations', {}).values():
        if isinstance(rel_category, list):
            for rel in rel_category:
                source = rel.get('source_entity', '')
                target = rel.get('target_entity', '')
                
                if source in entity_connections:
                    entity_connections[source].append(target)
                if target in entity_connections:
                    entity_connections[target].append(source)
    
    # Calculate criticality metrics for each entity
    for entity_id, entity in entity_map.items():
        connections = entity_connections.get(entity_id, [])
        
        criticality = {
            'entity_id': entity_id,
            'name': entity.get('name', 'UNKNOWN'),
            'agent_type': entity.get('agent_type', 'unknown'),
            'degree_centrality': len(set(connections)),  # Unique connections
            'financial_impact': extract_amount(entity.get('financial_impact', {})),
            'involvement_events': entity.get('involvement_events', 0),
            'roles': entity.get('role', ''),
            'conflict_of_interest': bool(entity.get('conflict_of_interest', {})),
            'criticality_score': 0
        }
        
        # Calculate criticality score (0-100)
        # Higher score = more likely to break network if removed
        score = 0
        score += min(len(set(connections)) * 5, 30)  # Connectivity (max 30)
        score += min(criticality['involvement_events'] * 2, 20)  # Involvement (max 20)
        score += min(criticality['financial_impact'] / 500000, 25)  # Financial impact (max 25)
        score += 25 if criticality['conflict_of_interest'] else 0  # Conflict (max 25)
        
        criticality['criticality_score'] = min(score, 100)
        criticality_scores[entity_id] = criticality
    
    # Sort by criticality score
    sorted_nodes = sorted(criticality_scores.values(), 
                         key=lambda x: x['criticality_score'], 
                         reverse=True)
    
    return {
        'total_entities': len(criticality_scores),
        'critical_nodes': sorted_nodes[:15],  # Top 15 most critical
        'all_scores': sorted_nodes
    }

def identify_conflicts(data):
    """Identify conflicted entities (forced to serve multiple masters)"""
    conflicts = []
    
    for entity in data['entities']:
        if entity.get('conflict_of_interest', {}):
            conflicts.append({
                'entity_id': entity.get('entity_id', ''),
                'name': entity.get('name', ''),
                'conflict': entity.get('conflict_of_interest', {}),
                'motive': entity.get('conflict_of_interest', {}).get('motive', 'unknown')
            })
    
    return conflicts

def rank_priorities(data, criticality, conflicts):
    """Rank interrogation priorities based on criticality and conflicts"""
    priorities = []
    
    critical_entities = criticality.get('critical_nodes', [])
    conflicted_entities = {c['entity_id']: c for c in conflicts}
    
    for entity in critical_entities[:10]:
        priority_score = entity.get('criticality_score', 0)
        
        # Boost score if conflicted
        if entity['entity_id'] in conflicted_entities:
            priority_score += 20
        
        priorities.append({
            'entity_id': entity['entity_id'],
            'name': entity['name'],
            'priority_score': min(priority_score, 100),
            'reason': f"High criticality: {entity['degree_centrality']} connections, " +
                     f"{entity['involvement_events']} events, " +
                     f"R{entity['financial_impact']:,.0f} involved",
            'is_conflicted': entity['entity_id'] in conflicted_entities
        })
    
    return {'priorities': priorities}

def generate_report(output, workflow_type):
    """Generate investigation report with Phase 3 formatting (markdown, CSV, diagrams)"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = OUTPUT_DIR / f"{workflow_type}_{timestamp}.json"
    
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, default=str)
    
    # Phase 3: Generate additional output formats
    if workflow_type == "complete-analysis":
        generate_forensic_report(output, OUTPUT_DIR, timestamp)
    elif workflow_type == "fund-tracing":
        generate_fund_flow_report(output, OUTPUT_DIR, timestamp)
    elif workflow_type == "weak-links":
        generate_interrogation_report(output, OUTPUT_DIR, timestamp)
    
    return report_file

def generate_forensic_report(output, output_dir, timestamp):
    """Generate comprehensive forensic markdown report (Phase 3)"""
    case_id = output.get('case_id', '2025-137857')
    md_file = output_dir / f"{case_id}_FORENSIC_REPORT_{timestamp}.md"
    
    perpetrators = output['findings'].get('perpetrators', [])
    hierarchy = output['findings'].get('hierarchy', {}).get('hierarchy_analysis', {})
    financial = output['findings'].get('financial_analysis', {}).get('financial_centrality', {})
    escalation = output['findings'].get('escalation', {})
    
    md = f"""# FORENSIC INVESTIGATION REPORT
## Revenue Stream Hijacking Case {case_id}
**Report Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## EXECUTIVE SUMMARY

### Conspiracy Overview
- **Total Identified Theft:** R{financial.get('total_stolen', 0):,.2f}
- **Perpetrators:** {len(perpetrators)}
- **Network Density:** {output['findings'].get('network_structure', {}).get('network_density', 'unknown')}
- **Investigation Status:** ACTIVE

### Crisis Timeline
- **Baseline Period:** {escalation.get('baseline_period', 'N/A')}  
- **Crisis Period:** {escalation.get('crisis_period', 'N/A')}
- **Acceleration Factor:** {escalation.get('acceleration_factors', {}).get('acceleration_factor', 0):.1f}x

---

## PERPETRATOR HIERARCHY

### APEX DECISION-MAKERS
"""
    
    for perp in hierarchy.get('apex', []):
        md += f"""
#### {perp['name']} (Entity: {perp['entity_id']})
- **Role:** {perp['role']}
- **Financial Benefit:** R{perp.get('financial_benefit', 0):,.2f}
- **Network Centrality:** {perp.get('hierarchy_score', 0):.1f}/100
- **Involvement Events:** {perp.get('involvement_events', 0)}
- **Key Actions:** {', '.join(perp.get('primary_actions', [])[:3])}
"""
    
    md += "\n### FACILITATORS & CO-CONSPIRATORS\n"
    for perp in hierarchy.get('facilitators', []):
        conflict_marker = " ⚠️ **CONFLICT OF INTEREST**" if perp.get('conflict_of_interest', {}) else ""
        md += f"""
#### {perp['name']} (Entity: {perp['entity_id']}){conflict_marker}
- **Role:** {perp['role']}
- **Financial Benefit:** R{perp.get('financial_benefit', 0):,.2f}
- **Involvement Events:** {perp.get('involvement_events', 0)}
- **Key Actions:** {', '.join(perp.get('primary_actions', [])[:3])}
"""
        if perp.get('conflict_of_interest', {}).get('triple_conflict'):
            md += f"- **MOTIVE:** {perp['conflict_of_interest'].get('motive', 'Unknown')}\n"
    
    md += "\n### OPERATIVES & INDIRECT PARTICIPANTS\n"
    operatives = hierarchy.get('operatives', [])
    if not operatives:
        md += "*No operatives identified*\n"
    
    md += f"""

---

## FINANCIAL ANALYSIS

### Wealth Distribution
- **Total Stolen:** R{financial.get('total_stolen', 0):,.2f}
- **Gini Coefficient:** {output['findings'].get('financial_analysis', {}).get('wealth_inequality', 0):.3f} (0=equal, 1=concentrated)
- **Concentration Level:** {financial.get('concentration_analysis', {}).get('concentration_level', 'unknown').upper()}
- **Top Perpetrator Share:** {financial.get('concentration_analysis', {}).get('top_perpetrator_percentage', 0):.1f}%

### Perpetrator Distribution
"""
    
    for perp in financial.get('perpetrators', [])[:5]:
        md += f"- **{perp['name']}:** R{perp['amount']:,.2f} ({perp['percentage']:.1f}%) - {perp['involvement_events']} events\n"
    
    md += f"""

---

## ESCALATION TIMELINE

### Crisis Indicators (2025)
"""
    
    for indicator in escalation.get('escalation_analysis', {}).get('crisis_indicators', [])[:10]:
        md += f"- **{indicator.get('date', 'TBD')}:** {indicator.get('title', 'Unknown')}\n"
    
    md += f"""

### Key Timeline Statistics
- **Baseline Activity:** {escalation.get('acceleration_factors', {}).get('baseline_avg', 0):.1f} events/year
- **Crisis Activity:** {escalation.get('acceleration_factors', {}).get('crisis_avg', 0):.1f} events/year
- **Acceleration:** {escalation.get('acceleration_factors', {}).get('acceleration_factor', 0):.1f}x increase

---

## NETWORK STRUCTURE

- **Total Entities:** {output['findings'].get('network_structure', {}).get('total_entities', 0)}
- **Total Relationships:** {output['findings'].get('network_structure', {}).get('total_relationships', 0)}
- **Entity Types:** {output['findings'].get('network_structure', {}).get('entity_types', {})}

---

## LEGAL SIGNIFICANCE

This investigation reveals a **coordinated conspiracy** with clear characteristics:

1. **Organization:** Hierarchical structure with apex decision-maker(s)
2. **Planning:** Multi-phase execution over extended timeline
3. **Coordination:** Simultaneous actions across multiple perpetrators
4. **Consciousness of Guilt:** Evidence destruction and rapid response to exposure
5. **Motive:** Financial enrichment and debt concealment

**Investigation Status:** ONGOING - Recommend presentation to legal counsel for affidavit preparation.

---
*Forensic Investigation System | Case 2025-137857 | Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f'✓ Forensic report: {md_file.name}')

def generate_fund_flow_report(output, output_dir, timestamp):
    """Generate fund flow analysis report (Phase 3)"""
    md_file = output_dir / f"FUND_FLOW_ANALYSIS_{timestamp}.md"
    
    findings = output['findings']
    perpetrators = findings.get('perpetrators', [])
    
    md = f"""# FUND FLOW ANALYSIS REPORT
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Transfer Chain

### Identified Perpetrator Receipts
"""
    
    total = 0
    for perp in perpetrators:
        if perp.get('financial_benefit', 0) > 0:
            md += f"\n**{perp['name']}**\n"
            md += f"- Received: R{perp['financial_benefit']:,.2f}\n"
            md += f"- Events: {perp['involvement_events']}\n"
            md += f"- Amount/Event: R{perp['financial_benefit'] / max(perp['involvement_events'], 1):,.2f}\n"
            total += perp['financial_benefit']
    
    md += f"\n## Summary\n**Total Identified Theft:** R{total:,.2f}\n"
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f'✓ Fund flow report: {md_file.name}')

def generate_interrogation_report(output, output_dir, timestamp):
    """Generate interrogation priorities report (Phase 3)"""
    md_file = output_dir / f"INTERROGATION_PRIORITIES_{timestamp}.md"
    
    findings = output['findings']
    if 'criticality' not in findings:
        return
    
    critical_nodes = findings['criticality'].get('critical_nodes', [])
    
    md = f"""# INTERROGATION PRIORITY ASSESSMENT
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Priority Ranking by Network Criticality

"""
    
    for i, node in enumerate(critical_nodes[:10], 1):
        md += f"""### Priority {i}: {node['name']}

- **Criticality Score:** {node.get('criticality_score', 0):.1f}/100
- **Role:** {node.get('roles', 'Unknown')}
- **Network Connections:** {node.get('degree_centrality', 0)}
- **Financial Impact:** R{node.get('financial_impact', 0):,.0f}
- **Event Involvement:** {node.get('involvement_events', 0)}
- **Conflict of Interest:** {'⚠️ YES' if node.get('conflict_of_interest') else 'No'}

"""
    
    md += "\n---\n*Higher criticality scores indicate greater leverage for investigation*\n"
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f'✓ Interrogation report: {md_file.name}')

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
