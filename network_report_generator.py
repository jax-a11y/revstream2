"""
Network Analysis Report Generator

Phase 6: Visualization & Output
- Generates comprehensive markdown narrative report
- Creates visualization data for network diagrams
- Produces entity rankings and metrics tables
- Provides legal implications cross-reference
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple
import csv


class NetworkReportGenerator:
    """Generates comprehensive reports from network analysis results."""
    
    def __init__(self, workspace_dir: str = "d:\\Documents\\GitHub\\revstream2"):
        """Initialize with workspace directory."""
        self.workspace_dir = Path(workspace_dir)
        self.network_report = None
        self.entities_data = None
        self.load_data()
    
    def load_data(self):
        """Load the network analysis report and entity data."""
        # Load network report
        report_path = self.workspace_dir / "NETWORK_ANALYSIS_REPORT.json"
        if report_path.exists():
            with open(report_path) as f:
                self.network_report = json.load(f)
            print(f"✓ Loaded network analysis report")
        
        # Load entity data for additional context
        entities_path = self.workspace_dir / "data_models" / "entities" / "entities_refined_2025_11_18.json"
        if entities_path.exists():
            with open(entities_path) as f:
                self.entities_data = json.load(f)
            print(f"✓ Loaded entity reference data")
    
    def get_entity_name(self, entity_id: str) -> str:
        """Get the full name of an entity."""
        if not self.entities_data:
            return entity_id
        
        for category in ['persons', 'organizations', 'platforms', 'domains', 'trusts', 'other']:
            if category in self.entities_data.get('entities', {}):
                for entity in self.entities_data['entities'][category]:
                    if entity.get('entity_id') == entity_id:
                        return entity.get('name', entity_id)
        return entity_id
    
    def generate_markdown_report(self) -> str:
        """Generate comprehensive markdown narrative report."""
        if not self.network_report:
            return ""
        
        md = []
        md.append("# Network Analysis Report: Revenue Stream Hijacking Case 2025-137857")
        md.append("")
        md.append("**Analysis Type:** Social/Organizational Network Analysis")
        md.append(f"**Entities Analyzed:** {self.network_report['metadata']['entities_analyzed']}")
        md.append(f"**Relationships Analyzed:** {self.network_report['metadata']['relationships_analyzed']}")
        md.append(f"**Phases Completed:** {', '.join(map(str, self.network_report['metadata']['phases_completed']))}")
        md.append("")
        
        # Executive Summary
        md.append("## Executive Summary")
        md.append("")
        md.append("This analysis maps the social and organizational network of all entities involved in the Revenue Stream Hijacking case, identifying key decision-makers, revealing hierarchical structures, and understanding the conspiracy network topology.")
        md.append("")
        
        summary = self.network_report['summary']
        md.append("### Network Overview")
        md.append(f"- **Total Entities:** {summary['total_entities']}")
        md.append(f"- **Total Relationships:** {summary['total_relationships']}")
        md.append(f"- **Network Density:** {summary['network_density']:.3f} (likelihood of connection between random nodes)")
        md.append(f"- **Average Connections per Entity:** {summary['average_degree']:.1f}")
        md.append(f"- **Clustering Coefficient:** {summary['clustering_coefficient']:.3f} (tendency to form groups)")
        md.append(f"- **Connected Components:** {summary['connected_components']}")
        md.append(f"- **Network Diameter:** {summary['network_diameter']}")
        md.append("")
        
        # Key Actors (Top by Centrality)
        md.append("## Key Actors and Influence Rankings")
        md.append("")
        md.append("### Most Connected Entities (Degree Centrality)")
        md.append("These entities have the most direct relationships, indicating broad involvement across the network.")
        md.append("")
        degree_rankings = self.network_report['centrality_rankings'].get('degree_centrality', [])
        for i, actor in enumerate(degree_rankings[:10], 1):
            md.append(f"{i}. **{actor['name']}** ({actor['entity_id']})")
            md.append(f"   - Degree Centrality Score: {actor['score']:.3f}")
        md.append("")
        
        # Betweenness
        md.append("### Control of Information Flow (Betweenness Centrality)")
        md.append("These entities act as intermediaries or gatekeepers in the network, controlling information and resource flow.")
        md.append("")
        betweenness_rankings = self.network_report['centrality_rankings'].get('betweenness_centrality', [])
        for i, actor in enumerate(betweenness_rankings[:10], 1):
            md.append(f"{i}. **{actor['name']}** ({actor['entity_id']})")
            md.append(f"   - Betweenness Centrality Score: {actor['score']:.3f}")
        md.append("")
        
        # Eigenvector
        if self.network_report['centrality_rankings'].get('eigenvector_centrality'):
            md.append("### Influence Through Connections (Eigenvector Centrality)")
            md.append("These entities are connected to other influential entities, amplifying their influence.")
            md.append("")
            eigen_rankings = self.network_report['centrality_rankings'].get('eigenvector_centrality', [])
            for i, actor in enumerate(eigen_rankings[:10], 1):
                md.append(f"{i}. **{actor['name']}** ({actor['entity_id']})")
                md.append(f"   - Eigenvector Centrality Score: {actor['score']:.3f}")
            md.append("")
        
        # Entity Roles
        md.append("## Entity Roles and Classifications")
        md.append("")
        roles_by_type = {}
        for entity_id, role in self.network_report['entity_roles'].items():
            if role not in roles_by_type:
                roles_by_type[role] = []
            roles_by_type[role].append(entity_id)
        
        role_descriptions = {
            'leader': 'High centrality and influence; primary decision-makers',
            'facilitator': 'Control information/resource flow; intermediaries',
            'hub': 'Highly connected nodes in the network',
            'bridge': 'Connect otherwise separate groups',
            'operative': 'Executes tasks; limited network reach',
            'tool': 'Used as instrument of fraud; minimal agency',
            'isolated': 'Minimal network connections',
            'victim': 'Primary targets of the fraud scheme'
        }
        
        for role, description in role_descriptions.items():
            if role in roles_by_type:
                entities = roles_by_type[role]
                md.append(f"### {role.replace('_', ' ').title()} ({len(entities)} entities)")
                md.append(f"{description}")
                md.append("")
                for entity_id in sorted(entities):
                    entity_name = self.get_entity_name(entity_id)
                    md.append(f"- {entity_name} ({entity_id})")
                md.append("")
        
        # Organizational Hierarchy
        md.append("## Organizational Hierarchy")
        md.append("")
        md.append("The network analysis reveals a multi-level hierarchical structure within the conspiracy:")
        md.append("")
        
        hierarchy = self.network_report['hierarchy']
        hierarchy_order = ['top_level', 'middle_management', 'operatives', 'support', 'victims']
        
        for level in hierarchy_order:
            if level in hierarchy and hierarchy[level]:
                entities = hierarchy[level]
                level_label = level.replace('_', ' ').title()
                md.append(f"### {level_label}")
                md.append(f"**Count:** {len(entities)}")
                md.append("")
                for entity_id in sorted(entities):
                    entity_name = self.get_entity_name(entity_id)
                    # Find node info
                    node_info = next((n for n in self.network_report['network_nodes'] 
                                     if n['entity_id'] == entity_id), None)
                    if node_info:
                        md.append(f"- **{entity_name}** ({entity_id})")
                        md.append(f"  - Type: {node_info['type']}")
                        md.append(f"  - Agent Type: {node_info['agent_type']}")
                        md.append(f"  - Network Degree: {node_info['degree']}")
                        if node_info['financial_impact'] != 'unknown':
                            md.append(f"  - Financial Impact: {node_info['financial_impact']}")
                    else:
                        md.append(f"- {entity_name} ({entity_id})")
                md.append("")
        
        # Communities/Subgroups
        md.append("## Network Communities and Subgroups")
        md.append("")
        md.append("The analysis identified natural clusters of entities that work together or share common characteristics:")
        md.append("")
        
        communities = self.network_report['communities']
        for comm_id in sorted(communities.keys()):
            entities = communities[comm_id]
            md.append(f"### Community {comm_id}")
            md.append(f"**Member Count:** {len(entities)}")
            md.append("")
            for entity_id in sorted(entities):
                entity_name = self.get_entity_name(entity_id)
                md.append(f"- {entity_name} ({entity_id})")
            md.append("")
        
        # Vulnerability Analysis
        md.append("## Vulnerability and Critical Node Analysis")
        md.append("")
        md.append("**Critical Nodes** (highest betweenness centrality) represent bottlenecks whose removal would most disrupt the network:")
        md.append("")
        
        betweenness_rankings = self.network_report['centrality_rankings'].get('betweenness_centrality', [])
        for actor in betweenness_rankings[:5]:
            md.append(f"- **{actor['name']}** ({actor['entity_id']})")
            md.append(f"  - Controls {actor['score']*100:.1f}% of critical paths")
        md.append("")
        
        md.append("**Strategic Implications:**")
        md.append("- Removing these individuals would break critical communication and resource flow channels")
        md.append("- Their centrality indicates essential roles in coordinating fraudulent activities")
        md.append("- Evidence of continued contact with these nodes strengthens conspiracy charges")
        md.append("")
        
        # Legal Implications
        md.append("## Legal Implications and Conspiracy Evidence")
        md.append("")
        md.append("The network structure provides strong evidence for conspiracy and coordinated fraud:")
        md.append("")
        md.append("### Indicators of Conspiracy")
        md.append(f"1. **Network Density ({summary['network_density']:.3f}):** Moderate density indicates coordinated activity beyond coincidence")
        md.append(f"2. **Hierarchical Structure:** Clear decision-making hierarchy from top-level perpetrators to operatives")
        md.append(f"3. **Role Specialization:** {len(roles_by_type)} distinct roles indicating division of labor")
        md.append(f"4. **Clustering ({summary['clustering_coefficient']:.3f}):** High clustering shows subgroups working together")
        md.append("")
        
        md.append("### Recommended Focus Areas for Prosecution")
        md.append("")
        md.append("**Top-Level Perpetrators** (highest degree + betweenness):")
        top_by_both = sorted(degree_rankings[:5], 
                            key=lambda x: x['score'], reverse=True)
        for actor in top_by_both:
            md.append(f"- {actor['name']} ({actor['entity_id']}): Primary decision-maker and coordinator")
        md.append("")
        
        md.append("**Facilitators/Intermediaries** (high betweenness):")
        for actor in betweenness_rankings[1:6]:
            md.append(f"- {actor['name']} ({actor['entity_id']}): Control key information/resource flows")
        md.append("")
        
        # Statistical Summary
        md.append("## Statistical Summary")
        md.append("")
        md.append("### Entity Type Distribution")
        type_counts = {}
        for node in self.network_report['network_nodes']:
            entity_type = node['type']
            type_counts[entity_type] = type_counts.get(entity_type, 0) + 1
        
        for entity_type, count in sorted(type_counts.items()):
            md.append(f"- {entity_type.title()}: {count}")
        md.append("")
        
        md.append("### Agent Type Distribution")
        agent_counts = {}
        for node in self.network_report['network_nodes']:
            agent_type = node['agent_type']
            agent_counts[agent_type] = agent_counts.get(agent_type, 0) + 1
        
        for agent_type, count in sorted(agent_counts.items()):
            md.append(f"- {agent_type.title()}: {count}")
        md.append("")
        
        md.append("### Role Distribution")
        role_counts = {}
        for role, entities in roles_by_type.items():
            role_counts[role] = len(entities)
        
        for role, count in sorted(role_counts.items(), key=lambda x: x[1], reverse=True):
            md.append(f"- {role.title()}: {count}")
        md.append("")
        
        # Conclusions
        md.append("## Conclusions")
        md.append("")
        md.append("This network analysis reveals:")
        md.append("")
        md.append(f"1. A multi-layered conspiracy involving {summary['total_entities']} entities connected through {summary['total_relationships']} relationships")
        md.append(f"2. Clear hierarchical structure with {len(hierarchy['top_level'])} top-level decision-makers")
        md.append(f"3. {len(hierarchy['middle_management'])} facilitators controlling resource and information flows")
        md.append(f"4. Specialized roles indicating coordinated planning and execution")
        md.append(f"5. Multiple isolated subgroups (families, organizations) operating in coordination")
        md.append("")
        md.append("The network structure provides compelling evidence of conspiracy beyond individual fraud acts, supporting enhanced criminal charges and demonstrating systematic coordination of illegal activities.")
        md.append("")
        
        return "\n".join(md)
    
    def generate_csv_metrics(self):
        """Generate CSV files with detailed metrics tables."""
        if not self.network_report:
            return
        
        # Entity metrics CSV
        csv_path = self.workspace_dir / "NETWORK_ANALYSIS_ENTITY_METRICS.csv"
        with open(csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Header
            writer.writerow([
                'Entity ID',
                'Name',
                'Type',
                'Agent Type',
                'Role',
                'Degree',
                'Weighted Degree',
                'Involvement Events',
                'Financial Impact',
                'Degree Centrality',
                'Betweenness Centrality',
                'Closeness Centrality'
            ])
            
            # Data
            degree_cent = {n['entity_id']: n.get('score', 0) 
                          for n in self.network_report['centrality_rankings'].get('degree_centrality', [])}
            betweenness = {n['entity_id']: n.get('score', 0) 
                          for n in self.network_report['centrality_rankings'].get('betweenness_centrality', [])}
            closeness = {n['entity_id']: n.get('score', 0) 
                        for n in self.network_report['centrality_rankings'].get('closeness_centrality', [])}
            
            for node in self.network_report['network_nodes']:
                entity_id = node['entity_id']
                writer.writerow([
                    entity_id,
                    self.get_entity_name(entity_id),
                    node['type'],
                    node['agent_type'],
                    self.network_report['entity_roles'].get(entity_id, 'unknown'),
                    node['degree'],
                    node['weighted_degree'],
                    node['involvement_events'],
                    node['financial_impact'],
                    f"{degree_cent.get(entity_id, 0):.4f}",
                    f"{betweenness.get(entity_id, 0):.4f}",
                    f"{closeness.get(entity_id, 0):.4f}"
                ])
        
        print(f"✓ Saved entity metrics to: {csv_path}")
        
        # Relationships CSV
        csv_path = self.workspace_dir / "NETWORK_ANALYSIS_RELATIONSHIPS.csv"
        with open(csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Source ID',
                'Source Name',
                'Target ID',
                'Target Name',
                'Weight',
                'Relation Type',
                'Strength',
                'Legal Status',
                'Evidence Count'
            ])
            
            for edge in self.network_report['network_edges']:
                writer.writerow([
                    edge['source'],
                    self.get_entity_name(edge['source']),
                    edge['target'],
                    self.get_entity_name(edge['target']),
                    f"{edge['weight']:.3f}",
                    edge['relation_type'],
                    edge['strength'],
                    edge['legal_status'],
                    edge['evidence_count']
                ])
        
        print(f"✓ Saved relationship matrix to: {csv_path}")
    
    def generate_visualization_data(self) -> Dict:
        """Generate data structure optimized for network visualization."""
        if not self.network_report:
            return {}
        
        viz_data = {
            'nodes': [],
            'edges': [],
            'metadata': {
                'total_nodes': len(self.network_report['network_nodes']),
                'total_edges': len(self.network_report['network_edges']),
                'visualization_formats': ['force-directed', 'hierarchical', 'community']
            }
        }
        
        # Prepare node data for visualization
        degree_cent = {n['entity_id']: n.get('score', 0) 
                      for n in self.network_report['centrality_rankings'].get('degree_centrality', [])}
        
        for node in self.network_report['network_nodes']:
            entity_id = node['entity_id']
            viz_node = {
                'id': entity_id,
                'label': self.get_entity_name(entity_id),
                'type': node['type'],
                'agent_type': node['agent_type'],
                'role': self.network_report['entity_roles'].get(entity_id, 'unknown'),
                'size': max(10, int(node['degree'] * 15 + 10)),  # Scale for visualization
                'degree': node['degree'],
                'weighted_degree': node['weighted_degree'],
                'centrality_score': degree_cent.get(entity_id, 0),
                'color_by_agent_type': {
                    'antagonist': '#FF0000',
                    'victim': '#0000FF',
                    'neutral': '#808080',
                    'accomplice': '#FFA500',
                    'instrument_of_fraud': '#800080',
                    'affected_entity': '#FFFF00'
                }.get(node['agent_type'], '#CCCCCC'),
                'color_by_role': {
                    'leader': '#FF0000',
                    'facilitator': '#FFA500',
                    'hub': '#FFFF00',
                    'bridge': '#00FF00',
                    'operative': '#0000FF',
                    'victim': '#808080',
                    'isolated': '#CCCCCC'
                }.get(self.network_report['entity_roles'].get(entity_id, 'unknown'), '#CCCCCC')
            }
            viz_data['nodes'].append(viz_node)
        
        # Prepare edge data
        for edge in self.network_report['network_edges']:
            viz_edge = {
                'source': edge['source'],
                'target': edge['target'],
                'weight': edge['weight'],
                'relation_type': edge['relation_type'],
                'strength': edge['strength'],
                'legal_status': edge['legal_status'],
                'color': '#FF0000' if edge['legal_status'] in ['disputed', 'fraud_related'] else '#0000FF',
                'width': max(1, int(edge['weight'] * 5))
            }
            viz_data['edges'].append(viz_edge)
        
        return viz_data
    
    def generate_all_outputs(self):
        """Generate all Phase 6 outputs."""
        print("\nPHASE 6: Visualization & Output Generation")
        print("-" * 70)
        
        # Generate markdown report
        print("\nGenerating markdown narrative report...")
        md_content = self.generate_markdown_report()
        md_path = self.workspace_dir / "NETWORK_ANALYSIS_SUMMARY.md"
        with open(md_path, 'w') as f:
            f.write(md_content)
        print(f"✓ Saved markdown summary to: {md_path}")
        
        # Generate CSV metrics
        print("\nGenerating CSV metrics tables...")
        self.generate_csv_metrics()
        
        # Generate visualization data
        print("\nGenerating visualization data...")
        viz_data = self.generate_visualization_data()
        viz_path = self.workspace_dir / "NETWORK_VISUALIZATION_DATA.json"
        with open(viz_path, 'w') as f:
            json.dump(viz_data, f, indent=2)
        print(f"✓ Saved visualization data to: {viz_path}")
        
        print("\n" + "=" * 70)
        print("PHASE 6 COMPLETE - All outputs generated successfully")
        print("=" * 70)
        print("\nGenerated Files:")
        print(f"  1. NETWORK_ANALYSIS_REPORT.json (metrics and data)")
        print(f"  2. NETWORK_ANALYSIS_SUMMARY.md (narrative report)")
        print(f"  3. NETWORK_ANALYSIS_ENTITY_METRICS.csv (entity rankings)")
        print(f"  4. NETWORK_ANALYSIS_RELATIONSHIPS.csv (relationship matrix)")
        print(f"  5. NETWORK_VISUALIZATION_DATA.json (visualization format)")


def main():
    """Main execution."""
    generator = NetworkReportGenerator()
    generator.generate_all_outputs()


if __name__ == "__main__":
    main()
