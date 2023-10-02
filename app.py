import time
import psutil
import os


def defineStatusColor(value, thresholds):
    if (value < thresholds['minimum']):
        return '92m'
    if (value > thresholds['maximum']):
        return '91m'
    return '93m'


def nice_coloured_string(prefix, info, thresholds=0):
    color = 0
    if (thresholds != 0):
        color = defineStatusColor(info, thresholds)
    if (color == 0):
        return "{} {}".format(prefix, info)
    return "{} \033[{} {}\033[00m".format(prefix, color, info)


def print_divider():
    print('-----------------------------------')


def print_cpu():
    cpu_thresholds = {'minimum': 15, 'maximum': 85}
    cpu_percent = psutil.cpu_percent()
    print(nice_coloured_string('CPU Load:', cpu_percent, cpu_thresholds))


def print_uptime():
    uptime_thresholds = {'minimum': 36000, 'maximum': 360000}
    boot_time = psutil.boot_time()
    uptime = int(time.time() - boot_time)
    print(nice_coloured_string('Uptime:', uptime, uptime_thresholds))


def print_memory():
    memory_total = psutil.virtual_memory().total / 1000000000
    memory_available = psutil.virtual_memory().available / 1000000000
    memory_thresholds = {'minimum': memory_total /
                         10, 'maximum': memory_total - 1}
    print(nice_coloured_string('RAM Total:', memory_total))
    print(nice_coloured_string('RAM Available:',
          memory_available, memory_thresholds))


def print_system_info():
    print_cpu()
    print_divider()
    print_uptime()
    print_divider()
    print_memory()


starttime = time.monotonic()
while True:
    os.system('clear')
    print_system_info()
    time.sleep(1.0 - ((time.monotonic() - starttime) % 1.0))
