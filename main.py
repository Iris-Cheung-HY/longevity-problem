def longest_career(albums):
  # Write your solution here!
  alb_dict = {}
  max_year_count = 0
  max_artist = ""

  # for row in albums:
  #   if row[0] not in alb_dict:
  #     alb_dict[row[0]] = [row[2]]
  #   else:
  #     alb_dict[row[0]] += [row[2]]
    
  for row in albums:
    art = row[0]
    year = row[2]
    if art not in alb_dict:
      alb_dict[art] = [year, year]
    else:
      item = alb_dict[art]
      alb_dict[art] = [min(item[0], year), max(item[1], year)]
  
  for key, values in alb_dict.items():
    diff = values[1] - values[0]

    if diff > max_year_count:
      max_year_count = diff
      max_artist = key

  return max_artist, max_year_count




      


# Test cases
albums_1 = [
    ("Rodrigo y Gabriela", "9 Dead Alive", 2014),
    ("Shakira", "El Dorado", 2017),
    ("Janelle Monáe", "The ArchAndroid", 2010),
    ("Shakira", "Magia", 1991),
    ("Shakira", "She Wolf", 2009),
    ("Rodrigo y Gabriela", "11:11", 2009),
    ("Rodrigo y Gabriela", "Rodrigo y Gabriela", 2006),
    ("Rodrigo y Gabriela", "Mettavolution", 2019),
    ("Janelle Monáe", "Dirty Computer", 2018)
]
assert longest_career(albums_1) == ("Shakira", 26)


albums_2 = [
    ("Skylar Kergil", "Tell Me a Story", 2015),
    ("Lil Nas X", "Old Town Road", 2018),
    ("Skylar Kergil", "Thank You", 2013),
    ("Lil Nas X", "Montero", 2021),
]
assert longest_career(albums_2) == ("Lil Nas X", 3)

print("All test cases passed!")
print("Finished early? Discuss time & space complexity")
