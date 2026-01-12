class MIRARStorage:
    def __init__(self):
        self._reflections = []
        self._reflection_index = {}
        self._temporal_relationships = []

    def store_reflection(self, reflection):
        self._reflections.append(reflection)
        reflection_id = reflection.get("id")
        if reflection_id is not None:
            self._reflection_index[reflection_id] = reflection
        temporal_relationship = reflection.get("temporal_relationship")
        if temporal_relationship is not None:
            self._temporal_relationships.append(
                {
                    "source_node_id": reflection_id,
                    "relationship": temporal_relationship,
                }
            )

    def revise_confidence(self, reflection_id, new_confidence):
        reflection = self._reflection_index.get(reflection_id)
        if reflection is None:
            return False
        reflection["confidence"] = new_confidence
        return True

    def export_all(self):
        return list(self._reflections)
