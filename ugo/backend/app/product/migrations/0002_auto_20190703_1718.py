# Generated by Django 2.2 on 2019-07-03 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttranslation',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productvarianttranslation',
            name='productvariant',
        ),
        migrations.DeleteModel(
            name='CategoryTranslation',
        ),
        migrations.DeleteModel(
            name='ProductTranslation',
        ),
        migrations.DeleteModel(
            name='ProductVariantTranslation',
        ),
    ]
