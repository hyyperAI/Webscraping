from bs4 import BeautifulSoup

"""  with open("website.html") as file:
    html_file=file.read()  """

file = open("website.html", encoding="utf8")
html_file = file.read()

# beautifulSoap( contents you want , parser: which file it is ,, html or xml)

soap = BeautifulSoup(html_file, "html.parser")
""" SYNTAX:  object.tag or object.tag.string,(p,em,href.......)  """
print(soap.title.string)
print(soap.prettify())
# -> give all code with indentation
print(soap.p)

'''name= tag'''

all_tag = soap.find_all(name="li")
'''-> list'''
print(all_tag)
print(all_tag[0])

single_tag = soap.find(name='ul')
print(single_tag)

all_paragraphs = soap.find_all("a")
print(all_paragraphs)
for item in all_paragraphs:
    print(item.getText())
    print(item.get("href"))

'''-----------         FIND METHOD           ----------------'''

call_through_class = soap.find(name='h3', class_="heading")
print(call_through_class)
print(call_through_class.get('class'))
print(call_through_class.name)
print(call_through_class.string)

call_secind_h3 = soap.find_all(name="h3")
print(call_secind_h3[1].string)

call_through_id = soap.find(name='h1', id="name")
print(call_through_id)

# --------------- SELECTOR -------------


company = soap.select_one(selector='p a')
"""->str"""
print(company)

CEO = soap.select_one(selector="#name")
print(CEO.string)

# LIST

headings = soap.select(selector='.heading')
print(headings)

company = (soap.select(selector='p em'))
"""->list"""
print(company)
