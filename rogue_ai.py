# ============================================================
# CMP 131 - ROGUE AI EMERGENCY DIAGNOSTIC SYSTEM
# Team members:
# ============================================================

print("========================================")
print("     ROGUE AI DIAGNOSTIC SYSTEM")
print("========================================")

# LEVEL 1 - TEMPERATURE DIAGNOSTIC
# Ask for the system temperature and make the required decision.
system_temperature= int(input("What is the system Tempature?"))
print("Tempature: ",system_temperature)
if system_temperature >= 100:
    print("WARNING: SYSTEM OVERHEATING")
else:
    print("Tempature Normal")
# LEVEL 2 - POWER DIAGNOSTIC
# Ask for the battery percentage and make the required decision.
battery_percentage= int(input("What is the battery percentage?"))
print("Battery Percentage: ",battery_percentage,"%")
if battery_percentage <20:
    print("LOW POWER")
else:
    print("Power Normal")

# LEVEL 3 - SECURITY DIAGNOSTIC
# Ask for the security status and make the required decision.
security_status=input("What is the security status?")
print("Security Status: ",security_status)
if security_status == "danger" or security_status == "DANGER":
    print("SHUTDOWN REQUIRED")
else:
    print("System Secure")


print("========================================")
print("Diagnostic complete.")
print("========================================")
