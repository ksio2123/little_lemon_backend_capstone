from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer

class MenuItemTest(TestCase):
    def test_get_item(self):
        menu_item = {
            'title': 'IceCream',
            'price': 80,
            'inventory': 100
        }
        item = MenuItem.objects.create(title=menu_item['title'], price=menu_item['price'], inventory=menu_item['inventory'])
        test_menu_item = {
            **menu_item,
            **{
                'price': '80.00',
                'id': 1
            }
        }
        self.assertEqual(MenuSerializer(item).data, test_menu_item)