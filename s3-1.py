#s3-1:

#リスト２

# -*- coding: utf-8 -*-

import urllib.request
import json
#url = 'http://weather.livedoor.com/forecast/webservice/json/vl?city=130010'
#url = 'http://weather.livedoor.com/area/forecast/130010'
url = 'http://weather.livedoor.com/plugin/common/forecast/12.js'
req = urllib.request.urlopen(url)
data = json.loads(req.read().decode('ascii'))
print([(item['date'],item['telop']) for item in data['forecasts']])

#<script language="javascript" charset="euc-jp" type="text/javascript" src="http://weather.livedoor.com/plugin/common/forecast/12.js"></script>
