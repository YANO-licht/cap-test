# Generated by Django 5.1 on 2024-10-07 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_remove_book_copies_available_book_available_copies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='available_copies',
            new_name='copies_available',
        ),
    ]
