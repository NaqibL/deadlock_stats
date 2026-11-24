"""Checks against the real cached source. Skipped until ``python build.py`` has populated ``.cache/``."""
from pathlib import Path

import pytest

from src import abilities, heroes, items, source, validate

REPO = Path(__file__).resolve().parent.parent / ".cache" / "deadlock-data"
pytestmark = pytest.mark.skipif(not (REPO / "data").exists(), reason="no cached source; run build.py first")


@pytest.fixture(scope="module")
def live():
    primary = source.load_primary(REPO)
    return (heroes.build_heroes(primary)[0], abilities.build_abilities(primary)[0], items.build_items(primary)[0])


def test_real_source_passes_structural_rules(live):
    counts = validate.table_counts(*live)
    findings = validate.check_counts(counts) + validate.check_completeness(*live)
    assert not validate.has_errors(findings), [str(f) for f in findings]


def test_real_source_matches_reference_values(live):
    """Fails after a balance patch changes a reference value: check the patch notes, then update SANITY."""
    findings = validate.check_sanity(*live)
    assert findings == [], [str(f) for f in findings]


def test_real_item_categories_are_english(live):
    assert {row["category"] for row in live[2]} == {"Weapon", "Vitality", "Spirit"}
