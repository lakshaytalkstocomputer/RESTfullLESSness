from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     # This is particularly useful for controlling how the browsable API should be displayed
#     code = serializers.CharField(style={"base_template": 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         Create and return a new Snippet instance, given the validated data
#         :param validated_data:
#         :return :
#         """
#         #  WHAT IS VALIDATED DATA ?
#         #  == Validated Data is OrderedDict() that contains all the data of instance of model .
#         #  ==  -- OrderedDict([('title', ''), ('code', 'print("hello, world")'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
#         #  ==  -- It can be accessed after chekcing whhether the data is valid by .is_valid()
#
#         # WHAT DOES create() RETURN
#         # == Snippet Object after creating it.
#         return Snippet.objects.create(**validated_data)
#
#
#     def update(self, instance, validated_data):
#         """
#
#         :param isntance:
#         :param validated_data:
#         :return:
#         """
#
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

## AlL of that can be written as :

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code','linenos', 'language', 'style']


