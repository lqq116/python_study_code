# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request

class DefaultSaxHandler(object):
    forecast = []
    def start_element(self, name, attrs):
        if attrs['city']:
            self.city=attrs['city']
            for 'yweather:forecast' in name:
                self.forecast.append({'date': attrs['date'], 'high': attrs['high'], 'low' :attrs['low']})
        else:
            print('there is something wrong!')
            

def parseXml(xml_str):

    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml_str)
    
    
    print(xml_str)
    return {
        'city': '?',
        'forecast': [
            {
                'date': '2017-11-17',
                'high': 43,
                'low' : 26
            },
            {
                'date': '2017-11-18',
                'high': 41,
                'low' : 20
            },
            {
                'date': '2017-11-19',
                'high': 43,
                'low' : 19
            }
        ]
    }




        




