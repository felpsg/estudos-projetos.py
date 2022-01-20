import csv
compromised_users = []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

with open('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_users in compromised_users:
    compromised_user_file.write(compromised_users)

import json

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    "recipient": 'The Boss'
    "message": 'Mission Success'
  }

  json.dump(boss_message_dict, boss_message)

  with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = ""
new_passords_obj.write(slash_null_sig)
