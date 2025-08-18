from django.db import models

# Create your models here.
class AboutUs(models.Model):
    image = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=255,null=True,blank=True)
    title_am = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True,blank=True)
    description_am = models.TextField(blank=True, null=True)


class Person(models.Model):
    """
    Represents a person who can be in charge of an organizational unit.
    """
    name = models.CharField(max_length=255)
    name_am = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)  # e.g., Manager, Director
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to="people/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.position})" if self.position else self.name


class OrganizationUnit(models.Model):
    """
    Represents a unit in an organizational structure (e.g., Company, Division, Department, Team).
    """
    name = models.CharField(max_length=255)
    name_am = models.CharField(max_length=255, blank=True, null=True)

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )

    description = models.TextField(blank=True, null=True)
    description_am = models.TextField(blank=True, null=True)

    # Who is in charge of this unit
    in_charge = models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="units_in_charge"
    )

    level = models.PositiveIntegerField(default=0, help_text="Hierarchy level (0=Top level, 1=Department, etc.)")
    order = models.PositiveIntegerField(default=0, help_text="Order for display sorting")

    class Meta:
        verbose_name = "Organization Unit"
        verbose_name_plural = "Organization Units"
        ordering = ["level", "order", "name"]

    def __str__(self):
        return self.name

    def get_full_path(self):
        """
        Returns the full path of the unit in the hierarchy, e.g.:
        'Company > Division > Department > Team'
        """
        parts = [self.name]
        parent = self.parent
        while parent is not None:
            parts.insert(0, parent.name)
            parent = parent.parent
        return " > ".join(parts)