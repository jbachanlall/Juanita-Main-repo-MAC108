raw_log = "ALERT | 2026-10-19 | 192.168.4.11 | SQL_Injection_Attempt"
ip = raw_log.split(" | ")[2]
print(ip)
banned_ips = ("10.0.0.1", "192.168.4.11", "172.16.0.5")
if ip in banned_ips:
            print ("ALERT: banned IP detected:",ip)