import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


#Make an API call and store the response.

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status code:",r.status_code)

#Store API response in a variable
response_dict = r.json()

#Process results
#print(response_dict.keys())
print("Total repositories: ",response_dict['total_count'])

#Explore information about the repositories
repo_dicts = response_dict['items']
#print("Repositories returned: ", len(repo_dicts))

names, stars = [],[]

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
     
#Make Visualization
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45, show_legend = False)
chart.title = 'Most Starred Python Projects on Github'
chart.x_labels = names

chart.add('',stars)
chart.render_in_browser()

#Examine the first repository
#repo_dict = repo_dicts[0]
#print("\nKeys: ",len(repo_dict))
#for key in sorted(repo_dict.keys()):
#    print(key)

"""print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print("Name: "+repo_dict['name'])
    print("GIT URL: "+repo_dict['git_url'])
    print("HTML URL: "+repo_dict['html_url'])
    print("Owner Login: "+repo_dict['owner']['login'])
    print("Owner Node: "+repo_dict['owner']['node_id'])
    print("Description: "+str(repo_dict['description']))
    print("\n--------------------------\n")"""
    
