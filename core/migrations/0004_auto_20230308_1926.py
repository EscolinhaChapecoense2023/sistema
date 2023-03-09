# Generated by Django 3.2.15 on 2023-03-08 22:26

from django.db import migrations, models
import django_cpf_cnpj.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_financeiro_datamovimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=django_cpf_cnpj.fields.CPFField(max_length=14),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='posicao',
            field=models.CharField(choices=[('GO', 'Goleiro'), ('LD', 'Lateral Direito'), ('LE', 'Lateral Esquerdo'), ('ZC', 'Zagueiro'), ('VOL', 'Volante'), ('MLG', 'Meia de Ligação'), ('MLD', 'Meia de Ligação Direita'), ('MLE', 'Meia de Ligação Esquerda'), ('MAT', 'Meia Atacante'), ('PTE', 'Ponta Esquerda'), ('PTD', 'Ponta Direita'), ('CA', 'Centroavante')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='comoSoube',
            field=models.CharField(choices=[('I', 'Internet'), ('J', 'Jornal'), ('R', 'Rádio'), ('O', 'Outros')], max_length=15),
        ),
        migrations.AlterField(
            model_name='professor',
            name='cpf',
            field=django_cpf_cnpj.fields.CPFField(max_length=14),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='cpf',
            field=django_cpf_cnpj.fields.CPFField(max_length=14),
        ),
    ]