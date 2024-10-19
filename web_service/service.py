import signal
import subprocess

from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

process = None


def run_volume_control():
    global process
    process = subprocess.Popen(
        ["python", "/home/jeison/dev/volume_control/src/main.py"]
    )


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/in-stream")
def start_logger(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_volume_control)
    return {"message": "Volume control task started"}


@app.get("/out-of-stream")
def stop_logger():
    global process
    if process is not None:
        process.send_signal(signal.SIGINT)
        process.wait()
        return {"message": "Volume control task stopped"}
    return {"error": "No process running"}
