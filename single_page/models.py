from django.db import models
from django.core.exceptions import ValidationError


class ToeicScore(models.Model):
    institution_code = models.CharField(max_length=255, null=True, blank=True)
    institution_name = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    registration_number = models.CharField(max_length=255, null=True, blank=True)
    administration_number = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    test_date = models.DateField()
    l_score = models.IntegerField()
    l_percentile_rank = models.IntegerField(null=True, blank=True)
    r_score = models.IntegerField()
    r_percentile_rank = models.IntegerField(null=True, blank=True)
    total_score = models.IntegerField()
    l_abilities_measured_1_percentage = models.IntegerField(null=True, blank=True)
    l_abilities_measured_1_average = models.IntegerField(null=True, blank=True)
    l_abilities_measured_2_percentage = models.IntegerField(null=True, blank=True)
    l_abilities_measured_2_average = models.IntegerField(null=True, blank=True)
    l_abilities_measured_3_percentage = models.IntegerField(null=True, blank=True)
    l_abilities_measured_3_average = models.IntegerField(null=True, blank=True)
    l_abilities_measured_4_percentage = models.IntegerField(null=True, blank=True)
    l_abilities_measured_4_average = models.IntegerField(null=True, blank=True)
    l_abilities_measured_5_percentage = models.IntegerField(null=True, blank=True)
    l_abilities_measured_5_average = models.IntegerField(null=True, blank=True)
    r_abilities_measured_1_percentage = models.IntegerField(null=True, blank=True)
    r_abilities_measured_1_average = models.IntegerField(null=True, blank=True)
    r_abilities_measured_2_percentage = models.IntegerField(null=True, blank=True)
    r_abilities_measured_2_average = models.IntegerField(null=True, blank=True)
    r_abilities_measured_3_percentage = models.IntegerField(null=True, blank=True)
    r_abilities_measured_3_average = models.IntegerField(null=True, blank=True)
    r_abilities_measured_4_percentage = models.IntegerField(null=True, blank=True)
    r_abilities_measured_4_average = models.IntegerField(null=True, blank=True)
    r_abilities_measured_5_percentage = models.IntegerField(null=True, blank=True)
    r_abilities_measured_5_average = models.IntegerField(null=True, blank=True)

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if self.total_score != self.l_score + self.r_score:
            raise ValidationError({'total_score': 'Total score must be the sum of l_score and r_score.'})

    def save(self, *args, **kwargs):
        self.full_clean() # Run full validation
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.test_date}"