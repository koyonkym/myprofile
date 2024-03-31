from django.test import TestCase
from .models import ToeicScore
from django.core.exceptions import ValidationError


class ToeicScoreTestCase(TestCase):
    def test_total_score_calculation(self):
        # Valid data: Total score matches the sum of l_score and r_score
        valid_score = ToeicScore.objects.create(
            test_date="2024-03-20",
            l_score=300,
            r_score=400,
            total_score=700
        )
        # This should not raise any validation error
        valid_score.full_clean()

        # Invalid data: Total score does not match the sum of l_score and r_score
        with self.assertRaises(ValidationError):
            invalid_score = ToeicScore.objects.create(
                test_date="2024-03-20",
                l_score=300,
                r_score=400,
                total_score=800  # Total score does not match l_score + r_score
            )
            # This should raise a validation error
            invalid_score.full_clean()