import serial # 시리얼통신 오픈

def get_GPS_info(buffer):
    nmea_latitude = buffer[1]  # 위도
    nmea_longitude = buffer[3]  # 경도

    # 3507.047447 / 12905.423882
    # print('{0} / {1}'.foramt(nmea_latitude, nmea_longitude))
    latitude = convert_to_degree(nmea_latitude)
    longitude = convert_to_degree(nmea_longitude)

def convert_to_degree(raw_value):
    decimal_value = float(raw_value)
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - degrees)/ 0.6
    position = '%.4f' %(degrees + mm_mmmm)
    return position


# 초기화
tag_info = 'GNGGA,' # 위치 NMEA GPGGA
ser = serial.Serial('/dev/ttyS0', baudrate=9600) # 시리얼 객체 생성

# 무한 루프
try:
    while True:
        if ser.readable():
            res = ser.readline()
            try:
                rec_data = res.decode(encoding='utf-8')[:len(res)-1]
                # print(res)
                tag_available = rec_data.find(tag_info)
                if (tag_available > 0) :
                    buffer = rec_data.split(tag_info, 1)[1]
                    # print(buffer)
                    nmea_buffer = (buffer.split('.'))
                    get_GPS_info(nmea_buffer)
            except:
                pass
except KeyboardInterrupt:
    print('GPS 종료！！')
