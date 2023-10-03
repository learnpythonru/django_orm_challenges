from django.db import models

import json


class Book(models.Model):
    title = models.CharField(max_length=256)
    author_full_name = models.CharField(max_length=256)
    isbn = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Laptop(models.Model):
    class Meta:
        db_table = 'Laptop_info'
        get_latest_by = 'created_at'
        ordering = ['-created_at']

    brand = models.CharField(max_length=120)
    year_of_issue = models.DateField()
    amount_of_ram = models.PositiveSmallIntegerField()
    hd_capacity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    quantity_in_stock = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def to_json(self):
        data = {
            'brand': self.brand,
            'year_of_issue': self.year_of_issue.strftime('%Y'),
            'amount_of_ram': self.amount_of_ram,
            'hd_capacity': self.hd_capacity,
            'price': self.price,
            'quantity_in_stock': self.quantity_in_stock,
            'created_at':self.created_at.strftime('%d-%m-%Y %H:%M:%S')
        }

        return json.dumps(data)