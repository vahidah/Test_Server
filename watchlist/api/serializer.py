from rest_framework import serializers

from watchlist.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    related_movie = serializers.SerializerMethodField()

    review_user = serializers.StringRelatedField()

    def get_related_movie(self, obj):

        return obj.watch.id

    class Meta:
        model = Review
        exclude = ('watch',)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    review = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"

    def get_len_name(self, object):
        return len(object.title)

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("name is too short")
    #     else:
    #         return value
    #
    # def validate(self, data):
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError("name and description can't be same")
    #     return data


class StreamPlatformSerializer(serializers.ModelSerializer):
    # watch_list = WatchListSerializer(many=True, read_only=True)
    watch_list = serializers.StringRelatedField(many=True, read_only=True)

    # watch_list = serializers.PrimaryKeyRelatedField(many=True)

    # watchlist = serializers.HyperlinkedIdentityField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie_detail'
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("name is too short")
#         else:
#             return value
#
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and description can't be same")
#         return  data
