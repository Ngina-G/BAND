from rest_framework import serializers
from sqlalchemy import null
from .models import User,Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image',)
        read_only_fields = ('username',)

    def get_image(self, obj):
        if obj.image:
            return obj.image

        return 'https://static.productionready.io/images/smiley-cyrus.jpg'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    bio = serializers.CharField(source='profile.bio', read_only=True)
    image = serializers.CharField(source='profile.image', read_only=True)
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','bio','image']
        extra_kwargs = {
            'password': {'write_only': True}
        }
def update(self, instance, validated_data):
    """Performs an update on a User."""

    password = validated_data.pop('password', None)


    profile_data = validated_data.pop('profile', {})

    for (key, value) in validated_data.items():
        # For the keys remaining in `validated_data`, we will set them on
        # the current `User` instance one at a time.
        setattr(instance, key, value)

    if password is not None:
        # `.set_password()` is the method mentioned above. It handles all
        # of the security stuff that we shouldn't be concerned with.
        instance.set_password(password)

    # Finally, after everything has been updated, we must explicitly save
    # the model. It's worth pointing out that `.set_password()` does not
    # save the model.
    instance.save()

    for (key, value) in profile_data.items():
        # We're doing the same thing as above, but this time we're making
        # changes to the Profile model.
        setattr(instance.profile, key, value)

    # Save the profile just like we saved the user.
    instance.profile.save()

    return instance

    
    
