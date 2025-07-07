import pandas as pd

data = {
    "name": [
        "Galaxy M14", "iPhone 13", "Redmi Note 12", "iPhone 13",
        "Realme Narzo", "Galaxy M14", "Redmi Note 12", "iPhone 15", "iPhone 15", "Galaxy M14"
    ],
    "brand": [
        "Samsung", "Apple", "Redmi", "Apple",
        "Realme", "Samsung", "Redmi", "Apple", "Apple", "Samsung"
    ],
    "price": [
        13500, 60999, 12999, 60999,
        10499, 13500, 12999, 70000, 70000, 13500
    ],
    "rating": [
        4.2, 4.8, 4.3, 4.8,
        4.1, 4.2, 4.3, 4.9, 4.9, 4.2
    ]
}

print("Printing dictionary once:")
print(data)
df = pd.DataFrame(data)
print(df)


# grouping here start
print("Printing AGD")

maximumMobilePrice = df.groupby("brand")["price"].max()
AvgMobilePrice = df.groupby("brand")["price"].mean()
BrandRating = df.groupby("brand")["rating"].mean()


print(BrandRating, AvgMobilePrice, BrandRating)





















