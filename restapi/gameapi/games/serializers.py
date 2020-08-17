from rest_framework import serializers
from .models import Game


# class GameSerializers(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length= 200)
#     release_date = serializers.DateTimeField()
#     game_category = serializers.CharField(max_length=200)
#     played = serializers.BooleanField(required=False)


#     def created(self,validate_date):
#         return Game.objects.created(**validate_date)

#     def updated(self,instance,validate_date):
#         instance.name = validate_date.get('name',instance.name)
#         instance.release_date = validate_date.get('release_date',instance.release_date)
#         instance.game_category = validate_date.get('game_category',instance.game_category)
#         instance.played = validate_date.get('played',instance.played)
#         instance.save
#         return instance


class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id','name','release_date','game_category','played')