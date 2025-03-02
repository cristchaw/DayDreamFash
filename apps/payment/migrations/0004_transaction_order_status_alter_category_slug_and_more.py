# Generated by Django 5.1.5 on 2025-01-27 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_product_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='order_status',
            field=models.CharField(choices=[('pending payment', 'Pending Payment'), ('On Process', 'On Process'), ('Completed', 'Completed')], default='pending payment', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
