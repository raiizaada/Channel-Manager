from rest_framework_json_api import serializers
from rentals.models import Bookings, Rental

class RentalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rental
        fields = ('id', 'rental_name')

class BookingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookings
        fields = ('rental','check_in','check_out','user_id')