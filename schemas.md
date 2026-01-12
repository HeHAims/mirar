# MIRAR Schemas

Illustrative JSON examples that lock meaning and authorship before any interface or tooling.
These are not validation rules, only shared shapes for reflection-driven data.

## QuantumFeelingNode (example JSON)
Fields express a single lived moment with context and narrative meaning.
If a CMIS-style layer is added later, the `context.trigger` or `narrative` text could be annotated
with `{subject, action, obj}` descriptors in a separate tag record.

```json
{
  "id": "7d2e2b0a-5ef3-4c7f-9b76-645b0e9f2a31",
  "timestamp": "2026-01-11T19:02:15Z",
  "emotion_label": "longing",
  "intensity": 0.78,
  "confidence": 0.72,
  "context": {
    "location": {
      "label": "front porch",
      "lat": 36.1699,
      "lon": -115.1398
    },
    "trigger": "Watching the rain settle and thinking about a friend.",
    "body_state": {
      "heart_rate": 74,
      "breath": "shallow",
      "temperature_c": 36.6
    }
  },
  "narrative": "I felt the distance as a soft ache, like a door left slightly open.",
  "previous_node": null,
  "next_node": "c5a4c0c5-1cf4-4d0f-8fe1-01a3f3c4f0b2",
  "temporal_relationship": {
    "type": "precedes",
    "target_node_id": "f4c7b0f7-9a61-4e8b-8b16-9d23a4e7b2c8",
    "strength": 0.64
  }
}
```

Notes:
- `previous_node` and `next_node` are optional; omit or set to null when no link exists.
- `temporal_relationship` is optional; Phase 1 allows at most one relationship per node.
- `strength` expresses perceived influence, not certainty.
- Relationships are human-authored, not inferred.
- See docs/vocabulary.md for temporal relationship types and meaning.
- Language stays human-authored and interpretive by design.

## AlmaframeNode (example JSON)
Fields express a reflective synthesis across multiple moments without prediction or automation.
If CMIS-style tagging is added later, `dominant_themes` could be complemented by `{subject, action, obj}`
tags stored alongside the themes, not embedded here.

```json
{
  "id": "2a4b53ab-9f6b-4f70-9e47-6fd3c5bf4c8c",
  "archetype": "The Threshold",
  "dominant_themes": [
    "distance",
    "returning",
    "quiet resolve"
  ],
  "time_window": {
    "start": "2026-01-10T06:00:00Z",
    "end": "2026-01-11T23:00:00Z"
  },
  "confidence": 0.66,
  "linked_quantum_feeling_node_ids": [
    "7d2e2b0a-5ef3-4c7f-9b76-645b0e9f2a31",
    "c5a4c0c5-1cf4-4d0f-8fe1-01a3f3c4f0b2",
    "0e72c5f7-1c6a-4b83-9b76-1c0d98fca3af"
  ]
}
```

## Why schemas come before UI
Schemas preserve meaning and authorship before interface decisions shape behavior. By agreeing on
the reflective data shapes first, the project protects narrative depth, keeps human intent explicit,
and makes later tools serve the lived record instead of redefining it.
