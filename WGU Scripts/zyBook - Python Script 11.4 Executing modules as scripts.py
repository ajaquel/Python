# web_search.py: Get the 1st page of results for a web search.
# Note that the program imports and uses the urllib module, which
# provides functions for fetching URLs. urllib is not supported in the online
# interpreter of this material and the example is for demo purposes only.

import urllib.request

def search(terms):
    """Do a fictional web engine search and return the results"""
    html = _send_request(terms)
    results = _get_results(html)
    return results

def _send_request(terms):
    """Send search to fictional web search engine and receive HTML response"""
    terms = terms.replace(' ', '%20')  #replace spaces

    url = 'http://www.search.fake.zybooks.com/search?q=' + terms
    info = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=info)

    response = urllib.request.urlopen(req)
    html = str(response.read())
    return html

def _get_results(html):
    """
    Finds the links returned in 1st page of results.
    """
    start_tag = '<cite>'  # start of results
    end_tag = '</cite>'   # Results end with this tag
    links = []            # list of result links

    start_tag_loc = html.find(start_tag)  # find 1st link

    while start_tag_loc > -1:
        link_start = start_tag_loc + len(start_tag)
        link_end = html.find(end_tag, link_start)
        links.append(html[link_start:link_end])
        start_tag_loc = html.find(start_tag, link_end)

    return links

search_term  = input('Enter search terms: ')
result = search(search_term)

print('Found {} links:'.format(len(result)))
for link in result:
    print(' ', link)







# domain_freq.py: Importing google_search causes unintended search to occur.
# Tracks frequency of domains in Google searches
import google_search  # Causes unintended search

domains = {}

terms = input("\nEnter search terms ('q' to quit): ")
while terms != 'q':
    results = google_search.search(terms)

    for link in results:
        if '.com' in link:
            domain_end = link.find('.com')
        elif '.net' in link:
            domain_end = link.find('.net')
        elif '.org' in link:
            domain_end = link.find('.org')
        else:
            print('Unknown top level domain')
            continue

        dom = link[:domain_end + 4]
        if dom not in domains:
            domains[dom] = 1
        else:
            domains[dom] += 1

    terms = input("Enter search terms ('q' to quit): ")

print('\nNumber of search results for each site:')
for domain, num in domains.items():
    print(domain + ':', num)





# Checking if a file is the executing script or an imported module.
if __name__ == "__main__":
    # File executed as a script






# google_search.py modified to run as either script or module.
#domain_freq.py

# Tracks frequency of domains in Google searches
import google_search

domains = {}

terms = input("Enter search terms ('q' to quit): ")
while terms != 'q':
    results = google_search.search(terms)

    # ...

print('\nNumber of search results for each site:')
for domain, num in domains.items():
    print(domain + ':', num  )



#google_search.py
import urllib.request

def search(terms):
    # ...

def _send_request(terms):
    # ...

def _get_results(html):
    # ...

if __name__ == "__main__":
    search_term  = input('Enter search terms:\n')
    result = search(search_term)

    print('Google returned %d links:' % len(result))
    for link in result:
        print(' ', link)






