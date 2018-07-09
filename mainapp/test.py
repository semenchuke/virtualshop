render_list = {
    'oculus': 'OculuRift.html',
    'psvr': 'PSVR.html',
    'htc_vive': 'HTC_Vive.html'
}


i = 'htc_vive'

if i in render_list:

    print(render_list[i])

a = 'mainapp/' + render_list[i]

print('a = ', a)

