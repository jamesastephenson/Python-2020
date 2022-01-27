user_name = "Weathered Tom"
message = "Hello, " + user_name + "welcome to Python."
print(message)

user_name_lower = user_name.lower()
user_name_upper = user_name.upper()
user_name_title_case = user_name.title()

print(user_name_lower)
print(user_name_upper)
print(user_name_title_case)

quote = "Spike Spiegel is known to say \'Whatever happens, happens.\'"
print(quote)

famous_person = "Spike Spiegel"
famous_quote = quote[30:] + "\n-" + famous_person
print(famous_quote)

unstripped_name = "     Tim Hecker      "
lstripped_name = unstripped_name.lstrip()
rstripped_name = unstripped_name.rstrip()
stripped_name = unstripped_name.strip()

print(lstripped_name)
print(rstripped_name)
print(stripped_name)
