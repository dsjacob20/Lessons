

holiday_options = {
    'Mexico': 5000,
    'Las Vegas': 3000,
    'Vancouver': 2000,
    'Leduc': 175,
    'needs': ("Suitcase", "Sunglasses", "Money",)
}


x = (holiday_options.get("Mexico"))
print ('\t',"{:<15}:{:>10}".format("Mexico", x))