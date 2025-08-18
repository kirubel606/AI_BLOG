from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import AboutUs, Person, OrganizationUnit
from .serializers import AboutUsSerializer, PersonSerializer, OrganizationUnitSerializer


# ---------------------------
# About Us Views
# ---------------------------
class AboutUsListCreateView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AboutUsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        # Force partial update even on PUT
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


# ---------------------------
# People Views (Generics)
# ---------------------------
class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


# ---------------------------
# Organization Unit Views (Generics)
# ---------------------------
class OrganizationUnitListCreateView(generics.ListCreateAPIView):
    queryset = OrganizationUnit.objects.all()
    serializer_class = OrganizationUnitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Optionally filter to only top-level units if ?root=true is passed.
        """
        queryset = super().get_queryset()
        root = self.request.query_params.get("root")
        if root:
            queryset = queryset.filter(parent__isnull=True)
        return queryset


class OrganizationUnitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrganizationUnit.objects.all()
    serializer_class = OrganizationUnitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
