from search.models import brand
import csv


def run():
    with open('search/ESG_sustainability_scores.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        brand.objects.all().delete()

        for row in reader:
            print(row)

            new = brand(name=row[0],
                        emissions=row[6],)
            new.save()