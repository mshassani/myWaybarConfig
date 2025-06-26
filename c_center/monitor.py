monitor_conf = "/home/sadra/.config/hypr/conf/monitor/monitor.conf"

def change_fps(hz):

    fps = f"monitor=,1920x1080@{hz},auto,auto"

    with open(monitor_conf, 'w')as conf:
        conf.write(fps)

def show_current():
    with open(monitor_conf, 'r') as conf:
        content = conf.read()

        sec = content.split(',')[1]

        return sec.split('@')[-1]