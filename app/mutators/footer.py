def footer(body):
  footer = open('data/footer.txt', 'r')
  body += '\n\n'
  for line in footer:
    body += line
  return body
