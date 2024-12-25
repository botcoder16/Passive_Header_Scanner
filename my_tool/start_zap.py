import subprocess
import time

# zap_jar_path = 'C:\\Program Files\\ZAP\\Zed Attack Proxy\\zap-2.15.0.jar'
# # Start ZAP in daemon mode
# zap_process = subprocess.Popen(['java', '-jar', zap_jar_path, '-daemon', '-port', '8081'])


# # Allow some time for ZAP to start
# time.sleep(10)

# # Check if ZAP is running
# if zap_process.poll() is None:
#     print("ZAP is running in daemon mode.")
# else:
#     print("Failed to start ZAP.")

# Run Uvicorn
uvicorn_process = subprocess.Popen(
    ['uvicorn', 'url_predictions.api_main:app', '--reload']
)

# Keep both processes running
try:
    # Wait for both processes to continue running
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down both ZAP and API server.")
    #zap_process.terminate()  # Stop ZAP
    uvicorn_process.terminate()  # Stop Uvicorn