from rest_framework import serializers

from products.models import Products


class ProductSerializer(serializers.ModelSerializer):
    """Сериализаация модели продуктов"""
    image = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = '__all__'

    def get_image(self, img):
        img_url = img.image.url
        return {
            'path': img_url[:img_url.rindex('.')],
            'formats': [img_url[img_url.rfind('.')+1:], 'webp']
        }