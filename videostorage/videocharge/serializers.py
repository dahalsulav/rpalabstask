
from rest_framework import serializers
from videocharge.models import VideoCharge


class VideoChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCharge
        fields = ('video_size_mb', 'video_length', 'video_type')

    def validate(self, data):
        charge = 0
        additional_charge = 0
        total_charge = 0

        # validate video size
        if(data['video_size_mb'] == None):
            raise serializers.ValidationError(
                "Video size cannot be left empty")
        elif(data['video_size_mb'] < 500):
            charge = 5
        elif(data['video_size_mb'] >= 500 and data['video_size_mb'] <= 1024):
            charge = 12.5
        else:
            raise serializers.ValidationError(
                'Video Size must be less or equal to 1GB(1024mb)')

        # validate video length
        if(data['video_length'] == None):
            raise serializers.ValidationError(
                "Video length cannot be left empty")
        elif(data['video_length']) <= 0:
            raise serializers.ValidationError(
                'Video Length cannot be zero or less')
        elif(data['video_length']) > 600:
            raise serializers.ValidationError(
                'Video Length cannot be greater than 10 minutes')
        elif (data['video_length']) <= 318:
            additional_charge = 12.5
        elif(data['video_length']) > 318:
            additional_charge = 20

        # validate video type
        if(data['video_type'] == None):
            raise serializers.ValidationError(
                "Video type cannot be left empty")
        elif(data['video_type'].lower() in ['.mp4', '.mkv', 'mkv', 'mp4']):
            pass
        else:
            raise serializers.ValidationError(
                "Video format must be in .mkv or .mp4")

        total_charge = charge + additional_charge
        print("total charge is " + str(total_charge))
        return data
