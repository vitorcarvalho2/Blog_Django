# Generated by Django 5.1 on 2025-01-15 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_equipe_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='icon',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=15, verbose_name='Icone'),
        ),
    ]