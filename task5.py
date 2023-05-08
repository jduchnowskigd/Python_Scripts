#!/usr/bin/python

"""
This script provides information about the machine on which it is currently running
"""
import argparse
import socket
import os
import psutil

def get_distro_info():
    """Get information about the currently used distribution"""
    with open('/etc/os-release', encoding='utf-8') as file:
        for line in file:
            if line.startswith('PRETTY_NAME'):
                return line.split('=')[1].strip().strip('"')
            return None

def get_memory_info():
    """Get information about memory"""
    mem = psutil.virtual_memory()
    return {
        'total': mem.total,
        'used': mem.used,
        'free': mem.available
    }


def get_cpu_info():
    """Get information about the CPU"""
    cpu = {}
    with open('/proc/cpuinfo',  encoding='utf-8') as file:
        for line in file:
            if line.startswith('model name'):
                cpu['model'] = line.split(':')[1].strip()
            elif line.startswith('cpu cores'):
                cpu['cores'] = int(line.split(':')[1].strip())
            elif line.startswith('cpu MHz'):
                cpu['speed'] = float(line.split(':')[1].strip())
    return cpu


def get_user_info():
    """Get information about the current user"""
    return os.getlogin()


def get_load_average():
    """Get information about current load average"""
    loadavg = os.getloadavg()
    return {
        '1 min': loadavg[0],
        '5 min': loadavg[1],
        '15 min': loadavg[2]
    }


def get_ip_address():
    """Get current IP address"""
    return socket.gethostbyname(socket.gethostname())


parser = argparse.ArgumentParser(description='Get system information.')
parser.add_argument('-d', '--distro', action='store_true', help='get distro info')
parser.add_argument('-m', '--memory', action='store_true', help='get memory info')
parser.add_argument('-c', '--cpu', action='store_true', help='get CPU info')
parser.add_argument('-u', '--user', action='store_true', help='get current user')
parser.add_argument('-I', '--load-average', action='store_true', help='get system load average')
parser.add_argument('-i', '--ip-address', action='store_true', help='get IP address')

args = parser.parse_args()

if args.distro:
    print('Distro Info:', get_distro_info())

if args.memory:
    mem_info = get_memory_info()
    print('Memory Info:')
    print(f'Total: {mem_info["total"]} bytes')
    print(f'Used: {mem_info["used"]} bytes')
    print(f'Free: {mem_info["free"]} bytes')

if args.cpu:
    cpu_info = get_cpu_info()
    print('CPU Info:')
    print(f'Model: {cpu_info["model"]}')
    print(f'Cores: {cpu_info["cores"]}')
    print(f'Speed: {cpu_info["speed"]} MHz')

if args.user:
    print('Current User:', get_user_info())

if args.load_average:
    load_avg = get_load_average()
    print('Load Average:')
    print(f'1 min: {load_avg["1 min"]}')
    print(f'5 min: {load_avg["5 min"]}')
    print(f'15 min: {load_avg["15 min"]}')

if args.ip_address:
    print('IP Address:', get_ip_address())
