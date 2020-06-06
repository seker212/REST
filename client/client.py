import requests
from getcommand import *

serviceAddress='http://192.168.0.45:5000'

def sendPOST(username, series_title, series_type, series_episodes, my_watched_episodes, my_score, my_status, my_times_watched):
    payload = 'series_title={}&series_type={}&series_episodes={}&my_watched_episodes={}&my_score={}&my_status={}&my_times_watched={}'.format(series_title, series_type, series_episodes, my_watched_episodes, my_score, my_status, my_times_watched)
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    url = '{}/list/{}'.format(serviceAddress, username)

    return requests.request("POST", url, headers=headers, data = payload)

def sendDELETE(username, series_title):
    url = '{}/list/{}/{}'.format(serviceAddress, username, series_title)

    return requests.request("DELETE", url , headers={}, data = {})

def sendPUT(username, series_title, parameter_name, new_parameter):
    payload = 'parameter_name={}&new_parameter={}'.format(parameter_name, new_parameter)
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    url = '{}/list/{}/{}'.format(serviceAddress, username, series_title)

    return requests.request("PUT", url, headers=headers, data = payload)

def sendGET(username = None, series_title = None, param = None):
    url = serviceAddress
    if username != None:
        url += '/list/{}'.format(username)
        if series_title != None:
            url += '/{}'.format(series_title)
            if param != None:
                url += '/{}'.format(param)

    return requests.request("GET", url)

#---------------------------------------------------------------------------------------------
print('-------------------------------------------------')
print('Server Client\nVersion: v0.1\nServer address: {}'.format(serviceAddress))
print('-------------------------------------------------')
print('Type help for command list', end='\n\n')

run = True
while run:
    print('>', end=' ')
    cmd = getCmd()
    resp = None
    try:
        if cmd[0].lower() == 'get':
            if len(cmd) == 1:
                resp = sendGET()
            elif len(cmd) == 2:
                resp = sendGET(cmd[1])
            elif len(cmd) == 3:
                resp = sendGET(cmd[1], cmd[2])
            elif len(cmd) == 4:
                resp = sendGET(cmd[1], cmd[2], cmd[3])
            else:
                raise IndexError
            
        elif cmd[0].lower() == 'post':
            data = []
            args = ['series_title', 'series_type', 'series_episodes', 'my_watched_episodes', 'my_score', 'my_status', 'my_times_watched']
            for i in args:
                w = i.replace('_',' ').title()
                print(w + ': ', end='\t')
                x = input()
                data.append(x)

            resp = sendPOST(cmd[1], data[0], data[1], data[2], data[3], data[4], data[5], data[6])

        elif cmd[0].lower() == 'put':
            resp = sendPUT(cmd[1], cmd[2], cmd[3], cmd[4])
        elif cmd[0].lower() == 'del':
            resp = sendDELETE(cmd[1], cmd[2])
        elif cmd[0].lower() == 'help':
            print(
                'get <username> <series_title> <parameter_name>\n'
                + 'post <username>\n'
                + 'put <username> <series_title> <parameter_name> <new_parameter>\n'
                + 'del <username> <series_title>\n'
                + 'quit\n'
            )
        elif cmd[0].lower() == 'quit' or cmd[0].lower() == 'exit':
            run = False
            break
        else:
            print('Invalid command. Try again')

        if resp != None:
            print(resp, end='\n\n')
            if resp.text.startswith('<!DOCTYPE html>'):
                result = re.findall( r'>([a-zA-Z0-9].*[a-zA-Z0-9:])<', resp.text)
                result.pop(0)
                a = ''
                for word in result:
                    a += word + '\n'
                    a = a.replace('&#34;','\"').replace('&#39;','\'').replace('&amp;', '&')
                print (a, end='\n\n')
            else:
                print (resp.text, end='\n\n')
        
    except IndexError:
        print('Invalid command. Try again')

    
