class Config:
    BBOX = '24.5,60,25.5,60.5'
    TIMESTEP = 60
    PARAMETERS = 'Temperature,Humidity,WindUMS,WindVMS,PrecipitationAmount,TotalCloudCover'
    AQI_PARAMS = 'AQIndex'
    FMI_QUERY_URL = 'http://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=getFeature&storedquery_id='
    AQI_QUERY = 'fmi::forecast::enfuser::airquality::helsinki-metropolitan::grid'
    FILEREF_MEMBER = './/{http://www.opengis.net/gml/3.2}fileReference'
