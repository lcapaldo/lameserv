def header(body):
  header = open('data/header.txt', 'r')
  top = ""
  for line in header:
    top += line
  return top + '\n' + body
