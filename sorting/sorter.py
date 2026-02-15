BULKY_VOLUME_MAX = 1_000_000  # cm^3
BULKY_DIMENSION_MAX = 150     # cm
HEAVY_MASS_MAX = 20           # kg


def sort(width: float, height: float, length: float, mass: float) -> str:
    """Classify a package into a stack based on dimensions and mass."""
    volume = width * height * length

    is_bulky = (
        volume >= BULKY_VOLUME_MAX
        or width >= BULKY_DIMENSION_MAX
        or height >= BULKY_DIMENSION_MAX
        or length >= BULKY_DIMENSION_MAX
    )

    is_heavy = mass >= HEAVY_MASS_MAX

    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"
