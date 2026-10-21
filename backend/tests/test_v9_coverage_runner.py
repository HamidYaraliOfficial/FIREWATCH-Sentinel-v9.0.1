"""Deterministic shard allocation and staged coverage range contracts."""
import importlib.util
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("firewatch_coverage_runner", ROOT / "scripts/run_coverage_shards.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)

@pytest.mark.parametrize("module_count", list(range(1, 81)))
@pytest.mark.parametrize("shard_count", [1, 2, 3, 5, 8, 13, 20])
def test_v9_sharding_preserves_every_module_exactly_once(module_count, shard_count):
    counts = {f"tests/test_{i:03}.py": (i % 17) + 1 for i in range(module_count)}
    bins = module.make_bins(counts, shard_count)
    flat = [name for bucket in bins for name in bucket]
    assert sorted(flat) == sorted(counts)
    assert len(flat) == len(set(flat))
    assert all(bucket for bucket in bins)

@pytest.mark.parametrize("shard_count", list(range(1, 21)))
def test_v9_default_shard_range_selects_every_shard(shard_count):
    assert module.parse_shard_range("", shard_count) == list(range(1, shard_count + 1))

@pytest.mark.parametrize("value,expected", [
    ("1-1", [1]), ("1-4", [1,2,3,4]), ("5-8", [5,6,7,8]),
    ("8-8", [8]), ("2-20", list(range(2,21))),
])
def test_v9_shard_range_parser_accepts_valid_inclusive_ranges(value, expected):
    assert module.parse_shard_range(value, 20) == expected

@pytest.mark.parametrize("value", [
    "0-1", "2-1", "1-0", "1-21", "1", "1-2-3", "a-3", "-3", "2-", " 1-3 ",
    "1;2", "../1-3", "-1-4", "1.0-3", "1 - 3",
])
def test_v9_shard_range_parser_rejects_malformed_or_out_of_bounds_ranges(value):
    with pytest.raises(ValueError):
        module.parse_shard_range(value, 20)

@pytest.mark.parametrize("shards", [0, -1, 21, True, 2.5, "8"])
def test_v9_shard_allocator_rejects_invalid_shard_counts(shards):
    with pytest.raises(ValueError):
        module.make_bins({"tests/test_a.py": 1}, shards)

@pytest.mark.parametrize("counts", [{}, {"": 2}, {"tests/a.py": 0}, {"tests/a.py": -1}, {"tests/a.py": 1.5}, {"tests/a.py": True}])
def test_v9_shard_allocator_rejects_invalid_module_count_maps(counts):
    with pytest.raises(ValueError):
        module.make_bins(counts, 2)


def test_v9_sharding_is_deterministic_when_mapping_insertion_order_changes():
    pairs = [(f"tests/test_{i:02}.py", (i * 7) % 19 + 1) for i in range(60)]
    a = module.make_bins(dict(pairs), 8)
    b = module.make_bins(dict(reversed(pairs)), 8)
    assert a == b
