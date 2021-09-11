text = input()

print(f"""The given string: {text}
The USA/usa count is: {text.count('USA') + text.count('usa')}
The new string: {text.replace('USA', 'Armenia').replace('usa', 'Armenia')}""")
