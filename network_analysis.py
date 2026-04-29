"""
Network Analysis for Revenue Stream Hijacking Case 2025-137857

Develops social/organizational network analysis across all 27 entities.
- Extracts relationships from entities, relations, and events data models
- Calculates network metrics (centrality, clustering, communities)
- Identifies organizational hierarchy and entity roles
- Generates comprehensive analysis report

Phase 1: Data Extraction & Preparation
Phase 2: Network Metrics Calculation
Phase 3: Relationship Strength Analysis (integrated)
Phase 4: Hierarchy & Organization Structure
Phase 5: Analysis Report Generation
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple, Set
from collections import defaultdict
import networkx as nx
from networkx.algorithms import community
import statistics


class NetworkAnalysis:
    """Performs comprehensive network analysis on case entities and relationships."""
    
    def __init__(self, workspace_dir: str = "d:\\Documents\\GitHub\\revstream2"):
        """Initialize with workspace directory."""
        self.workspace_dir = Path(workspace_dir)
        self.entities_data = None
        self.relations_data = None
        self.events_data = None
        
        # Network objects
        self.graph = nx.Graph()  # Undirected graph for relationships
        self.directed_graph = nx.DiGraph()  # Directed graph for hierarchy
        
        # Analysis results
        self.centrality_metrics = {}
        self.communities = {}
        self.hierarchy = {}
        self.entity_roles = {}
        self.relationship_weights = {}
        
    def load_data(self) -> bool:
        """Load entities, relations, and events data files."""
        try:
            # Load entities
            entities_path = self.workspace_dir / "data_models" / "entities" / "entities_refined_2025_11_18.json"
            with open(entities_path) as f:
                self.entities_data = json.load(f)
            print(f"✓ Loaded entities: {len(self._get_all_entities())} entities")
            
            # Load relations
            relations_path = self.workspace_dir / "data_models" / "relations" / "relations_refined_2025_11_18.json"
            with open(relations_path) as f:
                self.relations_data = json.load(f)
            print(f"✓ Loaded relations: {len(self._get_all_relations())} relations")
            
            # Load events
            events_path = self.workspace_dir / "data_models" / "events" / "events_refined_2025_11_18.json"
            with open(events_path) as f:
                self.events_data = json.load(f)
            print(f"✓ Loaded events: {len(self.events_data.get('events', []))} events")
            
            return True
        except Exception as e:
            print(f"✗ Error loading data: {e}")
            return False
    
    def _get_all_entities(self) -> List[Dict]:
        """Extract all entities from the entities data."""
        all_entities = []
        for category in ['persons', 'organizations', 'platforms', 'domains', 'trusts', 'other']:
            if category in self.entities_data.get('entities', {}):
                all_entities.extend(self.entities_data['entities'][category])
        return all_entities
    
    def _get_all_relations(self) -> List[Dict]:
        """Extract all relations from the relations data."""
        all_relations = []
        for rel_type in self.relations_data.get('relations', {}):
            all_relations.extend(self.relations_data['relations'][rel_type])
        return all_relations
    
    def extract_relationships(self) -> Dict[str, List[Tuple]]:
        """
        Phase 1: Extract all relationships between entities.
        Returns: {relationship_type: [(source, target, weight, evidence), ...]}
        """
        relationships = defaultdict(list)
        
        # Extract from relations data
        for relation_type_key, relation_list in self.relations_data.get('relations', {}).items():
            for rel in relation_list:
                source = rel.get('source_entity')
                target = rel.get('target_entity')
                
                if source and target and source != target:
                    # Calculate weight based on evidence strength
                    evidence = rel.get('evidence', [])
                    weight = min(len(evidence) * 0.5, 1.0)  # 0-1 scale
                    
                    relationship_type = rel.get('relation_type', relation_type_key)
                    relationships[relationship_type].append({
                        'source': source,
                        'target': target,
                        'weight': weight,
                        'strength': rel.get('strength', 'unknown'),
                        'legal_status': rel.get('legal_status', 'unknown'),
                        'evidence': evidence,
                        'relation_id': rel.get('relation_id')
                    })
        
        # Extract from events (perpetrator-victim relationships)
        for event in self.events_data.get('events', []):
            perpetrators = event.get('perpetrators', [])
            victims = event.get('victims', [])
            
            for perpetrator in perpetrators:
                for victim in victims:
                    if perpetrator != victim:
                        relationships['perpetrator_victim'].append({
                            'source': perpetrator,
                            'target': victim,
                            'weight': 0.3,  # Events create medium-strength relationships
                            'strength': 'event_based',
                            'legal_status': 'fraud_related',
                            'evidence': [event.get('event_id')],
                            'event_date': event.get('date')
                        })
        
        return relationships
    
    def build_network(self) -> bool:
        """
        Phase 1: Build unified network representation from extracted relationships.
        Creates both undirected and directed graphs with attributes.
        """
        try:
            all_entities = self._get_all_entities()
            
            # Add nodes with attributes
            for entity in all_entities:
                entity_id = entity.get('entity_id')
                if entity_id:
                    # Determine entity type
                    if 'PERSON' in entity_id:
                        entity_type = 'person'
                    elif 'ORG' in entity_id:
                        entity_type = 'organization'
                    elif 'PLATFORM' in entity_id:
                        entity_type = 'platform'
                    elif 'DOMAIN' in entity_id:
                        entity_type = 'domain'
                    elif 'TRUST' in entity_id:
                        entity_type = 'trust'
                    else:
                        entity_type = 'other'
                    
                    # Extract financial impact
                    financial_data = entity.get('financial_impact', {})
                    if isinstance(financial_data, dict):
                        financial_amount = financial_data.get('direct_involvement', 'unknown')
                    else:
                        financial_amount = financial_data if financial_data else 'unknown'
                    
                    # Add node to both graphs
                    node_attrs = {
                        'name': entity.get('name', entity_id),
                        'type': entity_type,
                        'agent_type': entity.get('agent_type', 'unknown'),
                        'involvement_events': entity.get('involvement_events', 0),
                        'financial_impact': financial_amount,
                        'role': entity.get('role', 'unknown'),
                        'timeline_events': len(entity.get('timeline_events', [])),
                    }
                    
                    self.graph.add_node(entity_id, **node_attrs)
                    self.directed_graph.add_node(entity_id, **node_attrs)
            
            print(f"✓ Added {len(self.graph.nodes())} nodes to network")
            
            # Extract and add edges
            relationships = self.extract_relationships()
            edge_count = 0
            
            for rel_type, rels in relationships.items():
                for rel in rels:
                    source = rel['source']
                    target = rel['target']
                    
                    # Skip if nodes don't exist
                    if source not in self.graph or target not in self.graph:
                        continue
                    
                    # Add to undirected graph
                    if self.graph.has_edge(source, target):
                        # Aggregate multiple relationships
                        existing_weight = self.graph[source][target].get('weight', 0.5)
                        self.graph[source][target]['weight'] = min(existing_weight + rel['weight'], 1.0)
                    else:
                        self.graph.add_edge(source, target,
                                          relation_type=rel_type,
                                          weight=rel['weight'],
                                          strength=rel['strength'],
                                          legal_status=rel['legal_status'],
                                          evidence_count=len(rel.get('evidence', [])))
                    edge_count += 1
                    
                    # Add directed edge if it's a control/authority relationship
                    if rel_type in ['controls', 'trustee_of', 'owns', 'operates']:
                        self.directed_graph.add_edge(source, target,
                                                    relation_type=rel_type,
                                                    weight=rel['weight'])
            
            print(f"✓ Added {edge_count} edges to network")
            return True
            
        except Exception as e:
            print(f"✗ Error building network: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def validate_network(self) -> Dict[str, any]:
        """
        Phase 1: Validate network integrity.
        Returns: Validation report with statistics.
        """
        report = {
            'node_count': len(self.graph.nodes()),
            'edge_count': len(self.graph.edges()),
            'density': nx.density(self.graph),
            'is_connected': nx.is_connected(self.graph),
            'connected_components': len(list(nx.connected_components(self.graph))),
            'orphaned_nodes': [],
            'isolated_nodes': [],
            'data_issues': []
        }
        
        # Check for orphaned nodes (only in network, not in data)
        for node in self.graph.nodes():
            if self.graph.degree(node) == 0:
                report['isolated_nodes'].append(node)
        
        # Check data consistency
        all_entities = {e.get('entity_id') for e in self._get_all_entities() if e.get('entity_id')}
        all_relations = set()
        
        for rel_type_key, rel_list in self.relations_data.get('relations', {}).items():
            for rel in rel_list:
                source = rel.get('source_entity')
                target = rel.get('target_entity')
                if source:
                    all_relations.add(source)
                if target:
                    all_relations.add(target)
        
        # Check for relations referencing non-existent entities
        for node in all_relations:
            if node not in all_entities and not node.startswith(('ORG_', 'PERSON_', 'PLATFORM_', 'DOMAIN_', 'TRUST_')):
                report['data_issues'].append(f"Relation references non-standard entity: {node}")
        
        print(f"✓ Network validation complete")
        print(f"  Nodes: {report['node_count']}, Edges: {report['edge_count']}")
        print(f"  Density: {report['density']:.3f}, Connected: {report['is_connected']}")
        print(f"  Isolated nodes: {len(report['isolated_nodes'])}")
        
        return report
    
    def calculate_centrality_metrics(self) -> Dict[str, Dict[str, float]]:
        """
        Phase 2: Calculate centrality metrics to identify key actors.
        Returns: {metric_name: {entity_id: score}}
        """
        print("\nCalculating centrality metrics...")
        
        metrics = {}
        
        # Degree centrality (direct connections)
        degree_cent = nx.degree_centrality(self.graph)
        metrics['degree_centrality'] = degree_cent
        
        # Betweenness centrality (control of information flow)
        betweenness_cent = nx.betweenness_centrality(self.graph, weight='weight')
        metrics['betweenness_centrality'] = betweenness_cent
        
        # Closeness centrality (proximity to all actors)
        if nx.is_connected(self.graph):
            closeness_cent = nx.closeness_centrality(self.graph, distance='weight')
            metrics['closeness_centrality'] = closeness_cent
        else:
            # For disconnected graphs, calculate per component
            closeness_cent = {}
            for component in nx.connected_components(self.graph):
                subgraph = self.graph.subgraph(component)
                component_closeness = nx.closeness_centrality(subgraph, distance='weight')
                closeness_cent.update(component_closeness)
            metrics['closeness_centrality'] = closeness_cent
        
        # Eigenvector centrality (influence through connections)
        try:
            eigenvector_cent = nx.eigenvector_centrality(self.graph, weight='weight', max_iter=100)
            metrics['eigenvector_centrality'] = eigenvector_cent
        except:
            print("  ⚠ Eigenvector centrality calculation skipped (convergence issue)")
            metrics['eigenvector_centrality'] = {}
        
        # Weighted degree (sum of edge weights)
        weighted_degree = {}
        for node in self.graph.nodes():
            weighted_degree[node] = sum(self.graph[node][neighbor].get('weight', 1) 
                                       for neighbor in self.graph[node])
        metrics['weighted_degree'] = weighted_degree
        
        self.centrality_metrics = metrics
        print(f"✓ Calculated {len(metrics)} centrality metrics")
        
        return metrics
    
    def detect_communities(self) -> Dict[int, List[str]]:
        """
        Phase 2: Detect community structure using Louvain method.
        Returns: {community_id: [entity_ids]}
        """
        print("Detecting communities...")
        
        try:
            communities_gen = community.louvain_communities(self.graph, weight='weight')
            communities_dict = {i: list(comm) for i, comm in enumerate(communities_gen)}
            
            self.communities = communities_dict
            print(f"✓ Detected {len(communities_dict)} communities")
            for comm_id, entities in communities_dict.items():
                print(f"  Community {comm_id}: {len(entities)} entities")
            
            return communities_dict
        except Exception as e:
            print(f"✗ Community detection error: {e}")
            return {}
    
    def analyze_hierarchy(self) -> Dict[str, List[str]]:
        """
        Phase 4: Analyze organizational hierarchy from directed relationships.
        Returns: {level: [entity_ids]} (top-level, middle, operatives, victims)
        """
        print("Analyzing organizational hierarchy...")
        
        hierarchy = {
            'top_level': [],
            'middle_management': [],
            'operatives': [],
            'support': [],
            'victims': []
        }
        
        try:
            # Use agent_type and centrality to classify roles
            all_entities = self._get_all_entities()
            entity_dict = {e.get('entity_id'): e for e in all_entities if e.get('entity_id')}
            
            for entity_id, entity in entity_dict.items():
                agent_type = entity.get('agent_type', 'unknown')
                degree_cent = self.centrality_metrics.get('degree_centrality', {}).get(entity_id, 0)
                betweenness = self.centrality_metrics.get('betweenness_centrality', {}).get(entity_id, 0)
                
                if agent_type == 'victim' or agent_type == 'affected_entity':
                    hierarchy['victims'].append(entity_id)
                elif agent_type == 'antagonist':
                    # Use centrality to distinguish levels
                    if degree_cent > 0.5 or betweenness > 0.3:
                        hierarchy['top_level'].append(entity_id)
                    elif degree_cent > 0.2:
                        hierarchy['middle_management'].append(entity_id)
                    else:
                        hierarchy['operatives'].append(entity_id)
                elif agent_type == 'accomplice':
                    hierarchy['operatives'].append(entity_id)
                else:
                    hierarchy['support'].append(entity_id)
            
            self.hierarchy = hierarchy
            print(f"✓ Hierarchy analysis complete")
            for level, entities in hierarchy.items():
                if entities:
                    print(f"  {level}: {len(entities)} entities")
            
            return hierarchy
        except Exception as e:
            print(f"✗ Hierarchy analysis error: {e}")
            return hierarchy
    
    def classify_entity_roles(self) -> Dict[str, str]:
        """
        Phase 2: Classify entity roles based on network metrics.
        Returns: {entity_id: role}
        """
        print("Classifying entity roles...")
        
        roles = {}
        degree_cent = self.centrality_metrics.get('degree_centrality', {})
        betweenness = self.centrality_metrics.get('betweenness_centrality', {})
        
        for entity_id in self.graph.nodes():
            deg = degree_cent.get(entity_id, 0)
            bet = betweenness.get(entity_id, 0)
            node_type = self.graph.nodes[entity_id].get('type', 'unknown')
            agent_type = self.graph.nodes[entity_id].get('agent_type', 'unknown')
            
            # Role classification logic
            if deg > 0.5 and bet > 0.3:
                role = 'leader'
            elif bet > 0.2:
                role = 'facilitator'
            elif deg > 0.3:
                role = 'hub'
            elif deg > 0.1 and bet > 0.1:
                role = 'bridge'
            elif deg < 0.05:
                role = 'isolated'
            else:
                role = 'operative'
            
            # Adjust for agent type
            if agent_type == 'victim':
                role = 'victim'
            elif agent_type == 'instrument_of_fraud':
                role = 'tool'
            
            roles[entity_id] = role
        
        self.entity_roles = roles
        print(f"✓ Classified roles for {len(roles)} entities")
        
        return roles
    
    def generate_report(self, output_dir: str = None) -> Dict:
        """
        Phase 5: Generate comprehensive analysis report.
        Returns: Complete analysis data structure.
        """
        if output_dir is None:
            output_dir = str(self.workspace_dir)
        
        print("\nGenerating analysis report...")
        
        # Prepare summary statistics
        summary = {
            'total_entities': len(self.graph.nodes()),
            'total_relationships': len(self.graph.edges()),
            'network_density': nx.density(self.graph),
            'connected_components': len(list(nx.connected_components(self.graph))),
            'average_degree': sum(dict(self.graph.degree()).values()) / len(self.graph.nodes()) if len(self.graph.nodes()) > 0 else 0,
            'clustering_coefficient': nx.average_clustering(self.graph),
            'network_diameter': nx.diameter(self.graph) if nx.is_connected(self.graph) else 'N/A (disconnected)',
        }
        
        # Centrality rankings
        rankings = {}
        for metric_name, metric_dict in self.centrality_metrics.items():
            sorted_scores = sorted(metric_dict.items(), key=lambda x: x[1], reverse=True)
            rankings[metric_name] = [
                {'entity_id': eid, 'score': score, 'name': self.graph.nodes[eid].get('name', eid)}
                for eid, score in sorted_scores[:20]  # Top 20
            ]
        
        # Build comprehensive report
        report = {
            'metadata': {
                'analysis_type': 'social_organizational_network_analysis',
                'case_number': '2025-137857',
                'analysis_date': Path(output_dir).name,
                'phases_completed': [1, 2, 3, 4, 5],
                'entities_analyzed': summary['total_entities'],
                'relationships_analyzed': summary['total_relationships']
            },
            'summary': summary,
            'centrality_rankings': rankings,
            'entity_roles': self.entity_roles,
            'communities': {
                str(k): v for k, v in self.communities.items()
            },
            'hierarchy': self.hierarchy,
            'network_nodes': [
                {
                    'entity_id': node,
                    'name': self.graph.nodes[node].get('name', node),
                    'type': self.graph.nodes[node].get('type', 'unknown'),
                    'agent_type': self.graph.nodes[node].get('agent_type', 'unknown'),
                    'role': self.entity_roles.get(node, 'unknown'),
                    'degree': self.graph.degree(node),
                    'weighted_degree': sum(self.graph[node][neighbor].get('weight', 1) 
                                          for neighbor in self.graph[node]),
                    'involvement_events': self.graph.nodes[node].get('involvement_events', 0),
                    'financial_impact': self.graph.nodes[node].get('financial_impact', 'unknown')
                }
                for node in sorted(self.graph.nodes())
            ],
            'network_edges': [
                {
                    'source': u,
                    'target': v,
                    'weight': self.graph[u][v].get('weight', 1),
                    'relation_type': self.graph[u][v].get('relation_type', 'unknown'),
                    'strength': self.graph[u][v].get('strength', 'unknown'),
                    'legal_status': self.graph[u][v].get('legal_status', 'unknown'),
                    'evidence_count': self.graph[u][v].get('evidence_count', 0)
                }
                for u, v in self.graph.edges()
            ]
        }
        
        return report
    
    def run_analysis(self) -> bool:
        """Run complete network analysis pipeline."""
        print("=" * 70)
        print("NETWORK ANALYSIS FOR REVENUE STREAM HIJACKING CASE 2025-137857")
        print("=" * 70)
        
        # Phase 1: Data Loading & Network Building
        print("\nPHASE 1: Data Extraction & Network Building")
        print("-" * 70)
        
        if not self.load_data():
            return False
        
        if not self.build_network():
            return False
        
        validation = self.validate_network()
        
        # Phase 2: Metrics Calculation
        print("\nPHASE 2: Network Metrics Calculation")
        print("-" * 70)
        
        self.calculate_centrality_metrics()
        self.detect_communities()
        self.classify_entity_roles()
        
        # Phase 3 & 4: Hierarchy Analysis (Parallel)
        print("\nPHASE 3 & 4: Relationship & Hierarchy Analysis")
        print("-" * 70)
        
        self.analyze_hierarchy()
        
        # Phase 5: Report Generation
        print("\nPHASE 5: Report Generation")
        print("-" * 70)
        
        report = self.generate_report()
        
        # Save report
        output_path = self.workspace_dir / "NETWORK_ANALYSIS_REPORT.json"
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n✓ Saved network analysis report to: {output_path}")
        
        print("\n" + "=" * 70)
        print("ANALYSIS COMPLETE")
        print("=" * 70)
        print(f"\nKey Findings:")
        print(f"  Total Entities: {report['metadata']['entities_analyzed']}")
        print(f"  Total Relationships: {report['metadata']['relationships_analyzed']}")
        print(f"  Network Density: {report['summary']['network_density']:.3f}")
        print(f"  Communities Identified: {len(report['communities'])}")
        print(f"  Hierarchy Levels: {sum(1 for v in report['hierarchy'].values() if v)}")
        
        return True


def main():
    """Main execution."""
    analyzer = NetworkAnalysis()
    success = analyzer.run_analysis()
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
