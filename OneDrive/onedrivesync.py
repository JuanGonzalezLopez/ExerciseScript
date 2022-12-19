import os
import requests
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT
APP_ID = '4390b30a-6c6f-42ce-93b1-eb235e6e5650'
SCOPES = ['Files.ReadWrite']

# access_token = generate_access_token(APP_ID,SCOPES)
# header = {
#     'Authorization' : 'Bearer' + access_token['access_token']
# }

hardcoded_access_token = 'EwBwA8l6BAAUkj1NuJYtTVha+Mogk+HEiPbQo04AAdFS6lSNrAs/UKYRr2emd/UJmNOKQjpM9KuMUNJwrIGDwxC1mX4mlOR+NczIVjVucUdJrY38Z0LfacCDVeaNsYEu4L5MREI1+HvoMLsw9n8EIrdZp4i4FMOsLpcmX11tXFrlDO8nJ2WnOj8XtYgI6gAyPMwqyjzIEBSwHNC+HDyeTF44zrwHDdfn0wYyZokmc/UVTB15SuiRjUYTCpQFcCSUiHrMlglXK8c8gGJOP+/gGlNO6HzkiOFcK/U4PbMTXJOvRupuOMDxcdeV9wdl6j4TtSTNFG6wAMYaSRfVfpQPuXYtD7Yvq2i559FqXNLxWSCAYcw7GIHgN+5t/z1voUkDZgAACKe0LTJrT+X4QAKqE9Weq5ExoVpStfw2z8xLtPEGgPmIc26J3qh+I7S/rL6P4BA7y+OIRW6hcCfqkNbXf0ULB4ifi5Qkw8nK8dnKuyN5ZPTCuK9/sQnGjRL4YD+l/LGQrrP0ZdBS6t75pepM+2gf987gd5nOQpRItltVO+vSj9oG64Rt6IPcgST1Prave6o9lnwHlYsoeBwmCeX6vvgk1n8eadYDrZxdUF7Pd+98YyCAboDmtQ4SHa3VIKbDGBSgfeQ3C2+t5Nz4UkJNMn/JmxZE2jdearroQZ+LOGXEFGZc1RZEyjBDIkkgLP28JHccrKYc7be5291LWHcFjkn6t3NAyqPEToNzkPB1ZMqptv6/fXKngllqN6jOgZJsl+FV2Jm/fKed80CHXaE3oWR+1pnsi+fjFpU7a9ZW/DRZwoAdU9b8EYp86gwek9dZc1nh6dxVdBHODr/uMgBUiiN5jcyHJsQkUTLYUB48TDSh6dbTBHs0riA9sulpeoYGork2tBJl1QDLo/Iymf5TH9bR1loTM8A+QGYvLTJHKjgfpK9cG05iW/ME3Mqe2K326ctGV0+YRvBE/Vl0u/4a90pDN6+4os2tLkEbT1b8UTyQEGDgOd5RZLJq6ylG61DK7MAPqQOaZy6um9E6tvni3qC3vrahu4xxbOGqi9At20mVglMQia7yra43gMJYx8Mt2BCsKYIzzncuCWRhqaHWImwewvIThFZj5+ycxnDc0kd/SmJO7dVHKEt9yCwfXq74iebhvwrwD3xFiMC75uiGAg=='
header = {
    'Authorization' : 'Bearer' + hardcoded_access_token
}
filepath = r'../Planners/Excel/Planner - Push.xlsx'
filename = os.path.basename(filepath)



with open(filepath, 'rb') as upload:
    media_content = upload.read()



# upload file to home dir

response = requests.put(GRAPH_API_ENDPOINT + f'/me/drive/items/root:/{filename}:/content',
             headers=header,
             data=media_content)

print(response.json())