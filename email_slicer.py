email = input("Enter your E-mail: ")
username, domain = email.split('@')
domain, extension = domain.split('.')

print(f"Username: {username}")
print(f"Domain: {domain}")
print(f"Extension: {extension}")