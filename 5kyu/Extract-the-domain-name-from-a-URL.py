"""
Extract the domain name from a URL

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""


def domain_name(url):
    # The split() method splits a string into a list.
    # You can specify the separator, default separator is any whitespace.

    domain_name = url.split('//')[-1].split('/')[0].split('.')
    if domain_name[0] == 'www':
        return domain_name[1]
    else:
        return domain_name[0]


print(domain_name("http://www.zombie-bites.com"))


def domain_name_alternative(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

print(domain_name_alternative("http://www.zombie-bites.com"))