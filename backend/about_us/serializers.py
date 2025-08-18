from rest_framework import serializers
from .models import AboutUs,Person,OrganizationUnit

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class OrganizationUnitSerializer(serializers.ModelSerializer):
    # Nested serializer for the person in charge
    in_charge = PersonSerializer(read_only=True)
    in_charge_id = serializers.PrimaryKeyRelatedField(
        queryset=Person.objects.all(),
        source="in_charge",
        write_only=True,
        required=False,
        allow_null=True
    )

    # Recursive/nested children
    children = serializers.SerializerMethodField()

    class Meta:
        model = OrganizationUnit
        fields = [
            "id",
            "name",
            "name_am",
            "parent",
            "description",
            "description_am",
            "in_charge",
            "in_charge_id",
            "level",
            "order",
            "children",
        ]

    def get_children(self, obj):
        """Recursively return children units"""
        return OrganizationUnitSerializer(obj.children.all(), many=True).data