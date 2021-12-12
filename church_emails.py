import sys
import os
import re

#
# https://lcr.churchofjesuschrist.org/messaging?lang=eng
# Because attempting to format an email via ^this is excessively painful:
# 1) Login and navigate to ^this URL
# 2) Add the recipients
# 3) Right click inspect within recipient area
# 4) Find the element with emails
# 5) Right click Copy > Copy Element
# 6) Paste into a new txt file
# 7) Run python3 church_emails.py <name-of-file-with-copied-element>.txt
# 8) Compose a well formated email in Gmail
# 9) To: 'Undisclosed recipients' <your-email@gmail.com>
# 10) Bcc: <copy list from script output>
#

def main():
  filepath = sys.argv[1]
  if not os.path.isfile(filepath):
    print("File path {} does not exist. Exiting...".format(filepath))
    sys.exit()

  with open(filepath) as fp:
      emails = re.findall(r'[\w\.-]+@[\w\.-]+', fp.read())
      if emails:
        recipients = ', '.join(emails)
        print(recipients)

if __name__ == '__main__':
  main()
