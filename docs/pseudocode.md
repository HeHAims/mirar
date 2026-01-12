# MIRAR Pseudocode

```python
class QuantumFeelingNode:
    id: uuid
    capture_time: datetime | None  # When sensing occurred, if known (capture time).
    reflection_time: datetime  # When meaning is authored (reflection time).
    emotion_label: str
    intensity: float | None  # Human-provided or None.
    confidence: float | None  # Human-provided, revisable.
    narrative: str  # Human-authored text.
    temporal_relationship: dict | None  # Human-authored relationship.


class MIRARStorage:
    def __init__(self):
        self.reflections = []
        self.reflection_index = {}
        self.temporal_relationships = []  # Stored edges, no analysis.

    def store_reflection(self, node):
        """Store a human-authored reflection without inference or analysis."""
        self.reflections.append(node)
        self.reflection_index[node.id] = node
        if node.temporal_relationship is not None:
            self.temporal_relationships.append(
                {
                    "source_node_id": node.id,
                    "relationship": node.temporal_relationship,
                }
            )

    def revise_confidence(self, node_id, new_confidence):
        """Human revision only."""
        if node_id in self.reflection_index:
            self.reflection_index[node_id].confidence = new_confidence

    def export_all(self):
        """Return reflections as authored."""
        return list(self.reflections)
```

## Phase 1 Constraints
- No inference
- No prediction
- No automation
- No graph analysis

## Design Notes
- Temporal relationships are explicit because meaning comes from lived interpretation, not inference.
- Strength is subjective because it reflects felt influence, not statistical certainty.
- This phase protects authorship by keeping storage simple and unautomated.
