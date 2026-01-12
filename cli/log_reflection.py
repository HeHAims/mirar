import json
import uuid
from datetime import datetime, timezone
from pathlib import Path


def prompt_required(label):
    while True:
        value = input(label).strip()
        if value:
            return value


def parse_optional_float(value):
    value = value.strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def prompt_temporal_relationship():
    rel_type = input(
        "Temporal relationship type (precedes/follows/parallels/triggers) [optional]: "
    ).strip()
    if not rel_type:
        return None
    target_node_id = input("Temporal relationship target node id: ").strip()
    if not target_node_id:
        return None
    strength = parse_optional_float(
        input("Temporal relationship strength 0.0-1.0 [optional]: ")
    )
    if strength is None:
        return None
    return {
        "type": rel_type.lower(),
        "target_node_id": target_node_id,
        "strength": strength,
    }


def main():
    emotion_label = prompt_required("Emotion label: ")
    narrative = prompt_required("Narrative: ")
    intensity = parse_optional_float(input("Intensity 0.0-1.0 [optional]: "))
    confidence = parse_optional_float(input("Confidence 0.0-1.0 [optional]: "))
    temporal_relationship = prompt_temporal_relationship()

    record = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "emotion_label": emotion_label,
        "narrative": narrative,
        "intensity": intensity,
        "confidence": confidence,
    }
    if temporal_relationship is not None:
        record["temporal_relationship"] = temporal_relationship

    base_dir = Path(__file__).resolve().parents[1]
    data_dir = base_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    file_path = data_dir / "my_reflections.json"

    if file_path.exists():
        try:
            with file_path.open("r", encoding="utf-8") as handle:
                reflections = json.load(handle)
            if not isinstance(reflections, list):
                reflections = []
        except (json.JSONDecodeError, OSError):
            reflections = []
    else:
        reflections = []

    reflections.append(record)
    with file_path.open("w", encoding="utf-8") as handle:
        json.dump(reflections, handle, indent=2)


if __name__ == "__main__":
    main()
