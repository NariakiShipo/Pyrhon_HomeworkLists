import math

rate_type = [183, 383, 983]

in_voice_rate = [0.08, 0.07, 0.06]
out_voice_rate = [0.1393, 0.1304, 0.1087]
local_voice_rate = [0.1349, 0.1217, 0.1018]

in_sms_rate = [1.1287, 1.1127, 0.9572]
out_sms_rate = [1.4803, 1.2458, 1.1243]


in_voice_sec = int(input())
out_voice_sec = int(input())
local_voice_sec= int(input())
in_sms_count = int(input())
out_sms_count = int(input())

total_cost = []
for i in range(len(rate_type)):
        cost = math.floor(in_voice_sec * in_voice_rate[i] + out_voice_sec * out_voice_rate[i] + local_voice_sec * local_voice_rate[i] + in_sms_count * in_sms_rate[i] + out_sms_count * out_sms_rate[i])

        if cost < rate_type[i]:
            cost = rate_type[i]
        total_cost.append(cost)
for i in range(len(rate_type)):
    if total_cost[i] == min(total_cost):
        print(total_cost[i])
        print(rate_type[i])
