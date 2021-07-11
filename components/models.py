from django.db import models
from polymorphic.models import PolymorphicModel


CPU = [
    ("Intel", (
        ("Core i9", "Core i9"),
        ("Core i7", "Core i7"),
        ("Core i5", "Core i5"),
        ("Core i3", "Core i3"),
        ("Celeron & Pentium", "Celeron & Pentium"))
    ),
    ("AMD", (
        ("Threadripper", "Threadripper"),
        ("Ryzen 9", "Ryzen 9"),
        ("Ryzen 7", "Ryzen 7"),
        ("Ryzen 5", "Ryzen 5"),
        ("Ryzen 3", "Ryzen 3"))
    )
]
BRAND = [
    ("Intel","Intel"),
    ("AMD", "AMD")
]

PROSESSOR_TYPE = [
    ("Desktop", "Desktop"),
    ("Laptop", "Laptop")
]

MEMORY_TYPE = [
    ("DDR4", "DDR4"),
    ("DDR3", "DDR3"),
    ("DDR2", "DDR2")
]

MOTHERBOARDS = [
    ("Intel", "Intel"),
    ("AMD", "AMD")
]

MEMORY = [
    ("Desktop Memory", "Desktop Memory"),
    ("Laptop Memory", "Laptop Memory"),
    ("Mac Memory", "Mac Memory")
]
MEMORY_SPEED = [
    ("DDR4 5100", "DDR4 5100"),
    ("DDR4 5000", "DDR4 5000"),
    ("DDR4 4800", "DDR4 4800"),
    ("DDR4 4600", "DDR4 4600"),
    ("DDR4 4500", "DDR4 4500"),
    ("DDR4 4400", "DDR4 4400")
]

STORAGE_CATEGORY =[
    ("Internal", 
        (("Desktop Hard Drives", "Desktop Hard Drives"),
         ("Laptop Hard Drives", "Laptop Hard Drives"))
    ),
    ("External",
        (("Desktop Hard Drives", "Desktop Hard Drives"),
         ("Laptop Hard Drives", "Laptop Hard Drives"))
    ),
    ("Portable External Hard Drives", "Portable External Hard Drives"),
    ("Mac Hard Drives", "Mac Hard Drives")
                    
]

HARD_DRIVE_MANUFACTURER= [
    ("Seagate", "Seagate"),
    ("Toshiba", "Toshiba"),
    ("Dell", "Dell"),
    ("GoHardDrive", "GoHardDrive"),
    ("Hitachi", "Hitachi")
]

SSD_CATEGORY = [
    ("Internal SSD", "Internal SSD"),
    ("External SSD", "External SSD")
]

class Component(PolymorphicModel):
    pass

class Processor(Component):
    type = models.CharField(max_length=200, choices=CPU, default="Intel")
    brand = models.CharField(max_length=200, choices=BRAND, default="Intel")
    processor_type = models.CharField(max_length=200, choices=PROSESSOR_TYPE, default="Desktop")
    series = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, default="Core i9-10900K")
    model = models.CharField(max_length=200, default="BX8070110900K")
    cores = models.IntegerField(blank=True)
    threads = models.IntegerField(blank=True)
    memory_types = models.CharField(max_length=200, choices=MEMORY_TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return '%s %s %s %s' %(self.brand, self.series, self.model, self.name)
    
class Motherboard(Component):
    type = models.CharField(max_length=200, choices=MOTHERBOARDS, default="AMD")
    cpu_socket_type = models.CharField(max_length=200, blank=True)
    cpu_type = models.CharField(max_length=200, blank=True)
    brand = models.CharField(max_length=200, default="GIGABIT")
    model = models.CharField(max_length=200, default="Z590I AORUS ULTRA")
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return '%s %s %s '% (self.brand, self.model, self.type)


class Memory(Component):
    system = models.CharField(max_length=200, choices=MEMORY, default="Laptop")
    type = models.CharField(max_length=200, choices=MEMORY_TYPE, default="DDR4")
    speed = models.CharField(max_length=200, choices=MEMORY_SPEED, default="DDR4 5100")
    capacity = models.CharField(max_length=200, default="16GB")
    brand = models.CharField(max_length=200, default="CORSAIR")
    series = models.CharField(max_length=200,  default="Vengeance RGB Pro SL")
    model = models.CharField(max_length=200, default="CMH16GX4M2D3600C18")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s %s %s '%(self.brand, self.series, self.model)



class Hard_Drive(Component):
    category = models.CharField(max_length=200, choices=STORAGE_CATEGORY, default="Portable EXternal Hard Drives")
    brand = models.CharField(max_length=200, default="WD")
    series = models.CharField(max_length=200, default="Red Pro")
    model = models.CharField(max_length=200, default="WD4003FFBX")
    capacity = models.CharField(max_length=200, default="4TB")
    manufacturer = models.CharField(max_length=200, choices=HARD_DRIVE_MANUFACTURER, default="Seagate")
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
         return '%s %s %s '%(self.brand, self.series, self.model)



class SSD(Component):
    category = models.CharField(max_length=200, choices=SSD_CATEGORY, default="Internal SSD")
    brand = models.CharField(max_length=200, default="SAMSUNG")
    series = models.CharField(max_length=200, default="860 EVO Series")
    model = models.CharField(max_length=200, default="MZ-76E500B/AM")
    capacity = models.CharField(max_length=200, default="500GB")

    def __str__(self):
         return '%s %s %s '%(self.brand, self.series, self.model)











