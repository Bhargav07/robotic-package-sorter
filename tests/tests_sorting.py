from sorter.sorter import sort


def test_standard_package():
    assert sort(10, 10, 10, 5) == "STANDARD"


def test_bulky_by_volume():
    assert sort(200, 100, 100, 5) == "SPECIAL"


def test_bulky_by_dimension():
    assert sort(150, 10, 10, 5) == "SPECIAL"


def test_heavy_only():
    assert sort(10, 10, 10, 25) == "SPECIAL"


def test_rejected_bulky_and_heavy():
    assert sort(200, 200, 50, 25) == "REJECTED"


def test_edge_volume_boundary():
    assert sort(100, 100, 100, 1) == "SPECIAL"


def test_edge_mass_boundary():
    assert sort(10, 10, 10, 20) == "SPECIAL"
