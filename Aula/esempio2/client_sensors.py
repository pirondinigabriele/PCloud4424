from requests import get, post
import time

base_url = 'https://mamei-test.appspot.com'

sensor = 's1'

for i in range(1000):
    print(sensor,'invio....')
    r = post(f'{base_url}/sensors/{sensor}',data={'val': i})
    time.sleep(1)

print('done')
