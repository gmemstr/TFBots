import Cache
import threading


def Visitor(ua, ip, url):
    #  Log new visitor, should be called
    #  when URL is requested
    #  Grap user-agent, geo location and
    #  visited URL

    #  Mostly for debug
    print("[Time] " + ua + " " + ip + " " + url)

