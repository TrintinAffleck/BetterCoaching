from rest_framework import serializers
from coaches.models import Coach, Review
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CoachSerializer(serializers.ModelSerializer):
    user_type = ProfileSerializer(many=False)
    reviews = serializers.SerializerMethodField() 
    class Meta:
        model = Coach
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
