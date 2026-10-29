import time
from ssmf.engine import detect_event
SAMPLES=[{"event_type":"request_succeeded","outcome":"success"},{"event_type":"authentication_failed"},{"event_type":"AttachUserPolicy"},{"event_type":"invocation_spike","invocations":150},{"event_type":"error_burst","error_count":15}]
N=10000; start=time.perf_counter(); alerts=0
for i in range(N): alerts += int(detect_event(SAMPLES[i%len(SAMPLES)])["alert"])
elapsed=time.perf_counter()-start
print(f"events={N}"); print(f"elapsed_seconds={elapsed:.6f}"); print(f"events_per_second={N/elapsed:.2f}"); print(f"alerts_generated={alerts}")
print("Note: local synthetic benchmark only; not AWS end-to-end latency or cost.")
