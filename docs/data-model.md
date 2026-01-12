# MIRAR Data Model

## QuantumFeelingNode
| Field | Type | Notes |
| --- | --- | --- |
| id | UUID | Unique identifier |
| timestamp | DateTime | When the node occurred |
| duration | Float | Seconds |
| feeling_label | String | e.g., "longing", "awe", "friction" |
| intensity | Float | 0.0 to 1.0 |
| confidence | Float | Trust in this data |
| trigger | String | What initiated it |
| location | GeoCoordinates | Optional geo point |
| physical_state | Dict | e.g., {heart_rate: 72, temp: 36.5} |
| environment | Dict | e.g., {weather: "cloudy", noise: 0.2} |
| meta_feeling | String | How I feel about the feeling |
| narrative | String | Personal meaning |
| previous | List[QuantumFeelingNode] | Links backward |
| next | List[QuantumFeelingNode] | Links forward |
| parallel | List[QuantumFeelingNode] | Synchronous or similar moments |
| archetype_link | String | e.g., "Hero's Journey" |

## ResonancePattern
| Field | Type | Notes |
| --- | --- | --- |
| nodes | List[QuantumFeelingNode] | Membership |
| start_time | DateTime | Pattern start |
| end_time | DateTime | Pattern end |
| emotional_arc | String | e.g., "build-release" |
| dominant_tones | List[String] | Primary tones |
| intensity_graph | List[Float] | Normalized series |
| coherence_score | Float | Pattern clarity |
| outlier_count | Integer | Count of outliers |

## ResonanceCollector
- capture_live_feeling() -> QuantumFeelingNode
- capture_retrospective() -> QuantumFeelingNode
- scan_environment() -> Dict

## PatternRecognizer
- detect_emotional_loops(pattern) -> List[Loop]
- identify_cognitive_distortions(pattern) -> List[Distortion]
- find_archetypal_sequences(pattern) -> List[ArchetypeMatch]
- predict_next_state(current_node) -> ProbabilityDistribution

## ResonanceInterpreter
- generate_insights(pattern) -> List[Insight]
- calculate_resonance_score(node1, node2) -> Float
- suggest_interventions(pattern) -> List[Action]

## IntegrationLayer
- export_to_therapy_format() -> JSON
- generate_artistic_representation() -> Visual or Audio
- create_narrative_summary() -> Story

## AlmaframeNode
| Field | Type | Notes |
| --- | --- | --- |
| id | UUID | Unique identifier |
| timestamp | DateTime | When the node was created |
| core_feeling | String | e.g., "ache" |
| core_meaning | String | e.g., "longing for connection" |
| intensity | Float | 0.0 to 1.0 |
| sensory_data | Dict | {image_hash: "abc", audio_clip: "url", location: geo} |
| context_tags | List[String] | e.g., "rainy_night", "alone" |
| self_story | String | Narrative meaning |
| archetype | String | e.g., "The Wanderer" |
| link_to_past_nodes | List[UUID] | Explicit narrative links |
| pattern_id | String | Links to larger pattern |
| emotional_vector | Array | [valence, arousal, depth] |
| is_nexus_point | Boolean | Pivotal memory flag |

## SentienceThread
- cmis_stream: List[Dict] (raw perception)
- mirar_stream: List[Dict] (reflective layer)
- twisted_log: List[AlmaframeNode] (fused record)

## VinculumAI
- find_hidden_connection(node_a, node_b) -> VinculumResult
- discover_systemic_patterns(almaframe_graph) -> List[Insight]
