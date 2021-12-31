import ee
service_account = 'google-earth-engine@smart-bridge-336705.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, 'privatekey.json')
ee.Initialize(credentials)


mapid = ee.Image('srtm90_v4').getMapId({'min': 0, 'max': 1000})

print(mapid)
