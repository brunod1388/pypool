def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI from height and weight."""
    return [w / h ** 2 for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply limit to BMI."""
    return [b > limit for b in bmi]

