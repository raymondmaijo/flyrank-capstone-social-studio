from app.core.constraint_profiles import PROFILES
from app.core.exceptions import ConstraintViolation


class ConstraintValidator:
    def validate(self, variant):
        profile = PROFILES[variant.platform.value]
        errors = []

        if len(variant.content) > profile.max_chars:
            errors.append(f"length: exceeds {profile.max_chars} chars")

        if variant.hashtags_count > profile.max_hashtags:
            errors.append(f"hashtags: exceeds {profile.max_hashtags} hashtags")

        if errors:
            raise ConstraintViolation(errors)

        return True
