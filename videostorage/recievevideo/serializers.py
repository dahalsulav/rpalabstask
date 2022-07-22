from rest_framework import serializers
from recievevideo.models import RecieveVideo
from moviepy.editor import VideoFileClip


class RecieveVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecieveVideo
        fields = ('video_name', 'video')

    def validate(self, data):
        if(data['video_name'] == None):
            raise serializers.ValidationError(
                'Video Name cannot be left empty')

        gb_into_byte = 1*1024*1024*1024
        if data['video'].size > gb_into_byte:
            raise serializers.ValidationError(
                'Video size must not exceed 1GB storage')

        video_ext = data['video'].name
        if video_ext.split('.')[-1] not in ['mkv', 'mp4']:
            raise serializers.ValidationError(
                'Video Format must be in mp4 or mkv format')

        # print(dir(data['video']))
        video_file = VideoFileClip(data['video'].temporary_file_path())
        # print(video_file.duration)
        if (video_file.duration) > 600:
            raise serializers.ValidationError(
                'Video Length cannot exceed 10 minutes')
        return data
