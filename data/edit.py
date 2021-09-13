f = open('data/__help__', 'r')
d = f.read()
f.close()

_d = d.replace("```", "```yml").replace("```yml\n***", "```\n***")

f = open('data/__help__', 'w')
f.write(_d)
f.close()
