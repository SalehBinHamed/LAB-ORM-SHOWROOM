# import random
# from django.core.management.base import BaseCommand
# from cars.models import Cars, Color

# class Command(BaseCommand):
#     help = "Generates cars and colors dynamically for testing"

#     def add_arguments(self, parser):
#         parser.add_argument('--num-cars', type=int, default=20, help="Number of cars to generate")

#     def handle(self, *args, **options):
#         num_cars = options['num-cars']
#         self.stdout.write(f"Generating {num_cars} cars...")


#         years = list(range(1952, 2025))