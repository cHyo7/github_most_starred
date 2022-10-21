import requests

from operator import itemgetter

# Make an API call and store the repsonse.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Porcess information about eache submision.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submision_dict = {
        'title': response_dict['title'], 
        'link': 'https://news.ycombinator.com/item?id' + str(submission_id), 
        'comments': response_dict.get('descendats', 0)
    }
    submission_dicts.append(submision_dict)

submision_dicts = sorted(submission_dicts, key=itemgetter('comments'),
 reverse=True)

for submission_dict in submision_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])