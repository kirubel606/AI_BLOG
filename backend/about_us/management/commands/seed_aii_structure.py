from django.core.management.base import BaseCommand
from about_us.models import Person, OrganizationUnit

class Command(BaseCommand):
    help = 'Seed the Ethiopian Artificial Intelligence Institute organizational structure'

    def handle(self, *args, **kwargs):
        # ----------------------
        # Create top-level leader
        # ----------------------
        worku = Person.objects.create(
            name="Dr. Worku Gachena",
            position="Director General",
            email="worku.gachena@aii.et",
            phone="+251-11-558-8786"
        )

        taye = Person.objects.create(
            name="Dr. Taye Girma",
            position="Deputy Director General",
            email="taye.girma@aii.et",
            phone="+251-11-558-8786"
        )
        yitagesu = Person.objects.create(
            name="Dr. Yitagesu Desalegn",
            position="Deputy Director General",
            email="yitagesu.desalegn@aii.et",
            phone="+251-11-558-8786"
        )
        amanu = Person.objects.create(
            name="Amanuel Kumsa",
            position="Deputy Director of Machine Learning and GeoAI",
            email="amanuel.kumsa@aii.et",
            phone="+251-11-558-8786"
        )

        # ----------------------
        # Create root organization
        # ----------------------
        root_unit = OrganizationUnit.objects.create(
            name="Ethiopian AI Institute",
            description="Top-level organization for AI research and development.",
            in_charge=worku,
            level=0
        )

        # ----------------------
        # Create child units
        # ----------------------
        research_unit = OrganizationUnit.objects.create(
            name='Research and Innovation',
            description='Focuses on AI research and innovation.',
            in_charge=amanu,
            parent=root_unit,
            level=1
        )
        tech_dev_unit = OrganizationUnit.objects.create(
            name='Technology Development',
            description='Responsible for AI technology development.',
            in_charge=taye,
            parent=root_unit,
            level=1
        )
        policy_unit = OrganizationUnit.objects.create(
            name='Policy and Strategy',
            description='Handles AI policy and strategic planning.',
            in_charge=yitagesu,
            parent=root_unit,
            level=1
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded Ethiopian AI Institute organizational structure.'))
