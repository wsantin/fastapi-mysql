import json
import requests

class ReniecService():
  BASE_URL = None
  RENIEC_API_KEY= None

  def __init__(self, serviceEnv):
    self.BASE_URL = serviceEnv.RENIEC_URL
    self.RENIEC_API_KEY = serviceEnv.RENIEC_API_KEY

  def get_dnidata(self, dni=None):
    if dni is None:
      raise  Exception('DNI null')

    url = '{}/{}'.format(self.BASE_URL, dni)
 
    headers = {
      'authorization': 'token {}'.format(self.RENIEC_API_KEY)
    }
    try:
      response = requests.request("GET", url, headers=headers)
     
      json_loads = json.loads(response.text)
      #{'dni': '', 'name': 'UPPER_CASE', 'first_name': '', 'last_name': '', 'cui': ''}
      return json_loads
    
    except Exception as e:
      print('Error al decodificar el json {}'.format(str(e)))
      return {"error":'Error al decodificar el json {}'.format(str(e))}