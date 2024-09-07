# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    physical_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_groups',  # Add a unique related name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions',  # Add a unique related name
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'physical_address', 'phone_number']

    username = None







    # accounts/models.py

from django.db import models

class Animal(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ] 


    SPECIES_CHOICES = [
    ('Cow', 'Cow'),
    ('Goat', 'Goat'),
    ('Sheep', 'Sheep'),
    ('Horse', 'Horse'),
    ('Donkey', 'Donkey'),
    ('Pig', 'Pig'),
    ('Chicken', 'Chicken'),
    ('Duck', 'Duck'),
    ('Turkey', 'Turkey'),
    ('Goose', 'Goose'),
    ('Dog', 'Dog'),
    ('Cat', 'Cat'),
    ('Rabbit', 'Rabbit'),
    ('Pigeon', 'Pigeon'),
    ('Guinea Pig', 'Guinea Pig'),
    ('Hamster', 'Hamster'),
    ('Parrot', 'Parrot'),
    ('Goldfish', 'Goldfish'),
    ('Budgerigar (Budgie)', 'Budgerigar (Budgie)'),
    ('Cockatiel', 'Cockatiel'),
    ('Ferret', 'Ferret'),
    ('Chinchilla', 'Chinchilla'),
    ('Dairy Goat', 'Dairy Goat'),
    ('Alpaca', 'Alpaca'),
    ('Llama', 'Llama'),
    ('Camel', 'Camel'),
    ('Yak', 'Yak'),
    ('Buffalo', 'Buffalo'),
    ('Ox', 'Ox'),
    ('Mule', 'Mule'),
    ('Quail', 'Quail'),
    ('Pheasant', 'Pheasant'),
    ('Swan', 'Swan'),
    ('Emu', 'Emu'),
    ('Guinea Fowl', 'Guinea Fowl'),
    ('Reindeer', 'Reindeer'),
    ('Ostrich', 'Ostrich'),
    ('Zebra (Domesticated)', 'Zebra (Domesticated)'),
    ('Miniature Donkey', 'Miniature Donkey'),
    ('Angora Goat', 'Angora Goat'),
    ('Silkie Chicken', 'Silkie Chicken'),
    ('Koi Fish', 'Koi Fish'),
    ('Dwarf Goat', 'Dwarf Goat'),
    ('Miniature Horse', 'Miniature Horse'),
    ('Jersey Cow', 'Jersey Cow'),
    ('Ayrshire Cow', 'Ayrshire Cow'),
    ('Rhode Island Red Chicken', 'Rhode Island Red Chicken'),
    ('Leghorn Chicken', 'Leghorn Chicken'),
    ('Pekin Duck', 'Pekin Duck'),
    ('Muscovy Duck', 'Muscovy Duck'),
]


    PRODUCTION_PURPOSE_CHOICES = [
    ('Milk Production', 'Milk Production'),
    ('Meat Production', 'Meat Production'),
    ('Egg Production', 'Egg Production'),
    ('Wool Production', 'Wool Production'),
    ('Fiber Production', 'Fiber Production'),
    ('Leather Production', 'Leather Production'),
    ('Fur Production', 'Fur Production'),
    ('Breeding', 'Breeding'),
    ('Beekeeping (Honey Production)', 'Beekeeping (Honey Production)'),
    ('Silk Production', 'Silk Production'),
    ('Work Animal', 'Work Animal'),
    ('Draft Animal', 'Draft Animal'),
    ('Companion Animal', 'Companion Animal'),
    ('Guard Animal', 'Guard Animal'),
    ('Herding', 'Herding'),
    ('Racing', 'Racing'),
    ('Show Animal', 'Show Animal'),
    ('Pest Control', 'Pest Control'),
    ('Therapy Animal', 'Therapy Animal'),
    ('Petting Zoo', 'Petting Zoo'),
    ('Conservation Grazing', 'Conservation Grazing'),
    ('Hunting', 'Hunting'),
    ('Truffle Hunting', 'Truffle Hunting'),
    ('Research', 'Research'),
    ('Service Animal', 'Service Animal'),
    ('Rescue Animal', 'Rescue Animal'),
    ('Sled Pulling', 'Sled Pulling'),
    ('Pack Animal', 'Pack Animal'),
    ('Sniffer Animal', 'Sniffer Animal'),
    ('Tracking', 'Tracking'),
    ('Dairy Production', 'Dairy Production'),
    ('Organic Farming', 'Organic Farming'),
    ('Animal Tourism', 'Animal Tourism'),
    ('Eco-tourism', 'Eco-tourism'),
    ('Riding Animal', 'Riding Animal'),
    ('Meat and Dairy Production', 'Meat and Dairy Production'),
    ('Leather and Meat Production', 'Leather and Meat Production'),
    ('Milk and Meat Production', 'Milk and Meat Production'),
    ('Manure Production', 'Manure Production'),
    ('Biofuel Production', 'Biofuel Production'),
    ('Poultry Production', 'Poultry Production'),
    ('Aquaculture', 'Aquaculture'),
    ('Pig Farming', 'Pig Farming'),
    ('Goat Farming', 'Goat Farming'),
    ('Sheep Farming', 'Sheep Farming'),
    ('Cattle Farming', 'Cattle Farming'),
    ('Horse Breeding', 'Horse Breeding'),
    ('Camel Dairy', 'Camel Dairy'),
    ('Buffalo Dairy', 'Buffalo Dairy'),
    ('Llama Wool Production', 'Llama Wool Production'),
    ('Alpaca Fiber Production', 'Alpaca Fiber Production'),
    ('Ostrich Farming', 'Ostrich Farming'),
    ('Reindeer Herding', 'Reindeer Herding'),
    ('Venison Production', 'Venison Production'),
    ('Exotic Meat Production', 'Exotic Meat Production'),
    ('Organic Wool Production', 'Organic Wool Production'),
    ('Sustainable Farming', 'Sustainable Farming'),
    ('Game Animal Farming', 'Game Animal Farming'),
    ('Feedlot Farming', 'Feedlot Farming'),
    ('Intensive Livestock Production', 'Intensive Livestock Production'),
    ('Free-Range Farming', 'Free-Range Farming'),
    ('Pasture-Based Farming', 'Pasture-Based Farming'),
    ('Aquaponics', 'Aquaponics'),
    ('Fertilizer Production', 'Fertilizer Production'),
    ('Bait Farming', 'Bait Farming'),
    ('Exotic Leather Production', 'Exotic Leather Production'),
    ('Perfume Production', 'Perfume Production'),
    ('Research and Experimentation', 'Research and Experimentation'),
    ('Zoological Breeding', 'Zoological Breeding'),
    ('Guide Animal', 'Guide Animal'),
    ('Assistance Animal', 'Assistance Animal'),
    ('Police Animal', 'Police Animal'),
    ('Military Animal', 'Military Animal'),
    ('Animal Traction', 'Animal Traction'),
    ('Therapeutic Riding', 'Therapeutic Riding'),
    ('Animal Training', 'Animal Training'),
    ('Educational Programs', 'Educational Programs'),
    ('Birdsong Production', 'Birdsong Production'),
    ('Insect Farming', 'Insect Farming'),
    ('Pigeon Racing', 'Pigeon Racing'),
    ('Falconry', 'Falconry'),
    ('Rodent Control', 'Rodent Control'),
    ('Reptile Breeding', 'Reptile Breeding'),
    ('Exotic Pet Breeding', 'Exotic Pet Breeding'),
    ('Cloning Research', 'Cloning Research'),
    ('Artificial Insemination', 'Artificial Insemination'),
    ('Cryogenic Storage', 'Cryogenic Storage'),
    ('Animal Transport', 'Animal Transport'),
    ('Circus Animal', 'Circus Animal'),
    ('Film and TV Animal', 'Film and TV Animal'),
    ('Show Jumping', 'Show Jumping'),
    ('Eventing', 'Eventing'),
    ('Dressage', 'Dressage'),
    ('Polo', 'Polo'),
    ('Animal Feed Production', 'Animal Feed Production'),
    ('Soil Fertility Improvement', 'Soil Fertility Improvement'),
    ('Waste Disposal', 'Waste Disposal'),
    ('Environmental Sustainability', 'Environmental Sustainability'),
    ('Pollination', 'Pollination'),
    ('Guarding Livestock', 'Guarding Livestock'),
]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animals')
    id = models.AutoField(primary_key=True)
    species = models.CharField(max_length=100, choices=SPECIES_CHOICES)
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=MALE,
    )
    date_of_birth = models.DateField()
    breed = models.CharField(max_length=100)
    production_purpose = models.CharField(max_length=100, choices=PRODUCTION_PURPOSE_CHOICES)
    about_animal = models.TextField()

    def __str__(self):
        return f"{self.breed} ({self.species})"
